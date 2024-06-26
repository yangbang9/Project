import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def offense_model(df_tr, df_pr, x_list, St, Rw, Lw):

    df_tr = pd.read_csv("./data/league_of.csv", encoding="cp949")
    df_pr = pd.read_csv("./data/22world_of.csv", encoding="cp949")
    
    x=df_tr[x_list]
    y=df_tr['WC_Rating']

    model = LinearRegression()
    model.fit(x, y)
    print("학습 데이터 점수: {:.2f}".format(model.score(x, y)))

    x_pr=df_pr[x_list]
    y_pr=model.predict(x_pr)

    df_pr["WC_Rating"] = y_pr
    df_pr = df_pr.sort_values("WC_Rating", ascending=False)
    
    St = df_pr.iloc[0].to_list()[2]
    Rw = df_pr.iloc[1].to_list()[2]
    Lw = df_pr.iloc[2].to_list()[2]
    
    return St, Rw, Lw

def passing_model(df_tr, df_pr, x_list2, Lm, Cm, Rm):

    df_tr = pd.read_csv("./data/league_ps.csv", encoding="cp949")
    df_pr = pd.read_csv("./data/22world_ps.csv", encoding="cp949")
    
    x=df_tr[x_list2]
    y=df_tr['WC_Rating']

    model = LinearRegression()
    model.fit(x, y)



    x_pr=df_pr[x_list2]
    y_pr=model.predict(x_pr)

    df_pr["WC_Rating"] = y_pr
    df_pr = df_pr.sort_values("WC_Rating", ascending=False)
    
    Lm = df_pr.iloc[0].to_list()[2]
    Cm = df_pr.iloc[1].to_list()[2]
    Rm = df_pr.iloc[2].to_list()[2]

    
    
    return Lm, Cm, Rm

def defense_model(df_tr, df_pr, x_list3, Lwb, Lb, Rb, Rwb, Gk):

    df_tr = pd.read_csv("./data/league_df.csv", encoding="cp949")
    df_pr = pd.read_csv("./data/22world_df.csv", encoding="cp949")
    df_gk = pd.read_csv("./data/22world_gk.csv", encoding="cp949")
    
    x=df_tr[x_list3]
    y=df_tr['WC_Rating']

    model = LinearRegression()
    model.fit(x, y)

    x_pr=df_pr[x_list3]
    y_pr=model.predict(x_pr)
    gk_pr = df_gk[x_list3]

    df_pr["WC_Rating"] = y_pr
    df_pr = df_pr.sort_values("WC_Rating", ascending=False)

    df_gk["WC_Rating"] = model.predict(gk_pr)
    df_gk = df_gk.sort_values("WC_Rating", ascending=False)
    
    Lwb = df_pr.iloc[0].to_list()[2]
    Lb = df_pr.iloc[1].to_list()[2]
    Rb = df_pr.iloc[2].to_list()[2]
    Rwb = df_pr.iloc[3].to_list()[2]
    Gk = df_gk.iloc[0].to_list()[1]
    
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