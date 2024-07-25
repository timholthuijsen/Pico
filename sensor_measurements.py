import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.spatial.transform import Rotation



np.random.seed(69)
gravity = 3.7206 # gravity on mars in m/s^2
gravity_vector = np.array([0,-gravity,0]) # unity convention


#%% Acceleration measurements (including gravity)

acc_file = "PhoneAcceleration.csv"

acc_data = pd.read_csv(acc_file)

# Plotting the data
plt.figure(figsize=(15, 15))

# Plot Acceleration Measurements
plt.subplot(3, 1, 1)
plt.plot(acc_data['time'], acc_data['ax'], label='True Acc X', linestyle='dashed')
plt.title('Acc X')
plt.xlabel('Time (s)')
plt.ylabel('Acc (units/s^2)')
plt.xticks(np.arange(0,acc_data['time'][len(acc_data['time'])-1],2))
plt.legend(loc = 0)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(acc_data['time'], acc_data['ay'], label='True Acc Y', linestyle='dashed')
plt.title('Acc Y')
plt.xlabel('Time (s)')
plt.ylabel('Acc (units/s^2)')
plt.xticks(np.arange(0,acc_data['time'][len(acc_data['time'])-1],2))
plt.legend(loc = 0)
plt.grid(True)


# Adjust layout for better spacing
plt.tight_layout()
plt.show()


#%% Position from linear acceleration (with removal of gravity)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_acc_pos(acc_filename):
    '''
    Parameters
    ----------
    acc_filename : string
        Path for acc file containing acceleration data
        (relative to current working directory, i.e. script directory)
        
    Returns
    -------
    acc_pos_data
        List containing [pos_x, pos_y, pos_z] computed from acceleration data.
    '''
    
    acc_data = pd.read_csv(acc_filename)
    
    time = np.array(acc_data['time'])
    
    acc_pos_data = []

    # Read accelerations
    acc_x = np.array(acc_data['ax'])
    acc_y = np.array(acc_data['ay'])
    acc_z = np.array(acc_data['az'])
    
    delta_t = np.diff(time)
    
    # Integrate once to get velocity
    vel_x = np.cumsum(acc_x[:-1] * delta_t)
    vel_y = np.cumsum(acc_y[:-1] * delta_t)
    vel_z = np.cumsum(acc_z[:-1] * delta_t)
    
    # Integrate once more to get position
    pos_x = np.cumsum(vel_x * delta_t)
    pos_y = np.cumsum(vel_y * delta_t)
    pos_z = np.cumsum(vel_z * delta_t)
    
    acc_pos_data.append([pos_x, pos_y, pos_z, time[1:]])
    
    return acc_pos_data

# Example usage
acc_file = 'PhoneAcceleration.csv'  # replace with your actual file path
acc_pos_data = get_acc_pos(acc_file) 

# Plot the path in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot X, Y, Z position
ax.plot(acc_pos_data[0][0], acc_pos_data[0][1], acc_pos_data[0][2], linestyle='-', color='green')

# Set labels and title
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Z position')
ax.set_title("Trajectory in 3D Space")

plt.show()
