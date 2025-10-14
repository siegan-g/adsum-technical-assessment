from datetime import datetime, timezone
from models.logs import Logs
from application.services.logs import insert

def database_sink(message):
    try:
        record = message.record
        log_entry = Logs(
            id=None, 
            level=record["level"].name,
            message=record["message"],
            timestamp=record["time"].replace(tzinfo=timezone.utc)
        )
        
        insert(log_entry)
    except Exception as e:
       print(f"Error writing log to database: {e}")

