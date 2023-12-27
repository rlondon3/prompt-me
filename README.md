ROUTES:
Chatgpt = "/resolution"
register email = "/users/register"
get all users = "/admin/users"
get user by id = "/admin/user/<int:id>"
update user = "/users/<int:id>"
delete user = "/users/<int:id>"

POSTGRES DB ENV:
DB_HOST=localhost
DB_NAME=yourDBname
DB_USER=postgres
DB_PASSWORD=yourPassword
