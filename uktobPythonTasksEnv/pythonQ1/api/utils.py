from flask import jsonify,request


# Validates the presence of 'Content-Type' = 'application/json' in the request headers. If not found,
# it adds the 'Content-Type' header with the value 'application/json', making it more user-friendly.
class RequestValidation():
    def validate_request_headers():
        if 'Content-Type' not in request.headers or request.headers.get('Content-Type') != 'application/json':
                request.environ['CONTENT_TYPE'] = 'application/json'

class SumNumbersValidation():

    # validates that the JSON object was parsed successfully
    def validate_json(request_sent):
        try:
            return request_sent.get_json()
        except:
            raise ValueError('Invalid input. list of numbers must contain only Integers or Decimals')
    
    
    # validates the presence of the key 'list_of_numbers' in the given data dictionary. 
    def validate_get_numbers_key(data):
        if 'list_of_numbers' not in data:
            raise ValueError("The request body must include a key named 'list of numbers'.")
        else:
            return data.get('list_of_numbers')

    # checks whether the numbers parameter is a list 
    # and whether all elements in the list are either integers or floats (decimals).
    def validate_numbers(numbers):
        if not isinstance(numbers, list):
            raise ValueError('Input should be a list of numbers')
        for num in numbers:
            if not isinstance(num, (int,float)):
                raise ValueError('Input should be a list of Integers or Decimals')
                
class ConcStringsValidation():
    
    # validates that the JSON object was parsed successfully
    def validate_json(request_sent):
        try:
            return request_sent.get_json()
        except:
            raise ValueError('Invalid JSON in the request body')
    
    # validates the presence of the keys 'string1' and 'string2' in the given data JSON dictionary. 
    def validate_get_strings_keys(data):
        if 'string1' not in data or 'string2' not in data:
            raise ValueError("The request body must include keys named 'string1' and 'string2")

    # validate that both keys values are strings
    def validate_strings(string1, string2):
        if not isinstance(string1, str) or not isinstance(string2, str):
            raise ValueError("Both string1 and string2 must be of type string")
        
    
    
        