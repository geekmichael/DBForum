# DB Forum

A practice for learning Python and PostgreSQL when I was in the Udacity online course.

# How to run

## Create a new database in PostgreSQL
```
\c forum
```
## Create a table
```sql
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```

### Run this application
```
python forum.py
```
Run a web browser and go to http://localhost:8000
