def coordinates(latitude: float, longitude: float) -> str:
    def convert_to_dms(decimal_degree, is_lat):
        is_positive = decimal_degree >= 0
        decimal_degree = abs(decimal_degree)
        degrees = int(decimal_degree)
        minutes_full = (decimal_degree - degrees) * 60
        minutes = int(minutes_full)
        seconds = (minutes_full - minutes) * 60
        if is_lat:
            direction = 'N' if is_positive else 'S'
        else:
            direction = 'E' if is_positive else 'W'
            
        return (f"{degrees}°"
                f"{str(minutes).rjust(2, "0")}'"
                f"{str(f'{seconds:.2f}').rjust(5, '0')}\""
                f"{direction}")
    
    return convert_to_dms(latitude, True) + " " + convert_to_dms(longitude, False)


def heading(heading_: float) -> str:
    match heading_:
        case h if h >= 337.5 or h < 22.5: direction = "N"
        case h if 22.5  <= h <  67.5: direction = "NE"
        case h if 67.5  <= h < 112.5: direction = "E"
        case h if 112.5 <= h < 157.5: direction = "SE"
        case h if 157.5 <= h < 202.5: direction = "S"
        case h if 202.5 <= h < 247.5: direction = "SW"
        case h if 247.5 <= h < 292.5: direction = "W"
        case h if 292.5 <= h < 337.5: direction = "NW"
        case _: direction = ""
    
    return f"{heading_}º {direction}"
