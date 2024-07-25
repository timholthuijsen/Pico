import time
import board
import busio
import adafruit_mpu6050

# Define variables for the I2C pins
scl_pin = board.GP5
sda_pin = board.GP4

# Create the I2C bus using the variables
i2c = busio.I2C(scl_pin, sda_pin)

# Create MPU6050 object
mpu = adafruit_mpu6050.MPU6050(i2c)

# Main loop
while True:
    # Read accelerometer data
    accel_x, accel_y, accel_z = mpu.acceleration
    # Read gyroscope data
    gyro_x, gyro_y, gyro_z = mpu.gyro

    # Print accelerometer data
    print("Accelerometer (m/s^2):")
    print("X:", accel_x)
    print("Y:", accel_y)
    print("Z:", accel_z)

    # Print gyroscope data
    #print("Gyroscope (rad/s):")
    #print("X:", gyro_x)
    #print("Y:", gyro_y)
    #print("Z:", gyro_z)

    # Add a delay for readability
    time.sleep(0.5)
