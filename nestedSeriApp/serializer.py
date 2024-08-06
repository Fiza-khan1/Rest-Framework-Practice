from rest_framework import serializers
from .models import *


from django.db import models
from rest_framework import serializers 

from django.contrib.auth.models import User   

class GFGSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = GFG 
        fields = ['name',]  
        
class ItemSerializer(serializers.ModelSerializer): 
    gfg = GFGSerializer()       
    class Meta: 
        model = Item  
        fields = '__all__'  
     
    def create(self, validated_data):
        gfg_data = validated_data.pop('gfg')
        gfg_instance, created = GFG.objects.get_or_create(**gfg_data)
        item_instance = Item.objects.create(gfg=gfg_instance, **validated_data)
        return item_instance

    def update(self, instance, validated_data):
        gfg_data = validated_data.pop('gfg')
        gfg_instance, created = GFG.objects.get_or_create(**gfg_data)
        instance.gfg = gfg_instance
        instance.item_title = validated_data.get('item_title', instance.item_title)
        instance.save()
        return instance

from rest_framework import permissions

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

















# from .models import Profile,Hobby


# class HobbySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hobby
#         fields = '__all__'
# class ProfileSerializer(serializers.ModelSerializer):
#     user_hobby = HobbySerializer(many=True)
#     class Meta:
#         model = Profile
#         fields = '__all__'


#     def create(self, validated_data):
#         user_hobby = validated_data.pop('user_hobby')
#         profile_instance = Profile.objects.create(**validated_data)
#         for hobby in user_hobby:
#             Hobby.objects.create(user=profile_instance,**hobby)
#         return profile_instance
    
#     def update(self, instance, validated_data):
#         user_hobby_list = validated_data.pop('user_hobby')
#         instance.display_name = validated_data.get('display_name', instance.display_name)
#         instance.mobile = validated_data.get('mobile', instance.mobile)
#         instance.address = validated_data.get('address', instance.address)
#         instance.dob = validated_data.get('dob', instance.dob)
#         instance.email = validated_data.get('email', instance.email)
#         instance.photo = validated_data.get('photo', instance.photo)
#         instance.save()
#         hobbies_with_same_profile_instance = Hobby.objects.filter(user=instance.pk).values_list('id', flat=True)

#         hobbies_id_pool = []

#         for hobby in user_hobby_list:
#             if "id" in hobby.keys():
#                 if Hobby.objects.filter(id=hobby['id']).exists():
#                     hobby_instance = Hobby.objects.get(id=hobby['id'])
#                     hobby_instance.name = hobby.get('name', hobby_instance.name)
#                     hobby_instance.description = hobby.get('description',hobby_instance.description)
#                     hobby_instance.save()
#                     hobbies_id_pool.append(hobby_instance.id)
#                 else:
#                     continue
#             else:
#                 hobbies_instance = Hobby.objects.create(user=instance, **hobby)
#                 hobbies_id_pool.append(hobbies_instance.id)

#         for hobby_id in hobbies_with_same_profile_instance:
#             if hobby_id not in hobbies_id_pool:
#                 Hobby.objects.filter(pk=hobby_id).delete()

#         return instance