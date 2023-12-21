# Admin Usage

## Installation

1. Clone the repo

    ```bash
    git clone git@github.com:revalgovender/wrestling-sorted.git
    ```
2. Create Postgres database and database user using `psql` or `pgAdmin`
3. Create Google Developer API key with access to the YouTube Data API v3

4. Copy `.env.example` to `.env`

    ```bash 
    cp .env.example .env
    ```

5. Complete `.env` with your own values
6. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

7. Run migrations with

    ```bash
    python manage.py migrate
    ```

8. Run fixtures with

    ```bash
    python manage.py loaddata fixtures/initial_data.json
    ```
   
9. Run server with

    ```bash
    python manage.py runserver
    ```

## Importing Highlights from YouTube

- Run the following command to import highlights from YouTube:
  ```bash
  python manage.py import_highlights
  ```

- Run the following command to import legacy highlights from YouTube:
  ```bash
  python manage.py import_legacy_highlights
  ```