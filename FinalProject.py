import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import matplotlib.ticker as ticker
import math
import statistics
cnt_indic=-1
files=['Set_erase_time.csv','Set_insert_time.csv','Set_search_time.csv','Simple_erase_height.csv','Simple_erase_time.csv','Simple_insert_height.csv','Simple_insert_time.csv','Simple_search_height.csv','Simple_search_time.csv','Splay_erase_height.csv','Splay_erase_time.csv','Splay_insert_height.csv','Splay_insert_time.csv','Splay_search_height.csv','Splay_search_time.csv','Treap_erase_height.csv','Treap_erase_time.csv','Treap_insert_height.csv','Treap_insert_time.csv','Treap_search_height.csv','Treap_search_time.csv']
def sred(a):
    summ=0
    for i in range(len(a)):
        if (abs(int(a[i])-statistics.median(a))>0.5*(statistics.median(a))):
            summ+=10*int(a[i])
        else:
            summ+=int(a[i])
    return(summ//len(a))
def exxcept(a):#удаляет выбросы
    exsm=[]
    if len(a)!=0:
        for ex in range(len(a)):
            if not a[ex]>(10*sred(a)):
                exsm.append(int(a[ex]))
            else:
                continue
    else:
        return max(a)
    return(max(exsm))
for k in range (len(files)):
    cnt_indic+=1
    cnt2=0
    with open(files[k],'r') as file:
        lines=file.readlines()
    processed_data =[]
    processed_data2=[]
    processed_data3=[]#итоговый массив с подмассивамми из чисел
    processed_data4=[]#массив с графиками

    for line in lines:
        clean_line = line.strip() 
        values = clean_line.split(',')
        processed_data.append(values)

    for i in processed_data:
        for j in i:
            processed_data2.append(j.split())
    for i in range(len(processed_data2)+1):
        processed_data3.append([])
    flagg=0
    pp=0
    for i in processed_data2:
        for j in i:
            if j.isdigit():
                processed_data3[flagg].append(int(j))
                pp=0
            else:
                if pp==2:
                    continue
                pp=2
                flagg+=1
    for i in range(1,len(processed_data3)):
        f2=processed_data3[i]
        d=[]
        for i in range(len(f2)):
            d.append(i)
        processed_data4.append([d,f2])



    for i in processed_data4:
        cnt2+=1
        fig, ax = plt.subplots()
        d=i[0]
        f2=i[1]
        
        plt.grid()
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax.grid(visible=1,axis='both',zorder=0.5)
        ax.set_title((files[cnt_indic],(cnt2))) #ПЕРЕДЕЛАТЬ, ПО 9 НА 1 МЕТОД
        ax.set_ylabel("Time (nanosecs)", fontsize=20, color='#3d3217')
        ax.set_xlabel("Iteration \U0001F600", fontsize=40, color='#3d3217')
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))
        
        ax.plot(d, f2, linewidth=1.0,color='#FF4500',label="Graph")
        ax.legend(loc='upper right', fontsize='large', handlelength=4.0)
        x_log = np.linspace(0.001, max(d), 100)
        log_values = np.log(x_log)



        if max(f2) > 0 and max(log_values) > 0:
            scale_factor = max(f2) / max(log_values)
            ax.plot(x_log, log_values * scale_factor, label='Log', linestyle='-', color='#FFD700', zorder=2)
            ax.legend(loc='upper right', fontsize='large', handlelength=4.0)

        if max(d) != 0 and max(f2) != 0 and sred(f2) != 0:
            ax.set(xlim=(0, max(d)*1.1), xticks=np.arange(0, max(d)*1.1, max(d)*1.1/10),  # Шаг делим на 10
                   ylim=(0, max(f2)*1.1), yticks=np.arange(0, max(f2)*1.1, max(f2)*1.1/10))  # Шаг делим на 10
        else:
            ax.set(xlim=(0, max(d)*1.1), xticks=np.arange(0, max(d)*1.1, max(d)*1.1/10),  # Шаг делим на 10
                   ylim=(0, max(f2)*1.1), yticks=np.arange(0, max(f2)*1.1, max(f2)*1.1/10))  # Шаг делим на 10


    #ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%.1f'))
        plt.show()






'''# ... Ваш цикл for i in processed_data4:
    for i in processed_data4:
        cnt2 += 1
        fig, ax = plt.subplots()

        d = i[0]
        f2 = i[1]

        # ---- ДОБАВКА 1: лёгкий фильтр выбросов -----------------
        clean_f2 = [v for v in f2 if abs(v - statistics.median(f2)) < 5 * statistics.median(f2)]
        ymax = max(clean_f2)            # ДОБАВКА 2
        # --------------------------------------------------------

        plt.grid()
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax.grid(visible=1, axis='both', zorder=0.5)
        ax.set_title((files[cnt_indic], (cnt2)))
        ax.set_ylabel("Time (nanosecs)", fontsize=20, color='#3d3217')
        ax.set_xlabel("Iteration", fontsize=20, color='#3d3217')
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))

        ax.plot(d, f2, linewidth=1.0, color='#FF4500', label="Graph")
        ax.legend(loc='upper right', fontsize='large', handlelength=4.0)

        x_log = np.linspace(0.001, max(d), 100)
        log_values = np.log(x_log)
        if ymax > 0 and max(log_values) > 0:
            scale_factor = ymax / max(log_values)
            ax.plot(x_log, log_values * scale_factor, label='Log', linestyle='-', color='#FFD700', zorder=2)

        # ---- ДОБАВКА 3‑4: чуть плотнее тики + новый ylim --------
        ax.set(xlim=(0, max(d) * 1.05),
               xticks=np.linspace(0, max(d) * 1.05, 12),   # плотнее
               ylim=(0, ymax * 1.05),                      # new limit
               yticks=np.linspace(0, ymax * 1.05, 12))     # плотнее
        # --------------------------------------------------------

        plt.show()
'''