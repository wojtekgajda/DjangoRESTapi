# Generated by Django 3.1.5 on 2021-01-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210126_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='type',
            field=models.TextField(choices=[('Unknown', 'Unknown'), ('Sci-fi', 'Sci-fi'), ('Horror', 'Horror'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Document', 'Document')]),
        ),
    ]
