from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    skin_type = models.CharField(
        max_length=20,
        choices=[
            ('Normal', 'Normal'),
            ('Oily', 'Oily'),
            ('Dry', 'Dry'),
            ('Combination', 'Combination'),
            ('Sensitive', 'Sensitive'),
        ]
    )
    skin_issues = models.TextField()  # Store as a comma-separated string

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)  # For 2-3 lines of text
    skin_type = models.CharField(
        max_length=20,
        choices=[
            ('Normal', 'Normal'),
            ('Oily', 'Oily'),
            ('Dry', 'Dry'),
            ('Combination', 'Combination'),
            ('Sensitive', 'Sensitive'),
        ]
    )
    skin_issues = models.TextField()  # Store as a comma-separated string
    price = models.DecimalField(max_digits=10, decimal_places=2)  # For product price

    def __str__(self):
        return self.name