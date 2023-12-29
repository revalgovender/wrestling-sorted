[![Project Status: WIP – Work in Progress](https://img.shields.io/badge/Project%20Status-WIP-yellow.svg)](https://github.com/your-username/your-repo)

# Wrestling Sorted

API to retrieve and sort highlights from YouTube for wrestling tv shows.

## Table of Contents

1. [API Docs](#api-docs)
2. [Installation](#installation)
3. [Local Development](#local-development)
4. [Usage](#usage)

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
    make build
    ```
5. Run the containers

    ```bash
    make run
    ```


## Local Development

### Database

- We have a database container running locally and a pgAdmin container to manage it
- pgAdmin can be accessed at http://localhost:5050/
- Database is seeded on startup
- Database data is persisted when containers are stopped

## PyCharm  Community Edition code completion

- You can create a venv in the project root to enable code completion
- Configure PyCharm's Python interpreter to use the venv

## Usage

- Import highlights from YouTube:

  ```bash
  make import
  ```
- Import legacy highlights from YouTube:

  ```bash
  make import_legacy
  ```