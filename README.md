# Monthly Active Users Graph

This Python script creates a line graph of monthly active users over time using data fetched from the Mastodon API (https://api.joinmastodon.org/statistics). The script utilizes the `matplotlib` library to generate the graph and the `requests` library to fetch data from the API.

## Dependencies

- Python 3.6 or higher
- matplotlib
- requests

You can install the required libraries using pip:

```
pip install matplotlib requests

```


## Usage

1. Clone the repository or download the `monthly_active_users.py` script.
2. Navigate to the directory containing the script using the terminal or command prompt.
3. Run the script:

```
python MastadonActiveUsers.py

```

The script will fetch data from the Mastodon API, generate a line graph of monthly active users over time, and save the graph as an image file named `monthly_active_users.png` in the current directory. The script will also display the graph in a separate window.
