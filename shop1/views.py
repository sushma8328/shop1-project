from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
	return render(request, 'home.html')

def count(request):
	#request.GET = ?name=sushma&fulltext=abcd
	text = request.GET['fulltext']
	name = request.GET['name']
	gender = request.GET['gender']
	lang = request.GET['lang']
	subjects = request.GET.getlist('chk[]')
	print(subjects)
	print(request.GET)
	print(text)
	wordlist = text.split()

	text2 = []
	for each in wordlist:
		if len(each) > 3:
			text2.append(each)
	text3 = ''.join(text2)

	subjects2 = ','.join(subjects)

	d = {}
	for each in wordlist:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1


	return render(request, 'count.html',{'fulltext_user':'ddddd','count_it':len(text2), 
		'f_name': name,'gender':gender,'lang':lang.upper(),'subjects':subjects2,'dictionary':d.items()})



def wordcount(request):
	return render(request, 'test.html')