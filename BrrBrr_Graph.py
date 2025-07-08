import matplotlib.pyplot as plt
import numpy as np
import webbrowser
from PIL import Image
import requests
from io import BytesIO
import matplotlib.animation as animation
from celluloid import Camera

f1=list(open('1.txt'))
f2=list(open('2.txt'))

fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
camera = Camera(fig)
ax.plot(f2,color='b')
ax.grid(linestyle='--', alpha=0.7, color='g')
response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Brr_brr_patapim.jpg/600px-Brr_brr_patapim.jpg')
img = Image.open(BytesIO(response.content))
#plt.imshow(img)
ax.plot(f1,color='g')
fig.figimage(img, 143, 366, zorder=3, alpha=0.5)
plt.tight_layout()
for i in range(2):
    plt.plot([i] * 10)
    camera.snap()
animation = camera.animate()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')
plt.title('БРР БРРР ПАТАПИММ')
plt.legend("ПАТАПИМ")
plt.show()






















