# Deploy Watcher

Flask RESTful API that can be integrated into your deployment pipeline to track deployment times.

## Installation

### Local

To run locally on your computer, ensure the following requirements are installed:

1. Python version 3.6+
2. Packages listed in `requirements_local.txt` with the command `pip install -r requirements_local.txt`
3. Git (to clone the repository). Alternatively, download the .zip from the repository and extract it.

With these requirements met, open your command line and execute the following:

#### Windows cmd / Powershell:

```bash
git clone https://github.com/akelopes/deployWatcher.git
cd deployWatcher
flask run
```

#### Linux shell:

```bash
git clone https://github.com/akelopes/deployWatcher.git
cd deployWatcher
flask run
```

### Docker

#### Dev

To deploy in development mode:

1. Ensure Python 3.6+, Docker, and Git are installed.
2. Open a command prompt:

```bash
git clone https://github.com/akelopes/deployWatcher.git
cd deployWatcher
docker build . -t deploywatcher
docker run -d -p 5000:5000 deploywatcher
```

#### Prod

A demonstration environment for production integrates the app with an http host (nginx + uwsgi) and a MySQL database via Docker.

Prerequisites:

1. Docker (Linux host preferred)
2. Docker-compose or Docker-Stack
3. Git (or download the .zip from the repository).

Execute the following:

```bash
git clone https://github.com/akelopes/deployWatcher.git
cd deployWatcher/prod_simulation
docker-compose build
docker-compose up
```

#### Use

To verify successful execution, visit: `https://127.0.0.1:5000/transitions`. The message "API: OK" should appear.

* Commands:
    * **GET**: Returns JSON with message `{"API": "OK"}`.
    * **POST**: Inserts a deployment status into the database. Accepts a JSON body with:
        * `component`: String (Max 140 characters)
        * `version`: String (e.g., "1.0")
        * `author`: String
        * `status`: String
        * `sent_timestamp`: Optional. Format: "yyyy-mm-dd hh:mm:ss.fff". If omitted, the current time is used.

Example using curl:

```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"component": "testApp", "version": "1.0", "author": "akelopes", "status": "started", "sent_timestamp": "2020-01-01 10:10:50.555"}' \
     http://127.0.0.1:5000/transitions
```

Errors like "Invalid date format", "Component too big", or database-related issues will return with appropriate error messages.

## Considerations

* The core system is designed to be agnostic to cloud providers and databases, ensuring flexibility.
* The RESTful standard is adhered to.
* Input handling is performed by the original system for flexibility in data translation.
* Local and Dev environments prioritize easy development over data persistence.

---

This revised documentation should address the issues previously mentioned and provide users with a clearer understanding of the application's functionality and constraints.