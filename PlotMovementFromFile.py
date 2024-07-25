import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
data = pd.read_csv('PhoneAcceleration.csv')

# Extract acceleration data
accel_x_list = data['ax'].values
accel_y_list = data['ay'].values

# Assuming uniform time intervals
dt = 1  # Time interval between samples, in seconds

# Convert lists to numpy arrays
accel_x = np.array(accel_x_list)
accel_y = np.array(accel_y_list)

# Integrate acceleration to get velocity
velocity_x = np.cumsum(accel_x) * dt
velocity_y = np.cumsum(accel_y) * dt

# Integrate velocity to get position
position_x = np.cumsum(velocity_x) * dt
position_y = np.cumsum(velocity_y) * dt

# Plot the spatial movement from top view
plt.figure(figsize=(8, 8))

# Plot X and Y position to show trajectory
plt.plot(position_x, position_y, marker='o', linestyle='-', color='b')
plt.xlabel('Position X (units)')
plt.ylabel('Position Y (units)')
plt.title('Trajectory of IMU Movement (Top View)')
plt.grid(True)
plt.show()
