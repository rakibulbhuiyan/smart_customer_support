from django.urls import path

from .views import (
    ConversationListAPIView,
    MessageHistoryAPIView,
    SendMessageAPIView,
    SuggestReplyAPIView,
)

urlpatterns = [
    path("conversations/", ConversationListAPIView.as_view(), name="conversation-list"),
    path("conversations/<int:id>/messages/", MessageHistoryAPIView.as_view(), name="message-history"),
    path("conversations/<int:id>/reply/", SendMessageAPIView.as_view(), name="send-message"),
    path("conversations/<int:id>/suggest-reply/", SuggestReplyAPIView.as_view(), name="suggest-reply")
]