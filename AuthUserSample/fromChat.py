import requests

# Replace these with your actual credentials and environment URL
CLIENT_ID = 'ADOT_PROD_6fc1f6b8c8d847c48747e2b7255c7d96'
CLIENT_SECRET = 'f1ceff23ba334359b9d11bfc6825a0352b7d95f454c24988a12b90f976b19408'
ENVIRONMENT_URL = 'https://adot.sumtotal.host/rcore/c/'  # e.g., https://au04sales.sumtotaldevelopment.net

# OAuth 2.0 token endpoint
TOKEN_URL = f'{ENVIRONMENT_URL}/apisecurity/connect/token'

# Request payload
payload = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': 'allapis'  # or 'odataapis' if you're accessing OData APIs
}

# Request headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Make the POST request to obtain the access token
response = requests.post(TOKEN_URL, data=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print('Access token obtained successfully.')
else:
    print(f'Failed to obtain access token. Status code: {response.status_code}')
    print(f'Response: {response.text}')
    exit()




# API endpoint to retrieve users
USERS_API_URL = f'{ENVIRONMENT_URL}/apis/api/v1/users'

# Authorization header with the obtained access token
auth_headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make the GET request to retrieve users
users_response = requests.get(USERS_API_URL, headers=auth_headers)

# Check if the request was successful
if users_response.status_code == 200:
    users_data = users_response.json()
    print('Users retrieved successfully:')
    print(users_data)
else:
    print(f'Failed to retrieve users. Status code: {users_response.status_code}')
    print(f'Response: {users_response.text}')


