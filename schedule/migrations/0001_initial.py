
from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accessPoints', '0001_initial'),

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('access_point', models.ManyToManyField(to='accessPoints.accesspoint')),
            ],
        ),
    ]
