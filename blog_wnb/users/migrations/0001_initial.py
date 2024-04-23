# Generated by Django 5.0.4 on 2024-04-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/')),
            ],
        ),
    ]