from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .python.NaiveBayes.NaiveBayes import testClassification
from .forms import TextForm
# Create your views here.

def output_2(request):
	if request.method == 'POST':
		form = TextForm(request.POST)
		if form.is_valid():
			return HttpResponse("bagus %r" %request.POST['your-text'])

	else:
		form = TextForm()
	hasil = testClassification(request.POST['your-text'])
	return HttpResponse("prediksi %r" %hasil)

def output(request):
	#text = request.POST.get('text', None);
	if request.method == 'POST' and request.is_ajax():
		text = request.POST.get("text");
		hasil = testClassification(text)
	return HttpResponse("prediksi %r" %hasil)
	
def index(request):
	template = loader.get_template('NaiveBayes/index.html')
	return HttpResponse(template.render())
	
def detail(request, question_id):
	return HttpResponse("this is detail view in question: "+ question_id)
