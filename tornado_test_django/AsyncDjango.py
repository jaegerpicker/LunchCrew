from lunch_crew.models import PlaceToEat, PlaceType, Address, Votes, SuggestedDate
from django.contrib.auth.models import User
import datetime
from django.core import serializers


class AsyncDjango():
    def __init__(self):
        pass

    def delete_place_to_eat(self, serializer, id, callback):
        p = PlaceToEat.objects.get(pk=id)
        p.delete()
        ret = {'msg': 'Place Removed!'}
        data = serializers.serialize(serializer, ret)
        callback(data)

    def update_place_to_eat(self, serializer, id, place_name, place_type_id, address_id, user_id, callback):
        p = PlaceToEat.objects.filter(pk=id)
        p.place_name = place_name
        pt = PlaceType.objects.filter(pk=place_type_id)
        p.place_type = pt
        a = Address.objects.filter(pk=address_id)
        p.address = a
        u = User.objects.filter(pk=user_id)
        p.user_added = u
        p.added_dt = datetime.datetime.now()
        p.save()
        ret = {'msg': 'Place to Eat Updated!', 'place': p}
        data = serializers.serialize(serializer, ret)
        callback(data)

    def insert_place_to_eat(self, serializer, place_name, place_type_id, address_id, user_id, callback):
        p = PlaceToEat()
        p.place_name = place_name
        pt = PlaceType.objects.filter(pk=place_type_id)
        p.place_type = pt
        a = Address.objects.filter(pk=address_id)
        p.address = a
        u = User.objects.filter(pk=user_id)
        p.user_added = u
        p.added_dt = datetime.datetime.now()
        p.save()
        ret = {'msg': 'Place to Eat Added!', 'place': p}
        data = serializers.serialize(serializer, ret)
        callback(data)

    def get_one_place_to_eat(self, serializer, id, callback):
        p = PlaceToEat.objects.filter(pk=id)
        data = serializers.serialize(serializer, p)
        callback(data)

    def get_place_to_eat(self, serializer, callback):
        p = PlaceToEat.objects.all()
        data = serializers.serialize(serializer, p)
        callback(data)

    def get_votes(self, serializer, id, callback):
        sd = SuggestedDate.objects.get(pk=id)
        v = Votes.objects.all(suggested_date=sd)
        data = serializers.serialize(serializer, v)
        callback(data)