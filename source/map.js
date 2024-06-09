// Initialise the map with constraints
map = L.map('map', {
    center: [20, 0],
    zoom: 2,
    minZoom: 2, // Set minimum zoom level
    maxZoom: 19, // Set maximum zoom level
});

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Define coordinates for the two points
point1 = [37.7749, -122.4194]; // San Francisco
point2 = [40.7128, -74.0060];  // New York City

// Add markers to the map
L.marker(point1).addTo(map).bindPopup('San Francisco');
L.marker(point2).addTo(map).bindPopup('New York City');
L.marker([0, 0]).addTo(map).bindPopup('0, 0');

// Draw a line between the two points
latlngs = [point1, point2];
polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map);

// Set the map view to fit the polyline with some padding
map.fitBounds(polyline.getBounds(), {padding: [50, 50]});

// Set max bounds to prevent the user from zooming out too far
bounds = map.getBounds().pad(0.5); // Add some padding to the bounds
map.setMaxBounds(bounds);