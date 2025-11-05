from enum import Enum


class TimePeriod(Enum):
    """
    An enumeration of time periods.
    """
    DAY = '24h'
    WEEK = '7d'
    MONTH = '30d'
    YEAR = '1y'


class FlightCategory(Enum):
    """
    An enumeration of flight categories.
    """
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
    """
    An enumeration of HTTP status codes.
    """
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500


class DataSources(Enum):
    """
    An enumeration of data sources.
    """
    ADSB = 'ADSB'
    MLAT = 'MLAT'
    ESTIMATED = 'ESTIMATED'
    ALL = None


class Direction(Enum):
    """
    An enumeration of directions.
    """
    BOTH = 'both'
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'


class Sort(Enum):
    """
    An enumeration of sort orders.
    """
    ASC = 'asc'
    DESC = 'desc'


class HistoricFlightEventTypes(Enum):
    """
    An enumeration of historic flight event types.
    """
    ALL = 'all'
    GATE_DEPARTURE = 'gate_departure'
    TAKEOFF = 'takeoff'
    CRUISING = 'cruising'
    AIRSPACE_TRANSITION = 'airspace_transition'
    DESCENT = 'descent'
    LANDED = 'landed'
    GATE_ARRIVAL = 'gate_arrival'
