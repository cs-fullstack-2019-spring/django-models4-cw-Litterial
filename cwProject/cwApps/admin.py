from django.contrib import admin

# Register your models here.
from .models import Mom
from .models import Child
admin.site.register(Mom)
admin.site.register(Child)