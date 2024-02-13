import os
import unittest

from aemet_forecast import AemetForecast


# Import API Key from .env file
API_KEY = os.getenv("AEMET_API_KEY")



class TestForecast(unittest.TestCase):
    API_KEY = API_KEY
    forecast = AemetForecast(api_key=API_KEY)
    MUNICIPIO_ID = 14021

    def test_get_daily_forecast(self):
        weekly_forecast_data = self.forecast.get_daily_forecast(self.MUNICIPIO_ID)
        print(weekly_forecast_data)


if __name__ == "__main__":
    unittest.main()