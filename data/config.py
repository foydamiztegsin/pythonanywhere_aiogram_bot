from dotenv import load_dotenv
import os


load_dotenv()

# .env fayl ichidan quyidagilarni o'qiymiz
PROXY_URL = os.environ.get("PROXY_URL")  # Bot uchun proxy
BOT_TOKEN = os.environ.get("BOT_TOKEN") # Bot token
ADMINS = os.environ.get("ADMINS")  # adminlar ro'yxati

