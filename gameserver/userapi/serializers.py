from rest_framework import serializers
from . import models


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ('username', 'email', 'password')
        write_only_fields = ('password')

    def create(self, validated_data):
        return models.Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.save(commit=False)
        password = validated_data.get('password', None)

        if password:
            instance.set_password(password)
        instance.save()