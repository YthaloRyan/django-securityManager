# Generated by Django 5.1.3 on 2024-11-15 18:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_admin',
            field=models.ManyToManyField(blank=True, related_name='org_admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
