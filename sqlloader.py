import os

from google.cloud.sql.connector import Connector, IPTypes
import pg8000

import sqlalchemy

from Message import Message


def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    instance_connection_name = "fdc-gen-ai-test:europe-west3:ai-hackathon-slack-off"  # e.g. 'project:region:instance'
    db_user = "postgres"  # e.g. 'my-db-user'
    db_pass = os.getenv("DB_PASS")  # e.g. 'my-db-password'
    db_name = "postgres"  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    # initialize Cloud SQL Python Connector object
    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        # ...
    )
    return pool


def get_all_messages_for_user(user):
    select_stmt = sqlalchemy.text(
        f"SELECT text FROM public.messages WHERE receiver='{user}' ORDER BY priority, ts LIMIT 1000;",
    )

    with connect_with_connector().connect() as db_conn:
        # query database
        result = db_conn.execute(select_stmt)

        # Do something with the results
        return result

def save_message_for_user(message: Message, user: str):
    insert_stmt = sqlalchemy.text(
        f"INSERT INTO public.messages (text, timestamp, priority, receiver, sender) VALUES ('{message.text}', '{message.ts}', {message.priority}, '{user}', '{message.user}');",
    )

    with connect_with_connector().connect() as db_conn:
        # query database
        db_conn.execute(insert_stmt)
        db_conn.commit()