from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect
from .models import Application
from .forms import HomeForm

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        # requires HTTP response
        args = {'form':form}
        return render(request, self.template_name, args)

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
            form.save()

            return render(request, 'home/applied.html')
        else:
            return render(request, 'home/home.html')

        args = {'form': form, 'first': first, 'last': last,
            'email': email, 'phone_number': phone_number, 'address1': address1,
            'address2':address2, 'zipcode': zipcode, 'city': city,
            'country': country, 'gender': gender, 'university':university,
            'gclass': gclass, 'major':major, 'track': track, 'reimbursement': reimbursement,
            'contingency': contingency, 'team': team, 'resume': resume}

        return render(request, self.template_name, args)

'''
    def post(self, request):
        # Handle file upload
        if request.method == 'POST':
            print("HI\n")
            form = HomeForm(request.POST, request.FILES)
            print(form.is_valid())
            print('\n')
            print(form.errors)
            print('\n')
            print(type(form.errors))
            if form.is_valid():
                # newdoc = Application(docfile = request.FILES['docfile'])
                # newdoc.save()
                print("BYE\n");

                form.save()

                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('home.views.home'))
        else:
            form = HomeForm() # A empty, unbound form

        # Load documents for the list page
        documents = Application.objects.all()

        return render(request, 'home/applied.html')

        # Render list page with the documents and the form
        # return render_to_response(
        #     'home/home.html',
        #     {'documents': documents, 'form': form},
        #     context_instance=RequestContext(request)
        # )
'''
