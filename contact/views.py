from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import ContactView
from django.contrib import messages


def contact(request):
    user = None
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(
                request, messages.INFO, 'Your message has been sent. Thank you.'
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactView()
    return render_to_response(
        'contact.html',
        {'form': form,
         'user': user,
        },
        context_instance=RequestContext(request)
    )
