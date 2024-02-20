import asyncio
import sys
import threading
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ) )

from ...telegram_bot.bot import start_telegram_bot
from ...update_quotes import update_quote
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        update_thread = threading.Thread(target=asyncio.run(update_quote()))
        bot_thread = threading.Thread(target=asyncio.run(start_telegram_bot()))
        update_thread.start()
        bot_thread.start()