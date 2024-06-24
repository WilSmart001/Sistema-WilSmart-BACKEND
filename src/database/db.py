import psycopg2
from psycopg2 import DatabaseError
from decouple import config
from flask import current_app

def get_connection():
    try:
        return psycopg2.connect(
            #host = config('PGSQL_HOST'),
            #user = config('PGSQL_USER'),
            #password = config('PGSQL_PASSWORD'),
            #database = config('PGSQL_DATABASE'),
            #port = config('PGSQL_PORT'),
            current_app.config['DATABASE_URL']
        )
    except DatabaseError as ex:
        raise ex
