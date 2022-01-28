import numpy as np
import pandas as pd


class System:
    def __init__(self, temp_init, volume, r, time_end, temp_env, dt):
        self.temp_init = temp_init
        self.temp_final = temp_init
        self.temp_env = temp_env
        self.volume = volume  # milliliters
        self.r = r  # Heat loss coefficient * heat transfer surface area
        self.time_end = time_end
        self.time_0 = 0
        self.dt = dt  # minutes


coffee = System(temp_init=90, temp_env=22, volume=300, r=0.01, time_end=30, dt=1)


def temp_diff(T, system):
    r, T_env, dt = system.r, system.temp_env, system.dt
    return r * (T - T_env) * dt


print(temp_diff(coffee.temp_init, coffee))

time_array = np.arange(coffee.time_0, coffee.time_0 + coffee.dt * 30, coffee.dt)
temp_array = np.zeros(len(time_array))
temp_array[0] = coffee.temp_init
for i in range(len(temp_array) - 1):
    temp_array[i + 1] = temp_array[i] - temp_diff(temp_array[i], coffee)

df = pd.DataFrame(data=temp_array, index=time_array, columns=["Temperature"])
df.plot()
