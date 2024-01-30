# LAB - Class 16

## Project: Serverless Functions

## Project Description

The back-end app uses requests library to interact with REST Countries API. Creates serverless function that handles two types of queries:

- a GET http request with a given country name that responds with a string with the form The capital of X is Y
- a GET http request with a given capital name that responds witha a string with the form "The capital of Chile is Santiago"

### Author: Rhett Chase

### Links and Resources

- [back-end server url](https://capital-finder-rhett-chase.vercel.app/api)
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [REST Countries API](https://restcountries.com/#rest-countries)

### Setup

- `pip install -r requirements.txt`

Alternatively:

- `pip install requests`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

- Run `vercel dev` in command line, and add with capital_name or country_name filled in the query: `api?capital={capital_name}` or `api?country={country_name}`

OR use below paths to query (click for examples)

- [`https://capital-finder-rhett-chase.vercel.app/api?capital={capital_name}`](https://capital-finder-rhett-chase.vercel.app/api?capital=washington,%20D.C.)
- [`https://capital-finder-rhett-chase.vercel.app/api?country={country_name}`](https://capital-finder-rhett-chase.vercel.app/api?country=chile)

#### How to use your library (where applicable)

- N/A

#### Tests

- N/A
