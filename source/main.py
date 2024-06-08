import random as rand
from opensky.python.opensky_api import OpenSkyApi

from Meta import Format, Process

api = OpenSkyApi()
states = api.get_states()

if states is None:
    raise Exception("No states found")

s = states.states[rand.randint(0, len(states.states))]
track = api.get_track_by_aircraft(s.icao24)

path_is_valid = track is not None

print(f"""
\torigin:\t\t{s.origin_country}
\tcall sign:\t{"unknown" if s.callsign in (None, "") else s.callsign}

\tcurrent coords:\t{Format.coordinates(s.latitude, s.longitude)}
\tstart coords:\t{Format.coordinates(*track.path[0][1:3]) if path_is_valid else "unknown"}
\tend coords:\t{Format.coordinates(*track.path[-1][1:3]) if path_is_valid else "unknown"}

\tstart location:\t{Process.find_nearest_airport(track.path[0][1:3])[0] if path_is_valid else "unknown"}
\tend location:\t{Process.find_nearest_airport(track.path[-1][1:3])[0] if path_is_valid else "unknown"}

\taltitude:\t{"unknown" if s.baro_altitude in (None, "") else (str(s.baro_altitude) + " m")}
\tvelocity:\t{"unknown" if s.velocity in (None, "") else (str(s.velocity) + " m/s")}
\theading:\t{Format.heading(s.true_track)}
""")
