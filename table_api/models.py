from django.db import models


CATEGORY_CHOICES = (
    ('Bill payment','1'),
    ('Withdrawal', '2'),
    ('Commissions','3'),
    ('Transfers','4'),
    ('Airtime/Data','5'),
    ('FX Transactions', '6'),
    ('Others', '7'),
    ('Salaries & wages', '8'),
    ('Interest & Dividends', '9')
)

SUB_CATEGORY_CHOICES = (
    ('Food', '1'),
    ('Internet Services', '2'),
    ('Shopping', '5'),
    ('Cash Withdrawal', '7'),
    ('ATM Withdrawal', '8'),
    ('Web Transactions', '12')
)


class Service(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='Bill payment')
    sub_category = models.CharField(max_length=25, choices=SUB_CATEGORY_CHOICES, default='Food')
    description = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)



    def __str__(self):
        return self.name
