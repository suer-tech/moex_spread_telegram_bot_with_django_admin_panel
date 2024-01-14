from django.core.management.base import BaseCommand

from mx.spread.update_quotes import update_quote


class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        update_quote()
        # start_telegram_bot()