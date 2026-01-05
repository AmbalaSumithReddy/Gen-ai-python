from dotenv import load_dotenv
import os
import requests
from typing import Any, Dict

# Load environment variables from .env (if present)
load_dotenv()


def get_api_key() -> str:
    """Return API_KEY from environment or exit with an error."""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise SystemExit("Missing API_KEY environment variable. Set it in .env or your shell.")
    return api_key


def fetch_json(url: str, headers: Dict[str, str] | None = None, timeout: int = 10) -> Any:
    """Fetch JSON from `url` using the API key for Authorization header by default.

    Returns parsed JSON or a dict containing non-JSON response text and status code.
    Raises requests.RequestException for network/HTTP errors.
    """
    if headers is None:
        headers = {"Authorization": f"Bearer {get_api_key()}"}

    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()

    # Try parsing JSON, otherwise return text with status
    try:
        return response.json()
    except ValueError:
        return {"_non_json_response": response.text, "_status_code": response.status_code}


def main() -> None:
    url = "https://api.example.com/data"  # <-- Verify this endpoint
    try:
        data = fetch_json(url)
        print(data)
    except requests.HTTPError as e:
        print("HTTP error:", e)
    except requests.RequestException as e:
        print("Request failed:", e)


if __name__ == "__main__":
    main()
