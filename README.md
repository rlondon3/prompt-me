# Project README

## Endpoints:

### 1. ChatGPT Resolution:
   - Endpoint: `/resolution`

### 2. User Registration:
   - Endpoint: `/users/register`

### 3. Get All Users:
   - Endpoint: `/admin/users`

### 4. Get User by ID:
   - Endpoint: `/admin/user/<int:id>`

### 5. Update User:
   - Endpoint: `/users/<int:id>`

### 6. Delete User:
   - Endpoint: `/users/<int:id>`

## PostgreSQL Database Environment:

Ensure the following environment variables are configured:

- **DB_HOST**: localhost
- **DB_NAME**: yourDBname
- **DB_USER**: postgres
- **DB_PASSWORD**: yourPassword
