# GigHub API

A backend API for **GigHub**, a Nairobi-based freelancing platform connecting freelancers (developers, designers, writers, marketers, data analysts, consultants) with clients posting short-term gigs.

**Admission Number:** C027-01-2633/2024

## Dataset configuration (derived from admission number)
- Last digit of xxxx (2633) = **3** → 5 + 3 = **8 gigs**
- xxxx = 2633 is **odd** → Categories: `Marketing`, `Data`, `Consulting`
- First two digits of xxxx = **26** (≥ 10) → Currency: **USD**

## Running the API

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/gigs` | GET | List all gigs, optional filters: `category`, `min_budget`, `max_budget` |
| `/gigs/search` | GET | Search gigs by title (`q` query param) |
| `/gigs/{gig_id}` | GET | Retrieve a single gig by ID (404 if not found) |
| `/gigs` | POST | Create a new gig (validated) |
| `/gigs/{gig_id}` | PUT | Update a gig's `budget` and/or `status` |
| `/gigs/{gig_id}` | DELETE | Delete a gig (404 if not found) |

## Data model

Each gig has: `id`, `title` (5-100 chars), `description` (20-500 chars), `category` (must be Marketing/Data/Consulting), `budget` (> 0), `currency` (USD), `status` (Open/In Progress/Closed), `client_name` (2-50 chars).

## Validation

- `GigCreate` validates all fields, including restricting `category` to the assigned category list via a `Literal` type.
- `GigUpdate` only allows changing `budget` and `status`; `status` is restricted to `Open`, `In Progress`, or `Closed`.
