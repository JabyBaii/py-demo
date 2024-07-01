from django.db import models

class Transaction(models.Model):
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category_code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)
    order_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.pk}"