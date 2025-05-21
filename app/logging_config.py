import logging

def setup_logger(name="Market_Simulation"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.WARNING)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        file_handler = logging.FileHandler("simulation.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
