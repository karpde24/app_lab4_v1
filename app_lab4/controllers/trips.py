from flask import Blueprint, jsonify, request

from services.trips import TripsService
from schemas.trips import TripDTO, CreateTripDTO

# Define the blueprint
trip_blueprint = Blueprint('trips', __name__, url_prefix='/trips')


@trip_blueprint.get("/")
def get_all_trips():
    """
    Get all trips
    ---
    tags:
      - Trips
    responses:
      200:
        description: List of trips
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
                example: 1
              start_time:
                type: string
                example: "2025-01-01 10:00:00"
              end_time:
                type: string
                example: "2025-01-01 10:45:00"
              price:
                type: number
                example: 250.50
              user_id:
                type: integer
                example: 3
              driver_id:
                type: integer
                example: 7
    """
    trips = TripsService.get_all_trips()
    response = [TripDTO.model_validate(trip).model_dump() for trip in trips]
    return jsonify(response)


@trip_blueprint.get("/<int:id>")
def get_trip(id: int):
    """
    Get trip by ID
    ---
    tags:
      - Trips
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Trip ID
    responses:
      200:
        description: Trip details
      404:
        description: Trip not found
    """
    trip = TripsService.get_trip_by_id(id=id)
    if not trip:
        return jsonify({"detail": "Trip not found"}), 404

    response = TripDTO.model_validate(trip).model_dump()
    return jsonify(response)


@trip_blueprint.post("/")
def create_trip():
    """
    Create a new trip
    ---
    tags:
      - Trips
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - start_time
            - end_time
            - price
            - user_id
            - driver_id
          properties:
            start_time:
              type: string
              example: "2025-01-01 10:00:00"
            end_time:
              type: string
              example: "2025-01-01 10:45:00"
            price:
              type: number
              example: 250.50
            user_id:
              type: integer
              example: 3
            driver_id:
              type: integer
              example: 7
    responses:
      201:
        description: Trip created successfully
    """
    body = CreateTripDTO.model_validate(request.get_json())
    trip = TripsService().create_trip(
        start_time=body.start_time,
        end_time=body.end_time,
        price=body.price,
        user_id=body.user_id,
        driver_id=body.driver_id
    )
    response = TripDTO.model_validate(trip).model_dump()
    return jsonify(response), 201


@trip_blueprint.put("/<int:id>")
def update_trip(id: int):
    """
    Update trip by ID
    ---
    tags:
      - Trips
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Trip ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            start_time:
              type: string
            end_time:
              type: string
            price:
              type: number
            user_id:
              type: integer
            driver_id:
              type: integer
    responses:
      200:
        description: Trip updated successfully
      404:
        description: Trip not found
    """
    body = CreateTripDTO.model_validate(request.get_json())
    trip = TripsService().update_trip(
        id=id,
        start_time=body.start_time,
        end_time=body.end_time,
        price=body.price,
        user_id=body.user_id,
        driver_id=body.driver_id
    )
    response = TripDTO.model_validate(trip).model_dump()
    return jsonify(response)


@trip_blueprint.delete("/<int:id>")
def delete_trip(id: int):
    """
    Delete trip by ID
    ---
    tags:
      - Trips
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Trip ID
    responses:
      200:
        description: Trip deleted successfully
      404:
        description: Trip not found
    """
    TripsService.delete_trip(id=id)
    return jsonify({"detail": "Trip deleted successfully"})
