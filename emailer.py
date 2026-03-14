import smtplib
import os
from email.message import EmailMessage
from config import EMAIL, APP_PASSWORD, RESUME_PATH


def send_email(recipient, company, role="Software Engineer"):

    msg = EmailMessage()

    msg["Subject"] = f"Application for {role} Role"
    msg["From"] = EMAIL
    msg["To"] = recipient

    body = f"""
Hello Hiring Manager,

I found an opportunity at {company} for the {role} position and wanted to apply.

I have experience in Software Development.

Please find my resume attached.

Best Regards
Chetan Sethi
"""

    msg.set_content(body)

    filename = os.path.basename(RESUME_PATH)

    with open(RESUME_PATH, "rb") as f:

        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=filename
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(EMAIL, APP_PASSWORD)
        smtp.send_message(msg)