from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DiabetesRecord)
admin.site.register(StrokeRecord)
admin.site.register(DepressionRecord)