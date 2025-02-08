# FastAPI Clean Architecture Boilerplate

This repository provides a boilerplate for building scalable and maintainable web applications using FastAPI and Clean Architecture principles.

## Features

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Clean Architecture**: Separation of concerns, making the codebase more maintainable and testable.
- **Dependency Injection**: Manage dependencies efficiently.
- **SQLAlchemy**: Powerful and flexible ORM for database interactions.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Alembic**: Database migrations tool.

## Project Structure

```
fastapi-postgresql-boilerplate/
├── migration/ # alembic migration
├── src/ 
│   ├── api/ 
│   │   ├── v1 #routes
│   │   │   ├── posts
│   │   │   │   ├── __init__.py 
│   │   │   │   ├── exeptions.py # exeptions
│   │   │   │   ├── model.py # sqlalchemy model
│   │   │   │   ├── router.py # api router
│   │   │   │   ├── schemas.py # pydantic models
│   │   │   │   ├── service.py # business logic
│   │   │   ├── router.py # v1 router
│   │   ├── global_router.py # api router
│   ├── __init__.py
│   ├── config.py #
│   ├── database.py # database connection
│   ├── main.py # main file
├── venv
├── .env
├── .gitignore
├── .alembic.ini
├── .dockerfile
├── README.md
├── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.7+
- PostgreSQL (or any preferred database)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/fastapi-postgresql-boilerplate.git
    cd fastapi-clean-architecture
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    ```sh
    cp .env.example .env
    ```

5. Run database migrations:
    ```sh
    alembic upgrade head
    ```

6. Start the application:
    ```sh
    uvicorn src.main:app --reload
    ```

<!-- ### Running Tests

To run the tests, use the following command:
```sh
pytest
``` -->

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Alembic](https://alembic.sqlalchemy.org/)
