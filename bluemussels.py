import matplotlib.pyplot as plt
import numpy as np
from math import e
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams

rcParams['axes.linewidth'] = 1.3
bgCOLOR = '#141c1e'
COLOR = '#dddddd'
font = {'fontname':'Verdana','color':'#dddddd','weight':'normal','size':'11'}
titlefont = {'fontname':'Franklin Gothic Medium','color':'#dddddd','weight':'bold','size':'15'}

growthConst: float = 0.1 # This growth constant will change the rate of population growth

fig, ax = plt.subplots(1,1,figsize=(7,5),dpi=100)

fig.set_facecolor(bgCOLOR)
ax.set_facecolor(bgCOLOR)

plt.tick_params(axis='both', which='major', labelsize=9.5, width=2)
ax.tick_params(axis='x',colors=COLOR)
ax.tick_params(axis='y',colors=COLOR)

ax.spines['left'].set_color(COLOR)
ax.spines['right'].set_color(COLOR)
ax.spines['top'].set_color(COLOR)
ax.spines['bottom'].set_color(COLOR)

ax.set_xlim(0,200)
ax.set_ylim(0,12000)

line, = ax.plot([],[],color='#FFBF00', linestyle='-', linewidth=3, markersize=1)

x = np.linspace(0,200,150)
y = (10000/(1+(49*e**(-growthConst*x))))

ax.set_xlabel("Time (in Years)", fontdict=font, alpha=0.95)
ax.set_ylabel("Population (# of Blue Mussels)", fontdict=font, alpha=0.95)
ax.set_title("Blue Mussel Growth Projection", fontdict=titlefont, alpha=0.95)
ax.grid(alpha=0.75, color='#c4ccce', linestyle='--', linewidth=1)

def animate(i):
  line.set_data(x[:i],y[:i])
  return line,

animation = FuncAnimation(fig, animate, frames=len(x)+1, interval=0.8, blit=True, repeat=False)
fig.canvas.draw()
animation.event_source.stop()

plt.show()