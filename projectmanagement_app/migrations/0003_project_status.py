# Generated by Django 4.0.4 on 2022-07-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement_app', '0002_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('NS', 'Not started'), ('IP', 'In Progress'), ('CO', 'Completed'), ('CA', 'Cancelled')], default='NS', max_length=2),
        ),
    ]
