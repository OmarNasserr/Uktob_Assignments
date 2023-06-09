from flask import Flask
from api.routes import api_bp

# creates an instance of the Flask application. It initializes a Flask object that represents the web application.
app = Flask(__name__)

# Register the Blueprint (A blueprint defines a collection of routes and views that are associated with a
#                         specific part of your application. It provides a way to encapsulate related functionality 
#                         and separate concerns within your application.)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
