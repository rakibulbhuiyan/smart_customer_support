from rest_framework import serializers
from .models import Conversation, Message


class ConversationListSerializer(serializers.ModelSerializer):

    last_message = serializers.SerializerMethodField()
    class Meta:

        model = Conversation
        fields = ("id","customer_name","status","created_at","last_message",)
    def get_last_message(self, obj):
        message = obj.messages.last()
        if message:
            return message.message

        return ""


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ("id","sender","message","timestamp",)