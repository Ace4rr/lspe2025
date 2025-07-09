import matplotlib.pyplot as plt
import numpy as np
import webbrowser
from PIL import Image
import requests
from io import BytesIO
import matplotlib.animation as animation
from celluloid import Camera
f2=[]
for i in list(open("f1.txt")):
    f2.append((i.split()))
f2=[int(i) for i in f2[0]]

tralalera=Image.open("Tralalero_Tralala.png")

fig,axs=plt.subplots(1,4,figsize=(5,2.7),layout='constrained')
f3=np.arange(len(f2))
data=10**f3
axs[0].plot(f3,data,label="САМАЯ ЛЕГЕНДА")
#axs[1].set_yscale('log')
axs[1].plot(f2,data,label="Первая легенда")
axs[2].plot(f2,data*45,label="Вторая легенда")
#axs[3].plot(f2,data,label="Третья легенда")
axs[3].plot(label="ЭТО ЖЕ ТРАЛАЛЕРА ТРАЛАЛА!!!")
axs[3].imshow(tralalera)
camera = Camera(fig)

axs[0].legend(fontsize='medium', loc='upper left')
axs[1].legend(fontsize='medium', loc='upper left')
axs[2].legend(fontsize='medium', loc='upper left')
axs[3].legend(fontsize='larger', loc='upper left')

fig.figimage(tralalera, 143, 366, zorder=3, alpha=0.5)
plt.tight_layout()
for i in range(2):
    plt.plot([i] * 10)
    camera.snap()
animation = camera.animate()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')
plt.title('ТРАЛАЛЛЕРА ТРАЛАЛЛА')
plt.legend("ea5y")
plt.show()
