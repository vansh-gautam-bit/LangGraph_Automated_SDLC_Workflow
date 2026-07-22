from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
from langgraph.checkpoint.postgres import PostgresSaver

from app.config import settings

pool = ConnectionPool(
    conninfo=settings.DATABASE_URL,
    max_size=10,
    kwargs={
        "autocommit": True,
        "row_factory": dict_row,
    },
)

checkpointer = PostgresSaver(pool)