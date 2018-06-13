from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import TRApplication
from .forms import TravelForm

class TravelView(TemplateView):
    template_name = 'travel/travel.html'

    def get(self, request):
        # ufirst_name = request.user.first_name;
        # ulast_name = request.user.last_name;
        # uemail = request.user.email;
        # form = TravelForm(initial={'first_name':ufirst_name, 'last_name':ulast_name, 'email':uemail})
        # application = TRApplication.objects.filter(user=request.user)[:1]
        # if application.count() > 0:
        #     return render(request, self.template_name, {'form': None, 'apps': application, 'user': request.user})
        form = TravelForm
        trApplication = TRApplication.objects.filter(user=request.user)[:1]
        if trApplication.count() > 0:
            return render(request, 'travel/applied.html')
        return render(request, self.template_name, {'form': form, 'apps': None})

    def post(self, request):
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()

            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            tr_essay = form.cleaned_data['tr_essay']
            contingency = form.cleaned_data['contingency']
            state = form.cleaned_data['state']
            type_reim = form.cleaned_data['type_reim']
            form.save()
            # contingency = form.cleaned_data['contingency']
            # team = form.cleaned_data['team']
            return render(request, 'travel/applied.html')
        return render(request, self.template_name, {'form': form})
