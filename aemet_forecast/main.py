from typing import List


from ._typing import ApiForecastResponse, Municipio
from .constants import (
    DAILY_FORECAST_API_URL,
    MUNICIPIOS_API_URL,
    MUNICIPIOS_DETALLE_API_URL,
)
from .utils.aemet_http import (
    http_get_api_urls,
    http_normal_data_api_call,
    http_forecast_api_call,
)


class Aemet:
    """Main Aemet class"""

    def __init__(self, api_key):
        self.api_key = api_key

    def get_all_municipios(self) -> List[Municipio]:
        """Get all municipios data

        Returns:
            List[Municipio]: Returns the list of all municipios with their data.
        """

        api_urls_response = http_normal_data_api_call(
            url=MUNICIPIOS_API_URL, api_key=self.api_key
        )

        return api_urls_response["data"]

    def get_municipio(self, id_municipio: str) -> Municipio:
        """Get the municipio data

        Args:
            id_municipio (str): Municipio id. ex: id14021

        Returns:
            Municipio: Return the municipio data
        """

        api_urls_response = http_normal_data_api_call(
            url=f"{MUNICIPIOS_DETALLE_API_URL}{id_municipio}", api_key=self.api_key
        )

        return api_urls_response["data"][0]


class AemetForecast(Aemet):
    """Aemet class for forecast data"""

    def get_daily_forecast(self, id_municipio: int) -> List[ApiForecastResponse]:
        """This function get the daily forecast data in the next 7 days-

        Args:
            municipio (int): the id aemet gives to the "Municipio" in int format. Ex: 14021 instead of "id14021"

        Raises:
            Exception: If request limit has been exceeded

        Returns:
            List[ApiForecastResponse]: List of all the weather data with the following format: -->

            List[
                fecha: str  # Período de validez de la Predicción.
                                Ex: '2022-06-01T00:00:00'
                uvMax: int  # Índice ultravioleta máximo
                probPrecipitacion: List[
                                        value: int  # %
                                        periodo: str  # 00-24 00-12 12-24 00-06
                                                        06-12 12-18 18-24
                                    ]
                cotaNieveProv: List[
                                    value: str  #  Valor de la cota de nieve
                                    periodo: str  # 00-24 00-12 12-24 00-06
                                                    06-12 12-18 18-24
                                ]
                estadoCielo: List[
                                descripcion: str  # Descripción del estado del cielo
                                value: str  # Código del estado del Cielo
                                periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24
                            ]
                viento: List[
                            periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24
                            direccion: str  # Dirección del viento (
                                                N/Norte, NE/Nordeste, E/Este,
                                                SE/Sudeste, S/Sur, SO/Suroeste,
                                                O / Oeste, NO / Noroeste, C / Calma
                                                )
                            velocidad: int  # Velocidad en Kilómetros por hora (km/h)
                        ]
                rachaMax: List[
                            periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24
                            direccion: str  # Dirección del viento (
                                                N/Norte, NE/Nordeste, E/Este,
                                                SE/Sudeste, S/Sur, SO/Suroeste,
                                                O / Oeste, NO / Noroeste, C / Calma)
                            velocidad: int  # Velocidad en Kilómetros por hora (km/h)
                        ]
                temperatura: List[
                                value: int  # Grados celsius
                                hora: int  # 0 to 24 horas
                            ]
                sensTermica: List[
                                value: int  # Grados celsius
                                hora: int  # 0 to 24 horas
                            ]
                humedadRelativa: List[
                                value: int  # Tanto por ciento (%)
                                hora: int  # 0 to 24 horas
                            ]
            ]
        """

        api_urls_response = http_get_api_urls(
            f"{DAILY_FORECAST_API_URL}{str(id_municipio)}", self.api_key
        )
        if api_urls_response["status"] == 429:
            raise Exception("LIMIT OF REQUESTS PER MINUTE. WAIT ONE MINUTE")
        url_data: str = api_urls_response["data"]
        forecast_response = http_forecast_api_call(url=url_data, api_key=self.api_key)
        forecast_data = forecast_response["data"]

        return forecast_data
