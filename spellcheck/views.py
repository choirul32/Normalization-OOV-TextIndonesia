from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .python.spellchecker import testSpellCheck
from .forms import TextForm
# Create your views here.

def output(request):
	if request.method == 'POST':
		form = TextForm(request.POST)
		if form.is_valid():
			return HttpResponse("bagus %r" %request.POST['your-text'])

	else:
		form = TextForm()
	hasil = testSpellCheck(request.POST['your-text'])
	# return render(request, 'templates/web/index.html', {'form': form})
	return HttpResponse("prediksi %r" %hasil)
	# return render_to_response('web/index.html',
 #                          {'form': form},
 #                          context_instance=RequestContext(request))
def index(request):
	template = loader.get_template('SpellCheck/index.html')
	return HttpResponse(template.render())

def detail(request, question_id):
	return HttpResponse("this is detail view in question: "+ question_id)

# def csrf_failure(request, reason=""):
#     ctx = {'message': 'some custom messages'}
#     return render_to_response('web/index.html', ctx)

def input_text(request):
    if 'your-text' in request.POST:
        message = request.POST['q']
    else:
        message = 'error'
    return render_to_response('output.html', {'message': message}, context_instance=RequestContext(request))