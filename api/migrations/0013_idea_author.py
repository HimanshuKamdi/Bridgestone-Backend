# Generated by Django 4.0.2 on 2023-01-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_admin_ideator_jury'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.ideator'),
        ),
    ]
