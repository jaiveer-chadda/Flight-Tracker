from typing import Optional
from math import sqrt

from Setup import Constants as c


def _euclidean_dist(coord1: tuple[float, float], coord2: tuple[float, float]) -> float:
    return sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)


def _get_coordinate_list() -> list[tuple[str, tuple[float, float]]]:
    with open(c.AIRPORTS_DB_FP, 'r') as database_txt:
        airport_list: list[str] = database_txt.read().split("\n")
        
    # EGLL,Heathrow,London,England,51.477,-0.461
    # Airport Code;Airport Name;City Name;Country Name;Country Code;Latitude;Longitude;World Area Code;City Name geo_name_id;Country Name geo_name_id;coordinates
        
    final_coord_list: list[tuple[str, tuple[float, float]]] = []
    
    for airport_string in airport_list:
        try:
            # print(airport_string)
            content: list[str] = airport_string.split(":")
            name: str = f"{content[1]} Airport - {content[2]}, {content[3]}"
            coords: tuple[str, tuple[float, float]] = name, (float(content[5]), float(content[6]))
            # Heathrow, 51.477, -0.461
            final_coord_list.append(coords)
        except ValueError | IndexError as e:
            print(airport_string)
            raise Exception
        
    return final_coord_list


def _find_closest_coordinate(given_coord: tuple[float, float]) -> tuple[str, tuple[float, float]]:
    coord_list: list[tuple[str, tuple[float, float]]] = _get_coordinate_list()
    
    closest_coord: Optional[tuple[float, float]] = None
    closest_airport: Optional[str] = None
    min_distance: float = float('inf')
    
    for name, coords in coord_list:
        distance: float = _euclidean_dist(given_coord, coords)
        if distance < min_distance:
            min_distance, closest_airport, closest_coord = distance, name, coords
    
    return closest_airport, closest_coord if closest_coord is not None and closest_airport is not None else ()


def find_nearest_airport(dec_coordinates: tuple[float, float]):
    return _find_closest_coordinate(dec_coordinates)
