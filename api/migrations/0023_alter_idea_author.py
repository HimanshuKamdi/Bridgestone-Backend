# Generated by Django 4.0.2 on 2023-01-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_idea_image_program_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='author',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
