from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Hello! I'm the Rocket Launch Bot.\nI'll help you find the exact moment of launch!")

def get_handlers():
    return [
        CommandHandler("start", start),
    ]
