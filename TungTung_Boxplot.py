import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
from PIL import Image
import requests
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from io import BytesIO
import matplotlib.animation as animation
from celluloid import Camera
fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
camera = Camera(fig)
ax.grid(linestyle='--', alpha=0.7, color='y')
response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Tung_tung_tung_sahur.webp/500px-Tung_tung_tung_sahur.webp.png')
img = Image.open(BytesIO(response.content))
fig.figimage(img, 255, 130, zorder=3, alpha=0.5)
plt.tight_layout()

f1=list(open('1.txt'))
f2=[]
for i in f1:
    f2.append(i[0:-1])
f2=[int(i) for i in f2]
# Sample data
data = np.random.normal(0, 1, 100) # Generates 100 random numbers from a normal distribution

# Create the boxplot
plt.boxplot(f2)

# Add a title and labels
plt.title('ТУНГ ТУНГ ТУНГ ТУНГ')
plt.ylabel('САХУР')
plt.ylim(-1000,4000)
ax.yaxis.set_major_locator(ticker.MultipleLocator(100)) # Example: ticks every 0.5 units
# Display the plot
plt.legend("САХУР")
plt.show()
#for x in range(100):
#    webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Tung_tung_tung_sahur.webp/500px-Tung_tung_tung_sahur.webp.png')
