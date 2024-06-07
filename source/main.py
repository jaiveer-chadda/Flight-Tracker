from opensky_api import OpenSkyApi

from Meta import Formatting

_24_hrs_in_secs = 24 * 60 * 60
_2_hrs_in_secs = 2 * 60 * 60

api = OpenSkyApi()
states = api.get_states()

s = states.states[50]

print(f"""
\torigin:\t\t{s.origin_country}
\tcall sign:\t{"unknown" if s.callsign in [None, ""] else s.callsign}

\tpos:\t\t{Formatting.coordinates(s.latitude, s.longitude)}

\talt:\t\t{s.baro_altitude} m
\tvel:\t\t{s.velocity} m/s
\theading:\t{Formatting.heading(s.true_track)}
""")

track = api.get_track_by_aircraft(s.icao24)

path_is_valid = track is not None

print(f"\tstart:\t\t{Formatting.coordinates(*track.path[0][1:3]) if path_is_valid else "unknown"}")
print(f"\tend:\t\t{Formatting.coordinates(*track.path[-1][1:3]) if path_is_valid else "unknown"}\n")
