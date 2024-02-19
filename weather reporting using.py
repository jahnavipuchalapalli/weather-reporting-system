import random
import matplotlib.pyplot as plt

# Function to generate simulated weather data
def generate_weather_data():
    temperature = random.uniform(20, 35)  # Temperature in Celsius
    humidity = random.uniform(40, 80)  # Relative humidity in percentage
    rain_intensity = random.uniform(0, 10)  # Rain intensity in mm/hr
    return temperature, humidity, rain_intensity

# Simulate weather data
num_iterations = 24  # Number of iterations to simulate (24 hours)
timestamps = range(num_iterations)
temperatures = []
humidity_values = []
rain_intensities = []

for _ in timestamps:
    temperature, humidity, rain_intensity = generate_weather_data()
    temperatures.append(temperature)
    humidity_values.append(humidity)
    rain_intensities.append(rain_intensity)

# Plotting the data
plt.figure(figsize=(12, 6))

# Plot Temperature
plt.subplot(3, 1, 1)
plt.plot(timestamps, temperatures, color='red')
plt.title('Temperature (°C)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature')

# Plot Humidity
plt.subplot(3, 1, 2)
plt.plot(timestamps, humidity_values, color='blue')
plt.title('Humidity (%)')
plt.xlabel('Time (hours)')
plt.ylabel('Humidity')

# Plot Rain Intensity
plt.subplot(3, 1, 3)
plt.plot(timestamps, rain_intensities, color='green')
plt.title('Rain Intensity (mm/hr)')
plt.xlabel('Time (hours)')
plt.ylabel('Rain Intensity')

plt.tight_layout()
plt.show()
