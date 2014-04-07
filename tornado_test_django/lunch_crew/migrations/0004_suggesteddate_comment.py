# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_crew', '0003_auto_20140224_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggesteddate',
            name='comment',
            field=models.ManyToManyField(default=1, to='lunch_crew.Comments'),
            preserve_default=False,
        ),
    ]
