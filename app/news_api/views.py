from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import NewsPostSerializer, CommentSerializer
from .models import NewsPost, Comment


class NewsPostViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

    @action(detail=True, methods=["put", "get"])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.amount_of_upvotes += 1
        post.save()
        return Response({"status": "upvoted"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
