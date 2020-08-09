from news_api.models import NewsPost

def upvote_reset():
    for post in NewsPost.objects.all():
        post.amount_of_upvotes = 0
        post.save()