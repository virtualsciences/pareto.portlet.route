function draw(daddr, $map) {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({
        address: daddr
    }, function(results, status) {
        if (results.length > 0) {
            daddr = results[0].geometry.location
            if (status == google.maps.GeocoderStatus.OK) {
                map = new google.maps.Map($map[0], {
                    center: daddr,
                    zoom: 13,
                    mapTypeControl: false,
                    mapTypeId: 'terrain'
                });
                var marker = new google.maps.Marker({
                    map: map,
                    icon: '/++theme++arbounie.site/img/geo.png',
                    shadow:  '/++theme++arbounie.site/img/geo_shade.png',
                    position: daddr
                });
            } else {
                daddr = undefined;
            }
        } else {
            daddr = undefined;
        }   
    });
}

$(document).ready(function () {
    var $portletRoute = $(".portletRoute");
    for(var i = 0; i < $portletRoute.length; i++) {
        var latLng,
            $pr = $portletRoute.eq(i),
            $portletHeader = $pr.find('.portletHeader'),
            daddr = $pr.find('input[name=daddr]').val(),
            $map = $('<div class="map">'),
            $mapContainer = $map.wrap('<dd class="portletItem">').parent(),
            mapWidth = $portletRoute.width(),
            mapHeight = mapWidth * 3 / 4;
        
        $map.width(mapWidth);
        $map.height(mapHeight);

        $mapContainer.insertAfter($portletHeader);
        draw(daddr, $map);
    };
});    
