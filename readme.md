# Movie Ticket Booking apis

This is a simple Fastapi-Postgres based microservice layer for movie ticket booking and analyser apis.

## Set up

### step -1

install python dependencies
go to `/backend/dependencies`

```sh
cd /backend/dependencies/
pip install -m requirements.txt
```

### Step-2 Database set up

- Bring up a fresh postgres database using dump file that is present in `/backend/util/database/`
- edit the config file that is present at /backend/config/db_config.py

### Step-3

Bring up the server using cmd

```sh
uvicorn main:app --reload --port=8000
```

### Step-4

Visit `localhost:8000/docs` for api document and testing

## Further improvements

- Though I have added the autherization code, but commented that as it is not working
- Authentication and Dockerization
