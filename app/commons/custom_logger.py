import logging
from pathlib import Path
import datetime

class CustomLogger():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CustomLogger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        if not getattr(self.logger, "_is_custom_configured", False):
            formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
            log_dir = Path(__file__).resolve().parents[2] / "logs" / name
            file_path = log_dir / f"{name}_{datetime.date.today()}.log"
            log_dir.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(str(file_path), encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO) 
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)


            self.logger.setLevel(logging.DEBUG)
            self.logger._is_custom_configured = True

    
    def get_logger(self):
        return self.logger
            