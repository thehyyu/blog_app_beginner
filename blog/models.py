from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    '''
    A given user can be the author of many different blog post but not the other
    way around.
    '''
    body = models.TextField()

    def __str__(self):
        return self.title
