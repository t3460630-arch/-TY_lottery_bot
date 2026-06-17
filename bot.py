from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

participants = set()

BOT_TOKEN = 8838413078:AAFWISiW-sboLmjndrCBqA8yj2uhsbt-9GU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 💜 ربات قرعه‌کشی روشنه")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id

    if user in participants:
        await update.message.reply_text("قبلاً وارد شدی ❌")
    else:
        participants.add(user)
        await update.message.reply_text("ثبت شدی ✔️")

async def draw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not participants:
        await update.message.reply_text("هیچ کسی نیست ❌")
        return

    winner = random.choice(list(participants))
    await update.message.reply_text(f"برنده 🎉: {winner}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("draw", draw))

app.run_polling()
