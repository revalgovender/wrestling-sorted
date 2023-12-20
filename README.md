# Wrestling Sorted

## About

- API to retrieve and sort highlights from YouTube for wrestling shows

## Installation

1. Clone the repo

```bash
git clone git@github.com:revalgovender/wrestling-sorted.git
```

2. Copy `.env.example` to `.env`

    ```bash 
    cp .env.example .env
    ```

3. Complete `.env` with your own values
4. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations with

    ```bash
    python manage.py migrate
    ```

6. Run server with

    ```bash
    python manage.py runserver
    ```