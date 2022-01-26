from rest_framework import serializers
from .models import Activity
from django.contrib.auth.models import User

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'title', 
            'content', 
            'created_on', 
            'get_leaders',
            'get_participants', 
            'trip_date_start', 
            'trip_date_end', 
            'get_activity_type_display', 
            'get_activity_requirements_display', 
            'activity_requirements_count'
            )
        owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Activity` instance, given the validated data.
        """
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Activity` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.code)
        instance.save()
        return instance

