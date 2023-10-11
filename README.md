# Deploy Watcher

Flask RESTful API that can be integrated into your deployment pipeline to track deployment times.

## Installation

### Local

To run locally on your computer, ensure the following requirements are installed:

1. Python version 3.6+
2. Packages listed in `requirements_local.txt` with the command `pip install -r requirements_local.txt`
3. Git (to clone the repository). Alternatively, download the .zip from the repository and extract it.

Execute the following steps:

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

For deployment in development mode:

1. Ensure Python 3.6+, Docker, and Git are installed.
2. Run:

```bash
git clone https://github.com/akelopes/deployWatcher.git
cd deployWatcher
docker build . -t deploywatcher
docker run -d -p 5000:5000 deploywatcher
```

#### Prod

A demo environment for production with the app, http host (nginx + uwsgi), and MySQL database via Docker.

Prerequisites:

1. Docker (Linux host preferred)
2. Docker-compose or Docker-Stack
3. Git (or download the .zip from the repository).

Run:

```bash
git clone https://github.com/akelopes/deployWatcher.git
cd deployWatcher/prod_simulation
docker-compose build
docker-compose up
```

### Usage

To verify successful execution, open `https://127.0.0.1:5000/transitions`. You should see "API: OK".

#### Transitions Resource

* **GET**:
    - **`/transitions`**: Returns a message `{"API": "OK"}`.
    - **`/transitions/<id>`**: Retrieves details of a specific transition by its ID. If it doesn't exist, you'll get a `404 Not Found` status with `{"message": "Transition not found"}`.
      
* **POST** (`/transitions`): Inserts a new deployment status into the database and returns the ID of the record. Accepts a JSON body with:
    - `component`: String (Max 140 characters)
    - `version`: String (e.g., "1.0")
    - `author`: String
    - `status`: String
    - `sent_timestamp`: Optional. Format: "yyyy-mm-dd hh:mm:ss.fff". Defaults to the current time if omitted.

Use curl for an example POST request:

```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"component": "testApp", "version": "1.0", "author": "akelopes", "status": "started", "sent_timestamp": "2020-01-01 10:10:50.555"}' \
     http://127.0.0.1:5000/transitions
```

Errors, such as "Invalid date format" or "Component too big", return with appropriate messages.

## Considerations

* The system is designed to be agnostic to cloud providers and databases.
* Adherence to the RESTful standard.
* Input handling is performed by the original system for flexible data translation.
* Local and Dev environments are for development, not persistent data.