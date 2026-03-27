from src.client import MoodleClient


def get_all_courses(client: MoodleClient) -> list[dict]:
    """Return all courses. Uses search fallback if token lacks system context."""
    try:
        return client.call("core_course_get_courses")
    except RuntimeError as e:
        if "errorcoursecontextnotvalid" not in str(e):
            raise
        # Token is scoped to a course context — use search instead
        result = client.call("core_course_search_courses", criterianame="search", criteriavalue="")
        return result.get("courses", [])


def get_enrolled_users(client: MoodleClient, course_id: int) -> list[dict]:
    """Return all users enrolled in a given course."""
    return client.call("core_enrol_get_enrolled_users", courseid=course_id)
