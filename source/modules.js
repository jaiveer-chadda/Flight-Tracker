// Define Meta module
const Meta = {
    Format: {
        coordinates: function(latitude, longitude) {
            return `(${latitude}, ${longitude})`;
        },
        heading: function(heading) {
            return `${heading} degrees`;
        }
    },
    Process: {
        find_nearest_airport: function(coords) {
            return [`Airport`, 0]; // Example return value
        }
    }
};

// Define opensky package
const opensky = {
    python: {
        opensky_api: {
            OpenSkyApi: function() {
                return {
                    get_states: function() {
                        return {
                            states: [
                                {
                                    origin_country: 'Country',
                                    callsign: 'Callsign',
                                    latitude: 0.0,
                                    longitude: 0.0,
                                    icao24: 'ICAO24',
                                    baro_altitude: 0.0,
                                    velocity: 0.0,
                                    true_track: 0.0
                                }
                            ]
                        };
                    },
                    get_track_by_aircraft: function(icao24) {
                        return {
                            path: [
                                [0.0, 0.0, 0.0],
                                [1.0, 1.0, 1.0]
                            ]
                        };
                    }
                };
            }
        }
    }
};

// Export Meta and opensky for Pyodide
language-python
self.Meta = Meta;
self.opensky = opensky;
