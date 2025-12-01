import argparse
import importlib
import asyncio
from app.commons.custom_logger import CustomLogger

def main():
    logger = CustomLogger("app").get_logger()
    parser = argparse.ArgumentParser(description="Script execution")
    parser.add_argument("--poblate_db", required=False, help="Execute poblate_db script", action="store_true")
    parser.add_argument("--generate_results_file", required=False, help="Execute generate_results_file script", action="store_true")

    args = parser.parse_args()

    try:
        if args.poblate_db:
            logger.info("Executing poblate_db script")
            poblate_db = importlib.import_module("app.poblate_db")
            asyncio.run(poblate_db.main())
        
        if args.generate_results_file:
            logger.info("Executing generate_results_file script")
            generate_results_file = importlib.import_module("app.generate_results_file")
            asyncio.run(generate_results_file.main())

    except Exception as e:
        logger.error(f"Error : {e}")
        raise

if __name__ == "__main__":
    main()