# Data Recovery Test

## Project Overview
This project is designed to fetch, transform, and store Pokémon data from multiple sources (HTTP and MongoDB). It also provides functionality to generate a results file containing sorted Pokémon data.
The api, db calls and write files all full async.
The process is idempotent, if you consume the same date the result will be the same
we are hasing the pokemon_id and the source field to obtain always the same hash and order.
The results will be in a file pokemons_yyyy_mm_dd.ndjson
The project also have a strong logging and retry policy.


## Part 2:  Debugging Scenario – Pipeline Failure with No Logs.

First, I would review the code. I could connect to the server via SSH and open a session using Remote SSH in Visual Studio Code, or review the code within the repository and examine the pipeline.

I would review the log configuration to determine why it's failing.
I could check if the files have execute permissions and if the user also has them; this is likely one of the issues when trying to create log files and the report.

I would also try running it locally or directly on the server to attempt to replicate the error in real time.

I could check if any of the data sources are failing. Depending on the test results, I could continue troubleshooting.

A plan for adding observability:

Add the complete stack trace of the error to the logs.

Add unit tests and integration testing.

Because it's a test, many things that wouldn't happen in a real project are omitted, such as a database without a password, creating a user other than root in the Dockerfile, and creating unit and integration tests and performance tests. Multiple logger instance creation would also be avoided and replaced with a global logger. In this case, the logger has a singleton pattern and always returns the same instance, preventing reconfiguration if one already exists.
 


## Features
- Fetch Pokémon data from an HTTP API.
- Fetch Pokémon data from a MongoDB database.
- Transform and normalize Pokémon data.
- Save the transformed data into a file.
- Populate the MongoDB database with Pokémon data.

## Project Structure
```
app/
├── __init__.py
├── generate_results_file.py  # Script to generate the results file
├── main.py                   # Main entry point for the application
├── poblate_db.py             # Script to populate the database
├── commons/                  # Common utilities
│   ├── custom_logger.py      # Custom logging utility
│   ├── retry_policy.py       # Retry policy for operations
│   └── transform_pokemon_data.py  # Data transformation logic
├── db/                       # Database-related utilities
│   ├── __init__.py
│   └── db_connector.py       # MongoDB connection logic
├── models/                   # Data models
│   └── pokemon.py            # Pokémon data model
├── services/                 # Service layer
│   ├── fetch_http_pokemon.py # Fetch Pokémon data from HTTP API
│   ├── fetch_mongodb_pokemon.py # Fetch Pokémon data from MongoDB
│   ├── insert_mongodb_pokemon.py # Insert Pokémon data into MongoDB
│   └── save_file.py          # Save data to a file
logs/                         # Log files
```

## Prerequisites
- Python 3.8 or higher
- Docker
- MongoDB

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/patinronin/data_recovery_test.git
   cd data_recovery_test
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `MONGO_URI`: MongoDB connection string (default: `mongodb://localhost:27017`)

4. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

## Usage

### Populate the Database
To populate the MongoDB database with Pokémon data, run:
```bash
python -m app.main --poblate_db
```

### Generate Results File
To generate a results file with sorted Pokémon data, run:
```bash
python -m app.main --genarate_results_file
```

Alternatively, you can use the `entrypoint.sh` script:
```bash
./entrypoint.sh
```

## Logging
Logs are stored in the `logs/` directory under `app/`.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.