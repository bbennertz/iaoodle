from src.client import MoodleClient


def get_all_courses(client: MoodleClient) -> list[dict]:
    """Return all courses from the Moodle instance."""
    return client.call("core_course_get_courses")


def get_enrolled_users(client: MoodleClient, course_id: int) -> list[dict]:
    """Return all users enrolled in a given course."""
    return client.call("core_enrol_get_enrolled_users", courseid=course_id)
