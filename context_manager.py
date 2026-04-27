from contextlib import contextmanager

@contextmanager
def database_connection():
    print("Connecting to database...")
    connection = "DB_CONNECTION"

    try:
        yield connection
    except Exception as e:
        print("Error occurred:", e)
    finally:
        print("Closing database connection...")


# Example
with database_connection() as conn:
    print("Using:", conn)