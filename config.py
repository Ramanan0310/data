import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


def get_connection_string() -> str:
    server = os.getenv("DB_SERVER", r"localhost\SQLEXPRESS")
    database = os.getenv("DB_NAME", "AC073_VANUR")
    driver = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    use_windows_auth = os.getenv("USE_WINDOWS_AUTH", "true").lower() == "true"

    odbc = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "TrustServerCertificate=yes;"
    )

    if use_windows_auth:
        odbc += "Trusted_Connection=yes;"
    else:
        user = os.getenv("DB_USER", "")
        password = os.getenv("DB_PASSWORD", "")
        odbc += f"UID={user};PWD={password};"

    return f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc)}"


SECRET_KEY = os.getenv("SECRET_KEY", "change-this-in-production")
