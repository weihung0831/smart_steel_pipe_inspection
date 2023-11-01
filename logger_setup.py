from pathlib import Path
import functools
import logging

class LoggerSetup:
    def __init__(self, log_path: str = "logs/app.log"):
        self.log_path = log_path
        self._setup_directory()
        self._setup_logging()

    def _setup_directory(self):
        directory_path = Path(self.log_path).parent
        directory_path.mkdir(parents=True, exist_ok=True)

    def _setup_logging(self):
        # Setup logging configuration
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="[%(asctime)s] [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    @staticmethod
    def log_execution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Starting {func.__name__} execution")
                return func(*args, **kwargs)
            except KeyboardInterrupt as e:
                logging.exception(e)
                raise e
            except Exception as e:
                logging.exception(e)
                raise e
            finally:
                logging.info(f"Finished {func.__name__} execution")

        return wrapper
