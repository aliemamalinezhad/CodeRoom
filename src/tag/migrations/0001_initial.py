# Generated by Django 3.2.9 on 2021-11-16 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tags', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]