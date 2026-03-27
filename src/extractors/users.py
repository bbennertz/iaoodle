from src.client import MoodleClient


def get_all_users(client: MoodleClient) -> list[dict]:
    """Return all users (requires site admin token)."""
    return client.call(
        "core_user_get_users",
        **{"criteria[0][key]": "email", "criteria[0][value]": "%"},
    )
