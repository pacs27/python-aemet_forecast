# PYTHON-AEMET_FORECAST

A Python module for accessing Aemet forecast data through its api

```python
from aemet_forecast import AemetForecast

API_KEY = "your-api-key"
MUNICIPIO_ID = 14021

forecast = AemetForecast(api_key=API_KEY)

weekly_forecast_data = forecast.get_daily_forecast(MUNICIPIO_ID)
```