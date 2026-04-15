from django.shortcuts import render, redirect
from .models import EnquiryForm

def user_form(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph_no = request.POST.get('ph_no')

        EnquiryForm.objects.create(
            name=name,
            email=email,
            ph_no=ph_no,
        )

        return redirect ("/crossworks.in/?submitted=1")

    # GET request
    submitted = request.GET.get("submitted") == "1"
    

    return render(request, "crossworks/homepage.html", {
        "submitted": submitted
    })

