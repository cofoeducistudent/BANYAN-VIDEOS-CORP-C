# Generated by Django 3.1.2 on 2020-11-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_account', '0003_userpurchasehistory_ph_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpurchasehistory',
            name='ph_transaction_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
