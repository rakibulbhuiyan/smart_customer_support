from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.agents_prompt import SuggestionService
from .models import Conversation, Message
from .serializers import ConversationListSerializer, MessageSerializer


class ConversationListAPIView(ListAPIView):

    queryset = Conversation.objects.all()
    serializer_class =  ConversationListSerializer
    search_fields = ["customer_name"]
    filterset_fields = ["status"]

class MessageHistoryAPIView(ListAPIView):

    serializer_class = MessageSerializer
    def get_queryset(self):
        return Message.objects.filter(conversation_id=self.kwargs["id"])
    
class SendMessageAPIView(CreateAPIView):

    serializer_class = (MessageSerializer)
    def perform_create(self,serializer):
        serializer.save(sender="agent",conversation_id=self.kwargs["id"])



class SuggestReplyAPIView(APIView):

    def post(self,request,id):

        text = request.data.get("message")
        suggestion = (SuggestionService.suggest(text))
        return Response(
            {
                "suggestion":suggestion
            }
        )