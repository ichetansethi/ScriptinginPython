# Automated Job Scraper and Email Sender

This Python project automates the process of:
1. Scraping job listings for roles like **Technical Support Engineer**, **Application Support Engineer**, **IT Support Engineer**, and **Site Reliability Engineer** from LinkedIn (via Google search).
2. Extracting HR contact emails from job descriptions (if available).
3. Sending cold emails with your resume to the collected email addresses.

---

## 🔧 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (auto-installed via `webdriver_manager`)
- A Gmail account with **App Password enabled**

---

## 📦 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-repo/job-email-automation.git
cd job-email-automation

2. Install Dependencies

pip install -r requirements.txt



⸻

🔐 Gmail App Password Setup (Important)

Gmail with 2FA does not allow regular password usage. You need to create an App Password.

How to generate an App Password:
	1.	Go to Google App Passwords
	2.	Select Mail as the app.
	3.	Select Your Device.
	4.	Click Generate.
	5.	Copy the 16-character password and use it in the script instead of your Gmail password.

⸻

🧠 Usage

1. Run Job Scraper

python linkedin_job_scraper.py

This will:
	•	Scrape job listings from LinkedIn via Google
	•	Store the data in linkedin_jobs.csv

2. Send Cold Emails

Before running, update the config section with:
	•	Your Gmail address
	•	Your App Password
	•	The path to your resume file

Then run:

python send_cold_emails.py

This will:
	•	Parse linkedin_jobs.csv
	•	Extract HR emails (if found)
	•	Send emails with your attached resume

⸻

📁 Folder Structure

├── linkedin_job_scraper.py       # Script to scrape job listings
├── send_cold_emails.py           # Script to send emails
├── linkedin_jobs.csv             # Scraped job listing data
├── resume.pdf                    # Your resume (place it here or provide a path)
├── README.md
└── requirements.txt



⸻

⚠️ Notes
	•	The email sending uses multithreading to speed up delivery.
	•	Email logs will be visible in your Sent items.
	•	Avoid spamming or sending too many emails in one go to stay compliant with Gmail limits.

⸻

✅ To-Do (Optional Enhancements)
	•	Add OAuth2-based Gmail authentication
	•	Add GUI to configure job filters and resume path
	•	Integrate email verification APIs (like Hunter.io)
