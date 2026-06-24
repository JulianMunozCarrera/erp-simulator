# ERP Simulator

# The imports
import numpy as np
import matplotlib.pyplot as plt

# The function to generate one trial
def generate_trial(condition):
    # 1. Create 1000 random noise values using np.random.normal
    noise = np.random.normal(0,1,1000)
    # 2. If condition is N400 add a negative bump between indices 300 and 500
    if condition == "N400":
        noise[300:500] -= 5
    # 3. If condition is P600 add a postive bump between indices 500 and 700
    elif condition == "P600":
        noise[500:700] += 5
    # 4. Return the array
    return noise 

# Test it
trial_n400 = generate_trial("N400")
plt.plot(trial_n400)
plt.show()

trial_p600 = generate_trial("P600")
plt.plot(trial_p600)
plt.show()

# The function to generate multiple trials
def generate_trials(condition, n_trials):
    trials = []
    for i in range(n_trials):
        trials.append(generate_trial(condition))
    return np.array(trials)
    
# Generate both datasets
n400_data = generate_trials("N400", 50)
p600_data = generate_trials("P600", 50)

# Average across the 50 trials
n400_avg = np.mean(n400_data, axis = 0)
p600_avg = np.mean(p600_data, axis = 0)

# Plot clean data
time = np.arange(1000)              # x-axis: 0 to 999 (representing milliseconds)
plt.plot(time, n400_avg, label="N400")
plt.plot(time, p600_avg, label="P600")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude (µV)")
plt.title("Simulated ERP Grand Averages")
plt.legend()
plt.savefig("erp_plot.png")
plt.show()