import os
import sys
import django
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import sys

# Step 1: Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

# Step 2: Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_api.settings')

# Step 3: Setup Django
import django
django.setup()

'''from app_api.models import TelegramUser

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    TelegramUser.objects.get_or_create(username=username)
    await update.message.reply_text(f"Hi {username}, I've saved your username!")

if __name__ == '__main__':
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()


'''