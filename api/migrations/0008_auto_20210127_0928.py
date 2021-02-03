# Generated by Django 3.1.5 on 2021-01-27 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.film'),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=32)),
                ('l_name', models.CharField(max_length=32)),
                ('movies', models.ManyToManyField(to='api.Film')),
            ],
        ),
    ]
