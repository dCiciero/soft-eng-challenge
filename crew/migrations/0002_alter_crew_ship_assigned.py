# Generated by Django 4.0.4 on 2022-04-28 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_delete_systemcontrol'),
        ('crew', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='ship_assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_member', to='ship.ship'),
        ),
    ]
