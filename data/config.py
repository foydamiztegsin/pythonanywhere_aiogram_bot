                                                                          
from dotenv import load_dotenv
import os
import json


load_dotenv()



PROXY_URL = os.environ.get("PROXY_URL")  # Bot uchun proxy
BOT_TOKEN = os.environ.get("BOT_TOKEN") # Bot token
ADMINS = json.loads(os.environ["ADMINS"]) # Adminlar 
