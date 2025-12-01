import json
import datetime
from pathlib import Path
import aiofiles
from app.commons.custom_logger import CustomLogger

async def save_file(name: str, data: list[dict]) -> None:
    """Save data to a file in NDJSON format asynchronously."""
    
    file_dir = Path(__file__).resolve().parents[2]
    file_path = file_dir / f"{name}_{datetime.date.today()}.ndjson"

    logger = CustomLogger("app").get_logger()

    try:
        async with aiofiles.open(file_path, "w") as file:
            for item in data:
                line = json.dumps(item, ensure_ascii=False)
                await file.write(line + "\n")

        logger.info(f"NDJSON successfully saved to {file_path}")
    
    except Exception as e:
        logger.error(f"Error saving NDJSON to {file_path}: {e}")
        raise