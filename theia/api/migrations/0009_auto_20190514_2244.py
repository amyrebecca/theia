# Generated by Django 2.2.1 on 2019-05-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_pipelinestage_select_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageryrequest',
            name='create_subject_set',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imageryrequest',
            name='subject_set_id',
            field=models.IntegerField(null=True),
        ),
    ]