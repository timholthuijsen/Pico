import time
import board
import busio
import adafruit_mpu6050

# Initialize I2C and MPU6050 sensor
i2c = busio.I2C(board.GP5, board.GP4)  # Adjust pins if needed
mpu = adafruit_mpu6050.MPU6050(i2c)

# Open a CSV file on the CIRCUITPY drive
csv_filename = "/sensor_data.csv"
try:
    with open(csv_filename, "w") as file:
        # Write header row
        file.write("Timestamp,Accel_X (m/s^2),Accel_Y (m/s^2),Accel_Z (m/s^2),Gyro_X (rad/s),Gyro_Y (rad/s),Gyro_Z (rad/s)\n")

        # Collect data and save to CSV
        for _ in range(100):  # Collect 100 samples
            # Read accelerometer data
            accel_x, accel_y, accel_z = mpu.acceleration
            # Read gyroscope data
            gyro_x, gyro_y, gyro_z = mpu.gyro

            # Get current timestamp
            timestamp = time.monotonic()

            # Write data to CSV
            file.write(f"{timestamp},{accel_x},{accel_y},{accel_z},{gyro_x},{gyro_y},{gyro_z}\n")

            # Print the data to the console for debugging (optional)
            print(f"Timestamp: {timestamp}, Accel: ({accel_x}, {accel_y}, {accel_z}), Gyro: ({gyro_x}, {gyro_y}, {gyro_z})")

            # Delay for readability
            time.sleep(0.5)
            
    print("Data written to CSV successfully.")
except OSError as e:
    print("Error:", e)
