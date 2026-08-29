from collectors.greenhouse import collect_greenhouse_jobs


def main():
    jobs = collect_greenhouse_jobs(
        company_slug="cloudflare",
        company_name="Cloudflare",
    )

    print(f"Found {len(jobs)} jobs.")

    for job in jobs[:10]:
        print(
            f"{job.company} | "
            f"{job.role} | "
            f"{job.location}"
        )


if __name__ == "__main__":
    main()
