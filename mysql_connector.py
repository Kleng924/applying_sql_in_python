import sqlite3

def create_connection(mysql_assignment_bd):
    conn = None
    try:
        conn = sqlite3.connect(mysql_assignment_bd)
        print("Connection to database successful.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create the Members table if it doesn't exist."""
    try:
        sql_create_members_table = """
        CREATE TABLE IF NOT EXISTS Members (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER CHECK(age > 0)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_members_table)
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def add_member(conn, member_id, name, age):
    """Add a new member to the Members table."""
    try:
        sql_insert_member = """
        INSERT INTO Members (id, name, age)
        VALUES (?, ?, ?);
        """
        cursor = conn.cursor()
        cursor.execute(sql_insert_member, (member_id, name, age))
        conn.commit()
        print("Member added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
    except sqlite3.Error as e:
        print(f"Error inserting member: {e}")

def main():
    database = "gym_database.db"
    
    conn = create_connection(database)
    
    if conn:
        create_table(conn)
        
        add_member(conn, 1, 'John Doe', 25)
        add_member(conn, 2, 'Jane Smith', 30)
        
        conn.close()

if __name__ == "__main__":
    main()