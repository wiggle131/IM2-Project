# Generated by Django 3.1.1 on 2020-09-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_customer_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
