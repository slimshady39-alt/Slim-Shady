#!/usr/bin/env python3
"""Simple echo Telegram bot"""

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo back the user's message"""
    await update.message.reply_text(update.message.text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text("Hello! I'm alive! Send me a message and I'll echo it back.")

def main():
    """Run the bot"""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set!")
        return

    app = ApplicationBuilder().token(token).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Bot started!")
    app.run_polling()

if __name__ == "__main__":
    from telegram.ext import CommandHandler
    main()
