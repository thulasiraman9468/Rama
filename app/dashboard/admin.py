from django.contrib import admin

# Register your models here.
from .models import theatre_manager, theatre, screen, movie, show
class theatre_managerAdmin(admin.ModelAdmin):
	class Meta:
		model = theatre_manager
admin.site.register(theatre_manager,theatre_managerAdmin)
class theatreAdmin(admin.ModelAdmin):
	class Meta:
		model = theatre
admin.site.register(theatre,theatreAdmin)
class screenAdmin(admin.ModelAdmin):
	class Meta:
		model = screen
admin.site.register(screen,screenAdmin)
class movieAdmin(admin.ModelAdmin):
	class Meta:
		model = movie
admin.site.register(movie,movieAdmin)
class showAdmin(admin.ModelAdmin):
	class Meta:
		model = show
admin.site.register(show,showAdmin)