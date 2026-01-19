import streamlit as st
import random
import time
import requests
import json

# 1. Configuration
url = "https://FINCAN-POC.snowflakecomputing.com/api/v2/databases/TAX_POLICY/schemas/GST/agents/TESTAGENT:run"
api_key = "{TEST_KEY}" # Replace with your actual JWT

# 2. Define Headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Snowflake-Authorization-Token-Type": "KEYPAIR_JWT"
}

# 3. Define the Request Body
data = {
    "name": "testify",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What was the total revenue by region last quarter?"
                }
            ]
        }
    ]
}

# 4. Execute the POST Request
try:
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Parse and print the JSON response
    result = response.json()
    st.write(json.dumps(result, indent=4))

except requests.exceptions.HTTPError as err:
    st.write(f"HTTP Error: {err}")
    st.write(f"Response: {response.text}")
except Exception as e:
    st.write(f"An error occurred: {e}")
