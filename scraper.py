from playwright.sync_api import sync_playwright
import pandas as pd
from config import JOB_ROLES, LOCATION

def scrape_jobs():

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for role in JOB_ROLES:
            for loc in LOCATION:

                url = f"https://www.linkedin.com/jobs/search/?keywords={role}&location={loc}"

                page.goto(url)

                page.wait_for_timeout(5000)

                cards = page.query_selector_all(".base-search-card")

                for job in cards:

                    try:

                        title = job.query_selector(".base-search-card__title").inner_text()
                        company = job.query_selector(".base-search-card__subtitle").inner_text()
                        link = job.query_selector("a").get_attribute("href")

                        jobs.append({
                            "title": title.strip(),
                            "company": company.strip(),
                            "link": link
                        })

                    except Exception as e:
                        print(f"Error parsing job card: {e}")

        browser.close()

    return pd.DataFrame(jobs)