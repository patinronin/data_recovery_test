import asyncio
import os
from app.commons.transform_pokemon_data import transform_pokemon_data
from app.db.db_connector import get_client
from app.commons.custom_logger import CustomLogger
from app.services.fetch_http_pokemon import fetch_pokemons
from app.services.insert_mongodb_pokemon import insert_pokemons_into_collection
from datetime import datetime

logger = CustomLogger("app").get_logger()

async def main():
    logger = CustomLogger("app").get_logger()
    logger.info("Starting Pokemon data population")
    pokemons = await fetch_pokemons()


    transformed_pokemons = []
    for pokemon_data in pokemons:
        pokemon = transform_pokemon_data(pokemon_data, source="mongo_db")
        if pokemon is None:
            continue
        transformed_pokemons.append(pokemon.model_dump())

    mongo_db1_uri = os.getenv("MONGO_URI","mongodb://localhost:27017")
    client1 = get_client(uri=mongo_db1_uri)    
    db1 = "poke_db"
    coll1 = "pokemons"
    await insert_pokemons_into_collection(client1, db1, coll1, transformed_pokemons)

    logger.info("Finished populating Pokemon data") 





if __name__ == "__main__":
    asyncio.run(main())