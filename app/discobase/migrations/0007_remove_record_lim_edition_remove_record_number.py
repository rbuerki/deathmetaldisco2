# Generated by Django 4.0.4 on 2022-06-10 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discobase', '0006_alter_artist_artist_name_alter_country_country_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='lim_edition',
        ),
        migrations.RemoveField(
            model_name='record',
            name='number',
        ),
    ]