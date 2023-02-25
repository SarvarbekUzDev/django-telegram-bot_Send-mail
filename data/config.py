from dotenv import load_dotenv, dotenv_values

env = dotenv_values(".env")

# ---- Read data ----
# Bot token, admins, ip
BOT_TOKEN = env.get("BOT_TOKEN")
ADMINS = list(env.get("ADMINS").split(","))
IP = env.get("IP")
NGROK_URL = env.get("NGROK_URL")

# Email backend
EMAIL_HOST_USER = env.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587

RECEIVING_MAILS = list(env.get("RECEIVING_MAILS").split(","))