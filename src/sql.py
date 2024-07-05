from sqlalchemy import create_engine, text

# Create the engine
engine = create_engine('mysql+pymysql://mahaputra971:mahaputra971@localhost:3306/bisnisproses_db')

def show_tables():
    try:
        with engine.connect() as connection:
            tables = connection.execute(text("SHOW TABLES"))
            connection.commit()

            for row in tables.mappings():
                print("Tables:", row)

            print("Connected successfully!")
    except Exception as e:
        print("Connection failed:", str(e))


def insert_tables():
    try:
        with engine.connect() as connection:
            # Perform the insert operation here
            # ...
            connection.commit()

            print("Tables inserted successfully!")
    except Exception as e:
        print("Insert failed:", str(e))
