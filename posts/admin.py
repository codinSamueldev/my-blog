from django.contrib import admin
from .models import PostModel

# Register your models here.


admin.site.register((PostModel))
admin.site.site_header = "Blogpost Admin Site"

