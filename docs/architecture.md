# System Architecture

The Job Search Intelligence Agent uses a multi-stage workflow to turn raw job listings into prioritized, application-ready opportunities.

## 1. Discovery

Searches:

- Company career pages
- Greenhouse
- Lever
- Ashby
- Workday
- YC companies
- Startup career pages
- Broader web sources

The system searches both a predefined company watchlist and companies not previously known to the candidate.

## 2. Verification

Potential opportunities are checked for:

- Active application page
- Posting recency
- Location eligibility
- Internship eligibility
- Official company or ATS source

Dead or unverifiable listings are excluded or flagged.

## 3. Qualification

Verified jobs are evaluated against the candidate profile for:

- Role relevance
- Experience overlap
- Skills overlap
- Location
- Career trajectory
- Full-time conversion potential

## 4. Prioritization

Opportunities are classified as:

- APPLY NOW
- HIGH PRIORITY
- CONSIDER
- SKIP

## 5. Application Preparation

High-priority opportunities can trigger:

- Resume-to-JD analysis
- Resume tailoring recommendations
- Hiring-contact research
- LinkedIn outreach
- Email outreach
- Application sequencing

## 6. Tracking

Previously discovered opportunities are retained so future searches can distinguish between:

- NEW
- UPDATED
- ALREADY REPORTED
- CLOSED

This allows recurring searches to focus on changes rather than repeating the entire research process.
