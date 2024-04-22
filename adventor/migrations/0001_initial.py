# Generated by Django 4.2.11 on 2024-04-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventOrganizerForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_start_datetime', models.DateTimeField()),
                ('event_closing_datetime', models.DateTimeField()),
                ('gate_opening_time', models.TimeField()),
                ('event_location', models.CharField(max_length=200)),
                ('event_organizer_name', models.CharField(max_length=200)),
                ('event_banner_image', models.ImageField(upload_to='event_banners/')),
                ('location_google_map_url', models.URLField()),
            ],
        ),
    ]
