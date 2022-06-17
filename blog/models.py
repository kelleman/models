from django.db import models
from django.forms import CharField
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    # User = get_user_model()

    # def sample_view(request):
    #     current_user = request.user
    #     print(current_user.id)
    #     if request.user.is_authenticated:
    #         pass
    #         # Do something for authenticated users.
    #     else:
    #         pass
    #         # Do something for anonymous users.
