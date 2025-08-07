import random

def sim_adc_value(channel):
    if channel== 0:
       return random.uniform(10.5,12.6)
    elif channel == 1:
       return random.uniform(0.5,2.0)
    elif channel == 2:
       return random.uniform(25.0,45.0)

