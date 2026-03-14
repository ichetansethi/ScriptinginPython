import csv
import os
from datetime import datetime

FILE = "applications.csv"


def save_application(job):

    file_exists = os.path.isfile(FILE)
    
    try:
        with open(FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            if not file_exists:
                writer.writerow(["company", "role", "link", "date"])
                
            writer.writerow([
                job.get("company", ""),
                job.get("title", ""),
                job.get("link", ""),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
            
    except Exception as e:
        print(f"Failed to save application to CSV: {e}")