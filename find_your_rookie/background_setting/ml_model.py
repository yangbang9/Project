import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#준비물  
#csv파일안에 독립변수(x)로 쓸 데이터 : goals, assists, etc
#csv파일안에 종속변수(y)로 쓸 데이터 : wc_rating -> 월드컵 csv파일에서 따로 가져와서 병합해야함
# def linear_model(df_tr, df_pr, x_list, file_name_tr, file_name_pr):
#     df_tr = pd.read_csv(file_name_tr)
#     x_train=df_tr[x_list]
#     y_train=df_tr['WC_Rating']

#     model = LinearRegression()

#     model.fit(x_train, y_train)

#     df_pr = pd.read_csv(file_name_pr)
#     x=df_pr[x_list]
#     y=model.predict(x)

#     df_pr["pred_rating"] = y

def offense_model(df_tr, df_pr, x_list, St, Rw, Lw):
    #, Lm, Cm, Rm, Lwb, Lb, Rb, Rwb, Gk
    #df_tr = pd.read_csv(file_name_tr)
    df_tr = pd.read_csv("./data/17_18_of.csv", encoding="cp949")
    # df_tr1 = pd.read_csv("./data/17_18_of_new.csv")
    # df_tr2 = pd.read_csv("./data/13_14_of_new.csv")
    df_pr = pd.read_csv("./data/finally_madeit_of5.csv", encoding="cp949")
    x=df_tr[x_list]
    # x1=df_tr1[x_list1]
    # x2=df_tr2[x_list1]
    y=df_tr['WC_Rating']

    model = LinearRegression()

    model.fit(x, y)

    #df_pr = pd.read_csv(file_name_pr)
    x_pr=df_pr[x_list]
    y_pr=model.predict(x_pr)

    df_pr["WC_Rating"] = y_pr
    
    df_pr = df_pr.sort_values("WC_Rating", ascending=False)
    
    St = df_pr.iloc[0].to_list()[2]
    Rw = df_pr.iloc[1].to_list()[2]
    Lw = df_pr.iloc[2].to_list()[2]
    
    return St, Rw, Lw

def passing_model(df_tr, df_pr, x_list2, Lm, Cm, Rm):
    #, Lm, Cm, Rm, Lwb, Lb, Rb, Rwb, Gk
    #df_tr = pd.read_csv(file_name_tr)
    df_tr = pd.read_csv("./data/17_18_ps.csv", encoding="cp949")
    df_pr = pd.read_csv("./data/finally_madeit_ps5.csv", encoding="cp949")
    x=df_tr[x_list2]
    y=df_tr['WC_Rating']

    model = LinearRegression()

    model.fit(x, y)

    #df_pr = pd.read_csv(file_name_pr)
    x_pr=df_pr[x_list2]
    y_pr=model.predict(x_pr)

    df_pr["WC_Rating"] = y_pr
    
    df_pr = df_pr.sort_values("WC_Rating", ascending=False)
    
    Lm = df_pr.iloc[0].to_list()[2]
    Cm = df_pr.iloc[1].to_list()[2]
    Rm = df_pr.iloc[2].to_list()[2]
    
    return Lm, Cm, Rm

def defense_model(df_tr, df_pr, x_list3, Lwb, Lb, Rb, Rwb, Gk):
    #, Lm, Cm, Rm, Lwb, Lb, Rb, Rwb, Gk
    #df_tr = pd.read_csv(file_name_tr)
    df_tr = pd.read_csv("./data/17_18_df.csv", encoding="cp949")
    df_pr = pd.read_csv("./data/finally_madeit_df5.csv", encoding="cp949")
    x=df_tr[x_list3]
    y=df_tr['WC_Rating']

    model = LinearRegression()

    model.fit(x, y)

    #df_pr = pd.read_csv(file_name_pr)
    x_pr=df_pr[x_list3]
    y_pr=model.predict(x_pr)

    df_pr["WC_Rating"] = y_pr
    
    df_pr = df_pr.sort_values("WC_Rating", ascending=False)
    
    Lwb = df_pr.iloc[0].to_list()[2]
    Lb = df_pr.iloc[1].to_list()[2]
    Rb = df_pr.iloc[2].to_list()[2]
    Rwb = df_pr.iloc[3].to_list()[2]
    Gk = df_pr.iloc[10].to_list()[2] # think later...
    
    return Lwb, Lb, Rb, Rwb, Gk

def inter_linear_model(df_inter_tr, df_inter_pr, x_list, St, Rw, Lw, Lm, Cm, Rm, Lwb, Lb, Rb, Rwb, Gk):
    #df_tr = pd.read_csv(file_name_tr)
    x=df_inter_tr[x_list]
    y=df_inter_tr['WC_Rating']

    model = LinearRegression()

    model.fit(x, y)

    #df_pr = pd.read_csv(file_name_pr)
    x_pr=df_inter_pr[x_list]
    y_pr=model.predict(x_pr)

    df_inter_pr["WC_Rating"] = y_pr
    
    df_inter_pr = df_inter_pr.sort_values("WC_Rating", ascending=False)
    
    St = df_inter_pr.iloc[0].to_list()[1]
    Rw = df_inter_pr.iloc[1].to_list()[1]
    Lw = df_inter_pr.iloc[2].to_list()[1]
    Lm = df_inter_pr.iloc[3].to_list()[1]
    Cm = df_inter_pr.iloc[4].to_list()[1]
    Rm = df_inter_pr.iloc[5].to_list()[1]
    Lwb = df_inter_pr.iloc[6].to_list()[1]
    Lb = df_inter_pr.iloc[7].to_list()[1]
    Rb = df_inter_pr.iloc[8].to_list()[1]
    Rwb = df_inter_pr.iloc[9].to_list()[1]
    Gk = df_inter_pr.iloc[10].to_list()[1]
    
    return St, Rw, Lw, Lm, Cm, Rm, Lwb, Lb, Rb, Rwb, Gk