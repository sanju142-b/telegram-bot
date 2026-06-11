import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8765834694:AAFvhGf-jmzLnGE9NPxu5cYiPtJaJwnLkXw"

API_URL = "https://indianmethods-api.vercel.app/api/search?number="

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ready 🚀")

async def num(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("API calling...")

    if not context.args:
        await update.message.reply_text("Usage: /num 9063545727")
        return

    num_id = context.args[0]

    try:
        print("URL:", API_URL + num_id)

        r = requests.get(API_URL + num_id)

        await update.message.reply_text(r.text)

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("num", num))

print("Bot running...")
app.run_polling()