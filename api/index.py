from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

def generate_user_id(full_name):
    current_date = datetime.now()
    date_string = current_date.strftime("%d%m%Y")
    return f"{full_name.lower()}_{date_string}"

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_alphabet(string):
    return string.isalpha()

def is_special_character(string):
    return len(string) == 1 and not string.isalnum()

def process_array(data_array):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    numbers_sum = 0
    all_alphabets = []
    
    for item in data_array:
        if is_number(item):
            num = float(item)
            if num.is_integer():
                num = int(num)
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
                numbers_sum += num
        elif is_alphabet(item):
            alphabets.append(item.upper())
            all_alphabets.extend(list(item))
        elif is_special_character(item):
            special_characters.append(item)
    
    all_alphabets.reverse()
    concat_string = ""
    for i, char in enumerate(all_alphabets):
        if i % 2 == 0:
            concat_string += char.upper()
        else:
            concat_string += char.lower()
    
    return {
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(numbers_sum),
        "concat_string": concat_string
    }

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        request_data = request.get_json()
        
        if not request_data or 'data' not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Missing 'data' field in request"
            }), 400
        
        data_array = request_data['data']
        
        if not isinstance(data_array, list):
            return jsonify({
                "is_success": False,
                "error": "'data' must be an array"
            }), 400
        
        processed_data = process_array(data_array)
        
        response = {
            "is_success": True,
            "user_id": "akshat_kumar_17091999",
            "email": "akshat@xyz.com",
            "roll_number": "ABCD123",
            "odd_numbers": processed_data["odd_numbers"],
            "even_numbers": processed_data["even_numbers"],
            "alphabets": processed_data["alphabets"],
            "special_characters": processed_data["special_characters"],
            "sum": processed_data["sum"],
            "concat_string": processed_data["concat_string"]
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

@app.route('/')
def home():
    return jsonify({
        "message": "BFHL API is running",
        "endpoint": "/bfhl",
        "method": "POST"
    })

if __name__ == '__main__':
    app.run(debug=True)