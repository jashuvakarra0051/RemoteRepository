from django.shortcuts import render,redirect

# Create your views here.
from .models import StudentData

def Student_data_view(request):
    if request.method == "POST":
        fname1 = request.POST.get('fname')
        lname1= request.POST.get('lname')
        cname1 = request.POST.get('cname')
        sname1 = request.POST.get('sname')
        mob1 = request.POST.get('mob')
        mail1 = request.POST.get('mail')
        tel1 = request.POST.get('tel')
        hin1 = request.POST.get('hin')
        eng1 = request.POST.get('eng')
        mat1 = request.POST.get('mat')
        sci1 = request.POST.get('sci')
        soc1 = request.POST.get('soc')
        data = StudentData(
            first_name=fname1,
            last_name=lname1,
            class_name=cname1,
            section_name=sname1,
            mobile_number=mob1,
            email_id=mail1,
            telugu=tel1,
            hindi=hin1,
            english=eng1,
            maths=mat1,
            science=sci1,
            social=soc1
        )
        data.save()
        displaydata = StudentData.objects.all()
        return render(request, 'studentdata_inserting.html', {'displaydata': displaydata})

    else:
        displaydata = StudentData.objects.all()
        return render(request,'studentdata_inserting.html',{'displaydata':displaydata})


def Updateview(request,id):
    updatedata = StudentData.objects.get(id=id)
    return render(request,'dataupdate.html',{'updatedata':updatedata})

def updated_data_view(request,id):
    datasaved=StudentData.objects.get(id=id)
    datasaved.first_name = request.POST.get('fname')
    datasaved.last_name = request.POST.get('lname')
    datasaved.class_name = request.POST.get('cname')
    datasaved.section_name = request.POST.get('sname')
    datasaved.mobile_number = request.POST.get('mob')
    datasaved.email_id = request.POST.get('mail')
    datasaved.telugu = request.POST.get('tel')
    datasaved.hindi = request.POST.get('hin')
    datasaved.english = request.POST.get('eng')
    datasaved.maths = request.POST.get('mat')
    datasaved.science = request.POST.get('sci')
    datasaved.social = request.POST.get('soc')
    datasaved.save()
    return redirect('/')


def Delete_view(request,id):
    datadelete =  StudentData.objects.get(id=id)
    datadelete.delete()
    return redirect('/')