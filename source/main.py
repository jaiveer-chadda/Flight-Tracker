from opensky_api import OpenSkyApi

_24_hrs_in_secs = 24 * 60 * 60
_2_hrs_in_secs = 2 * 60 * 60

api = OpenSkyApi()
states = api.get_states()

s = states.states[0]
print(f"""
\torigin:\t\t{s.origin_country}
\tcall sign:\t{s.callsign if s.callsign is not None else "unknown"}
    
\tpos:\t\t({s.latitude}, {s.longitude})
    
\talt:\t\t{s.baro_altitude} m
\tvel:\t\t{s.velocity} m/s
\tangle:\t\t{s.true_track}º
""")

track = api.get_track_by_aircraft(states.states[0].icao24)

print(f"\tstart:\t\t{tuple(track.path[0][1:3])}")
print(f"\tend:\t\t{tuple(track.path[-1][1:3])}\n")
