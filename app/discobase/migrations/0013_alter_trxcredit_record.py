# Generated by Django 4.0.4 on 2022-06-13 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discobase', '0012_dump'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxcredit',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trx_credit', to='discobase.record'),
        ),
    ]
