from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import TRApplication
from .forms import TravelForm, TravelReceiptForm
from accounts.models import UserProfile



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
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = get_object_or_404(UserProfile, user=request.user)
        form = TravelReceiptForm(request.POST, request.FILES, instance=user)
        if form.is_valid():

            travel_date_from = form.cleaned_data['travel_date_from']
            travel_date_to = form.cleaned_data['travel_date_to']
            travel_location_city = form.cleaned_data['travel_location_city']
            travel_location_state = form.cleaned_data['travel_location_state']
            receipt_amount = form.cleaned_data['receipt_amount']
            reimburse_amount = form.cleaned_data['reimburse_amount']

            trApplication = get_object_or_404(TRApplication, user=request.user)
            trApplication = form.save()

            user = form.save()

            return render(request, 'home/home.html', {'user': request.user})
        return render(request, self.template_name, {'form': form})
