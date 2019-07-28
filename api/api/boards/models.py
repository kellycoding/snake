from django.db import models

# 汉字难度等级.
class Level(models.Model):
	name = models.CharField(max_length=20, unique=True)
	description = models.CharField(max_length=200)

# 汉字库.
class Word(models.Model):
	name = models.CharField(max_length=20, unique=True)
	level = models.ForeignKey(Level, related_name='names', null=True, on_delete=models.SET_NULL)


