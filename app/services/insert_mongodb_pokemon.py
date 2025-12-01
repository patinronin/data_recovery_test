from app.db.db_connector import get_session
from app.commons.custom_logger import CustomLogger


async def insert_pokemons_into_collection(client, db_name: str, coll_name: str, pokemons: list[dict]):
    """Insert a pokemons list of dicts into the given client's database.collection using a session."""
    logger = CustomLogger("app").get_logger()
    db = client[db_name]
    coll = db[coll_name]
    try:
        logger.info(f"Inserting {len(pokemons)} pokemons into {db_name}.{coll_name}")
        async with get_session(client=client) as session:
            result = await coll.insert_many(pokemons, session=session)
            return result.inserted_ids
    except Exception as e:
        logger.error(f"Error inserting pokemons into {db_name}.{coll_name}: {e}")