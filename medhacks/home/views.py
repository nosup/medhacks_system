from django.views.generic import TemplateView
from home.forms import HomeForm
from home.models import Application
from django.shortcuts import render, redirect
from .models import Application
from .forms import HomeForm

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        ufirst_name = request.user.first_name;
        ulast_name = request.user.last_name;
        uemail = request.user.email;
        form = HomeForm(initial={'first_name':ufirst_name, 'last_name':ulast_name, 'email':uemail})
        application = Application.objects.filter(user=request.user)[:1]
        if application.count() > 0:
            return render(request, self.template_name, {'form': None, 'apps': application, 'user': request.user})
        return render(request, self.template_name, {'form': form, 'apps': None})

    def post(self, request):
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            birthday = form.cleaned_data['birthday']
            gender = form.cleaned_data['gender']
            race = form.cleaned_data['race']
            education = form.cleaned_data['education']
            university = form.cleaned_data['university']
            gclass = form.cleaned_data['graduating_class']
            major = form.cleaned_data['major']
            secondmajor = form.cleaned_data['secondmajor']
            attended = form.cleaned_data['attended']
            reimbursement = form.cleaned_data['reimbursement']
            essay1 = form.cleaned_data['essay1']
            essay2 = form.cleaned_data['essay2']
            essay3 = form.cleaned_data['essay3']
            essay4 = form.cleaned_data['essay4']
            how_heard_medhacks = form.cleaned_data['how_heard_medhacks']
            permission = form.cleaned_data['permission']
            conduct = form.cleaned_data['conduct']
            form.save()
            return render(request, 'home/applied.html')
        return render(request, self.template_name, {'form': form})
