from flask import Flask
from flasgger import Swagger

from controllers.drivers import driver_blueprint
from controllers.trips import trip_blueprint
from controllers.users import user_blueprint

app = Flask(__name__)

# 🔹 Swagger configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Lab4 Flask API",
        "description": "API for managing users, drivers and trips",
        "version": "1.0.0"
    }
}

Swagger(app, config=swagger_config, template=swagger_template)

# 🔹 Register blueprints (url_prefix already inside blueprints)
app.register_blueprint(user_blueprint)
app.register_blueprint(driver_blueprint)
app.register_blueprint(trip_blueprint)


@app.route("/")
def index():
    return "Welcome to the Lab4 Flask API", 200


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)
