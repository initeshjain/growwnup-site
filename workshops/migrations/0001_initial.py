# Generated by Django 3.1.7 on 2021-07-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Workshop Title')),
                ('desc', models.CharField(max_length=2000, verbose_name='Description')),
                ('price', models.CharField(max_length=5, verbose_name='Price Per Entry')),
                ('banner', models.ImageField(upload_to='static/workshops_images')),
            ],
        ),
    ]
