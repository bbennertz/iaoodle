from src.client import MoodleClient


def get_grades(client: MoodleClient, course_id: int, user_id: int) -> list[dict]:
    """Return grade items for a user in a course."""
    return client.call(
        "gradereport_user_get_grade_items",
        courseid=course_id,
        userid=user_id,
    )
