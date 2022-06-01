import json
from typing import Any

from requests import request

from .._typing import HttpGetApiUrl, HttpApiCallData

headers = {
    "cache-control": "no-cache",
    "Content-type": "application/json",
}


def http_get_api_urls(url: str, api_key: str) -> HttpGetApiUrl:
    """This function gets the urls from the api where the data is stored.

        When a first API call is made, Aemet returns two URLs instead of the data.
        One URL has the data and the other the metadata.
        Therefore, to get the data it is necessary to make two requests

    Args:
        url (str): API URL
        api_key (str): The Aemet API key

    Returns:
        HttpGetApiUrl: return a dictionary with the "status" of the request
                        and the "data" and "metadata" urls
    """
    response = request("GET", url, headers=headers, params={"api_key": api_key})
    return {
        "status": response.status_code,
        "data": response.text.split()[9].replace('"', "").strip(","),
        "metadata": response.text.split()[12].replace('"', "").strip(","),
    }


def http_normal_data_api_call(url: str, api_key: str) -> Any:
    """This function returns the data from the url data (The second one)

    Args:
        url (str): Url of the data
        api_key (str): The Aemet API key

    Returns:
        HttpApiCallData: return a dictionay with the "status" and the "data"
    """
    response = request("GET", url, headers=headers, params={"api_key": api_key})
    return {
        "status": response.status_code,
        "data": json.loads(response.text),
    }


def http_forecast_api_call(url: str, api_key: str) -> HttpApiCallData:
    """This function returns the data from the url forecast data
        Is the same as http_normal but with only the data returned
        (Access to [0].preficcion.dia is necessary to get only the data)


    Args:
        url (str): Url of the data
        api_key (str): The Aemet API key

    Returns:
        HttpApiCallData: return a dictionay with the "status" and the "data"
    """
    response = http_normal_data_api_call(url=url, api_key=api_key)
    response["data"] = response["data"][0]["prediccion"]["dia"]
    return response
