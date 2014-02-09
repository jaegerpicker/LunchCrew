# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_crew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='ME', max_length=255),
            preserve_default=False,
        ),
    ]
