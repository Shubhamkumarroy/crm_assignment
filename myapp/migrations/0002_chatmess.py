# Generated by Django 4.2 on 2023-11-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.TextField()),
                ('receiver_email', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
