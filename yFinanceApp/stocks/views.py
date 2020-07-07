from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
# from .models import Question, Choice
# from django.urls import reverse
from django.views.generic import TemplateView
# from django.utils import timezone
from stocks.forms import HomeForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'stocks/index.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)



# class DetailView(generic.DetailView):
#     model = Stock
#     template_name = 'stocks/detail.html'
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
