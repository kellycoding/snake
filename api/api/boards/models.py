from django.db import models

# 汉字难度等级：1.基础汉字200个；2.初级汉字500个；3.中级汉字1500个；4.高级汉字2500个。
class Level(models.Model):
	name = models.CharField(max_length=20, unique=True)
	description = models.CharField(max_length=200)

# 学习进度：
#0-4.不认识；
#5-9.认识；
#10-14.记住了；
#15-19.强化记忆；
#20.熟练掌握。
class Proficiency(models.Model):
	count = models.IntegerField()
	description = models.CharField(max_length=200)

# 汉字库.
class Word(models.Model):
	name = models.CharField(max_length=20, unique=True)
	level = models.ForeignKey(Level, related_name='words', null=True, on_delete=models.SET_NULL)
	proficiency = models.ForeignKey(Proficiency, related_name='words', null=True, on_delete=models.SET_NULL)

class Sentence(models.Model):
	sentence = models.CharField(max_length=2000, unique=False)



