from rest_framework import serializers
from djangular_polls.models import Poll, PollItem


class PollItemSerializer(serializers.ModelSerializer):
    percentage = serializers.ReadOnlyField()

    class Meta:
        model = PollItem
        fields = ('id', 'name', 'text', 'votes', 'percentage')


class PollSerializer(serializers.ModelSerializer):
    items = PollItemSerializer(many=True, required=False)
    total_votes = serializers.ReadOnlyField()

    class Meta:
        model = Poll
        fields = ('id', 'title', 'publish_date', 'items', 'total_votes')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        poll = Poll.objects.create(**validated_data)
        for item in items_data:
            PollItem.objects.create(poll=poll, **item)
        return poll
