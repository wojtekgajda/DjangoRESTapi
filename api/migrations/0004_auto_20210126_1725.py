# Generated by Django 3.1.5 on 2021-01-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210126_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('type', models.IntegerField(choices=[(2, 'Horror'), (1, 'Sci-fi'), (5, 'Document'), (3, 'Drama'), (0, 'Unknown'), (4, 'Comedy')], default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='additional_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalinfo'),
        ),
        migrations.DeleteModel(
            name='Additional_Info',
        ),
    ]