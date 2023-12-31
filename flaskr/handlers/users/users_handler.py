from flaskr.models.user.user import User_Store
from flask import request

# Create an instance of the User_Store class
store = User_Store()


class User_Handler:
    def register_user():
        """Registers a new user based on JSON data provided in the request."""
        try:
            data = request.get_json()
            email = data["email"]
            user = store.create(email)
            if user:
                return {"data": user}
        except Exception as e:
            # Handle exceptions and return an error message
            return {"errors": [str(e)]}, 400

    def get_users():
        """Retrieves all users from the store."""
        try:
            users = store.index()
            if users:
                return users
        except Exception as e:
            # Handle exceptions and return an error message along with a 404 status code
            return {"errors": [str(e)]}, 404

    def get_user(id):
        """Retrieves a specific user from the store."""
        user_id = id
        try:
            user = store.show(user_id)
            if user:
                return user
        except Exception as e:
            # Handle exceptions and return an error message
            return {"errors": [str(e)]}

    def update_user(id):
        """Updates a user in the store."""
        try:
            user_id = id
            data = request.get_json()
            email = data["email"]
            user = store.update(user_id, email)
            if user:
                return user
        except Exception as e:
            # Handle exceptions and return an error message
            return {"errors": [str(e)]}

    def delete_user(id):
        """Deletes a user from the store."""
        try:
            user_id = id
            user = store.delete(user_id)
            if user:
                return {"deleted_id": user}
        except Exception as e:
            # Handle exceptions and return an error message
            return {"errors": [str(e)]}


# Define routes for user-related operations
def user_route(app):
    app.add_url_rule(
        "/users/register", "register_user", User_Handler.register_user, methods=["POST"]
    )
    app.add_url_rule(
        "/admin/users", "show_users", User_Handler.get_users, methods=["GET"]
    )
    app.add_url_rule(
        "/admin/user/<int:id>", "show_user", User_Handler.get_user, methods=["GET"]
    )
    app.add_url_rule(
        "/users/<int:id>", "update_user", User_Handler.update_user, methods=["PUT"]
    )
    app.add_url_rule(
        "/users/<int:id>", "delete_user", User_Handler.delete_user, methods=["DELETE"]
    )
