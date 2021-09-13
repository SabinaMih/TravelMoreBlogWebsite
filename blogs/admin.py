from django.contrib import admin
from .models import Blogs, Comment  # import our models


# Register our models
admin.site.register(Blogs)
admin.site.register(Comment)
