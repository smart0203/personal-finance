# Generated by Django 4.1.3 on 2022-12-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='earning',
            name='investment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='management.investment'),
        ),
        migrations.AddField(
            model_name='expense',
            name='debt',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='debts', to='management.debt'),
        ),
    ]
