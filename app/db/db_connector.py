import os
from typing import AsyncGenerator
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
from contextlib import asynccontextmanager
from app.commons.custom_logger import CustomLogger

logger = CustomLogger("app").get_logger()

def get_client(uri: str) -> AsyncIOMotorClient:
    try:
        logger.info(f"Creating MongoDB client for URI: {uri}")
        client = AsyncIOMotorClient(uri)
        return client
    except Exception as e:
        logger.error(f"Error creating MongoDB client: {e}")
        raise

@asynccontextmanager
async def get_session(
    client:AsyncIOMotorClient,
) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
    try: 
        logger.info("Starting MongoDB session")
        async with await client.start_session() as session:
            yield session
    except Exception as e:
        logger.error(f"Error in MongoDB session: {e}")
        raise