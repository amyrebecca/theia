from django.db import models as models
from django.contrib.postgres.fields import ArrayField, JSONField
from .pipeline import Pipeline


class PipelineStage(models.Model):
    sort_order = models.IntegerField(null=False)
    output_format = models.CharField(max_length=8, null=True)
    operation = models.CharField(max_length=64, null=False)
    select_images = ArrayField(models.CharField(max_length=64, null=False), null=True)
    config = JSONField()
    pipeline = models.ForeignKey(Pipeline, related_name='pipeline_stages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['pipeline', 'sort_order']
