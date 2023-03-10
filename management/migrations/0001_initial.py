# Generated by Django 4.1.3 on 2022-12-02 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Earning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('One Time', 'One Time'), ('Weekly', 'Weekly'), ('Bi-Weekly', 'Bi-Weekly'), ('Monthly', 'Monthly'), ('Annually', 'Annually')], default='One Time', max_length=100)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('payment_start_date', models.DateField()),
                ('payment_end_date', models.DateField(blank=True, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
