# Generated by Django 5.0.1 on 2024-01-16 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='division',
            old_name='screensize',
            new_name='screen',
        ),
    ]