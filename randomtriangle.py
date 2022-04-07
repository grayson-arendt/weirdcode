import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams

title: str = "Triangle Generator"

rcParams['axes.linewidth'] = 1.3
rcParams['toolbar'] = 'None'
bgCOLOR = '#141c1e'
font = {'fontname':'Verdana','color':'#dddddd','weight':'normal','size':'11'}
titlefont = {'fontname':'Franklin Gothic Medium','color':'#dddddd','weight':'bold','size':'15'}

fig, ax = plt.subplots(1,1,figsize=(6,5),dpi=100)

plt.get_current_fig_manager().canvas.set_window_title('Triangle Generator')

plt.tick_params(left=False,
                    bottom=False,
                    labelleft=False,
                    labelbottom=False)

ax.set_title(title, fontdict=titlefont, alpha=0.95)

ax.set_xlim(0,10)
ax.set_ylim(0,10)

fig.set_facecolor(bgCOLOR)
ax.set_facecolor(bgCOLOR)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

def animate(i):
    plt.cla()

    ax.set_title(title, fontdict=titlefont, alpha=0.95)

    x1 = np.random.randint(low=0, high=10)
    x2 = np.random.randint(low=0, high=10)
    x3 = np.random.randint(low=0, high=10)

    y1 = np.random.randint(low=0, high=10)
    y2 = np.random.randint(low=0, high=10)
    y3 = np.random.randint(low=0, high=10)

    cx = (x1 + x2 + x3)/3
    cy = (y1 + y2 + y3)/3

    p1 = [x1, y1]
    p2 = [x2, y2]
    p3 = [x3, y3]

    xcoords = [x1, x2, x3, x1]
    ycoords = [y1, y2, y3, y1]

    plt.scatter(x1, y1, s=7, c='#FFBF00',marker='.')
    plt.scatter(x2, y2, s=7, c='#FFBF00',marker='.')
    plt.scatter(x3, y3, s=7, c='#FFBF00',marker='.')
    plt.scatter(cx, cy, s=40, c='#FFBF00',marker='x')

    plt.plot(xcoords,ycoords,color='#FFBF00',linewidth=3)

    print(p1,p2,p3)

animation = FuncAnimation(fig, animate, interval=100, blit=False, repeat=False)
animation.event_source.stop()

plt.show()
