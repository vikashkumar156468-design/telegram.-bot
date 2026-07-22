from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")  # Render par BOT_TOKEN environment variable set karna

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\nMain Auto Reply Bot hoon."
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "hi":
        reply = "Hello! 👋"
    elif text == "hello":
        reply = "Hi! Kaise ho? 😊"
    elif text == "bye":
        reply = "Bye! 👋"
    else:
        reply = "✅ Aapka message mil gaya."

    await update.message.reply_text(reply)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

app.run_polling()
