from django.contrib import admin
from collection.models import Collection, Team, Card

# Register your models here.

class CardInline(admin.StackedInline):
    model = Card

class TeamAdmin(admin.ModelAdmin):
    fields = ['team_name', 'team_image','collection_id']
    list_display = ('team_name','collection_id')
    inlines = [CardInline]

admin.site.register(Collection) 
admin.site.register(Team, TeamAdmin)