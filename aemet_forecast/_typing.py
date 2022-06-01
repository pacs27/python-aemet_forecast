from typing import TypedDict, List


class HttpGetApiUrl(TypedDict):
    status: int
    data: str
    metadata: str


class Municipio(TypedDict):
    id: str  # ex: id44001
    nombre: str  # name. ex: Ababuj
    id_old: str  # ex: 44004
    url: str  # ex: 'ababuj-id44001'
    num_hab: str  # number persons. ex: 65
    latitud: str  # ex: '40º32\'54.450744"'
    latitud_dec: str  # ex: '40.54845854'
    longitud_dec: str  # ex: '-0.80780117'
    longitud: str  # ex: '-0º48\'28.084212"'
    altitud: str  # meters, ex: 1372
    destacada: str  # ex: 0


class ProbPrecipValue(TypedDict):
    value: int  # %
    periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24


class CotNieveValue(TypedDict):
    value: str  # Valor de la cota de nieve
    periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24


class EstadoCieloValue(TypedDict):
    descripcion: str  # Descripción del estado del cielo
    value: str  # Código del estado del Cielo
    periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24


class VientoValue(TypedDict):
    periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24
    direccion: str  # Dirección del viento (N/Norte, NE/Nordeste, E/Este, SE/Sudeste, S/Sur, SO/Suroeste, O / Oeste, NO / Noroeste, C / Calma
    velocidad: int  # Velocidad en Kilómetros por hora (km/h)


class RachaMaxValue(TypedDict):
    periodo: str  # 00-24 00-12 12-24 00-06 06-12 12-18 18-24
    value: str  # velocidad del viento en Kilómetros por hora (km/h)


class TemperaturaHoraValue(TypedDict):
    value: int  # Grados celsius
    hora: int  # 0 to 24 horas


class TemperaturaValue(TypedDict):
    maxima: int  # Grados celsius
    minima: int  # Grados celsius
    dato: List[TemperaturaHoraValue]


class SensacionTermicaValue(TypedDict):
    maxima: int  # Grados celsius
    minima: int  # Grados celsius
    dato: List[TemperaturaHoraValue]


class HumedadRelativaHoraValue(TypedDict):
    value: int  # Tanto por ciento (%)
    hora: int  # 0 to 24 horas


class HumedadRelativaValue(TypedDict):
    maxima: int  # Tanto por ciento (%)
    minima: int  # Tanto por ciento (%)
    dato: List[HumedadRelativaHoraValue]


class ApiForecastResponse(TypedDict):
    fecha: str  # Período de validez de la Predicción. Ex: '2022-06-01T00:00:00'
    uvMax: int  # Índice ultravioleta máximo
    probPrecipitacion: List[ProbPrecipValue]
    cotaNieveProv: List[CotNieveValue]
    estadoCielo: List[EstadoCieloValue]
    viento: List[VientoValue]
    rachaMax: List[RachaMaxValue]
    temperatura: List[TemperaturaValue]
    sensTermica: List[SensacionTermicaValue]
    humedadRelativa: List[HumedadRelativaValue]


class HttpApiCallData(TypedDict):
    status: int
    data: List[ApiForecastResponse]
