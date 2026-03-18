import json
import logging
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "service": "my-service",
            "message": record.getMessage(),
        }
        if hasattr(record, "path"):
            log_record["path"] = record.path
        if hasattr(record, "method"):
            log_record["method"] = record.method
        return json.dumps(log_record)

def setup_logger():
    logger = logging.getLogger("my_service")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(JsonFormatter())
        logger.addHandler(stream_handler)

        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(JsonFormatter())
        logger.addHandler(file_handler)

        logger.propagate = False
        
    return logger

logger = setup_logger()
