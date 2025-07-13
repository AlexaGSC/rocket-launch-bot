from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from bot.handlers import get_handlers


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    for handler in get_handlers():
        app.add_handler(handler)

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
