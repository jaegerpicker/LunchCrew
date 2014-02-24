from lunch_crew.models import PlaceToEat, PlaceType, Address, Votes, SuggestedDate, Comments, Pics
from django.contrib.auth.models import User
import datetime
from django.core import serializers


class AsyncDjango():
    def __init__(self):
        pass


    #######Place To Eat
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



    #######Votes
    def get_votes(self, serializer, id, callback):
        sd = SuggestedDate.objects.get(pk=id)
        v = Votes.objects.all(suggested_date=sd)
        data = serializers.serialize(serializer, v)
        callback(data)

    def insert_votes(self, serializer, id, vote_val, user_id, callback):
        sd = SuggestedDate.objects.get(pk=id)
        user = User.objects.get(pk=user_id)
        vote = Votes()
        vote.user_voting = user
        vote.suggested_date = sd
        vote.vote = True if vote_val == 1 else False
        vote.vote_dt = datetime.datetime.now(tz=datetime.tzinfo.tzname(datetime.datetime.dst()))
        vote.counter_dt = datetime.datetime.now(tz=datetime.tzinfo.tzname(datetime.datetime.dst()))
        vote.save()
        data = serializers.serialize(serializer, vote)
        callback(data)

    def update_vote(self, serializer, vote_id, vote_val, callback):
        vote = Votes.objects.get(pk=vote_id)
        vote.vote = True if vote_val == 1 else False
        vote.counter_dt = datetime.datetime.now(tz=datetime.tzinfo.tzname(datetime.datetime.dst()))
        vote.save()
        data = serializers.serialize(serializer, vote)
        callback(data)

    def delete_vote(self, serializer, vote_id, callback):
        vote = Votes.objects.get(pk=vote_id)
        vote.delete()
        ret = {'vote_id':vote_id,'status':'deleted'}
        data = serializers.serialize(serializer, ret)
        callback(data)



    ########Place Type
    def get_place_type(self, serializer, place_type_id, callback):
        place_type = PlaceType.objects.get(pk=place_type_id)
        data = serializers.serialize(serializer, place_type)
        callback(data)

    def get_place_types(self, serializer, callback):
        place_types = PlaceType.objects.all()
        data = serializers.serialize(serializer, place_types)
        callback(data)

    def insert_place_type(self, serializer, pt_name, callback):
        place_type = PlaceType()
        place_type.type_name = pt_name
        place_type.save()
        data = serializers.serialize(serializer, place_type)
        callback(data)

    def update_place_type(self, serializer, pt_name, place_type_id, callback):
        place_type = PlaceType.objects.get(pk=place_type_id)
        place_type.type_name = pt_name
        place_type.save()
        data = serializers.serialize(serializer, place_type)
        callback(data)

    def delete_place_type(self, serializer, place_type_id, callback):
        place_type = PlaceType.objects.get(pk=place_type_id)
        place_type.delete()
        ret = {'place_type_id':place_type_id,'status':'deleted'}
        data = serializers.serialize(serializer, ret)
        callback(data)

    ######Address
    def get_address(self, serializer, address_id, callback):
        address = Address.objects.get(pk=address_id)
        data = serializers.serialize(serializer, address)
        callback(data)

    def get_addresses(self, serializer, callback):
        addresses = Address.objects.all()
        data = serializers.serialize(serializer, addresses)
        callback(data)

    def insert_address(self, serializer, city, lat, lon, state, street, street2, zipcode, callback):
        address = Address()
        address.city = city
        address.lat = lat
        address.lon = lon
        address.state = state
        address.street = street
        address.street2 = street2
        address.zipcode = zipcode
        address.save()
        data = serializers.serialize(serializer, address)
        callback(data)

    def update_address(self, serializer, city, lat, lon, state, street, street2, zipcode, address_id, callback):
        address = Address.objects.get(pk=address_id)
        address.city = city
        address.lat = lat
        address.lon = lon
        address.state = state
        address.street = street
        address.street2 = street2
        address.zipcode = zipcode
        address.save()
        data = serializers.serialize(serializer, address)
        callback(data)

    def delete_address(self, serializer, address_id, callback):
        address = Address.objects.get(pk=address_id)
        address.delete()
        ret = {'place_type_id': address_id, 'status': 'deleted'}
        data = serializers.serialize(serializer, ret)
        callback(data)

    ######Comments
    def get_comment(self, serializer, comment_id, callback):
        comment = Comments.objects.get(pk=comment_id)
        data = serializers.serialize(serializer, comment)
        callback(data)

    def get_comments(self, serializer, callback):
        comments = Comments.objects.all()
        data = serializers.serialize(serializer, comments)
        callback(data)

    def insert_comment(self, serializer, comment_text, user_id, callback):
        comment = Comments()
        comment.comment_text = comment_text
        comment.added_dt = datetime.datetime.now()
        comment.user_leaving_commit = User.objects.get(pk=user_id)
        comment.save()
        data = serializers.serialize(serializer, comment)
        callback(data)

    def update_comment_text(self, serializer, comment_id, comment_text, callback):
        comment = Comments.objects.get(pk=comment_id)
        comment.comment_text = comment_text
        comment.save()
        data = serializers.serialize(serializer, comment)
        callback(data)

    def delete_comment(self, serializer, comment_id, callback):
        comment = Comments.objects.get(pk=comment_id)
        comment.delete()
        ret = {'comment': comment_id, 'status': 'deleted'}
        data = serializers.serialize(serializer, ret)
        callback(data)

    #######Pics
    def get_pic(self, serializer, pic_id, callback):
        pic = Pics.objects.get(pk=pic_id)
        data = serializers.serialize(serializer, pic)
        callback(data)

    def get_pics(self, serializer, callback):
        pics = Pics.objects.all()
        data = serializers.serialize(serializer, pics)
        callback(data)

    def insert_pic(self, serializer, img_path, user_id, place_to_eat_id, callback):
        pic = Pics()
        pic.img_path = img_path
        pic.user_added = User.objects.get(pk=user_id)
        pic.place = PlaceToEat.objects.get(pk=place_to_eat_id)
        pic.save()
        data = serializers.serialize(serializer, pic)
        callback(data)


    def delete_pic(self, serializer, pic_id, callback):
        pic = Pics.objects.get(pk=pic_id)
        pic.delete()
        ret = {'place_type_id': pic_id, 'status': 'deleted'}
        data = serializers.serialize(serializer, ret)
        callback(data)

    #######Suggested Date
    def get_suggested_date(self, serializer, suggested_date_id, callback):
        suggested_date = SuggestedDate.objects.get(pk=suggested_date_id)
        data = serializers.serialize(serializer, suggested_date)
        callback(data)

    def get_suggested_dates(self, serializer, callback):
        suggested_dates = SuggestedDate.objects.all()
        data = serializers.serialize(serializer, suggested_dates)
        callback(data)

    def insert_suggested_date(self, serializer, dt_to_eat, place_to_eat_id, callback):
        suggested_date = SuggestedDate()
        suggested_date.added_dt = datetime.datetime.now(tz=datetime.tzinfo.tzname(datetime.datetime.dst()))
        suggested_date.dt_to_eat = dt_to_eat
        suggested_date.place = PlaceToEat.objects.get(pk=place_to_eat_id)
        suggested_date.save()
        data = serializers.serialize(serializer, suggested_date)
        callback(data)

    def update_suggested_date(self, serializer, suggested_date_id, dt_to_eat, place_to_eat_id, callback):
        suggested_date = SuggestedDate.objects.get(pk=suggested_date_id)
        suggested_date.place = PlaceToEat.objects.get(pk=place_to_eat_id)
        suggested_date.dt_to_eat = dt_to_eat
        suggested_date.save()
        data = serializers.serialize(serializer, suggested_date)
        callback(data)

    def delete_suggested_date(self, serializer, suggested_date_id, callback):
        suggested_date = PlaceType.objects.get(pk=suggested_date_id)
        suggested_date.delete()
        ret = {'suggested_date_id': suggested_date_id, 'status': 'deleted'}
        data = serializers.serialize(serializer, ret)
        callback(data)

    def add_comment_to_sgdt(self, serializer, suggested_date_id, comment_text, user_id, callback):
        comment = Comments()
        comment.added_dt = datetime.datetime.now()
        comment.comment_text = comment_text
        comment.user_leaving_commit = User.objects.get(pk=user_id)
        comment.save()
        suggested_date = SuggestedDate.objects.get(pk=suggested_date_id)
        suggested_date.comments.add(comment)
        data = serializers.serialize(serializer, suggested_date)
        callback(data)

    def remove_comment_from_sgdt(self, serializer, suggested_date_id, comment_id, callback):
        comment = Comments.objects.get(pk=comment_id)
        suggested_date = SuggestedDate.objects.get(pk=suggested_date_id)
        suggested_date.comments.remove(comment)
        data = serializers.serialize(serializer, suggested_date)
        callback(data)