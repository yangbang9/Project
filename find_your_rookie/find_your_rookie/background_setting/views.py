from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import ForwardForm, MidfielderForm, DefenderForm    
from django.views.generic import TemplateView
# Create your views here.
from .ml_model import offense_model, passing_model, defense_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df_tr = pd.DataFrame()
df_pr = pd.DataFrame()
# example
# x_list1 = ['Goals', 'SpG', 'Drb', 'Assists', 'KeyP']
# x_list2 = ['PS%','Crosses','LongB', 'Assists','KeyP']
# x_list3 = ['Tackles','Inter','Clear','Blocks']

x_list1 = []
x_list2 = []
x_list3 = []
St = "st" 
Rw = "rw" 
Lw = "lw" 
Lm = "lm" 
Cm = "cm" 
Rm = "rm" 
Lwb = "lwb" 
Lb = "lb" 
Rb = "rb" 
Rwb = "rwb" 
Gk ="gk"

def index(request):
    return render(request, 'index.html')

def back_setting(request):
    global x_list1, x_list2, x_list3
    x_list1 = []
    x_list2 = []
    x_list3 = []
    # POST REQUSET --> CONFIRM THE FORM CONTENTS --> BACK TO HOMEPAGE
    # ELSE, RENDER FORM
    if request.method == 'POST':
        form = ForwardForm(request.POST)
        form2 = MidfielderForm(request.POST)
        form3 = DefenderForm(request.POST)
        
        if form.is_valid():
            checkbox_info = form.cleaned_data
            print(checkbox_info)
            if(checkbox_info["Goals"] == True):
               x_list1.append("Goals")
            if(checkbox_info["Assists1"] == True):
               x_list1.append("Assists")
            if(checkbox_info["SpG"] == True):
               x_list1.append("SpG")
            if(checkbox_info["KeyP1"] == True):
               x_list1.append("KeyP")
            if(checkbox_info["Drb"] == True):
               x_list1.append("Drb") 
            
        if form2.is_valid():
            checkbox_info2 = form2.cleaned_data
            print(checkbox_info2)
            if(checkbox_info2["Assists2"] == True):
               x_list2.append("Assists")
            if(checkbox_info2["KeyP2"] == True):
               x_list2.append("KeyP")
            if(checkbox_info2["AvgP"] == True):
               x_list2.append("AvgP")
            if(checkbox_info2["Crosses"] == True):
               x_list2.append("Crosses")
            if(checkbox_info2["LongB"] == True):
               x_list2.append("LongB")
                           
        if form3.is_valid():
            checkbox_info3 = form3.cleaned_data
            print(checkbox_info3)
            if(checkbox_info3["Tackles"] == True):
               x_list3.append("Tackles")
            if(checkbox_info3["Inter"] == True):
               x_list3.append("Inter")
            if(checkbox_info3["Clear"] == True):
               x_list3.append("Clear")
            if(checkbox_info3["Blocks"] == True):
               x_list3.append("Blocks")
            
    else:
        form = ForwardForm()
        form2 = MidfielderForm()
        form3 = DefenderForm()

    return render(request, 'background_setting/back_setting.html', {'form':form, 'form2':form2, 'form3':form3})
        

def best11(request):
    #pandas dataframe index -> candidates index
    st, rw, lw = offense_model(df_tr, df_pr, x_list1, St, Rw, Lw)
    lm, cm, rm = passing_model(df_tr, df_pr, x_list2, Lm, Cm, Rm)
    lwb, lb, rb, rwb, gk = defense_model(df_tr, df_pr, x_list3, Lwb, Lb, Rb, Rwb, Gk)
    my_dict = {"St":st, "Rw":rw, "Lw":lw, "Lm":lm, "Cm":cm, "Rm":rm, "Lwb":lwb, "Lb":lb, "Rb":rb, "Rwb":rwb, "Gk":gk}
    print(my_dict)
    return render(request, 'background_setting/best11.html', context=my_dict)

def ranking(request):
    candidates = models.defensive.objects.all()
    context = {'candidates':candidates}
    return render(request, 'background_setting/ranking.html', context=context)

def international(request):
    st, rw, lw = offense_model(df_tr, df_pr, x_list1, St, Rw, Lw)
    lm, cm, rm = passing_model(df_tr, df_pr, x_list2, Lm, Cm, Rm)
    lwb, lb, rb, rwb, gk = defense_model(df_tr, df_pr, x_list3, Lwb, Lb, Rb, Rwb, Gk)
    my_dict = {"St":st, "Rw":rw, "Lw":lw, "Lm":lm, "Cm":cm, "Rm":rm, "Lwb":lwb, "Lb":lb, "Rb":rb, "Rwb":rwb, "Gk":gk}
    print(my_dict)
    return render(request, 'background_setting/international.html', context=my_dict)

# def option(request):
#     if request.POST:
#         number = int(request.POST['goals'])
#         models.option.objects.create(list=number)
#         return redirect(reverse('templates:index'))
#     return render(request,index.html)
#  계획 : offensive/defensive/passing -> 3개의 카테고리에서 체크박스 번호를 넘겨받아서 번호별로 가중치 부여해서 rating 책정
