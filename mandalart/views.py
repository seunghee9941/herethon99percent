from django.shortcuts import render, get_object_or_404, redirect
from .models import Mandalart

def home(request):
    mandals = Mandalart.objects
    return render(request, 'home.html', {'mandals':mandals})
    
def new(request): # 차트 만드는 new.html
    return render(request, 'new.html')

def create(request):    # 데이터베이스에 넣음
    mandal = Mandalart()
    mandal.title = request.GET['title']
    mandal.subject1=request.GET['subject1']
    mandal.subject2=request.GET['subject2']
    mandal.subject3=request.GET['subject3']
    mandal.subject4=request.GET['subject4']
    mandal.subject5=request.GET['subject5']
    mandal.subject6=request.GET['subject6']
    mandal.subject7=request.GET['subject7']
    mandal.subject8=request.GET['subject8']
    mandal.subject1_1=request.GET['subject1_1']
    mandal.subject1_2=request.GET['subject1_2']
    mandal.subject1_3=request.GET['subject1_3']
    mandal.subject1_4=request.GET['subject1_4']
    mandal.subject1_5=request.GET['subject1_5']
    mandal.subject1_6=request.GET['subject1_6']
    mandal.subject1_7=request.GET['subject1_7']
    mandal.subject1_8=request.GET['subject1_8']
    mandal.subject2_1=request.GET['subject2_1']
    mandal.subject2_2=request.GET['subject2_2']
    mandal.subject2_3=request.GET['subject2_3']
    mandal.subject2_4=request.GET['subject2_4']
    mandal.subject2_5=request.GET['subject2_5']
    mandal.subject2_6=request.GET['subject2_6']
    mandal.subject2_7=request.GET['subject2_7']
    mandal.subject2_8=request.GET['subject2_8']
    mandal.subject3_1=request.GET['subject3_1']
    mandal.subject3_2=request.GET['subject3_2']
    mandal.subject3_3=request.GET['subject3_3']
    mandal.subject3_4=request.GET['subject3_4']
    mandal.subject3_5=request.GET['subject3_5']
    mandal.subject3_6=request.GET['subject3_6']
    mandal.subject3_7=request.GET['subject3_7']
    mandal.subject3_8=request.GET['subject3_8']
    mandal.subject4_1=request.GET['subject4_1']
    mandal.subject4_2=request.GET['subject4_2']
    mandal.subject4_3=request.GET['subject4_3']
    mandal.subject4_4=request.GET['subject4_4']
    mandal.subject4_5=request.GET['subject4_5']
    mandal.subject4_6=request.GET['subject4_6']
    mandal.subject4_7=request.GET['subject4_7']
    mandal.subject4_8=request.GET['subject4_8']
    mandal.subject5_1=request.GET['subject5_1']
    mandal.subject5_2=request.GET['subject5_2']
    mandal.subject5_3=request.GET['subject5_3']
    mandal.subject5_4=request.GET['subject5_4']
    mandal.subject5_5=request.GET['subject5_5']
    mandal.subject5_6=request.GET['subject5_6']
    mandal.subject5_7=request.GET['subject5_7']
    mandal.subject5_8=request.GET['subject5_8']
    mandal.subject6_1=request.GET['subject6_1']
    mandal.subject6_2=request.GET['subject6_2']
    mandal.subject6_3=request.GET['subject6_3']
    mandal.subject6_4=request.GET['subject6_4']
    mandal.subject6_5=request.GET['subject6_5']
    mandal.subject6_6=request.GET['subject6_6']
    mandal.subject6_7=request.GET['subject6_7']
    mandal.subject6_8=request.GET['subject6_8']
    mandal.subject7_1=request.GET['subject7_1']
    mandal.subject7_2=request.GET['subject7_2']
    mandal.subject7_3=request.GET['subject7_3']
    mandal.subject7_4=request.GET['subject7_4']
    mandal.subject7_5=request.GET['subject7_5']
    mandal.subject7_6=request.GET['subject7_6']
    mandal.subject7_7=request.GET['subject7_7']
    mandal.subject7_8=request.GET['subject7_8']
    mandal.subject8_1=request.GET['subject8_1']
    mandal.subject8_2=request.GET['subject8_2']
    mandal.subject8_3=request.GET['subject8_3']
    mandal.subject8_4=request.GET['subject8_4']
    mandal.subject8_5=request.GET['subject8_5']
    mandal.subject8_6=request.GET['subject8_6']
    mandal.subject8_7=request.GET['subject8_7']
    mandal.subject8_8=request.GET['subject8_8']
    mandal.save()
    return redirect('view/'+str(mandal.id))
    
def view(request, mandal_id):
    mandal_detail = get_object_or_404(Mandalart, pk=mandal_id)
    return render(request, 'view.html', {'views':mandal_detail})
