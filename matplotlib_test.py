import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure(figsize=(6,6))

x = np.linspace(0,10,1000)
y = np.sin(x)

for i in range(6) : 
    fig.add_subplot(3,2,i+1)  
    plt.style.use(plt.style.available[i])
    plt.plot(x,y)
    plt.text(s=plt.style.available[i],x=5,y=2,color='red')

plt.show()

