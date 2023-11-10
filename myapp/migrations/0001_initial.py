# Generated by Django 4.2 on 2023-11-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.TextField()),
                ('gstnumber', models.TextField()),
                ('mailreminder', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_detail_name', models.TextField()),
                ('user_detail_email', models.TextField()),
                ('user_detail_address', models.TextField()),
                ('user_detail_phone', models.TextField()),
                ('user_detail_otp', models.TextField()),
                ('user_detail_password', models.TextField()),
            ],
        ),
    ]
