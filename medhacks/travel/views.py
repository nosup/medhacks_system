from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import TRApplication
from .forms import TravelForm, TravelReceiptForm
from accounts.models import UserProfile
from home.models import Application
from home.forms import HomeForm


class TravelHomeView(TemplateView):
    template_name = 'travel/home.html'

    def get(self, request):
        ufirst_name = request.user.first_name;
        ulast_name = request.user.last_name;
        uemail = request.user.email;
        form = HomeForm(initial={'first_name':ufirst_name, 'last_name':ulast_name, 'email':uemail})
        application = Application.objects.filter(user=request.user)[:1]
        # travel reciept info
        tr_app = TRApplication.objects.filter(user=request.user)
        args = {}
        if application.count() > 0:
            args = {'form': None, 'apps': application[0], 'user': request.user}
            if len(tr_app) != 0:
                args['tr_app'] = tr_app[0]
            return render(request, self.template_name, args)

        return render(request, self.template_name, {'form': form, 'apps': None})

class TravelView(TemplateView):
    template_name = 'travel/travel.html'

    def get(self, request):
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
            return render(request, 'travel/applied.html')
        return render(request, self.template_name, {'form': form})


class RecieptView(TemplateView):
    template_name = 'travel/receipt.html'

    def get(self, request):
        form = TravelReceiptForm
        q1 = TRApplication.objects.filter(user=request.user)
        print(len(q1))
        if len(q1) == 0:
            return redirect(reverse('home:home'))
        if len(q1[0].travel_location_city) > 1:
            return render(request, 'travel/applied.html')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = get_object_or_404(UserProfile, user=request.user)
        trApplication = TRApplication.objects.get(user=request.user)
        form = TravelReceiptForm(request.POST, request.FILES, instance=user)
        form2 = TravelReceiptForm(request.POST, request.FILES, instance=trApplication)

        if form.is_valid():

            post_data = form.save(commit=False)
            post_data.user = request.user
            post_data.save()
            travel_date_from = form.cleaned_data['travel_date_from']
            travel_date_to = form.cleaned_data['travel_date_to']
            travel_location_city = form.cleaned_data['travel_location_city']
            travel_location_state = form.cleaned_data['travel_location_state']
            receipt_amount = form.cleaned_data['receipt_amount']
            reimburse_amount = form.cleaned_data['reimburse_amount']
            form.save()
            form2.save()

            return render(request, 'travel/receipt_submitted.html')
        return render(request, self.template_name, {'form': form})
