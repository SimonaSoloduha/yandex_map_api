ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [59.932666, 30.329596],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            clusterize: true,
            gridSize: 32,
            clusterDisableClickZoom: true
        });

    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    myMap.geoObjects.add(objectManager);

    $.ajax({
        url: "static/json_path/json_2.json"
    }).done(function(data) {
        objectManager.add(data);
    });

}