import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)


project_name = "RagNavigator"
list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/pdf_processor.py",  
    f"src/{project_name}/components/url_processor.py",  
    f"src/{project_name}/components/data_cleaner.py",  
    f"src/{project_name}/components/vectorizer.py",  
    f"src/{project_name}/components/database_manager.py",  
    f"src/{project_name}/components/api_connector.py",  
    f"src/{project_name}/components/chat_history.py",  
    f"src/{project_name}/components/configuration_manager.py",  
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common_utils.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  
    f"src/{project_name}/ui/__init__.py",
    f"src/{project_name}/ui/streamlit_app.py", 
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "app.py",  
    "main.py",  
    "Dockerfile", 
    "artifacts/.gitkeep",
    "research/trials.ipynb",  
]


# Create the files and directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file {filepath}")

    else:
        logging.info(f"File {filepath} already exists")


