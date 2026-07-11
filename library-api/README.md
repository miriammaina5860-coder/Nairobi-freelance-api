&#x20;Library API



A simple library management API built with FastAPI, SQLModel, and PostgreSQL.



Name: Miriam  Maina

Admission Number: C027-01-2633/2024



Features

\-  Book Management: Create, read, update, and delete books

\-  Category Management: Organize books by categories (Fiction, Science, History)

\-  Search: Search for books by author or title

\-  Validation: All inputs are validated for correctness

\-  Database: Uses PostgreSQL with SQLModel ORM



&#x20;Technologies Used

\- FastAPI

\- SQLModel

\- PostgreSQL

\- Docker

\- Uvicorn



&#x20;How to Run

1\. Start PostgreSQL: docker compose up -d

2\. Install dependencies: uv add fastapi uvicorn sqlmodel psycopg2-binary alembic python-dotenv

3\. Run the application: uv run uvicorn main:app --reload

4\. Access API Docs: http://127.0.0.1:8000/docs



&#x20;Endpoints

| Method | Endpoint | Description |

|--------|----------|-------------|

| GET | / | Welcome message |

| POST | /books | Create a new book |

| GET | /books | List all books |

| GET | /books/{id} | Get a specific book by ID |

| GET | /books/search | Search books by author or title |

| PATCH | /books/{id} | Update a book's details |

| POST | /categories | Create a new category |

| GET | /categories | List all categories |



&#x20;Exercises Completed



&#x20;Exercise 1: Category Model with relationships

&#x20;Exercise 2: Search endpoint by author and title

&#x20;Exercise 3: Update endpoint for books

