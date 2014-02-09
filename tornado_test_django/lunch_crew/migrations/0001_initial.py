# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=255)),
                ('street2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField()),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_leaving_commit', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('comment_text', models.TextField()),
                ('added_dt', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pics',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_path', models.CharField(max_length=255)),
                ('user_added', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('added_dt', models.DateTimeField()),
                ('attached_to_type', models.CharField(max_length=25)),
                ('attached_to_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceToEat',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=255)),
                ('place_type', models.ForeignKey(to='lunch_crew.PlaceType', to_field=u'id')),
                ('address', models.ForeignKey(to='lunch_crew.Address', to_field=u'id')),
                ('user_added', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('added_dt', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuggestedDate',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_to_eat', models.DateTimeField()),
                ('comment', models.ForeignKey(to='lunch_crew.Comments', to_field=u'id')),
                ('added_dt', models.DateTimeField()),
                ('place', models.ForeignKey(to='lunch_crew.PlaceToEat', to_field=u'id')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('suggested_date', models.ForeignKey(to='lunch_crew.SuggestedDate', to_field=u'id')),
                ('vote', models.BooleanField()),
                ('user_voting', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('vote_dt', models.DateTimeField()),
                ('counter_dt', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
