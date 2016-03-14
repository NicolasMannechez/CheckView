from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import io
from wsgiref.util import FileWrapper
from polls2.models import Document


def index(request):
    context = {}
    toto = "bonjour"
    documents = Document.objects.all()
    context['greatings'] = toto
    context['documents'] = documents
    return render(request, 'index.html', context)


def generate_file(request):
    # generate the file
    nom = "Bussiere"
    ad = "issy"
    cp = "92130"
    myfile = io.StringIO()
    myfile.write("%s;%s;%s"%(nom,ad,cp))
    myfile.flush()
    myfile.seek(0)
    response = HttpResponse(FileWrapper(myfile), content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=myfile.csv'
    response['Content-Length'] = myfile.tell()
    return response


def upload_file(request):
    if request.method == 'POST':
        instance = Document(docfile=request.FILES['datafile'])
        instance.save()
        return HttpResponseRedirect('../')
    else:
        return render(request, 'upload.html')


def formular(request):
    context = {}
    if 'group1' in request.POST:
        cross = int(request.POST.get('cross', 0))
        if cross == 1 :
            print(cross)
            context['cross'] = cross
            return render(request, 'form2.html', context)
        else :
            print("54")
            return generate_file(request)
    else :
        pass
    documents = Document.objects.all()
    context['documents'] = documents
    
    return render(request, 'form.html', context)




