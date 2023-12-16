from dotenv import load_dotenv
import os 

load_dotenv()
print(os.environ.get('LOGIN1'))
print(os.environ.get('LOGIN2'))

# Использовать переменные окружения в коде
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

