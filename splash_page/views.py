from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .forms import EmailPostForm

# Create your views here.
#def home(request):
#	return render(request, 'splash_page/home.html')

def home(request):
	sent = False

	if request.method == 'POST':
	# Form was submitted
		form = EmailPostForm(request.POST)
		if form.is_valid():
			# Form field passed validation
			cd = form.cleaned_data

		subject = 'Sixty Mill Street - Thank you for contacting us!'
		message = 'We will reach out to you within one business day. \
		You may respond to this email or call us at 817-629-3670 if you \
		have additional questions.' 
		sender = 'michael@sixtymill.com'
		to = [cd['to']]

		send_mail(subject, message, sender, to)
		sent = True

	else:
		form = EmailPostForm()

	context = {
			'form': form,
			'sent':sent,
			}
	return render(request, 'splash_page/home.html', context)












