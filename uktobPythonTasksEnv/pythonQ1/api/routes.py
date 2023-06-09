from flask import Blueprint, Flask, jsonify, request
from api.utils import SumNumbersValidation, RequestValidation, ConcStringsValidation
from .status_codes import StatusCodes

# creating a blueprint named 'api' and assigning it to the variable api_bp.
api_bp = Blueprint('api', __name__)

# access the api POST request on http://127.0.0.1:5000/sum 
# body should look like 
@api_bp.route('/sum', methods=['POST'])
def sum_numbers():  
    try:
        
        # Validates the presence of 'Content-Type' = 'application/json' in the request headers. If not found,
        # it adds the 'Content-Type' header with the value 'application/json', making it more user-friendly.
        RequestValidation.validate_request_headers()
        
        # validates that the JSON object was parsed successfully
        data=SumNumbersValidation.validate_json(request)
            
        # validates the presence of the key 'list_of_numbers' in the given data JSON dictionary. 
        numbers = SumNumbersValidation.validate_get_numbers_key(data)
        
        # checks whether the numbers parameter is a list 
        # and whether all elements in the list are either integers or floats (decimals).
        SumNumbersValidation.validate_numbers(numbers)
    
        total = sum(numbers)
        return jsonify({'result': total,'status_code':StatusCodes.success})
    
    except (KeyError, ValueError) as e:
        return {'error':str(e), 'status_code': StatusCodes.bad_request}



@api_bp.route('/concatenate', methods=['POST'])
def concatenate_strings():
    try:
        # Validates the presence of 'Content-Type' = 'application/json' in the request headers. If not found,
        # it adds the 'Content-Type' header with the value 'application/json', making it more user-friendly.
        RequestValidation.validate_request_headers()
        
        ## validates that the JSON object was parsed successfully
        data=ConcStringsValidation.validate_json(request)
        
        # validates the presence of the keys 'string1' and 'string2' in the given data JSON dictionary. 
        ConcStringsValidation.validate_get_strings_keys(data)
        
        string1 = data['string1']
        string2 = data['string2']
        
        # validate that both keys values are strings
        ConcStringsValidation.validate_strings(string1, string2)
        
        # add both strings
        result = string1 + string2
        return jsonify({'result': result,'status_code':StatusCodes.success})
    
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e), 'status_code': StatusCodes.bad_request})
