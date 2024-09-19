import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt
Heart_rate_data = np.random.randint(50,180, size = 1440)

print(Heart_rate_data)
plt.plot(Heart_rate_data , label = "monitor")
smoothed_Heart_data = sc.savgol_filter(Heart_rate_data, window_length=51, polyorder=3) 
Avg_rate = []
print(Avg_rate)



for i in range(24): 
    hourly_avg = np.mean(smoothed_Heart_data[i*60:(i+1)*60])
    Avg_rate.append(hourly_avg)
    print(hourly_avg)
        
print(Avg_rate)


plt.plot(smoothed_Heart_data , color = "red")
plt.plot(Avg_rate , color = "yellow")

plt.show()












