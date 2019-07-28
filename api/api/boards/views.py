from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
from .models import Sentence, Homograph, Word

# return sentence list
"""def sentence(request):
	sentences = Sentence.objects.all()
	x = len(sentences)
	if x == 0: 
		s = {'sentence': '没有句子'}
		return JsonResponse(s)

	y = random.randint(0, x-1)
	s = {'sentence': sentences[y].sentence}
	return JsonResponse(s)
"""

# return sentence for sneak game
def getRandomSentence(request):
	sentence = Sentence.objects.order_by("?").first()
	s = {'sentence': sentence.sentence}

	display = {}
	for i in range(0, len(sentence.sentence)):
		w = sentence.sentence[i]
		word = Word.objects.filter(name=w).first()
		if word:
			homograph = word.homographs.order_by("?").first()
		if homograph:
			display[w] = homograph.name

	s['homographs'] = display 

	return JsonResponse(s)


