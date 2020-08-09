from django.db import models


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=100, unique=True)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        NewsPost, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author_name
