import os
import requests
from dotenv import load_dotenv

load_dotenv()


class MoodleClient:
    """Low-level client for the Moodle REST Web Service API."""

    def __init__(self):
        self.base_url = os.environ["MOODLE_URL"].rstrip("/")
        self.token = os.environ["MOODLE_TOKEN"]
        self._session = requests.Session()

    def call(self, function: str, **params) -> dict | list:
        """Call a Moodle WS function and return the parsed JSON response."""
        response = self._session.post(
            f"{self.base_url}/webservice/rest/server.php",
            data={
                "wstoken": self.token,
                "wsfunction": function,
                "moodlewsrestformat": "json",
                **params,
            },
        )
        response.raise_for_status()
        data = response.json()

        if isinstance(data, dict) and "exception" in data:
            raise RuntimeError(f"Moodle API error: {data.get('message')} ({data.get('errorcode')})")

        return data
