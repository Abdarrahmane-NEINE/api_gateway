import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    # Applies the Singleton pattern so that all modules share the same logger configuration.
    if not logger.handlers:
        # Configure logger only once
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
