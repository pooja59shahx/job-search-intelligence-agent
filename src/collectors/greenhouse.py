import requests

from models import Job


def collect_greenhouse_jobs(company_slug: str, company_name: str):
    """
    Collect jobs from a company's public Greenhouse job board.

    Example company_slug:
    'cloudflare'
    """

    url = f"https://boards-api.greenhouse.io/v1/boards/{company_slug}/jobs"

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    data = response.json()
    jobs = []

    for item in data.get("jobs", []):
        location = item.get("location", {}).get("name", "")

        jobs.append(
            Job(
                company=company_name,
                role=item.get("title", ""),
                location=location,
                source_url=item.get("absolute_url", ""),
                status="ACTIVE",
            )
        )

    return jobs
