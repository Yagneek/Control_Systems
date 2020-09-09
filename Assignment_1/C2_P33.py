import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgn

system = sgn.lti([3],[20,13,4]) #Specifying the system with its transfer function

T, y_ir = sgn.impulse(system)   #Generating y values of the impulse response
y_imp = np.zeros(T.shape)   #Generating y values of the impulse
y_imp[0] = 1

#Plotting the impulse and the impulse response
plt.plot(T,y_ir,label="Impulse response")
plt.plot(T,y_imp,label="Impulse")
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.show()

T, y_sr = sgn.step(system)  #Generating y values of the step response
y_step = np.ones(T.shape)   #Generating y values of the unit step

#Plotting the unit step and the step response
plt.plot(T,y_sr,label="Step response")
plt.plot(T,y_step,label="Unit step")
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()