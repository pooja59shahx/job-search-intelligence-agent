from models import Job
from scoring import assign_priority
from dedup import deduplicate_jobs
from storage import save_jobs


def main():
    jobs = [
        Job(
            company="Example Company",
            role="Sales Operations Intern",
            location="San Francisco, CA",
            source_url="https://example.com/job1",
            fit_score=91,
            status="ACTIVE",
        ),
        Job(
            company="Example Company",
            role="Sales Operations Intern",
            location="San Francisco, CA",
            source_url="https://example.com/job1",
            fit_score=91,
            status="ACTIVE",
        ),
        Job(
            company="Example Startup",
            role="Growth Operations Intern",
            location="Remote - California",
            source_url="https://example.com/job2",
            fit_score=84,
            status="ACTIVE",
        ),
    ]

    jobs = deduplicate_jobs(jobs)

    for job in jobs:
        job.priority = assign_priority(job.fit_score)

    save_jobs(jobs)

    print(f"Saved {len(jobs)} unique jobs.")


if __name__ == "__main__":
    main()
