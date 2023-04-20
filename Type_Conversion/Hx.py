import requests
import json

# Set the IP address of the Cisco HyperFlex cluster
hyperflex_ip = '192.168.1.100'

# Set the username and password to authenticate with the cluster
username = 'admin'
password = 'password'

# Create a session object and authenticate with the cluster
session = requests.Session()
session.auth = (username, password)

# Set the API endpoint for retrieving HyperFlex node information
api_endpoint = f'https://{hyperflex_ip}/anp/v1/hyperflex/nodes'

# Make the API request and store the response
response = session.get(api_endpoint)

# Parse the JSON response and print the list of nodes
nodes = json.loads(response.content)
for node in nodes:
    print(node['name'])