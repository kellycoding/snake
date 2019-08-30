from django.db import models

# 汉字难度等级：1.基础汉字200个；2.初级汉字500个；3.中级汉字1500个；4.高级汉字2500个。
class Level(models.Model):
	name = models.CharField(max_length=20, unique=True)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def toJson(self):
		return {'id': self.id, 'name':self.name, 'description':self.description}

# 学习进度：
#0-4.不认识；
#5-9.认识；
#10-14.记住了；
#15-19.强化记忆；
#20.熟练掌握。
class Proficiency(models.Model):
	count = models.IntegerField()
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.description

	def toJson(self):
		return {'id': self.id, 'count':self.count, 'description':self.description}

# 汉字库.
class Word(models.Model):
	name = models.CharField(max_length=20, unique=True)
	spell = models.CharField(max_length=200)
	level = models.ForeignKey(Level, related_name='words', null=True, on_delete=models.SET_NULL)
	proficiency = models.ForeignKey(Proficiency, related_name='words', null=True, on_delete=models.SET_NULL)

	def toJson(self):
		#print(self.homographs.all())
		return {'id': self.id, 'name':self.name, 'spell':self.spell, 'level':self.level.toJson(), 'proficiency':self.proficiency.toJson()
				, 'homographs':[l.toJson() for l in self.homographs.all()]}

	def homograph_list(self):
		return ''.join(h.name for h in self.homographs.all())

	def update_homographs(self, hs):
		for h in self.homographs.all():
			if h.name in hs:
				hs = hs.replace(h.name, '')
				
			else:
				h.delete()

		for w in hs:
			Homograph.objects.create(name=w, word=self)

# 形似字库
class Homograph(models.Model):
	word = models.ForeignKey(Word, related_name='homographs', on_delete=models.CASCADE)
	name = models.CharField(max_length=20, unique=False)

	def toJson(self):
		return {'id': self.id, 'name':self.name}


class Sentence(models.Model):
	sentence = models.CharField(max_length=2000, unique=False)


# 词语库
class Phrase(models.Model):
	phrase = models.CharField(max_length=200, unique=False)
	spell = models.CharField(max_length=200)
	level = models.ForeignKey(Level, related_name='phrases', null=True, on_delete=models.SET_NULL)
	proficiency = models.ForeignKey(Proficiency, related_name='phrases', null=True, on_delete=models.SET_NULL)

	def toJson(self):
		#print(self.homographs.all())
		return {'id': self.id, 'name':self.phrase, 'spell':self.spell, 'level':self.level.toJson()
					, 'proficiency':self.proficiency.toJson()
				}

# 课文
class Text(models.Model):
	title = models.CharField(max_length=200, unique=True)
	text = models.TextField(blank=True, null=True)

	def toJson(self):
		return {'id': self.id, 'title':self.title, 'text':self.text}




