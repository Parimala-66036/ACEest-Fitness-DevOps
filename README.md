# ACEest Fitness & Gym — DevOps Assignment

## 1. Project Overview

ACEest Fitness & Gym is a Flask-based web application developed to demonstrate DevOps practices, including version control, automated testing, Docker containerization, and Continuous Integration and Continuous Deployment (CI/CD).

## 2. Technologies Used

- Python 3
- Flask
- Pytest
- Git and GitHub
- Docker
- GitHub Actions
- Jenkins

## 3. Project Structure

- `app.py` — Flask application
- `test_app.py` — Automated application tests
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker image configuration
- `Jenkinsfile` — Jenkins pipeline definition
- `.github/workflows/main.yml` — GitHub Actions workflow
- `.gitignore` — Files excluded from version control

## 4. Run the Application Locally

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open the application in a browser:

`http://127.0.0.1:5000/`

## 5. Run Automated Tests

Execute the following command:

```bash
python -m pytest -v
```

The application tests verify:
- Home page response.
- Application health-check endpoint.

**Test result:** 2 tests passed.

## 6. Docker Containerization

Build the Docker image:

```bash
docker build -t aceest-fitness:latest .
```

Run the container:

```bash
docker run -p 5000:5000 aceest-fitness:latest
```

Access the application at `http://127.0.0.1:5000/`.

## 7. Git and GitHub

The project source code is maintained in a GitHub repository.

Repository: https://github.com/Parimala-66036/ACEest-Fitness-DevOps

Git commands used:

```bash
git add .
git commit -m "Update project files"
git push origin main
```

## 8. GitHub Actions

A GitHub Actions workflow is configured in `.github/workflows/main.yml`.

The workflow is triggered by repository updates and performs automated testing and Docker image build operations.

The GitHub Actions workflow was successfully executed.

## 9. Jenkins CI/CD Pipeline

A Jenkins pipeline is configured using the `Jenkinsfile` stored in the project repository.

The pipeline performs the following stages:

1. Checkout source code from GitHub.
2. Create a Python virtual environment.
3. Install project dependencies.
4. Execute automated tests using Pytest.
5. Build the Docker image.
6. Publish automated test results.

**Jenkins execution result:** Build #3 completed successfully.

## 10. Application Health Check

The application provides a health-check endpoint:

`http://127.0.0.1:5000/health`

It returns a JSON response indicating application health.

## 11. Conclusion

This project demonstrates the implementation of a basic DevOps workflow using Flask, GitHub, Pytest, Docker, GitHub Actions, and Jenkins. It covers source-code management, automated testing, containerization, and CI/CD pipeline execution.

## Author

Prepared as part of the DevOps Assignment.