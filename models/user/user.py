from flask import request
from dotenv import load_dotenv
from database import connection
from migrations.sql.users.user_statements import (
    CREATE_USERS_TABLE,
    INSERT_INTO_USERS_TABLE_RETURNING_ID,
    GET_USERS,
    GET_USER_BY_ID,
    GET_USER_BY_EMAIL,
    UPDATE_USERS_TABLE_RETURNING_USER,
    DELETE_FROM_USERS_RETURNING_ID,
)
import psycopg2.extras
import re

# Instantiate a class that holds user schema as methods
class User_Store:
    User: None

    def index(self):
        """Get all users."""
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(GET_USERS)
                    connection.commit()
                    users = cursor.fetchall()
                    # Convert the list of tuples to a list of dictionaries
                    return [{"id": user[0]['id'], "email": user[0]['email']} for user in users]
                except Exception as e:
                    return {"errors": [str(e)]}

    def show(self, user_id):
        """Get user by id."""
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(GET_USER_BY_ID, (user_id,))
                connection.commit()
                user = cursor.fetchone()[0]
                try:
                    if user:
                        return user
                except Exception as e:
                    cursor.close()
                    return {"error": str(e)}

    def create(self, email):
        """Create user with email."""
        with connection:
            
            with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(CREATE_USERS_TABLE)
                cursor.execute(GET_USER_BY_EMAIL, (email,))
                user = cursor.fetchone()
               
                if user:
                    return [{"message": "User already registered"}]
                elif not re.match(r'[\w.]+\@[\w.]+', email):
                    return [{"message": "Invalid: please check email address."}]
                else:
                    cursor.execute(INSERT_INTO_USERS_TABLE_RETURNING_ID, (email,))
                    connection.commit()
                    return email

    def update(self, user_id, email):
        """Update a user."""
        if user_id:
            try:
                with connection:
                    with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                        cursor.execute(GET_USER_BY_ID, (user_id,))
                        user = cursor.fetchone()[0]
                        if user:
                            cursor.execute(UPDATE_USERS_TABLE_RETURNING_USER, (email, user_id))
                            connection.commit()
                            return user
            except Exception as e:
                return {"error": str(e)}

    def delete(self, user_id):
        """Delete a user."""
        if user_id:
            try:
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(DELETE_FROM_USERS_RETURNING_ID, (user_id,))
                        connection.commit()
                        user = cursor.fetchone()[0]
                        return user

            except Exception as e:
                return {"error": str(e)}
