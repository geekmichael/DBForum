# DB Forum

A practice for learning Python and PostgreSQL when I was in the Udacity online course.

# How to run

## Create a new database in PostgreSQL
```sql
CREATE DATABASE forum
```
## Create a table
```sql
\c forum
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```

### Run this application
```
python forum.py
```
Run a web browser and go to http://localhost:8000
