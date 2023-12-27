# Project README

## Endpoints:

### 1. ChatGPT Resolution:

- **Endpoint:** `/resolution`
- **Description:** Retrieves ChatGPT resolution data.
- **Currently Returning:**
  ```json
  {
  	"completion": "dummy completion",
  	"topic": "health"
  }
  ```
- **Topic Array:**
  ```
  random_topics = ["health", "career", "finance", "love", "family", "investments", "friendships", "opportunities"]
  ```

### 2. User Registration:

- **Endpoint:** `/users/register`
- **Description:** Allows users to register.

### 3. Get All Users:

- **Endpoint:** `/admin/users`
- **Description:** Retrieves information about all users.

### 4. Get User by ID:

- **Endpoint:** `/admin/user/<int:id>`
- **Description:** Retrieves information about a specific user by ID.

### 5. Update User:

- **Endpoint:** `/users/<int:id>`
- **Description:** Updates information for a specific user.

### 6. Delete User:

- **Endpoint:** `/users/<int:id>`
- **Description:** Deletes a specific user.

## PostgreSQL Database Environment:

Ensure the following environment variables are configured:

- **DB_HOST:** localhost
- **DB_NAME:** yourDBname
- **DB_USER:** postgres
- **DB_PASSWORD:** yourPassword
