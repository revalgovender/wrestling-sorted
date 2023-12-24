[![Project Status: WIP – Work in Progress](https://img.shields.io/badge/Project%20Status-WIP-yellow.svg)](https://github.com/your-username/your-repo)

# Wrestling Sorted

API to retrieve and sort highlights from YouTube for wrestling tv shows.

## API Docs

- Swagger has been implemented to document the API
- It can be accessed locally at http://127.0.0.1:8000/docs/

## Installation

### Prerequisites

- Docker Compose
- Google Developer API key with access to the YouTube Data API v3

### Steps

1. Clone the repo

    ```bash
    git clone git@github.com:revalgovender/wrestling-sorted.git
    ```
2. Copy `.env.example` to `.env`

    ```bash 
    cp .env.example .env
    ```

3. Complete `.env` with your own values
4. Build the images

    ```bash
    docker-compose build
    ```
5. Run the containers

    ```bash
    docker-compose up -d
    ```

## Importing Highlights from YouTube

- Run the following command to import highlights from YouTube:
  ```bash
  python manage.py import_highlights --tv_show_id=1 --max_items_to_parse=50
 
  ```

- Run the following command to import legacy highlights from YouTube:
  ```bash
  python manage.py import_legacy_highlights --tv_show_id=1 --max_items_to_parse=50

  ```