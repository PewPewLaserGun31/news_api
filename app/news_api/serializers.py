from rest_framework import serializers
from .models import NewsPost, Comment


class NewsPostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="comment-detail"
    )

    class Meta:
        model = NewsPost
        fields = [
            "id",
            "url",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "url", "author_name", "content", "creation_date", "post"]
