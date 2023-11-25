from django.http import HttpResponse
from django.shortcuts import render
from workshops.models import Workshop_form, Enroll

def workshops(request):
    all_workshops = Workshop_form.objects.all()
    params = {"all_workshops":all_workshops}
    return render(request, 'pages/workshop.html', params)

def GoToWorkshop(request, slug):
    WorkshopMain = Workshop_form.objects.filter(slug=slug).first()
    if WorkshopMain != None:
        context = {'WorkshopMain' : WorkshopMain}
        return render(request, 'pages/WorkshopView.html', context)
    
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        waphone = request.POST['wa']
        phphone = request.POST['ph']
        intro = request.POST['intro']
        tag = request.POST['slug']

        #to-do
        #Add checks if data is there or not.


        enroll = Enroll(name=name, email=email, wa_number=waphone, ph_number=phphone, intro=intro, tag=tag)
        enroll.save()

        print(name, email, waphone, phphone,intro,tag)
        return(HttpResponse("CONFIRMED"))

# def submit(request):
#     print("SUBMITTED")
#     if request.method == 'POST':
#         #name = request.POST['fullname']
#         #email = request.POST['email']
#         #waphone = request.POST['wa']
#         #phphone = request.POST['ph']
#         #intro = request.POST['intro']
#         #tag = request.get
#         print(request.POST[WorkshopMain.slug])
        