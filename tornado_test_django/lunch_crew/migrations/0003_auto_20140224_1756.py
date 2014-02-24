# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_crew', '0002_address_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='pics',
            name='place',
            field=models.ForeignKey(to='lunch_crew.PlaceToEat', default=1, to_field=u'id'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pics',
            name='attached_to_id',
        ),
        migrations.RemoveField(
            model_name='pics',
            name='attached_to_type',
        ),
        migrations.RemoveField(
            model_name='suggesteddate',
            name='comment',
        ),
    ]
