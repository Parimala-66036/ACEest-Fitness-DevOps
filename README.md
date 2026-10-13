# ACEest Fitness & Gym — DevOps Assignment

## Project Overview
ACEest Fitness & Gym is a Flask-based web application demonstrating DevOps practices, including version control, automated testing, Docker containerization, and CI/CD pipelines.

## Technologies Used
- Python and Flask
- Pytest
- Git and GitHub
- Docker
- GitHub Actions
- Jenkins

## Project Structure
- `app.py` — Flask application
- `test_app.py` — Automated tests
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker image configuration
- `.github/workflows/main.yml` — GitHub Actions workflow

## Run Locally
Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and start the application:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Run Automated Tests

```bash
python -m pytest -v
```

## Build and Run with Docker

```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

## CI/CD
GitHub Actions runs the automated tests and builds the Docker image when code is pushed. Jenkins checks out the GitHub repository and executes the configured build steps.

## Health Check
Visit http://127.0.0.1:5000/health to verify application health.

## Author
Prepared as part of the DevOps Assignment.
