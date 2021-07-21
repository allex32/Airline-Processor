import json
import logging
import logging.config
import os
from datetime import datetime

logging_config_file_path = os.path.join(os.path.dirname(__file__), 'app_logger.conf')
logging.config.fileConfig(logging_config_file_path, disable_existing_loggers=True)
logger = logging.getLogger('requests')

def log_response(fn):
    def decorator(*args, **kwargs):
        command = args[0].command
        logger.info(f'Datetime: {datetime.utcnow()}. Request name: {command}')
        result = fn(*args, **kwargs)
        d = result.__dict__
        logger.info(f'Request name: {command}. Result: {json.dumps(result.__dict__)}')
        return result
    return decorator
