from django.shortcuts import render
from community.forms import *
# Create your views here.
def write(request) :
    if request.method == 'POST' : # POST인 경우 form의 내용을 db에 저장한다.
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else : # POST가 아닌 경우 단순히 form을 출력한다.
        form = Form()

    return render(request, 'write.html', {'form':form}); 
    #write.html 파일에 form 속성에 community.forms.py를 전달

def list(request) :
    articleList = Article.objects.all() #우리가 만든 Article이란 모든 컬럼을 불러온다.
    return render(request, 'list.html',{'articleList' : articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num) #Article 객체로 저장된 데이터를 id가 일치하는 것을 가져온다.
    return render(request, 'view.html', {'article' : article})