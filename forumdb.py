#
# Database access functions for the web forum.
#

import time
import bleach
import psycopg2

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    ## Database connection
    DB = psycopg2.connect("dbname=forum")
    cursor = DB.cursor()
    cursor.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in cursor]
    posts.sort(key=lambda row: row['time'], reverse=True)
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    ## Database connection
    DB = psycopg2.connect("dbname=forum")
    t = time.strftime('%c', time.localtime())
    cursor = DB.cursor()
#    cursor.execute("INSERT INTO posts (content) VALUES ('%s')" % content)
    # To prevent the SQL injection bug and sanitize text from the web form
    content = bleach.clean(content)
    cursor.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    DB.commit()
    DB.close()
