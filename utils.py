import re
import requests


def find_email(url):

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        page = response.text

        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", page)
        
        # Filter out common junk emails
        blocked = ["privacy", "support", "noreply", "no-reply", "jobs@", "careers@", "sentry", "example"]
        valid_emails = [e for e in emails if not any(b in e.lower() for b in blocked)]

        if valid_emails:
            return valid_emails[0]

    except Exception as e:
        print(f"Error fetching email from {url}: {e}")

    return None