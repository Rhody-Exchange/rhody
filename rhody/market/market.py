import requests


class Market:
    @staticmethod
    def price(symbol: str):
        """
        Fetch the latest market price for a given symbol from the Flask API.

        :param symbol: Stock ticker (e.g., "AAPL", "BTC-USD")
        :return: Latest price as a float, or None if the request fails
        """
        API_URL = "https://api.rhodyexchange.org/market/price"  # Replace with your actual Flask API URL

        try:
            response = requests.get(f"{API_URL}/{symbol}")
            response.raise_for_status()  # Raise error if bad response
            data = response.json()
            return data.get("price", None)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
