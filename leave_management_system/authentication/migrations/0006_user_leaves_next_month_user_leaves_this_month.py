# Generated by Django 5.2.1 on 2025-06-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_senior_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='leaves_next_month',
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.AddField(
            model_name='user',
            name='leaves_this_month',
            field=models.PositiveIntegerField(default=4),
        ),
    ]
