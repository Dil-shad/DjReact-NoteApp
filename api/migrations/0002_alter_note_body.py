# Generated by Django 4.2.4 on 2023-08-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
