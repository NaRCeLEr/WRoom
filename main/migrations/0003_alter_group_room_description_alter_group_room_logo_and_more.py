# Generated by Django 4.1 on 2023-05-27 15:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_category_group_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_room',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='group_room',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/%Y/%m/%d')),
                ('Group_Room', models.ManyToManyField(to='main.group_room')),
                ('admins', models.ManyToManyField(related_name='team_admins', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='team_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
