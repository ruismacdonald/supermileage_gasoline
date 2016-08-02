import numpy as np
from matplotlib import pyplot as plt
# from scipy import stats
# t_ = open('file from ecu', r)
data1 = np.linspace(1.5, 4, 61, True)
data2 = np.random.choice(data1, 101)
f_ = list()
data3 = list()
f0 = 0.0000177626    # to = 1
f1 = 0.00073794  # to = 1.5
f2 = 0.001023884  # to = 2
f3 = 0.00131157  # to = 2.5
f4 = 0.001609573  # to = 3
f5 = 0.00183335  # to = 3.5
f6 = 0.002067593  # to = 4
for i, to in enumerate(data2):
    if to == 1:
        f = f0 / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
    elif 1 < to < 1.5:
        f = (f0 + (to - 1) * (f1 - f0) / (1.5 - 1)) / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
    elif to == 1.5:
        f = f1/0.7006/30000
        f_.append(f)
        data3.append(i)
    elif 1.5 < to < 2:
        f = (f1 + (to - 1.5)*(f2 - f1)/(2 - 1.5)) / 0.7006/30000
        f_.append(f)
        data3.append(i)
    elif to == 2:
        f = f2 / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
    elif 2 < to < 2.5:
        f = (f2 + (to - 2) * (f3 - f2) / (2.5 - 2)) / 0.7006/30000
        f_.append(f)
        data3.append(i)
    elif to == 2.5:
        f = f3 / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
    elif 2.5 < to < 3:
        f = (f3 + (to - 2.5) * (f4 - f3) / (3 - 2.5)) / 0.7006/30000
        f_.append(f)
        data3.append(i)
    elif to == 3:
        f = f4 / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
    elif 3 < to < 3.5:
        f = (f4 + (to - 3) * (f5 - f4) / (3.5 - 3)) / 0.7006/30000
        f_.append(f)
        data3.append(i)
    elif to == 3.5:
        f = f5 / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
    elif 3.5 < to < 4:
        f = (f5 + (to - 3.5) * (f6 - f5) / (4 - 3.5)) / 0.7006/30000
        f_.append(f)
        data3.append(i)
    else:
        f = f6 / 0.7006 / 30000
        f_.append(f)
        data3.append(i)
print(sum(f_))
fig, ax1 = plt.subplots()
ax1.plot(data3, f_, 'b-')
plt.suptitle("Cycle vs. Volume of Gasoline vs. Open Time")
ax1.set_ylabel('Volume of Gasoline per Cycle (ml)', color='b')
ax1. set_xlabel('Cycle')
ax2 = ax1.twinx()
ax2.plot(data3, data2, "r-")
ax2.set_ylabel("Open Time (ms)", color='r')
plt.show()
#  plt.savefig('Figure{0}.png'.format(str(data)))
