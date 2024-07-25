import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the processed data
data = pd.read_csv('/Volumes/My Passport/vesha designs/processed_amenities.csv')

# Initialize the Prophet model
model = Prophet()

# Fit the model
model.fit(data)

# Create a dataframe for future dates
future = model.make_future_dataframe(periods=12, freq='M')  # Adjust periods as needed

# Predict future values
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
plt.show()

# Save the forecast to a CSV file
forecast.to_csv('/Volumes/My Passport/vesha designs/forecast.csv', index=False)

print("Forecast saved to 'forecast.csv'.")
