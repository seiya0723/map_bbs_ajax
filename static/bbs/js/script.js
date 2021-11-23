window.addEventListener("load" , function (){
    map_load();
});


//マップのデータをGET文で手に入れる
function map_load(){

    let form_elem   = "#form_area";

    let url     = $(form_elem).prop("action");
    let method  = "GET";

    $.ajax({
        url: url,
        type: method,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) {

        console.log(data.topics);
        map_draw(data.topics);

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    });
}

//マップにマーカーを描画
function map_draw(topics){

    console.log("マップドロー")

    for (let topic of topics ){
        L.marker([topic["lat"], topic["lon"]]).addTo(map).bindPopup(topic["comment"]).openPopup();
    }

}




