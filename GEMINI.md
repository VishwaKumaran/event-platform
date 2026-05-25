# Event Platform GEMINI.md

This project is a high-performance event management and tracking platform built with FastAPI, SQLModel, and TimescaleDB.

## Project Overview

- **Backend**: A modular FastAPI application handling authentication, user management, and event tracking.
- **Worker**: A background process for handling asynchronous tasks (e.g., event processing).
- **Database**: TimescaleDB (PostgreSQL) for time-series event data and relational models.
- **Cache/Queue**: Redis for state management and potential stream processing.
- **Tooling**: Managed with `uv` for lightning-fast dependency resolution and environment management.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ORM/Validation**: [SQLModel](https://sqlmodel.tiangolo.com/) (SQLAlchemy + Pydantic)
- **Database**: [TimescaleDB](https://www.timescale.com/) (PostgreSQL)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Configuration**: [Pydantic Settings](https://docs.pydantic.dev/latest/usage/pydantic_settings/)
- **Auth**: JWT-based authentication
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

## Project Structure

```text
.
├── backend/                # FastAPI application
│   ├── app/                # Main application package
│   │   ├── core/           # Config, security, database setup
│   │   ├── dependencies/   # FastAPI dependencies (auth, sessions)
│   │   ├── models/         # SQLModel database models
│   │   ├── routers/        # API endpoints
│   │   ├── schemas/        # Pydantic models for request/response
│   │   └── services/       # Business logic
│   └── pyproject.toml      # Backend dependencies and configuration
├── worker/                 # Background worker
│   ├── main.py             # Worker entry point
│   └── pyproject.toml      # Worker dependencies
└── docker-compose.yaml     # Infrastructure orchestration
```

## Building and Running

### Local Development

1.  **Environment Setup**:
    Ensure `uv` is installed. Copy `.env.example` to `.env` in the `backend/` directory and configure your variables.

2.  **Infrastructure**:
    Start the database and Redis using Docker Compose:
    ```bash
    docker-compose up -d postgres redis
    ```

3.  **Backend**:
    ```bash
    cd backend
    uv sync
    uv run uvicorn app.main:app --reload
    ```

4.  **Worker**:
    ```bash
    cd worker
    uv sync
    uv run python main.py
    ```

### Testing

-   TODO: Implement and document testing procedures.

## Development Conventions

-   **Type Safety**: Use explicit type hints everywhere.
-   **Async First**: All database and I/O operations should be asynchronous using `async`/`await`.
-   **Service Pattern**: Keep business logic in `services/`, keeping `routers/` thin.
-   **Schema Validation**: Use Pydantic schemas for all API inputs and outputs.
-   **Database Migrations**: Always use Alembic for database schema changes.
    ```bash
    # In backend directory
    uv run alembic revision --autogenerate -m "description"
    uv run alembic upgrade head
    ```
-   **Dependency Management**: Use `uv add <package>` to add new dependencies.
