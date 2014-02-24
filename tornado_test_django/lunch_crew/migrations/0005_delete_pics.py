# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_crew', '0004_suggesteddate_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pics',
        ),
    ]
