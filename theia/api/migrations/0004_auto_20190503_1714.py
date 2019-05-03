# Generated by Django 2.2.1 on 2019-05-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190503_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageryrequest',
            name='pipeline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagery_requests', to='api.Pipeline'),
        ),
        migrations.AlterField(
            model_name='imageryrequest',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagery_requests', to='api.Project'),
        ),
        migrations.AlterField(
            model_name='jobbundle',
            name='current_stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_bundles', to='api.PipelineStage'),
        ),
        migrations.AlterField(
            model_name='jobbundle',
            name='imagery_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_bundles', to='api.ImageryRequest'),
        ),
        migrations.AlterField(
            model_name='jobbundle',
            name='pipeline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_bundles', to='api.Pipeline'),
        ),
        migrations.AlterField(
            model_name='jobbundle',
            name='requested_scene',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_bundles', to='api.RequestedScene'),
        ),
        migrations.AlterField(
            model_name='pipeline',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipelines', to='api.Project'),
        ),
        migrations.AlterField(
            model_name='pipelinestage',
            name='pipeline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipeline_stages', to='api.Pipeline'),
        ),
    ]
