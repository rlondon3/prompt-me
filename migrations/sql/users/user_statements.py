CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY, 
                        email VARCHAR (50) NOT NULL
                        )"""
GET_USER_BY_EMAIL = "SELECT * FROM users WHERE email = %s;"
GET_USER_BY_ID = "SELECT row_to_json(t) FROM users t WHERE id = %s;"
GET_USERS = "SELECT row_to_json(t) FROM users t;" #returns key value pair
INSERT_INTO_USERS_TABLE_RETURNING_ID = """INSERT INTO users (
                                        email 
                                    ) VALUES (%s) RETURNING id;"""
UPDATE_USERS_TABLE_RETURNING_USER = """UPDATE users SET email=(%s) WHERE id=(%s) RETURNING *;"""
DELETE_FROM_USERS_RETURNING_ID = "DELETE FROM users WHERE id=(%s) RETURNING *;"