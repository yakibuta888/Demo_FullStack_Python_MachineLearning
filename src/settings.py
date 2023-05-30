import os
from pathlib import Path

cwd: Path = Path(__file__).resolve().parent


LOG_FILE: str = os.path.normpath(os.path.join(cwd, "appserver.log"))
DB_NAME: str = os.path.normpath(os.path.join(cwd, "appserver.sql"))
TEMPLATE_FOLDER_PATH: str = os.path.normpath(os.path.join(cwd, "templates"))
STATIC_FOLDER_PATH: str = os.path.normpath(os.path.join(cwd, "static"))
PORT: int = 5000
DEBUG: bool = True
RECOMMEND_ENGINE_ENABLE = True
