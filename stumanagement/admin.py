from django.contrib import admin

# Register your models here.
from .models import students, board, medium, standard

admin.site.register(students)
admin.site.register(board)
admin.site.register(medium)
admin.site.register(standard)