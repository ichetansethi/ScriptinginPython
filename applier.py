import json
import time
from playwright.sync_api import sync_playwright

def load_profile():
    with open("profile.json", "r") as f:
        return json.load(f)

def apply_to_greenhouse(url):
    profile = load_profile()
    
    print(f"Starting application for: {url}")

    with sync_playwright() as p:
        # Launching headless=False so we can watch it work!
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(url)
            page.wait_for_load_state("networkidle")

            # 1. Fill basic Info (Greenhouse uses standard IDs for these)
            print("Filling out basic information...")
            
            # First Name
            if page.locator("input[id='first_name']").count() > 0:
                page.fill("input[id='first_name']", profile["first_name"])
            
            # Last Name
            if page.locator("input[id='last_name']").count() > 0:
                page.fill("input[id='last_name']", profile["last_name"])
            
            # Email
            if page.locator("input[id='email']").count() > 0:
                page.fill("input[id='email']", profile["email"])
            
            # Phone
            if page.locator("input[id='phone']").count() > 0:
                page.fill("input[id='phone']", profile["phone"])

            # 2. Upload Resume
            # Greenhouse often has a file input that handles the actual upload, often hidden behind a button
            print("Uploading Resume...")
            file_input = page.locator("input[type='file'][data-source='attach']").first
            if file_input.count() > 0:
                file_input.set_input_files(profile["resume_path"])
                page.wait_for_timeout(2000) # wait for upload to process

            # 3. Fill URLs (LinkedIn, GitHub)
            print("Filling out URLs...")
            
            # Different companies label their custom questions differently. We use generic selectors to guess
            # Look for labels containing "LinkedIn"
            linkedin_label = page.locator("label:has-text('LinkedIn')")
            if linkedin_label.count() > 0:
                 linkedin_input_id = linkedin_label.first.get_attribute("for")
                 if linkedin_input_id:
                     page.fill(f"input[id='{linkedin_input_id}']", profile["linkedin"])

            # Look for labels containing "GitHub"
            github_label = page.locator("label:has-text('GitHub')")
            if github_label.count() > 0:
                 github_input_id = github_label.first.get_attribute("for")
                 if github_input_id:
                     page.fill(f"input[id='{github_input_id}']", profile["github"])
            
            print("Application filled successfully! Pausing to let you review.")
            
            # Pause so the user can see what was filled in before it closes
            time.sleep(10)
            
            # DANGEROUS: Actually clicking submit. We leave this commented out for safety during testing.
            # page.click("input[type='submit'][id='submit_app']")
            print("NOTE: Submit button click is commented out for safety.")

        except Exception as e:
            print(f"Error during application process: {e}")
            
        finally:
            browser.close()

if __name__ == "__main__":
    # Test URL: A random public greenhouse job (You should replace this with a real one you want to test)
    test_url = "https://boards.greenhouse.io/openai/jobs/5283995004" 
    apply_to_greenhouse(test_url)
