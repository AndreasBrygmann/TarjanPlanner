import time
import logging
logFile = "./logfile.log"
logLevel = logging.INFO
logging.basicConfig(level=logLevel, filename=logFile, filemode="a", format="%(asctime)-15s %(levelname)-8s %(message)s")

logger = logging.getLogger("logger")
import functools

def logg(func, logger: logging.Logger):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        try:
            logging.info(f"Function {func.__name__} executed in {execution_time:.5f} seconds")
        except Exception as e:
            logging.exception(e)
        return result
    return wrapper

defaultLogger = functools.partial(logg, logger=logger)