from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import EngineerForm
from .models import Engineer
from django.views import generic
from binascii import a2b_base64
import re
import base64
import random
from django.template.loader import render_to_string
from django.template import Context, Template, RequestContext

import datetime
from django.views.generic import View

from app.utils import render_to_pdf
import weasyprint

from django.core.mail import EmailMessage
from django.conf import settings

# for update data
from django.views.generic import DetailView,ListView
from django.views.generic.edit import UpdateView
from .forms import EngineerUpdateForm
from django.shortcuts import get_object_or_404
class EngineerSide(FormView):
	template_name = "EngineerSide2.html"
	form_class = EngineerForm

	def form_valid(self, form, *args, **kwargs):
		obj = form.save()
		# print(obj.id)

		engineersign = Engineer.objects.get(id = obj.id).engineersign
		CUSTOMER = Engineer.objects.get(id = obj.id).CUSTOMER
		STORE = Engineer.objects.get(id = obj.id).STORE
		STORE_NO = Engineer.objects.get(id = obj.id).STORE_NO
		CALL_OUT_NO = Engineer.objects.get(id = obj.id).CALL_OUT_NO
		newid = obj.id
		print(newid)
		data = {
			"engineersign" : engineersign,
			"CUSTOMER" : CUSTOMER,
			"STORE":STORE,
			"STORE_NO":STORE_NO,
			"CALL_OUT_NO":CALL_OUT_NO,
			"newid" :newid,

	 	}
	 
		# html = render_to_string('pdf/rendertostring.html',context)
		# pdf = weasyprint.HTML(string=html).write_pdf()


		# to_emails = ['apurvpatel444@gmail.com', 'errorfor4004@gmail.com']
		# subject = "Certificate from " + CUSTOMER
		# message = render_to_string('pdf/rendertostring.html', context)
		# email = EmailMessage(subject, body=message, from_email=settings.EMAIL_HOST_USER, to=to_emails)
		# # email.attach("certificate.pdf", pdf, "application/pdf")
		# email.content_subtype = "html"  # Main content is now text/html
		# email.encoding = 'us-ascii'
		# email.send()

		renderpdf = render_to_pdf('pdf/invoice.html', data)
		return HttpResponse(renderpdf, content_type='application/pdf')

		# return redirect('return/')

def index(request):
	return render(request,'index.html')


class UpdateFormView(UpdateView):
	template_name = 'update.html'
	form_class = EngineerUpdateForm
	model = Engineer
	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Engineer,id=id)



	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["engineer"] = Engineer.objects.get(id=self.kwargs.get('id'))
		# print(context["engineer"])
		return context

	def form_valid(self,form):
		# print(form.cleaned_data)

		obj = form.save(commit=False)
		obj.managersign = form.cleaned_data['managersign_data']
		
		obj.save()

		engineersignb = Engineer.objects.get(id = obj.id).engineersign
		CUSTOMER = Engineer.objects.get(id = obj.id).CUSTOMER
		STORE = Engineer.objects.get(id = obj.id).STORE
		STORE_NO = Engineer.objects.get(id = obj.id).STORE_NO
		CALL_OUT_NO = Engineer.objects.get(id = obj.id).CALL_OUT_NO

		managersign = Engineer.objects.get(id = obj.id).managersign
		
		dataaa = {
			"engineersign" : engineersignb,
			"CUSTOMER" : CUSTOMER,
			'STORE':STORE,
			"STORE_NO":STORE_NO,
			"CALL_OUT_NO":CALL_OUT_NO,
			'managersign':managersign,
		}

		html = render_to_string('pdf/invoice.html',dataaa)
		pdf = weasyprint.HTML(string=html).write_pdf()

		# to_emails = ['errorfor4004@gmail.com']
		# subject = "Certificate from " + STORE
		# message = "Report Approved"
		# email = EmailMessage(subject, body=message, from_email=settings.EMAIL_HOST_USER, to=to_emails)
		# email.attach("certificate.pdf", pdf, "application/pdf")
		# email.content_subtype = "html"  # Main content is now text/html
		# email.encoding = 'us-ascii'
		# email.send()

		
		renderpdf = render_to_pdf('pdf/invoice.html', dataaa)
		return HttpResponse(renderpdf, content_type='application/pdf')
		# return super().form_valid(form)


class DetailFormView(DetailView):
	template_name = "detail.html"

	def get_object(self):
		id = self.kwargs.get("id")
		return get_object_or_404(Engineer,id=id)




def LoadEngineerDataInPdf(request, id):
	engineersign = Engineer.objects.get(id = id).engineersign
	CUSTOMER = Engineer.objects.get(id = id).CUSTOMER
	STORE = Engineer.objects.get(id = id).STORE
	STORE_NO = Engineer.objects.get(id = id).STORE_NO
	CALL_OUT_NO = Engineer.objects.get(id = id).CALL_OUT_NO
	managersign = Engineer.objects.get(id = id).managersign
	data = {
		"engineersign" : engineersign,
		"CUSTOMER" : CUSTOMER,
		"STORE":STORE,
		"STORE_NO":STORE_NO,
		"CALL_OUT_NO":CALL_OUT_NO,
		"managersign":managersign,
    }
	pdf = render_to_pdf('pdf/invoice.html', data)
	return HttpResponse(pdf, content_type='application/pdf')





class EngineersReportsList(ListView):
	model = Engineer
	template_name = 'EngineersReportsList.html'
