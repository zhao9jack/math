# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt
import decimal
d0 = decimal.Decimal(0)
xn=[1, 2, 3, 4, 5, 6, 7]
yn=[2, 4, 5, 8, 12, 18, 15]

plt.plot(xn, yn, 'ro')#画圆


Zxiyi = d0
Zxi2 = d0
Zxi = sum(xn) + d0
Zyi = sum(yn) + d0
for i in range(0, len(xn)):
    Zxiyi = xn[i] * yn[i]
    Zxi2 = xn[i] * xn[i]


k = (len(xn)*Zxiyi - Zxi*Zyi) / (len(xn) * Zxi2 - Zxi*Zxi)
b = (Zyi - k*Zxi) / (len(xn))
x0=0
y0=0
x1=10
y1=k*x1+b
plt.plot([x0,x1], [y0,y1])#画线

plt.axis([0,10, 0, 20])
plt.show()

"""
least squares
已知(x1, y1), (x2, y2), (x3, y3)..(xn, yn)求y=kx+b，使得函数和上述点最逼近

1.转化为数学目标函数
z = (k*x1+b - y1)^2 + ...(k*xn+b - yn)^2最小

2.类比成高等数学中z=f(x,y)，求x,y使得z最小,方法就是求z对x,y的偏导,使的z'(x) = 0 且 z'(y) = 0

3.所以转化为求ｚ对ｋ、b的偏导
z'(k) = 2(k*x1+b - y1)*x1 + ... +  2(k*xn+b - yn)*xn = 2×Z(k*xi+b - yi)*xi
z'(b) = 2(k*x1+b - y1) + ... + 2(k*xn+b - yn) = 2*Z(k*xi+b -yi)

4.使得z'(k) = 0, z'(b) = 0
=>
Z(k*xi+b - yi)*xi = 0
Z(k*xi+b -yi) = 0

=>
kZ(xi^2) + bZxi - Zxi*yi=0
kZxi + nb - Zyi = 0

=>
Z(xi^2)*k + Zxi*b = Zxiyi
Zxi*k + nb = Zyi

=>
k = (nZxiyi - ZxiZyi) / (nZxi^2 - (Zxi)^2)
b = (Zyi - kZxi) / n
"""
