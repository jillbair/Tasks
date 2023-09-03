import sqlalchemy
from sqlalchemy import create_engine, text

# Replace with your actual database connection URL
db_url = "postgresql://username:password@localhost/database_name"

# Create a database engine
engine = create_engine(db_url)

# Define the SQL query
sql_query = text("""
    SELECT p.id, p.title, IFNULL(SUM(r.number_of_tickets), 0) AS reserved_tickets
    FROM plays p
    LEFT JOIN reservations r ON p.id = r.play_id
    GROUP BY p.id, p.title
    ORDER BY reserved_tickets DESC, p.id ASC
""")

# Execute the query
with engine.connect() as connection:
    result = connection.execute(sql_query)
    for row in result:
        print(f"Play ID: {row['id']}, Title: {row['title']}, Reserved Tickets: {row['reserved_tickets']}")
