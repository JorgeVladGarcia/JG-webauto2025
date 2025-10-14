import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# set base URL
BASE_URL = {
    "development": "https://casaideas.com.bo",
    "staging": "http://staging.casaideas.com.bo",
    "production": "http://production.casaideas.com.bo"
}