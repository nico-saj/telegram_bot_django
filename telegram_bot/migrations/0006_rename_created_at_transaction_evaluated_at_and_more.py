# Generated by Django 5.1.1 on 2024-10-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0005_transaction_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='created_at',
            new_name='evaluated_at',
        ),
        migrations.AddField(
            model_name='transaction',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
