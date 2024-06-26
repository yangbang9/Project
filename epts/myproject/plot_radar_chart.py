import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import euclidean

def plot_radar_chart(player_data, player_name):
  stats = player_data.drop(['Name', 'Position', 'Total',
                              ]).values
  labels = player_data.drop(['Name', 'Position', 'Total',
                               ]).keys()
  angles = [n / float(len(labels)) * 2 * 3.141592 for n in range(len(labels))]
  angles += angles[:1]

  stats = list(stats)
  stats += stats[:1]

  plt.figure(figsize=(8, 8))
  ax = plt.subplot(111, polar=True)

  # 간격과 최대 값 설정
  plt.yticks(range(0, 101, 10), color="grey", size=8)
  plt.ylim(0, 100)

  ax.plot(angles, stats, 'o-', linewidth=2)
  ax.fill(angles, stats, alpha=0.25)

  plt.xticks(angles[:-1], labels)
  plt.title(f"{player_name}")

  # plt.savefig(f"./static/img/{player_name}_radar_chart.png")
