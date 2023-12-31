# Generated by Django 4.2.5 on 2023-09-30 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='customer',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='location',
            new_name='location_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='booking',
            new_name='booking_id',
        ),
        migrations.RemoveField(
            model_name='travellist',
            name='activities',
        ),
        migrations.AddField(
            model_name='travellist',
            name='place',
            field=models.CharField(choices=[('mountain', 'Mountain'), ('sea', 'Sea')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='travellist',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='travellist',
            name='type',
            field=models.CharField(choices=[('risky', 'Risky'), ('resortive', 'Resortive')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Favor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mountain', models.BooleanField(default=False)),
                ('sea', models.BooleanField(default=False)),
                ('risky', models.BooleanField(default=False)),
                ('resortive', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
