// import * as maplibregl from "maplibre-gl";
let markers = {};

let map = new maplibregl.Map({
    container: 'map',
    style: 'https://api.maptiler.com/maps/basic-v2/style.json?key=pVdKxpS1InGttwBR4kGp',
    center: [12.3295, 51.3361],
    zoom: 8
});

document.addEventListener("mqtt", function (e) {
    let data = JSON.parse(e.detail);
    if (data.lat !== undefined) {
        if (markers[data.hex]) {
            markers[data.hex].setLngLat([data.lon, data.lat]);
            markers[data.hex].setRotation(data.track);
        }
        else {
            var el = document.createElement('div');
            el.className = 'custom-marker';
            el.style.backgroundImage = 'url(plane.png)';
            el.style.width = '32px';
            el.style.height = '32px';

            let popup = new maplibregl.Popup({ closeButton: false, closeOnClick: false })
                .setHTML('<h3>' + data.hex + '</h3><p>Additional information here</p>');

            let marker = new maplibregl.Marker({
                element: el,
                anchor: 'center'
            }).setLngLat([data.lon, data.lat]).setRotation(data.track).setPopup(popup).addTo(map);
            markers[data.hex] = marker;
        }
    }
});
