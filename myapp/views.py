from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email to support@jokin.co.ke
            send_mail(
                'New Inquiry Submission',
                'You have a new contact submission Inquiry from Jokin Consortium Limited. Please check it up',
                settings.DEFAULT_FROM_EMAIL,
                ['support@jokin.co.ke'],
                fail_silently=False,
            )
            # Send confirmation email to user
            send_mail(
                'We received your message',
                'Thank you for reaching out to us. We will get back to you shortly.',
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
