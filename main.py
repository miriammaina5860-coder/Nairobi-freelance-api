# GigHub API
# Admission Number: C027-01-2633/2024
# Last digit: 3 -> 8 gigs
# xxxx = 2633 (odd) -> Categories: Marketing, Data, Consulting
# First two digits of xxxx = 26 (>= 10) -> Currency: USD

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal

app = FastAPI(
    title="GigHub API",
    description="An API for GigHub, a Nairobi-based freelancing platform. Admission No: C027-01-2633/2024",
    version="1.0.0"
)

VALID_CATEGORIES = ["Marketing", "Data", "Consulting"]
CURRENCY = "USD"
VALID_STATUSES = ["Open", "In Progress", "Closed"]

# In-memory "database"
gigs_db = [
    {"id": 1, "title": "Run a Facebook Ads Campaign", "description": "Plan and run a two-week Facebook ads campaign for a local skincare brand targeting Nairobi customers.", "category": "Marketing", "budget": 300.0, "currency": "USD", "status": "Open", "client_name": "Wanjiru Kamau"},
    {"id": 2, "title": "SEO Audit for E-commerce Site", "description": "Perform a full SEO audit for an online store selling handmade jewelry, including keyword research and a report.", "category": "Marketing", "budget": 250.0, "currency": "USD", "status": "Open", "client_name": "Brian Otieno"},
    {"id": 3, "title": "Clean and Analyze Sales Dataset", "description": "Clean a messy CSV of two years of sales data and produce summary statistics and trend charts.", "category": "Data", "budget": 400.0, "currency": "USD", "status": "In Progress", "client_name": "Amina Hassan"},
    {"id": 4, "title": "Build a Power BI Dashboard", "description": "Design an interactive Power BI dashboard for tracking monthly revenue and expenses across three branches.", "category": "Data", "budget": 500.0, "currency": "USD", "status": "Open", "client_name": "Peter Mwangi"},
    {"id": 5, "title": "Business Registration Advisory", "description": "Advise a first-time entrepreneur on the process of registering a limited company in Kenya, step by step.", "category": "Consulting", "budget": 150.0, "currency": "USD", "status": "Closed", "client_name": "Grace Njeri"},
    {"id": 6, "title": "Market Entry Strategy for Uganda", "description": "Research and prepare a market entry strategy document for a Kenyan retailer expanding into Uganda.", "category": "Consulting", "budget": 600.0, "currency": "USD", "status": "Open", "client_name": "Samuel Kiptoo"},
    {"id": 7, "title": "Email Marketing Funnel Setup", "description": "Set up an email marketing funnel including welcome sequence and abandoned cart emails for a fashion store.", "category": "Marketing", "budget": 220.0, "currency": "USD", "status": "In Progress", "client_name": "Faith Wambui"},
    {"id": 8, "title": "Data Entry Automation Script", "description": "Write an automation script to pull data from supplier PDFs into a structured spreadsheet weekly.", "category": "Data", "budget": 180.0, "currency": "USD", "status": "Open", "client_name": "David Njoroge"},
]


# Pydantic model for creating a new gig
class GigCreate(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=20, max_length=500)
    category: Literal["Marketing", "Data", "Consulting"]
    budget: float = Field(gt=0)
    client_name: str = Field(min_length=2, max_length=50)


# Pydantic model for updating an existing gig
class GigUpdate(BaseModel):
    budget: Optional[float] = Field(None, gt=0)
    status: Optional[Literal["Open", "In Progress", "Closed"]] = None


@app.get("/gigs")
def get_gigs(
    category: Optional[str] = None,
    min_budget: Optional[float] = None,
    max_budget: Optional[float] = None
):
    """
    Retrieve all gigs, optionally filtered by category and/or min_budget/max_budget.
    """
    results = gigs_db

    if category:
        results = [g for g in results if g["category"].lower() == category.lower()]
    if min_budget is not None:
        results = [g for g in results if g["budget"] >= min_budget]
    if max_budget is not None:
        results = [g for g in results if g["budget"] <= max_budget]

    return results


@app.get("/gigs/search")
def search_gigs(q: str):
    """
    Search for gigs by title.
    """
    results = [g for g in gigs_db if q.lower() in g["title"].lower()]
    return results


@app.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    """
    Retrieve a single gig by its ID.
    """
    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig
    raise HTTPException(status_code=404, detail="Gig not found")


@app.post("/gigs")
def create_gig(gig: GigCreate):
    """
    Create a new gig posting.
    """
    new_id = max([g["id"] for g in gigs_db]) + 1 if gigs_db else 1

    new_gig = {
        "id": new_id,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category,
        "budget": gig.budget,
        "currency": CURRENCY,
        "status": "Open",
        "client_name": gig.client_name
    }

    gigs_db.append(new_gig)

    return {"message": "Gig created successfully", "gig": new_gig}


@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, gig_update: GigUpdate):
    """
    Update a gig's budget and/or status.
    """
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            if gig_update.budget is not None:
                gigs_db[index]["budget"] = gig_update.budget
            if gig_update.status is not None:
                gigs_db[index]["status"] = gig_update.status

            return {"message": "Gig updated successfully", "gig": gigs_db[index]}

    raise HTTPException(status_code=404, detail="Gig not found")


@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):
    """
    Delete a gig from the listings.
    """
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            deleted_gig = gigs_db.pop(index)
            return {"message": "Gig deleted successfully", "gig": deleted_gig}

    raise HTTPException(status_code=404, detail="Gig not found")