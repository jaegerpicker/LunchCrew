from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PlaceType(models.Model):
	"""Types of Places"""
	type_name = models.CharField(max_length=255)


class Address(models.Model):
	"""The Address of the place to go eat"""
	street = models.CharField(max_length=255)
	street2 = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	zipcode =  models.IntegerField()
	state = models.CharField(max_length=255)
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)


class PlaceToEat(models.Model):
	"""Place to go to eat at"""
	place_name = models.CharField(max_length=255)
	place_type = models.ForeignKey(PlaceType)
	address = models.ForeignKey(Address)
	user_added = models.ForeignKey(User)
	added_dt = models.DateTimeField()


class Comments(models.Model):
	"""Comments about places to eat"""
	user_leaving_commit = models.ForeignKey(User)
	comment_text = models.TextField()
	added_dt = models.DateTimeField()


class SuggestedDate(models.Model):
	"""Date suggested to go to eat"""
	dt_to_eat =  models.DateTimeField()
	users = models.ManyToManyField(User)
	comment = models.ForeignKey(Comments)
	added_dt = models.DateTimeField()
	place = models.ForeignKey(PlaceToEat)



class Votes(models.Model):
	"""Votes for a date time"""
	suggested_date = models.ForeignKey(SuggestedDate)
	vote = models.BooleanField()
	user_voting = models.ForeignKey(User)
	vote_dt = models.DateTimeField()
	counter_dt = models.DateTimeField()


class Pics(models.Model):
	"""Picures of the place/food"""
	img_path = models.CharField(max_length=255)
	user_added = models.ForeignKey(User)
	added_dt = models.DateTimeField()
	attached_to_type = models.CharField(max_length=25)
	attached_to_id = models.IntegerField()




		