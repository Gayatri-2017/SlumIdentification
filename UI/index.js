
// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 19.0760, lng: 72.8777};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}

function genScreenshot() {
    html2canvas($('#map')/* document.body */, {
      proxy: "server.js",
      useCORS: true,
      onrendered: function(canvas) {
       /* $('#map').html("");
       $('#map').append(canvas); */ 
      if (navigator.userAgent.indexOf("MSIE ") > 0 || 
					navigator.userAgent.match(/Trident.*rv\:11\./)) 
			{
      	var blob = canvas.msToBlob();
        window.navigator.msSaveBlob(blob,'Test file.png');
      }
      else {
        $('#test').attr('href', canvas.toDataURL("image/png"));
        $('#test').attr('download','Test file.png');
        $('#test')[0].click();
      } 
      }
      
    }, );
    
}