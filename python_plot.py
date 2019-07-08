#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:20:10 2019

@author: dvelasco
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,100)
plt.plot(t, np.exp(t), label="Nik's Graph")
plt.xlabel("t [radians]")
plt.ylabel("exp(t)")
plt.xlim(0,2*np.pi)
plt.title("Nik's Even Better Exponential Graph")
plt.legend()
plt.show()
