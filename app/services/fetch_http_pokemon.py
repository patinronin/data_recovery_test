from aiohttp import ClientSession
import asyncio
from app.commons.custom_logger import CustomLogger
import aiohttp
from app.commons.retry_policy import retry

sem = asyncio.Semaphore(5)  # Limit concurrent requests
logger = CustomLogger("app").get_logger()

async def fetch_pokemon(session: ClientSession, url: str) -> dict | None:
    """Fetch a single Pokemon from the API."""
    try:
        logger.info(f"Fetching Pokemon data from {url}")
        async with sem:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return None


@retry(logger=logger)
async def fetch_pokemons(limit: int = 11, offset: int = 1):
    """Fetch Pokemon from the PokeAPI."""
    try:
        logger.info(f"Fetching pokemons from {offset} to {limit -1}")
        async with aiohttp.ClientSession() as session:
            tasks = []
            for pokemon_id in range(offset, limit):
                url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
                tasks.append(fetch_pokemon(session, url))

            pokemons = await asyncio.gather(*tasks)
            return pokemons
    except Exception as e:
        logger.error(f"Error fetching pokemons: {e}")
        return []