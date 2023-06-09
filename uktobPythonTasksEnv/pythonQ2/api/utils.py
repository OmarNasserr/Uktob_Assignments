from flask import jsonify,request

from api.status_codes import StatusCodes

# Validates the presence of 'Content-Type' = 'application/json' in the request headers. If not found,
# it adds the 'Content-Type' header with the value 'application/json', making it more user-friendly.
class RequestValidation():
    def validate_request_headers():
        if 'Content-Type' not in request.headers or request.headers.get('Content-Type') != 'application/json':
                request.environ['CONTENT_TYPE'] = 'application/json'


class JSONValidation():
    # validates that the JSON object was parsed successfully
    def validate_json(request_sent):
        try:
            return request_sent.get_json()
        except:
            raise ValueError('Invalid JSON in the request body')
        

class Authvalidation():
    
    # validates the presence of the keys 'username' and 'password' in the given data JSON dictionary. 
    def validate_auth_keys(data):
        if 'username' not in data or 'password' not in data:
            raise ValueError("The request body must include keys named 'username' and 'password")
        
    # checks if a user with the same username exists in the database
    def check_user_exist(username,users_db):
        if username in users_db.keys():
             raise ValueError('This username is already taken by another user.')
    
    # checks if the given username exists in the database, then checks if the given password is 
    # the same as the stored password. multiple checks are performed to return the correct message.
    def login_validation(username,password,users_db):
        if username in users_db.keys():
            stored_password = users_db.get(username)
            if stored_password == password:
                return jsonify({'message': 'Login successful. Access granted.','status_code':StatusCodes.success})
            else:
                return jsonify({'message': 'Incorrect password. Please try again.',
                                'status_code': StatusCodes.bad_request})
        else:
            return jsonify({'message': 'No user exist with this username', 
                            'status_code': StatusCodes.bad_request})
