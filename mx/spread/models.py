from django.db import models


class Quote(models.Model):
    ticker = models.CharField(max_length=50)
    spot_price = models.DecimalField(max_digits=10, decimal_places=3)
    perp_price = models.DecimalField(max_digits=10, decimal_places=3)
    quart_price = models.DecimalField(max_digits=10, decimal_places=3)
    spread = models.DecimalField(max_digits=10, decimal_places=3)

