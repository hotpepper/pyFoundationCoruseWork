import os

class Map():
    """ generates the map for the most full and most empty station"""

    def __init__(self, la1, ln1, la2, ln2, cnt, pctFull1, pctFull2):
        self.la1 = la1
        self.ln1 = ln1
        self.la2 = la2
        self.ln2 = ln2
        self.cnt = cnt
        self.pctFull1 = pctFull1
        self.pctFull2 = pctFull2
        self.txt = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map-canvas { height: 100% }
    </style>
    <script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBdDoZL9UQuvbSTNNISUilgLVo_L9tfR5Y&sensor=false">
    </script>
    <script type="text/javascript">
      function initialize() {
	  
		var mapCenter=new google.maps.LatLng("""+str(la1)+""", """+str(ln1)+""");
		var myCenter=new google.maps.LatLng("""+str(la2)+""", """+str(ln2)+""");
		var myCenter2=new google.maps.LatLng("""+str(cnt[0])+""", """+str(cnt[1])+""");
		
		var marker = new google.maps.Marker({
			position: myCenter,
			title:'Click to zoom'
			});
		
		var marker2 = new google.maps.Marker({
			position: myCenter2,
			title:'Click to zoom'
			});
			
			
        var mapOptions = {
          center: mapCenter,
          zoom: 13,
          mapTypeId: google.maps.MapTypeId.HYBRID
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
		
		marker.setMap(map);
		marker2.setMap(map);
		
      var infowindow = new google.maps.InfoWindow({
		content:"%s"
		});
	var infowindow2 = new google.maps.InfoWindow({
		content:"%s"
		});
		
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
		});
		
	google.maps.event.addListener(marker2, 'click', function() {
		infowindow2.open(map,marker2);
		});
	
}
	  
	  
      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"/>
  </body>
</html>
""" % (str(pctFull1*100)+'% full' , str(pctFull2*100)+'% full')

    def write(self):
        output = open('reschufel.html', 'w')
        output.write(self.txt)
        output.close()
        os.startfile('reschufel.html')
            
