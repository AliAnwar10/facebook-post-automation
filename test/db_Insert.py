import sqlite3

def insert_credential(email, password):
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO credentials (email, password) VALUES (?, ?)', 
                                            (email, password))
    conn.commit()
    conn.close()

def insert_group(group_name, group_url):
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO group_links (group_name, group_url) VALUES (?, ?)', 
                                            (group_name, group_url))
    conn.commit()
    conn.close()

def insert_post(title, description, hashtags, image_path):
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, description, hashtags, image_path) VALUES (?, ?, ?, ?)', 
                                      (title, description, hashtags, image_path))
    conn.commit()
    conn.close()

def insert_post_selection(credential_id, group_id, post_id, selected=1):
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO post_selections (credential_id, group_id, post_id, selected) VALUES (?, ?, ?, ?)', 
                                                (credential_id, group_id, post_id, selected))
    conn.commit()
    conn.close()

def get_credentials():
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM credentials')
    creds = cursor.fetchall()
    conn.close()
    return creds

def get_groups():
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM group_links')
    groups = cursor.fetchall()
    conn.close()
    return groups

def get_posts():
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    conn.close()
    return posts

def get_selected_posts(credential_id):
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT g.group_name, g.group_url, p.title, p.description, p.hashtags, p.image_path
        FROM post_selections ps
        JOIN group_links g ON ps.group_id = g.id
        JOIN posts p ON ps.post_id = p.id
        WHERE ps.selected = 1 AND ps.credential_id = ?
    ''', (credential_id,))
    selections = cursor.fetchall()
    conn.close()
    return selections

def clear_selections():
    conn = sqlite3.connect('facebook_automation.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM post_selections')
    conn.commit()
    conn.close()