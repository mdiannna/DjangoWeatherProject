# Generated by Django 4.0.3 on 2022-03-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWeatherObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('temperature', models.IntegerField()),
                ('wind', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('weather_type', models.CharField(choices=[('SUN', 'sunny'), ('WIND', 'windy'), ('SNOW', 'snowy'), ('FOG', 'foggy'), ('RAIN', 'rainy'), ('WARM', 'warm'), ('COLD', 'cold'), ('-', 'undefined')], default='-', max_length=4)),
            ],
        ),
    ]
