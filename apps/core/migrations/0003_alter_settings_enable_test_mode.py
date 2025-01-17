# Generated by Django 5.0.3 on 2024-09-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_settings_show_products_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='enable_test_mode',
            field=models.BooleanField(default=True, help_text='Tryb testowy pozwala na wymianę WSZYSTKICH danych w bazie danych (w celach pokazowych', verbose_name='Włącz tryb testowy'),
        ),
    ]
