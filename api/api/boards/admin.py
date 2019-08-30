from django import forms
from django.contrib import admin
from .models import Level, Proficiency, Word, Homograph, Sentence, Phrase, Text

class LevelAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
admin.site.register(Level, LevelAdmin)

class ProficiencyAdmin(admin.ModelAdmin):
	list_display = ('id', 'count', 'description')
admin.site.register(Proficiency, ProficiencyAdmin)


class WordAdminForm(forms.ModelForm):

	homographs = forms.CharField()

	def __init__(self, *args, **kwargs):
		instance = kwargs.get('instance')
		if instance:
			self.base_fields['homographs'].initial = instance.homograph_list()
		super().__init__(*args, **kwargs)

	class Meta:
		model = Word
		fields = '__all__'

class WordAdmin(admin.ModelAdmin):
	form = WordAdminForm
	list_display = ('id', 'spell', 'name', 'level', 'proficiency', 'homograph_list')

	def save_model(self, request, obj, form, change):
		homographs = form.cleaned_data['homographs']
		obj.update_homographs(homographs)
		obj.save()

admin.site.register(Word, WordAdmin)

class HomegraphAdmin(admin.ModelAdmin):
	list_display = ('id', 'word', 'name')
admin.site.register(Homograph, HomegraphAdmin)

class SentenceAdmin(admin.ModelAdmin):
	list_display = ('id', 'sentence')
admin.site.register(Sentence, SentenceAdmin)

class PhraseAdmin(admin.ModelAdmin):
	list_display = ('id', 'phrase', 'spell', 'level', 'proficiency')
admin.site.register(Phrase, PhraseAdmin)

class TextAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'text')
admin.site.register(Text, TextAdmin)

