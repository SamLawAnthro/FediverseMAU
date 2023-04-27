import matplotlib.pyplot as plt
import datetime
import requests

# Fetch JSON data from URL
url = "https://api.joinmastodon.org/statistics"
response = requests.get(url)
data = response.json()

# Extract dates and active user counts
dates = [datetime.datetime.strptime(item["period"], "%Y-%m-%d") for item in data]
active_user_counts = [int(item["active_user_count"]) for item in data]

# Create the line graph
plt.figure(figsize=(10, 5))
plt.plot(dates, active_user_counts)
plt.xlabel("Date")
plt.ylabel("Monthly Active Users")
plt.title("Monthly Active Users Over Time")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Save the graph as an image file
plt.savefig("monthly_active_users.png", bbox_inches="tight")

# Show the graph
plt.show()

