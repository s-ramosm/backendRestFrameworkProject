# Generated by Django 4.0.5 on 2022-08-31 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('states', '0001_initial'),
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('nit', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('comercial_name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=50)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
        ),
    ]
