# Generated by Django 3.2.3 on 2021-05-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rights',
            field=models.PositiveIntegerField(blank=True, choices=[(9, 'full'), (5, 'normal'), (0, 'simple')], null=True),
        ),
    ]