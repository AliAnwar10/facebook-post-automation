import sqlite3

def create_database():
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()

    # Create credentials table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create group_links table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS group_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL,
            group_url TEXT NOT NULL
        )
    ''')

    # Create posts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            hashtags TEXT,
            image_path TEXT
        )
    ''')

    # Create post_selections table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS post_selections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            credential_id INTEGER,
            group_id INTEGER,
            post_id INTEGER,
            selected INTEGER DEFAULT 0,
            FOREIGN KEY (credential_id) REFERENCES credentials(id),
            FOREIGN KEY (group_id) REFERENCES group_links(id),
            FOREIGN KEY (post_id) REFERENCES posts(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database setup completed.")

if __name__ == "__main__":
    create_database()