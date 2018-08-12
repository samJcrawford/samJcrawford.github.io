# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 21:46:13 2018

@author: Sam
"""
import numpy as np
import matplotlib.pyplot as plt

def alpha(t):
    return np.piecewise(t, [t <= 0, t > 0], [0, lambda t: np.e**(-1./t**2)])

def beta(t):
    return alpha(t)/(alpha(t) + alpha(1.-t))

def gamma(t):
    return beta(2+t)*beta(2-t)

ts = np.linspace(-3,3, num = 1000)

plt.plot(ts, alpha(ts), ts, beta(ts), ts, gamma(ts))
plt.grid(True)
plt.show()