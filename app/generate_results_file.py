import asyncio
import os
from app.commons.custom_logger import CustomLogger
from app.services.fetch_http_pokemon import fetch_pokemons
from app.services.fetch_mongodb_pokemon import  fetch_all_pokemons
from app.services.save_file import save_file
from app.commons.retry_policy import retry
from app.commons.transform_pokemon_data import transform_pokemon_data
from app.db.db_connector import get_client



async def main():

    logger = CustomLogger("app").get_logger()
    
    pokemons_http = await fetch_pokemons()

    transformed_pokemons = []
    for pokemon_data in pokemons_http:
        pokemon = transform_pokemon_data(pokemon_data, source="http")
        if pokemon is None:
            continue
        transformed_pokemons.append(pokemon.model_dump())
    
    mongo_db_uri =  os.getenv("MONGO_URI","mongodb://localhost:27017")
    client = get_client(uri=mongo_db_uri)
    db = client["poke_db"]

    pokemons_mongo = await fetch_all_pokemons(db)
    for pokemon_data in pokemons_mongo:
        pokemon = transform_pokemon_data(pokemon_data, source="mongo_db")
        if pokemon is None:
            continue
        transformed_pokemons.append(pokemon.model_dump())
    
    sorted_pokemons = sorted(transformed_pokemons, key=lambda p: p["hash_id"])
    await save_file(name="pokemons", data=sorted_pokemons)

if __name__ == "__main__":
    asyncio.run(main())