import matplotlib.pyplot as plt
import numpy as np
'''
plt.style.use('_mpl-gallery-nogrid')
fig,ax=plt.subplots()
ax.imshow(f3,origin='lower')
plt.show()
'''
sp=['111.txt','222.txt','333.txt','444.txt','555.txt','666.txt','777.txt','888.txt','999.txt','1000.txt','1111.txt','2222.txt','3333.txt','4444.txt','5555.txt',]
def f(a):
    p=[]
    f3=[]
    file=list(open(a))
    for i in file:
        f3.append(i.split())
    f3=[int(i) for i in f3[0]]
    for i in range(len(f3)-2):
        p.append([f3[i],f3[i+1],f3[i+2]])
    print(p)
    return p


plt.style.use('_mpl-gallery-nogrid')


fig,axs=plt.subplots(1,16,figsize=(70,700),layout='constrained')
data=[]
for i in range(0,len(sp)):
    data.append(10**np.arange(len(sp[i])))
print('-------------------------------------------------------')
print(len(data))
print(len(sp))
axs[0].imshow(f(sp[0]),label="САМАЯ ЛЕГЕНДА")
axs[1].imshow(f(sp[1]),label="САМАЯ ЛЕГЕНДА")
axs[2].imshow(f(sp[2]),label="САМАЯ ЛЕГЕНДА")
axs[3].imshow(f(sp[3]),label="САМАЯ ЛЕГЕНДА")
axs[4].imshow(f(sp[4]),label="САМАЯ ЛЕГЕНДА")
axs[5].imshow(f(sp[5]),label="САМАЯ ЛЕГЕНДА")
axs[6].imshow(f(sp[6]),label="САМАЯ ЛЕГЕНДА")
axs[7].imshow(f(sp[7]),label="САМАЯ ЛЕГЕНДА")
axs[8].imshow(f(sp[8]),label="САМАЯ ЛЕГЕНДА")
axs[9].imshow(f(sp[9]),label="САМАЯ ЛЕГЕНДА")
axs[10].imshow(f(sp[10]),label="САМАЯ ЛЕГЕНДА")
axs[11].imshow(f(sp[11]),label="САМАЯ ЛЕГЕНДА")
axs[12].imshow(f(sp[12]),label="САМАЯ ЛЕГЕНДА")
axs[13].imshow(f(sp[13]),label="САМАЯ ЛЕГЕНДА")
axs[14].imshow(f(sp[14]),label="САМАЯ ЛЕГЕНДА")


axs[0].legend(fontsize='medium', loc='upper left')
axs[1].legend(fontsize='medium', loc='upper left')
axs[2].legend(fontsize='medium', loc='upper left')
axs[3].legend(fontsize='medium', loc='upper left')
axs[4].legend(fontsize='medium', loc='upper left')
axs[5].legend(fontsize='medium', loc='upper left')
axs[6].legend(fontsize='medium', loc='upper left')
axs[7].legend(fontsize='medium', loc='upper left')
axs[8].legend(fontsize='medium', loc='upper left')
axs[9].legend(fontsize='medium', loc='upper left')
axs[10].legend(fontsize='medium', loc='upper left')
axs[11].legend(fontsize='medium', loc='upper left')
axs[12].legend(fontsize='medium', loc='upper left')
axs[13].legend(fontsize='medium', loc='upper left')
axs[14].legend(fontsize='medium', loc='upper left')

plt.show()
