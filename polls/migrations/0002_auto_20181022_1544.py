# Generated by Django 2.0.9 on 2018-10-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frage',
            old_name='question_text',
            new_name='frage_text',
        ),
    ]
