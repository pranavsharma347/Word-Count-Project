from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'WordCountApp/home.html')

def about(request):
	return render(request, 'WordCountApp/about.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			# increase the number
			worddictionary[word] += 1
		else:
			# added to dictionary

			worddictionary[word] = 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'WordCountApp/count.html' , {'fulltext' : fulltext, 'count': len(wordlist), 'worddictionary': sortedwords })

