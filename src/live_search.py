from collectors.greenhouse import collect_greenhouse_jobs
from dedup import deduplicate_jobs
from filtering import filter_jobs
from search_config import get_all_keywords


def main():
    keywords = get_all_keywords()

    companies = [
        {
            "name": "Cloudflare",
            "greenhouse_slug": "cloudflare",
        },
    ]

    all_jobs = []

    for company in companies:
        try:
            jobs = collect_greenhouse_jobs(
                company_slug=company["greenhouse_slug"],
                company_name=company["name"],
            )

            all_jobs.extend(jobs)

        except Exception as error:
            print(
                f"Could not collect {company['name']}: "
                f"{error}"
            )

    unique_jobs = deduplicate_jobs(all_jobs)

    matched_jobs = filter_jobs(
        unique_jobs,
        keywords,
    )

    print(
        f"\nFound {len(matched_jobs)} "
        "potential matches:\n"
    )

    for job in matched_jobs:
        print(job.company)
        print(job.role)
        print(job.location)
        print(job.source_url)
        print("-" * 50)


if __name__ == "__main__":
    main()
