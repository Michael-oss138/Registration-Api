# Generated by Django 5.1.2 on 2025-01-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0002_students_coursecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='coursecode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
