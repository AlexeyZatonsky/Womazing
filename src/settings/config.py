from dotenv import load_dotenv
import os

def chek_variable(value)-> str | None:
    load_dotenv()
    value = os.environ.get("DB_USER")

    if value is None:
        return 'src/settings'
    
    return None

DB_USER = ''

load_dotenv(chek_variable(DB_USER))

DB_USER = os.environ.get("DB_USER")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")

SECRET_AUTH = os.environ.get("SECRET_AUTH")
