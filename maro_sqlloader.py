# @title Set Your Values Here { display-mode: "form" }
PROJECT_ID = "fdc-gen-ai-test "  # @param {type:"string"}
REGION = "europe-west3"  # @param {type: "string"}
INSTANCE = "ai-hackathon-slack-off"  # @param {type: "string"}
DATABASE = "postgres"  # @param {type: "string"}
TABLE_NAME = "public.messages"  # @param {type: "string"}

# fdc-gen-ai-test:europe-west3:ai-hackathon-slack-off

from langchain_google_cloud_sql_pg import PostgresEngine
from langchain_google_cloud_sql_pg import PostgresLoader


def search():
    engine = PostgresEngine.afrom_instance(
        project_id=PROJECT_ID,
        region=REGION,
        instance=INSTANCE,
        database=DATABASE,
    )

    # Creating a basic PostgreSQL object
    loader = PostgresLoader.create(engine, table_name=TABLE_NAME)

    docs = loader.aload()
    print(docs)


search()
