# Generated by Django 4.1 on 2023-05-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_group_room_description_alter_group_room_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='Stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
