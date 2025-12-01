# Data Recovery Test

## Project Overview
This project is designed to fetch, transform, and store Pokémon data from multiple sources (HTTP and MongoDB). It also provides functionality to generate a results file containing sorted Pokémon data.

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