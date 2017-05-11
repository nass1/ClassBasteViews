from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models
# Create your views here.
#

class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    # 'models' is used to connect to databse
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    # 'models' is used to connect to databse
    model = models.School
    # template_name is required to view the the pages. like below
    template_name = 'basic_app/school_detail.html'




















def index(request):
    return render(request, 'index.html')



class CB(View):
    def get(self,request):
        return HttpResponse("<h1> this is cool stuff </h1>")



class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    # template_name is required to view the the pages. like below
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC Injection'
        return context

