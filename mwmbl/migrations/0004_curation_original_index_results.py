# Generated by Django 4.2.6 on 2023-12-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mwmbl', '0003_auto_20231203_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='curation',
            name='original_index_results',
            field=models.JSONField(default=list),
        ),
    ]
