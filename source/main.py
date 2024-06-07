import random as rand
from opensky_api import OpenSkyApi

from Meta import Formatting

api = OpenSkyApi()
states = api.get_states()
s = states.states[rand.randint(0, len(states.states))]
track = api.get_track_by_aircraft(s.icao24)
path_is_valid = track is not None

print(f"""
\torigin:\t\t{s.origin_country}
\tcall sign:\t{"unknown" if s.callsign in [None, ""] else s.callsign}

\tcurrent pos:\t{Formatting.coordinates(s.latitude, s.longitude)}
\tstart pos:\t{Formatting.coordinates(*track.path[0][1:3]) if path_is_valid else "unknown"}
\tend pos:\t{Formatting.coordinates(*track.path[-1][1:3]) if path_is_valid else "unknown"}

\talt:\t\t{s.baro_altitude} m
\tvel:\t\t{s.velocity} m/s
\theading:\t{Formatting.heading(s.true_track)}
""")
