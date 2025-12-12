from flask import Blueprint, jsonify, request
from services.drivers import DriversService
from schemas.drivers import DriverDTO, CreateDriverDTO
from schemas.trips import DriverWithTripDTO

# Define the blueprint
driver_blueprint = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_blueprint.get("/")
def get_all_drivers():
    """
    Get all drivers
    ---
    tags:
      - Drivers
    responses:
      200:
        description: List of drivers
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: John Smith
              licence_number:
                type: string
                example: ABC12345
              phone_number:
                type: string
                example: "+380991234567"
              rating:
                type: number
                example: 4.8
              experince_years:
                type: integer
                example: 5
              status:
                type: string
                example: active
    """
    drivers = DriversService.get_all_drivers()
    response = [
        DriverWithTripDTO.model_validate(driver.__dict__).model_dump()
        for driver in drivers
    ]
    return jsonify(response)


@driver_blueprint.get("/<int:id>")
def get_driver(id: int):
    """
    Get driver by ID
    ---
    tags:
      - Drivers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Driver ID
    responses:
      200:
        description: Driver details
      404:
        description: Driver not found
    """
    driver = DriversService.get_driver_by_id(id=id)
    response = DriverWithTripDTO.model_validate(driver.__dict__).model_dump()
    return jsonify(response)


@driver_blueprint.post("/")
def create_driver():
    """
    Create a new driver
    ---
    tags:
      - Drivers
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - licence_number
            - phone_number
          properties:
            name:
              type: string
              example: John Smith
            licence_number:
              type: string
              example: ABC12345
            phone_number:
              type: string
              example: "+380991234567"
            rating:
              type: number
              example: 4.9
            experince_years:
              type: integer
              example: 7
            status:
              type: string
              example: active
    responses:
      201:
        description: Driver created successfully
    """
    body = CreateDriverDTO.model_validate(request.get_json())
    driver = DriversService.create_driver(
        name=body.name,
        licence_number=body.licence_number,
        phone_number=body.phone_number,
        rating=body.rating,
        experince_years=body.experince_years,
        status=body.status
    )
    response = DriverDTO.model_validate(driver.__dict__).model_dump()
    return jsonify(response), 201


@driver_blueprint.put("/<int:id>")
def update_driver(id: int):
    """
    Update driver by ID
    ---
    tags:
      - Drivers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Driver ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            licence_number:
              type: string
            phone_number:
              type: string
            rating:
              type: number
            experince_years:
              type: integer
            status:
              type: string
    responses:
      200:
        description: Driver updated successfully
      404:
        description: Driver not found
    """
    body = CreateDriverDTO.model_validate(request.get_json())
    driver = DriversService.update_driver(
        id=id,
        name=body.name,
        licence_number=body.licence_number,
        phone_number=body.phone_number,
        rating=body.rating,
        experince_years=body.experince_years,
        status=body.status
    )
    response = DriverDTO.model_validate(driver.__dict__).model_dump()
    return jsonify(response)


@driver_blueprint.delete("/<int:id>")
def delete_driver(id: int):
    """
    Delete driver by ID
    ---
    tags:
      - Drivers
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Driver ID
    responses:
      200:
        description: Driver deleted successfully
      404:
        description: Driver not found
    """
    DriversService.delete_driver(id=id)
    return jsonify({"detail": "Driver deleted successfully"})
