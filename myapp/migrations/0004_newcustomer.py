# Generated by Django 4.2 on 2023-11-17 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_detail_check_admin_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newcustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.TextField()),
                ('gstnumber', models.TextField()),
                ('mailreminder', models.TextField()),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newcustomers', to='myapp.user_detail')),
            ],
        ),
    ]
