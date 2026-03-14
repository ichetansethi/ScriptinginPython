import time
import random
from scraper import scrape_jobs
from utils import find_email
from emailer import send_email
from tracker import save_application


def run_agent():

    print("Starting job scraping...")
    try:
        jobs = scrape_jobs()
    except Exception as e:
        print(f"Error scraping jobs: {e}")
        return

    for _, job in jobs.iterrows():

        print(f"Checking: {job.get('company', 'Unknown')}")

        email = find_email(job.get("link", ""))

        if email:

            try:

                send_email(email, job.get("company", "Unknown"), job.get("title", "Software Engineer"))

                save_application(job)

                print(f"Applied to {job.get('company')} at {email}")
                
                # Sleep to avoid rate limiting
                sleep_time = random.uniform(5, 15)
                print(f"Sleeping for {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)

            except Exception as e:

                print(f"Failed to apply to {job.get('company')}: {e}")

        else:

            print("No email found")


if __name__ == "__main__":

    run_agent()