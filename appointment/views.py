from django.shortcuts import render, redirect
from .models import Appointment,TakeAppointment,ValidadeDoctor
from .forms import ValidadeDoctorForm

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
    user = request.user
    if not user.is_authenticated:
        return redirect('/accounts/login')
    else:
        if user.role == 'PATIENT':
            takes = TakeAppointment.objects.filter(patient__id=user.id)
            return render(request, "next_appointment.html", context={'appointments': takes})
        else:
            return render(request, "access_denied.html")


def search(request):
    location = request.GET["location"]
    department = request.GET["department"]
    appointments = Appointment.objects.filter(status_appointment=True,praticient__location=location,praticient__department=department)
    return render(request, "home.html", context={ 'appointments':appointments})
    
def take_appointment(request,id):
    patient = request.user
    if not patient.is_authenticated:
            return redirect('/accounts/login')
    else:
        if patient.role == 'PATIENT':
            appointment = Appointment.objects.get(id=id)
            take = TakeAppointment.objects.create(patient=patient,appointment=appointment)
            take.save()
            Appointment.objects.filter(id=id).update(status_appointment=0)
            return render(request, "detail_appointment.html",context={'appointment':appointment})
        else:
            return render(request, "access_denied.html")


def appointment_manager(request):
    praticient = request.user
    if not praticient.is_authenticated:
        return redirect('/accounts/login')
    else:
        if praticient.role == 'PRATICIENT':
            if request.method == 'POST':
                    start = request.POST["start_time"]
                    end = request.POST["end_time"]
                    if start > end:
                        message = "invalide date time"
                        return render(request, "appointement_handler.html", context={'message': message})
                    else:
                        validate = ValidadeDoctor.objects.get(praticient__id=praticient.id)
                        print(validate.id)
                        if validate is not None:
                            Appointment.objects.create(praticient=validate,start_time=start,end_time=end)
                            apts = Appointment.objects.filter(praticient__id=validate.id)
                            print(apts)
                            return render(request, "appointement_handler.html", context={'apts': apts})
                        else:
                            return render(request, "appointement_handler.html", context={'message': "vous devez completer votre compte pour ajouter un rendez-vous"})
            else:
                validate = ValidadeDoctor.objects.get(praticient_id=praticient.id)
                if validate is not None:
                    apts = Appointment.objects.filter(praticient__id=validate.id)
                    if apts is not None:
                        return render(request, "appointement_handler.html",context={'apts': apts})
                    else:
                        return render(request, "appointement_handler.html")
                    
                else:
                    return render(request, "appointement_handler.html")
        else:
            return render(request, "access_denied.html")

def validateDoctor(request):
    praticient = request.user
    form = ValidadeDoctorForm()
    if not praticient.is_authenticated:
        return redirect('/accounts/login')
    else:
        if praticient.role == 'PRATICIENT':
            if request.method == 'POST':
                form = ValidadeDoctorForm(request.POST)
                if form.is_valid():
                    department=form.cleaned_data['department']
                    qualification_name=form.cleaned_data['qualification_name']
                    location=form.cleaned_data['location']
                    hospital_name=form.cleaned_data['hospital_name']
                    ValidadeDoctor.objects.create(praticient=praticient, department=department,qualification_name=qualification_name, location=location,hospital_name=hospital_name)
            return render(request, "validate_form.html",context={'form': form})
        else:
            return render(request, "access_denied.html")

        