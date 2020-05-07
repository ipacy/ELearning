from rest_framework import serializers
from ..models import *
from rest_auth.serializers import UserDetailsSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'groups', 'first_name', 'last_name', 'biography', 'website',
                  'qualification', 'phone']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


        # fields = ('id', 'title', 'author', 'email')


class UserSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('__all__',)

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('userprofile', {})
    #     # company_name = profile_data.get('company_name')
    #
    #     instance = super(UserSerializer, self).update(instance, validated_data)
    #
    #     # # get and update user profile
    #     # profile = instance.userprofile
    #     # if profile_data and company_name:
    #     #     profile.company_name = company_name
    #     #     profile.save()
    #     return instance
