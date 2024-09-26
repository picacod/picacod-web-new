# Generated by Django 5.0.7 on 2024-09-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picacodapp', '0002_rename_no_of_vaccancy_jobs_no_of_vaccancies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='experience',
        ),
        migrations.AddField(
            model_name='jobs',
            name='max_experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='min_experience',
            field=models.IntegerField(null=True),
        ),
    ]
