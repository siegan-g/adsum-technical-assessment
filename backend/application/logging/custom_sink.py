from datetime import timezone
from models.logs import Logs
from application.services.logs import AgentLogsService 

# def database_sink(message):
#     record = message.record
#     log_entry = Logs(
#         id=None, 
#         level=record["level"].name,
#         message=record["message"],
#         timestamp=record["time"].replace(tzinfo=timezone.utc)
#     )
    
#     log_service.insert(log_entry)

class DatabaseSink:
    def __init__(self,agent_logs_service:AgentLogsService):
        self.agent_logs_serice = agent_logs_service
    def __call__(self, message):
        record = message.record
        log_entry = Logs(
            id=None, 
            level=record["level"].name,
            message=record["message"],
            timestamp=record["time"].replace(tzinfo=timezone.utc)
        )
        
        self.agent_logs_serice.insert(log_entry)