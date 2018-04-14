from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        # requires HTTP response
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            zipcode = form.cleaned_data['zipcode']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            gender = form.cleaned_data['gender']
            university = form.cleaned_data['university']
            gclass = form.cleaned_data['graduating_class']
            major = form.cleaned_data['major']
            track = form.cleaned_data['track']
            reimbursement = form.cleaned_data['reimbursement']
            contingency = form.cleaned_data['contingency']
            team = form.cleaned_data['team']
            return redirect('home:home')



        args = {'form': form, 'text': text, 'first': first, 'last': last,
            'email': email, 'phone_number': phone_number, 'address1': address1,
            'address2':address2, 'zipcode': zipcode, 'city': city,
            'country': country, 'gender': gender, 'university':university,
            'gclass': gclass, 'major':major, 'track': track, 'reimbursement': reimbursement,
            'contingency': contingency, 'team': team}
        # args = {'form': form, 'text': text, 'first': first, 'last_name': last_name,
        #     'email': email, 'phone_number': address1, 'address1': address1,
        #     'address2': address2, 'zipcode': zipcode, 'city': city,
        #     'country': country, 'gender': gender, 'university': university,
        #     'graduating_class': graduating_class, 'major': major, 'track': track,
        #     'reimbursement': reimbursement, 'contingency': contingency, 'team': team,
        # }
        return render(request, self.template_name, args)
