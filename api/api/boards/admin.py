from django.contrib import admin
from .models import Level, Proficiency, Word, Homograph, Sentence

class LevelAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
admin.site.register(Level, LevelAdmin)

class ProficiencyAdmin(admin.ModelAdmin):
	list_display = ('id', 'count', 'description')
admin.site.register(Proficiency, ProficiencyAdmin)

class WordAdmin(admin.ModelAdmin):
	list_display = ('id', 'spell', 'name', 'level', 'proficiency', 'homograph_list')		
admin.site.register(Word, WordAdmin)

class HomegraphAdmin(admin.ModelAdmin):
	list_display = ('id', 'word', 'name')
admin.site.register(Homograph, HomegraphAdmin)

class SentenceAdmin(admin.ModelAdmin):
	list_display = ('id', 'sentence')
admin.site.register(Sentence, SentenceAdmin)

