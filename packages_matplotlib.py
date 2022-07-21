from tkinter import font
from turtle import color
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

# t = [0,25,36,12,18]
# ts = [25,45,96,15,35]
# plt.bar(t,ts,color='yellow')                                      # Vertical way
# plt.show()

# import numpy as np
# import matplotlib as mb
# print(np.__version__)
# print(mb.__version__)


# t = [0,25,36,12,18]
# ts = [25,45,96,15,35]
# plt.barbs(t,ts,color='yellow')
# plt.show()                                          # Doubt session


# t = [0,25,36,12,18]
# ts = [25,45,96,15,35]
# plt.barh(t,ts,color='yellow')
# plt.show()                                              # It will plot the graph in horizontal way


# import numpy as np
# c = np.array(1254)
# f = np.array([1254])
# e = np.array([[1254]])
# o = np.array([1254,23.36,2563.,23])
# p = np.array([[[1254],[1,3.6,152],[123.23,526,2,36,52]]])
# print(c.ndim)                                                   #0
# print(f.ndim)                                                   #1
# print(e.ndim)                                                   #2
# print(o.ndim)                                                   #1
# print(p.ndim)                                                   #2


# c = np.array([0,9])
# d = np.array([11,20])
# plt.plot(c,d,color='cyan')
# plt.show()                                                            # plot the points in a straight line


# c = np.array([0,18,25,9,11])
# d = np.array([0,30,35,20,25])
# plt.plot(c,d,color='green')                                               # plot the points acc to the axis
# plt.show()


# w = np.array([1,11])
# s = np.array([21,31])
# plt.plot(w,s,'p')
# plt.plot(w,s,'o')
# plt.plot(w,s,'h')
# plt.plot(w,s,'s')
# plt.show()                                                          # plot only two points in the different mentioned shapes


# w = np.array([1,11])
# s = np.array([21,31])
# plt.plot(w,s,'p')
# plt.plot(w,s,marker='p')                                   # we can also use marker to shape the plotted points
# plt.plot(w,s,'s:k')
# plt.plot(w,s,'p-.r')
# plt.plot(w,s,'h--g',ms=25,mec='darkred',mfc='k')
# plt.plot(w,s,'h--g',ls='solid',ms=25,mec='darkred',mfc='k')
# plt.plot(w,s,ls='dashdot',lw = 10,marker='h',ms=15,mec='blue')
# plt.show()


# a = np.array([10,11,12,13,14,15])
# b = np.array([20,21,22,23,24,25])
# font1 = {'family': 'TimesNewRoman', 'color':'red','size' : 15}
# font2 = {'family':'Calibri','color':'blue','size':20}
# plt.title('plot graph', fontdict = font1)
# plt.xlabel('code environment',fontdict = font2)
# plt.ylabel('python environment',fontdict = font1)
# plt.plot(a,b)
# plt.show()



# c= np.array([25,50,75,88])
# font1 = {'family': 'TimesNewRoman', 'color':'red','size' : 15}
# plt.xlabel('code environment',fontdict = font1)
# plt.pie(c)
# plt.show()


