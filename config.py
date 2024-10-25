import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENPOINT = os.getenv('DI-ENDPOINT')
    KEY = os.getenv('DI-KEY')
    AZURE_STORAGE_CONNECTION_STRING = os.getenv('STORAGE-CONNECTION')
    CONTAINER_NAME = os.getenv('CONTAINER-NAME')