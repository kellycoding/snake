from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random, json
from .models import Sentence, Homograph, Word, Level, Proficiency
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

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

# log words from ui form
@csrf_exempt
@transaction.atomic
def createWords(request):
	if request.method=='POST':
		#received_json_data=json.loads(request.body)
		received_json_data = json.loads(request.body.decode("utf-8"))

		word = received_json_data["char"]
		spell = received_json_data["spell"]
		level = received_json_data["level"]
		progress = received_json_data["progress"]
		newWord = Word.objects.create(name=word, spell=spell, level_id=level, proficiency_id=progress)

		homographs = received_json_data["homo_chars"]

		for i in range(0, len(homographs)):
			homograph = Homograph.objects.create(word=newWord, name=homographs[i])

		s = {'id': newWord.id }
 
	return JsonResponse(s)

# return level list
def getLevels(request):
	if request.method=='GET':
		levels = Level.objects.all()

		s = {'levels': [l.toJson() for l in levels]}

	return JsonResponse(s)

# return Proficiency list
def getProficiencies(request):
	if request.method =='GET':
		proficiencies = Proficiency.objects.all()

		s  = {'Proficiencies': [l.toJson() for l in proficiencies]}

	return JsonResponse(s)

# return word full list
def getWordFullList(request):
	if request.method == 'GET':
		words = Word.objects.all()

		s  = {'words': [l.toJson() for l in words]}

	return JsonResponse(s)

# return word Proficiency in the snake game
def updateProficiencyInSnake(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)

		words = received_json_data["words"]
		for i in range(0, len(words)):
			word = words[i][word]
			count = words[i][count]

			if word is not None and count is not None:
				if count == 1 or count == -1:
					wordObject = Word.objects.filter(name=word).first()
					if wordObject is not None:
						oldProficiency = Proficiency.objects.filter(count=wordObject.proficiency.count).first()
						if oldProficiency is None:
							newProficiency = Proficiency.objects.filter(count=0).first()
						elif oldProficiency >= 0 and oldProficiency < 19:
							newProficiency = Proficiency.objects.filter(count=wordObject.proficiency.count+count).first()
							if newProficiency is not None:
								wordObject.proficiency = newProficiency
								wordObject.save()
							else:
								return HttpResponseBadRequest({"error": "update proficiency failded."})
					else:
						return HttpResponseBadRequest({"error": "invalid word."})
				elif count == 0:
					pass
				else:
					return HttpResponseBadRequest({"error": "invalid count."})
			else:
				return HttpResponseBadRequest({"error": "invalid word object."})


# return word for testing
def getRandomWord(request):
	if request.method == 'GET':
		level = request.GET.get("level")
		word = Word.objects.filter(level=level, proficiency__lt=19).order_by("?").first()
		s = {'word': word.name}

	return JsonResponse(s)

# update testing result
def updateTestResult(request):
	if request.method == 'POST':
		received_json_data=json.loads(request.body)

		word = received_json_data["word"]
		spell = received_json_data["spell"]
		wordObject = Word.objects.filter(name=word, spell=spell).first()
		if wordObject is not None and wordObject.proficiency >= 0: 
			if wordObject.proficiency < 19:
				wordObject.proficiency += 5
		else:
			return HttpResponseBadRequest({"error": "invalid word."})

