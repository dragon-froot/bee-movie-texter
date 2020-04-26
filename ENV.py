import os

# set env variables
os.environ['API_USERNAME'] = ''
os.environ['API_TOKEN'] = ''

# Get env variables
USER = os.getenv('API_USERNAME')
TOKEN = os.environ.get('API_TOKEN')