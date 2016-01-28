from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Pan, Patient
# Create your views here.

class HomeView(TemplateView):
    template_name = 'homepage.html'

class CreatePanView(CreateView):
    model = Pan
    fields = ['patient', 'prefix']
    template_name_suffix = '_create_form'
    success_url = '#' #'pams/createpat/thanks'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Pan.objects.order_by('date_generated')
        kwargs['listype'] = 'Attendant'
        kwargs['formtype'] = 'Patient Attendance Form'
        return super(CreatePanView, self).get_context_data(**kwargs)

class RegisterPatientView(CreateView):
    model = Patient
    fields = ['surname', 'firstname', 'gender', 'dob', 'address', 'phone_no', 'card_no', 'photo']
    template_name_suffix = '_create_form'
    success_url = '#'

    #def get_success_url(self):
        #return reverse('thanks')
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Patient.objects.order_by('surname')
        kwargs['listype'] = 'Registered'
        kwargs['formtype'] = 'Patient Registration Form'
        return super(RegisterPatientView, self).get_context_data(**kwargs)

class ThanksView(TemplateView):
    template_name = 'pams/thanks.html'

class PanListView(ListView):
    model = Pan
    template_name = 'base.html'


class PanDetailView(DetailView):
    model = Pan
    context_object_name = 'pan'
    template_name = 'pams/PanDetail.html'

    def get_context_data(self, **kwargs):
        content = super(PanDetailView, self).get_context_data(**kwargs)
        content['formtype'] = 'PAN Details'
        content['object_list'] = Pan.objects.order_by('date_generated')
        content['listype'] = 'Attendant'

        return content


class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'pan'
    template_name = 'pams/PatDetail.html'

    def get_context_data(self, **kwargs):
        content = super(PatientDetailView, self).get_context_data(**kwargs)
        content['formtype'] = 'Patient Details'
        content['object_list'] = Patient.objects.order_by('surname')
        content['listype'] = 'Registered'
        #content[]

        return content







