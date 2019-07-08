#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:20:10 2019

@author: dvelasco
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,100)
plt.plot(t, np.sin(t), label="David's Graph")
plt.xlabel("t [radians]")
plt.ylabel("sin(t)")
plt.xlim(0,2*np.pi)
plt.title("David's Awesome Sine Graph")
plt.legend()
plt.show()
