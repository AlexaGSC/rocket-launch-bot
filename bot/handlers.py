from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
)
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler,
)
from bot.bisector import FrameXBisector
import io

user_sessions = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Hello! I'm the Rocket Launch Bot.\n"
        "Send /launch to start the search!"
    )

async def launch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bisector = FrameXBisector("Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c")
    user_sessions[user_id] = bisector
    bisector.index = bisector.count // 2
    await send_frame(update, bisector)

async def send_frame(update_or_query, bisector: FrameXBisector):
    bio = io.BytesIO(bisector.image_data)
    bio.name = "frame.jpg"
    bio.seek(0)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Sí, ya despegó", callback_data="yes")],
        [InlineKeyboardButton("🕒 No, aún no", callback_data="no")],
    ])

    if isinstance(update_or_query, Update):
        await update_or_query.message.reply_photo(
            photo=bio,
            caption=f"Frame {bisector.index} – ¿Ha despegado el cohete?",
            reply_markup=keyboard,
        )
    else:
        await update_or_query.edit_message_media(
            media=InputMediaPhoto(
                bio,
                caption=f"Frame {bisector.index} – ¿Ha despegado el cohete?",
            ),
            reply_markup=keyboard,
        )

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    bisector = user_sessions.get(user_id)

    if not bisector:
        await query.edit_message_text(
            "No hay una búsqueda activa. Envía /launch para comenzar."
        )
        return

    answer = query.data
    current = bisector.index

    if not hasattr(bisector, "left"):
        bisector.left = 0
        bisector.right = bisector.count - 1

    if answer == "yes":
        bisector.right = current
    else:
        bisector.left = current + 1

    if bisector.left >= bisector.right:
        await query.edit_message_caption(
            caption=f"¡El cohete despegó en el frame {bisector.right}!"
        )
        del user_sessions[user_id]
        return

    bisector.index = (bisector.left + bisector.right) // 2
    await send_frame(query, bisector)

def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("launch", launch),
        CallbackQueryHandler(handle_response),
    ]
