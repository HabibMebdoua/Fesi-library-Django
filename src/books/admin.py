from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(LendBook)
admin.site.register(LostLend)
admin.site.register(Copy)