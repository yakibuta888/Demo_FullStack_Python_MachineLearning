import logging

from app.controllers.roboter import server
import settings

logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("running server")
    server.start(debug=settings.DEBUG)
