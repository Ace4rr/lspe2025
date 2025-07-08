import matplotlib.pyplot as plt
import numpy as np
import random
f2=[]
n1,n2=[],[]
with open("11.txt") as file:
    for x in file:
        m=x.split()
        f2.append(m)
fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
for x in range(len(f2)):
    n1.append(f2[x][0])
    n2.append(f2[x][1])
n1=[int(i) for i in n1]
n2=[int(i) for i in n2]
pp=[".",",","o","v","^","1","2","3","8","p","s","*","H","X","D","|"]
for i in range(3):
    ax.scatter(n1,n2,marker=random.choice(pp))
ax.set_xlim(0,2500)
ax.legend("Scatter")
plt.show()
