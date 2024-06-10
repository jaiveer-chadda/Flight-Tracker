// // Initialise the map with constraints
// map = L.map('map', {
//     center: [20, 0],
//     zoom: 2,
//     minZoom: 2, // Set minimum zoom level
//     maxZoom: 19, // Set maximum zoom level
// });
//
// // Add a tile layer to the map
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 19,
//     attribution: '© OpenStreetMap contributors'
// }).addTo(map);
//
// // Define coordinates for the two points
// point1 = [37.7749, -122.4194]; // San Francisco
// point2 = [40.7128, -74.0060];  // New York City
//
// // Add markers to the map
// L.marker(point1).addTo(map).bindPopup('San Francisco');
// L.marker(point2).addTo(map).bindPopup('New York City');
// L.marker([0, 0]).addTo(map).bindPopup('0, 0');
//
// // Draw a line between the two points
// latlngs = [point1, point2];
// polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map);
//
// // Set the map view to fit the polyline with some padding
// map.fitBounds(polyline.getBounds(), {padding: [50, 50]});
//
// // Set max bounds to prevent the user from zooming out too far
// bounds = map.getBounds().pad(0.5); // Add some padding to the bounds
// map.setMaxBounds(bounds);

/* Transfer code from Python */

async function runPythonCode() {
    // Load Pyodide
    const pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.17.0/full/" });

    // Load custom modules
    await pyodide.loadScript('path_to_custom_modules.js');

    // Your Python code
    const pythonCode = `
import random as rand

api = opensky.python.opensky_api.OpenSkyApi()
states = api.get_states()

if states is None:
    raise Exception("No states found")

s = states.states[rand.randint(0, len(states.states))]
track = api.get_track_by_aircraft(s.icao24)

path_is_valid = track is not None

print(f"""
    \torigin:\t\t{s.origin_country}
    \tcall sign:\t{"unknown" if s.callsign in (None, "") else s.callsign}

    \tcurrent coords:\t{Meta.Format.coordinates(s.latitude, s.longitude)}
    \tstart coords:\t{Meta.Format.coordinates(*track.path[0][1:3]) if path_is_valid else "unknown"}
    \tend coords:\t{Meta.Format.coordinates(*track.path[-1][1:3]) if path_is_valid else "unknown"}

    \tstart location:\t{Meta.Process.find_nearest_airport(track.path[0][1:3])[0] if path_is_valid else "unknown"}
    \tend location:\t{Meta.Process.find_nearest_airport(track.path[-1][1:3])[0] if path_is_valid else "unknown"}

    \taltitude:\t{"unknown" if s.baro_altitude in (None, "") else (str(s.baro_altitude) + " m")}
    \tvelocity:\t{"unknown" if s.velocity in (None, "") else (str(s.velocity) + " m/s")}
    \theading:\t{Meta.Format.heading(s.true_track)}
""")
    `;

    // Run Python code
    const output = await pyodide.runPythonAsync(pythonCode);
    document.getElementById("output").innerText = output;
}
