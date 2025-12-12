from flask import Blueprint, jsonify, request

from services.users import UsersService
from schemas.users import UserDTO, CreateUserDTO
from schemas.trips import UserWithTripDTO

# Define the blueprint
user_blueprint = Blueprint('users', __name__, url_prefix='/users')


@user_blueprint.get("/")
def get_all_users():
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of users with their trips
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: Alice Brown
              phone_number:
                type: string
                example: "+380991234567"
              email:
                type: string
                example: alice@mail.com
              rating:
                type: number
                example: 4.7
              trips:
                type: array
                items:
                  properties:
                    id:
                      type: integer
                      example: 10
                    price:
                      type: number
                      example: 120.50
    """
    users = UsersService.get_all_users()
    response = [
        UserWithTripDTO.model_validate(user).model_dump()
        for user in users
    ]
    return jsonify(response)


@user_blueprint.get("/<int:id>")
def get_user(id: int):
    """
    Get user by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: User details with trips
      404:
        description: User not found
    """
    user = UsersService.get_user_by_id(id=id)
    response = UserWithTripDTO.model_validate(user).model_dump()
    return jsonify(response)


@user_blueprint.post("/")
def create_user():
    """
    Create a new user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - phone_number
            - email
          properties:
            name:
              type: string
              example: Alice Brown
            phone_number:
              type: string
              example: "+380991234567"
            email:
              type: string
              example: alice@mail.com
            rating:
              type: number
              example: 4.8
    responses:
      201:
        description: User created successfully
    """
    body = CreateUserDTO.model_validate(request.get_json())
    user = UsersService.create_user(
        name=body.name,
        phone_number=body.phone_number,
        email=body.email,
        rating=body.rating
    )
    response = UserDTO.model_validate(user).model_dump()
    return jsonify(response), 201


@user_blueprint.put("/<int:id>")
def update_user(id: int):
    """
    Update user by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: User ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            phone_number:
              type: string
            email:
              type: string
            rating:
              type: number
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    body = CreateUserDTO.model_validate(request.get_json())
    user = UsersService.update_user(
        id=id,
        name=body.name,
        phone_number=body.phone_number,
        email=body.email,
        rating=body.rating
    )
    response = UserDTO.model_validate(user).model_dump()
    return jsonify(response)


@user_blueprint.delete("/<int:id>")
def delete_user(id: int):
    """
    Delete user by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    UsersService.delete_user(id=id)
    return jsonify({"detail": "User deleted successfully"})
