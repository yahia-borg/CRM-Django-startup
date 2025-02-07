# CRM-Django-startup
starter backend project using Django, postgres, docker.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.10

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/CRM-Django-startup.git
    cd CRM-Django-startup
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```sh
    cp .env.example .env
    ```

5. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

### Running the Project

To start the Django development server, run:
```sh
docker-compose up