# Generated by Django 4.0.4 on 2023-09-28 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailsm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('country_code', models.CharField(default='+91', max_length=4)),
                ('contact', models.CharField(max_length=10)),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('postal', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
