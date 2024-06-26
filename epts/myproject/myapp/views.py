# myapp/views.py

from django.shortcuts import render
import os
from subprocess import call
import pandas as pd
from .models import UserProfile, SelectedPlayer
from .forms import UserProfileForm
from .comparison_visual import final
from .compare import final1


def home(request):
    return render(request, 'myapp/home.html')


def find_similar_player(request):
    user_profile = UserProfile.objects.first()

    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'comparison_visual.py')
    call(["python", script_path])

    text, result_data = final()


    return render(request, 'myapp/result.html', {
        'user_profile': user_profile,
        'text': text,
        'result_data': result_data,
    })




def input_info(request):
    user_profile, created = UserProfile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form  = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'myapp/input_info.html', {'form': form})

def compare_players(request):
    if request.method == 'GET':
        # 선수 데이터를 불러오는 로직 (CSV 파일에서 데이터를 읽어오는 예시)
        data = pd.read_csv('./data/processed_data.csv')
        
        
        # 사용자가 검색한 선수 이름
        search_query = request.GET.get('search_query')

        # 검색어를 사용하여 선수 데이터 필터링
        if search_query:
            filtered_data = data[data['Name'].str.contains(search_query, case=False)]
        else:
            filtered_data = data

        return render(request, 'myapp/compare_player.html', {'filtered_data': filtered_data})
        
    elif request.method == "POST":
        selected_player_name = request.POST.get("selected_player_name")
        user_profile = UserProfile.objects.first()
        # 선택한 선수 이름을 SelectedPlayer 모델에 저장
        selected_player = SelectedPlayer(name=selected_player_name)
        selected_player.save()
        

        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'compare.py')
        call(["python", script_path])
    
        result_data1 = final1()
        return render(request, 'myapp/compare_result.html', {
        'result_data': result_data1,
        'selected_player_name': selected_player_name,
        
        })

def compare_result(request):
    

    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'compare.py')
    call(["python", script_path])

    result_data1 = final1()

    return render(request, 'myapp/compare_result.html', {
        
        'result_data': result_data1,

    })
        
    
    
    
    
    
    


