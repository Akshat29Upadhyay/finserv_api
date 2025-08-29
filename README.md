# BFHL API

A REST API that processes arrays and returns categorized data including numbers, alphabets, and special characters.

## Features

- Processes arrays containing mixed data types
- Categorizes numbers into even and odd
- Converts alphabets to uppercase
- Identifies special characters
- Calculates sum of numbers
- Creates concatenated string with alternating case
- Returns user information with proper formatting

## API Endpoint

**POST** `/bfhl`

### Request Format

```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

### Response Format

```json
{
  "is_success": true,
  "user_id": "akshat_kumar_17091999",
  "email": "akshat@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Testing with cURL

### Local Testing (when running locally)
```bash
# Start the server first: python api/index.py
# Then use these commands:

# Test Case 1: Example A
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R", "$"]}'

# Test Case 2: Example B
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]}'

# Test Case 3: Example C
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["A","ABcD","DOE"]}'

# Test Case 4: Mixed data with decimals
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["10.5","abc","@","7","XYZ","#","42"]}'

# Test Case 5: Only numbers
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["1","2","3","4","5","6","7","8","9","10"]}'

# Test Case 6: Only alphabets
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["hello","WORLD","python","API"]}'

# Test Case 7: Only special characters
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["@","#","$","%","&","*","!","?"]}'

# Test Case 8: Empty array
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": []}'
```

### Deployed Testing (replace with your actual deployed URL)
```bash
# Replace YOUR_DEPLOYED_URL with your actual Vercel/Railway/Render URL
# Example: https://your-app.vercel.app

# Test Case 1: Example A
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R", "$"]}'

# Test Case 2: Example B
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]}'

# Test Case 3: Example C
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["A","ABcD","DOE"]}'

# Test Case 4: Mixed data with decimals
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["10.5","abc","@","7","XYZ","#","42"]}'

# Test Case 5: Only numbers
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["1","2","3","4","5","6","7","8","9","10"]}'

# Test Case 6: Only alphabets
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["hello","WORLD","python","API"]}'

# Test Case 7: Only special characters
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["@","#","$","%","&","*","!","?"]}'

# Test Case 8: Empty array
curl -X POST https://YOUR_DEPLOYED_URL/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": []}'
```

### Error Testing
```bash
# Test missing data field
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{}'

# Test invalid data type (not array)
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": "not an array"}'

# Test malformed JSON
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a", "b", "c"'
```

## Expected Responses

### Example 1
**Request:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "akshat_kumar_17091999",
  "email": "akshat@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

### Example 2
**Request:**
```json
{
  "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "akshat_kumar_17091999",
  "email": "akshat@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["5"],
  "even_numbers": ["2", "4", "92"],
  "alphabets": ["A", "Y", "B"],
  "special_characters": ["&", "-", "*"],
  "sum": "103",
  "concat_string": "ByA"
}
```

### Example 3
**Request:**
```json
{
  "data": ["A", "ABcD", "DOE"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "akshat_kumar_17091999",
  "email": "akshat@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": [],
  "even_numbers": [],
  "alphabets": ["A", "ABCD", "DOE"],
  "special_characters": [],
  "sum": "0",
  "concat_string": "EoDdCbAa"
}
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python api/index.py
```

3. The API will be available at `http://localhost:5000`

## Deployment

This API is configured for deployment on Vercel. The `vercel.json` file contains the necessary configuration for routing all requests to the Flask application.

## Error Handling

The API includes comprehensive error handling for:
- Missing or invalid request data
- Malformed JSON
- Server errors

All errors return appropriate HTTP status codes and error messages.
