from flask import Blueprint, Flask, jsonify, request
from api.utils import RequestValidation, JSONValidation, Authvalidation
from api.status_codes import StatusCodes

# creating a blueprint named 'api' and assigning it to the variable api_bp.
api_bp = Blueprint('api', __name__)

# This dictionary stands-in for a database
users_db = {}

@api_bp.route('/register', methods=['POST'])
def register():
    try:
        # Validates the presence of 'Content-Type' = 'application/json' in the request headers. If not found,
        # it adds the 'Content-Type' header with the value 'application/json', making it more user-friendly.
        RequestValidation.validate_request_headers()
        
        # validates that the JSON object was parsed successfully
        data=JSONValidation.validate_json(request) 
        
        # validates the presence of the keys 'username' and 'password' in the given data JSON dictionary.
        Authvalidation.validate_auth_keys(data)
        
        username = data.get('username')
        password = data.get('password')
        
        # checks if a user with the same username exists in the database
        Authvalidation.check_user_exist(username,users_db)
        
        users_db[username] = password
        return jsonify({'message': 'Registration successful.','status_code':StatusCodes.success})
    except (KeyError, ValueError) as e:
        return jsonify({'error':str(e), 'status_code': StatusCodes.bad_request})


@api_bp.route('/login', methods=['POST'])
def login():
    
    try:
        # Validates the presence of 'Content-Type' = 'application/json' in the request headers. If not found,
        # it adds the 'Content-Type' header with the value 'application/json', making it more user-friendly.
        RequestValidation.validate_request_headers()

        # validates that the JSON object was parsed successfully
        data=JSONValidation.validate_json(request) 
        
        # validates the presence of the keys 'username' and 'password' in the given data JSON dictionary.
        Authvalidation.validate_auth_keys(data)
        
        username = data.get('username')
        password = data.get('password')
        
        # checks if the given username exists in the database, then checks if the given password is 
        # the same as the stored password. multiple checks are performed to return the correct message.        
        response=Authvalidation.login_validation(username, password,users_db)
        
        return response
    except (KeyError, ValueError) as e:
        return jsonify({'error':str(e), 'status_code': StatusCodes.bad_request})