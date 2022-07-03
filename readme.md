# Movie Ticket Booking apis

This is a simple Express-Postgres based microservice layer for movie ticket booking and analyser apis.

## requirements

- `node-v14.*`
- `postgres-v10+`

## Set up

### step -1

install `node` dependecies
go to `/backend/` and do

```sh
npm install
```

### Step-2 Database set up

- Bring up a fresh postgres database using dump file that is present in `/backend/database/dump/`
- edit the `.env` and add the db credentials file at `/backend/.env`

### Step-3

Bring up the server using cmd

```sh
nodemon api.js
or
node api.js
```

### Step-4

Visit `localhost:3000` for details and api-docs(`localhost:3000/api-docs`)

## Further improvements

- autherization and authentication
- bring up http models(for request/response parameters and validations)
- introduction of ORM models
- Dockerization
