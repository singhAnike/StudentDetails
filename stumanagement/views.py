from django.shortcuts import render, HttpResponse
from django.views import View
from django.template import loader
from .models import students, board, medium, standard

# Create your views here.

# creating greeting view
class welcome(View):
    def get(self, request):
        return HttpResponse("!!!!!Hello Welcome to this Student Management system!!!!!")


# this is the get and post view to handle http request
class CreateData(View):
    def get(self, request):
        # students_list = students.objects.all()
        boards = board.objects.values('Board').distinct()
        Med= medium.objects.values('Medium').distinct()
        std= standard.objects.values('Standard').distinct()
        context={
            'boards': boards,
            'Med': Med,
            'std': std
        }
        return render(request, 'form.html', context)

    def post(self, request):
        student_name = request.POST.get('student_name')
        board_name = request.POST.get('board_name')
        medium_name = request.POST.get('medium_name')
        standard_name = request.POST.get('standard_name')

        student = students.objects.create(Student_Name=student_name)
        board_obj = board.objects.create(Board=board_name, StudentB=student)
        medium_obj = medium.objects.create(Medium=medium_name, StudentM= student)
        standard_obj = standard.objects.create(Standard=standard_name, StudentS= student)

        students_list = students.objects.all()
        return render(request, 'table.html', {'students_list': students_list})

    