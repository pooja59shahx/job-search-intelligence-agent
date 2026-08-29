def matches_keywords(job, keywords):
    role = job.role.lower()

    return any(
        keyword.lower() in role
        for keyword in keywords
    )


def matches_location(job):
    location = job.location.lower()

    allowed_locations = [
        "san francisco",
        "south san francisco",
        "palo alto",
        "bay area",
        "california",
        "remote",
    ]

    return any(
        location_name in location
        for location_name in allowed_locations
    )


def filter_jobs(jobs, keywords):
    matched_jobs = []

    for job in jobs:
        if matches_keywords(job, keywords) and matches_location(job):
            matched_jobs.append(job)

    return matched_jobs
