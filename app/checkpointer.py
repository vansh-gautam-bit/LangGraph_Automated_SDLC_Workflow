from psycopg import connect 
from langgraph.checkpoint.postgres import PostgresSaver

from app.config import settings

conn = connect(settings.DATABASE_URL)

checkpointer = PostgresSaver(conn)