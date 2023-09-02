# Generated by Django 4.1.7 on 2023-09-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='سوال')),
                ('answer', models.TextField(verbose_name='پاسخ')),
            ],
            options={
                'verbose_name': 'سوالات متداول',
                'verbose_name_plural': 'سوال متداول',
            },
        ),
    ]