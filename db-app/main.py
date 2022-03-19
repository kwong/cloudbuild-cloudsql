from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from psycopg2.errors import DuplicateTable

import os
from pathlib import Path

# grab connection values from ENV
dbuser = os.environ.get("DB_USER")
dbpass = os.environ.get("DB_PASS")
dbhost = os.environ.get("DB_HOST")
dbport = os.environ.get("DB_PORT")
dbname = os.environ.get("DB_NAME")


engine = create_engine(f"postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}")
pathlist = Path("./db-app/migrations/").glob("**/*.sql")
with engine.connect() as conn:
    # db = scoped_session(sessionmaker(bind=engine))

    for path in sorted(pathlist):
        # example statement to execute
        with open(str(path)) as file:
            try:
                print(f"executing {file.name}")
                query = text(file.read())
                result = conn.execute(query)
                [print(x) for x in result]
            except Exception as e:
                print("error found")
                print(e)
