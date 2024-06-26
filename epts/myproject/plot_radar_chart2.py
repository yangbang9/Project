import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def compare_radar_chart(df, target1, target2):

    player1_stats = df[df['Name'] == target1].iloc[0]
    player2_stats = df[df['Name'] == target2].iloc[0]
    
    def plot_radar_chart2(player_data, player_name, ax, color):
        stats = player_data.drop(['Name','Position','Total']).values
        labels = player_data.drop(['Name','Position','Total']).keys()
        angles = [n / float(len(labels)) * 2 * 3.141592 for n in range(len(labels))]
        angles += angles[:1]

        stats = list(stats)
        stats += stats[:1]

        ax.plot(angles, stats, 'o-', linewidth=2, label=player_name, color=color)
        ax.fill(angles, stats, alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        ax.set_title(player_name)

    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(polar=True))

    # 간격과 최대 값 설정
    ax.set_yticks(range(0, 101, 10))
    ax.set_yticklabels(["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"], color="grey", size=8)
    ax.set_ylim(0, 100)

    # 레이더 차트 생성
    plot_radar_chart2(player1_stats, target1, ax, color='b')
    plot_radar_chart2(player2_stats, target2, ax, color='r')

    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.title(f"{target1} vs {target2}")

    # 이미지 파일로 저장
    plt.savefig(f"./static/img/3.png")

    score = round((player1_stats.Total / player2_stats.Total), 2)

    return score


    
