import asyncio
import sys
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ) )

from spread.telegram_bot.bot import start_telegram_bot
from spread.update_quotes import update_quote
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        asyncio.run(update_quote())
        start_telegram_bot()