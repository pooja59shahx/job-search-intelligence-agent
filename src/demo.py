from models import Job
from scoring import assign_priority, is_alert_worthy


def main():
    job = Job(
        company="Example Company",
        role="Sales Operations Intern",
        location="San Francisco, CA",
        source_url="https://example.com/job",
        fit_score=91,
    )

    job.priority = assign_priority(job.fit_score)

    print(f"Company: {job.company}")
    print(f"Role: {job.role}")
    print(f"Fit Score: {job.fit_score}")
    print(f"Priority: {job.priority}")
    print(f"Alert Worthy: {is_alert_worthy(job.fit_score)}")


if __name__ == "__main__":
    main()
