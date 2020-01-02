from django.contrib import admin

# Register your models here.
from .models import person,internship,certification,skill,awards,education

admin.site.register(person)
admin.site.register(internship)
admin.site.register(certification)
admin.site.register(skill)
admin.site.register(awards)
admin.site.register(education)
