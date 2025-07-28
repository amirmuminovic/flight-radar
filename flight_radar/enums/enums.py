from enum import Enum


class TimePeriod(Enum):
    DAY = '24h'
    WEEK = '7d'
    MONTH = '30d'
    YEAR = '1y'


class FlightCategory(Enum):
    PASSENGER = 'P'
    CARGO = 'C'
    MILITARY_AND_GOVERNMENT = 'M'
    BUSINESS_JETS = 'J'
    GENERAL_AVIATION = 'T'
    HELICOPTERS = 'H'
    LIGHTER_THAN_AIR = 'B'
    GLIDERS = 'G'
    DRONES = 'D'
    GROUND_VEHICLES = 'V'
    OTHER = 'O'
    NON_CATEGORIZED = 'N'


class HTTPStatus(Enum):
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500


class DataSources(Enum):
    ADSB = 'ADSB'
    MLAT = 'MLAT'
    ESTIMATED = 'ESTIMATED'
    ALL = None


class Direction(Enum):
    BOTH = 'both'
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'


class Sort(Enum):
    ASC = 'asc'
    DESC = 'desc'


class HistoricFlightEventTypes(Enum):
    ALL = 'all'
    GATE_DEPARTURE = 'gate_departure'
    TAKEOFF = 'takeoff'
    CRUISING = 'cruising'
    AIRSPACE_TRANSITION = 'airspace_transition'
    DESCENT = 'descent'
    LANDED = 'landed'
    GATE_ARRIVAL = 'gate_arrival'
