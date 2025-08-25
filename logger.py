import json
import datetime

def log(level, request_id, input_value, message=None, error=None):
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "level": level,
        "requestId": request_id,
        "input": input_value
    }
    if message:
        log_entry["message"] = message
    if error:
        log_entry["error"] = error

    print(json.dumps(log_entry))  # could also write to a file or external service
