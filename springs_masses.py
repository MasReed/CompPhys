# A basic simulation for springs and masses
# /|~~k1~~|m1|~~k2CC~~|m2|~~k3~~|\
# Refer to https://scienceworld.wolfram.com/physics/SpringsThreeSpringsandTwoMasses.html

import numpy as np
import matplotlib.pyplot as plt

# Spring Constants
k1 = 1
k2 = 2
k3 = 3

# Mass Constants
m1 = 0.5
m2 = 1.5

# Spring and Mass vectors
K = np.array([[k1+k2, -k2],
              [-k2, k2+k3]])
M = np.array([[m1, 0],
              [0, m2]])

# Take dot product between M^(-1) and K vectors
MinvK = np.dot(np.linalg.inv(M), K)

# Calculate eigenvalues, eigenvectors
w2, v = np.linalg.eig(MinvK)

# Transpose eigenvectors
v = v.T

# Start masses outside equilibrium
x0 = np.array([0.1, 0.2])

# Amplitude of oscillations
a0 = np.dot(x0, v[0])
a1 = np.dot(x0, v[1])

# spring frequencies, omega
w0, w1 = np.sqrt(w2[0]), np.sqrt(w2[1])


def x_of_t(t):
    # calculate position of masses from equilibrium at time t.
    return a0*v[0]*np.cos(w0*t) + a1*v[1]*np.cos(w1*t)


# Start simulation at time zero
t = 0
while True:
    xx = x_of_t(t)

    plt.xlim(-0.5, 1.5)
    plt.plot(xx[0], 0, '*r')
    plt.plot(xx[1]+1, 0, '*b')
    plt.pause(0.07)
    plt.cla()
    t += 0.3
