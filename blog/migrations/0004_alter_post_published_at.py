# Generated by Django 3.2.25 on 2024-05-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240504_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
