# Generated by Django 4.0.2 on 2022-04-25 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('women', '0003_women_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='content',
            new_name='cont',
        ),
        migrations.AlterField(
            model_name='women',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usr'),
        ),
    ]
