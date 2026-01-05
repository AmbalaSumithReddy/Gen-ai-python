from dotenv import load_dotenv
import os

# Load environment variables from a .env file (if present)
load_dotenv()


def get_api_key():
    """Return API_KEY from environment, raise SystemExit if missing."""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise SystemExit("Missing API_KEY environment variable. Set it in .env or your shell.")
    return api_key


if __name__ == "__main__":
    key = get_api_key()
    print(f"API_KEY is set (length {len(key)})")

