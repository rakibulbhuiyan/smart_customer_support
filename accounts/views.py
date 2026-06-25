from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from conversations.models import Conversation, Message
from conversations.serializers import ConversationSerializer, MessageSerializer
from accounts.agents_prompt import AISuggestionService

class ConversationListView(generics.ListAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Conversation.objects.all().order_by('-created_at')
        search_query = self.request.query_params.get('search', None)
        status_query = self.request.query_params.get('status', None)

        if search_query:
            queryset = queryset.filter(customer_name__icontains=search_query)
        if status_query:
            queryset = queryset.filter(status=status_query)
            
        return queryset


class ThreadHistoryView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.kwargs['id']
        return Message.objects.filter(conversation_id=conversation_id).order_by('created_at')


class SuggestReplyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        message_text = request.data.get('message', '')
        if not message_text:
            return Response({"error": "Message body is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        suggestion = AISuggestionService.get_suggestion(message_text)
        return Response({"suggestion": suggestion}, status=status.HTTP_200_OK)