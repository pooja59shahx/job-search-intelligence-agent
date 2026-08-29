def job_key(job) -> str:
    return f"{job.company}|{job.role}|{job.location}".strip().lower()


def deduplicate_jobs(jobs):
    seen = set()
    unique_jobs = []

    for job in jobs:
        key = job_key(job)

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs
