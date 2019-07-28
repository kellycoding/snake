from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
from .models import Sentence

# return sentence for sneak game.
def sentence(request):
	sentences = Sentence.objects.all()
	x = len(sentences)
	if x == 0: 
		s = {'sentence': '没有句子'}
		return JsonResponse(s)

	y = random.randint(0, x-1)
	s = {'sentence': sentences[y].sentence}
	return JsonResponse(s)


