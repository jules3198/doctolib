from django.shortcuts import render, redirect


def past(request):
    arr = ["a","b","c","d","e","f","g","h"]
    user = request.user
    if not user.is_authenticated:
        return redirect('/accounts/login')
    else:
        if user.role == 'PATIENT':
            return render(request, "past_appointment.html", context={'appointments': arr})
        else:
            return render(request, "access_denied.html")

def next(request):
    return render(request, "next_appointment.html")
