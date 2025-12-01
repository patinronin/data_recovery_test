from typing import List, Dict, Any
from app.db.db_connector import get_client
from app.commons.custom_logger import CustomLogger
from app.commons.retry_policy import retry

logger = CustomLogger("app").get_logger()

@retry(logger=logger)
async def fetch_all_pokemons(db) -> List[Dict[str, Any]]:
    """Fetch all pokemons from the pokemons collection in the given database."""
    logger = CustomLogger("app").get_logger()
    try:
        logger.info("Fetching all pokemons from the database")
        collection = db["pokemons"]

        result  = await collection.find().to_list(length=None)
        return result
    except Exception as e:
        logger.error(f"Error fetching pokemons: {e}")
        return []
    
async def main():
    mongo_db_uri = "mongodb://localhost:27017"
    client = get_client(uri=mongo_db_uri)
    db = client["poke_db"]
    pokemons = await fetch_all_pokemons(db)    
    logger.info(f"Fetched {len(pokemons)} pokemons from the database.")

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())