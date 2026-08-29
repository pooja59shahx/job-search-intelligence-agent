import csv
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

JOBS_FILE = DATA_DIR / "jobs.csv"


def save_jobs(jobs):
    with JOBS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "company",
            "role",
            "location",
            "source_url",
            "date_posted",
            "status",
            "fit_score",
            "priority",
        ])

        for job in jobs:
            writer.writerow([
                job.company,
                job.role,
                job.location,
                job.source_url,
                job.date_posted,
                job.status,
                job.fit_score,
                job.priority,
            ])
