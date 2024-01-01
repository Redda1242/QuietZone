
from django.views.generic import ListView
from .models import QuietZone
from django.views.generic import DetailView
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

class QuietZoneListView(ListView):
    model = QuietZone
    context_object_name = 'zones'
    template_name = 'list.html'



class QuietZoneDetailView(DetailView):
    model = QuietZone
    context_object_name = 'zone'
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        zone = context['zone']  # Use the context's 'zone', which is already fetched

        if zone.location:
            context['latitude'] = zone.location.y  # Latitude
            context['longitude'] = zone.location.x  # Longitude
        else:
            context['latitude'], context['longitude'] = None, None

        return context


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                'Message from ' + form.cleaned_data['name'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['your_email@example.com'],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def map_view(request):
    return render(request, 'map.html')
