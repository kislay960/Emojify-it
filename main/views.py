from django.shortcuts import render
from django.views.generic import TemplateView, View

from services.emojifier import api
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'

    def post(self,request):
        content = request.POST['content']
        emoji = api.predict(content)

        content = {
            "content": content, 
            "emoji": emoji
        }
        return render(request,self.template_name,content)