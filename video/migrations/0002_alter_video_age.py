# Generated by Django 4.2.2 on 2023-07-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='age',
            field=models.CharField(blank=True, choices=[('بزرگسال', 'بزرگسال'), ('نوجوان', 'نوجوان'), ('کودک', 'کودک')], max_length=10, null=True, verbose_name='رده سنی'),
        ),
    ]
