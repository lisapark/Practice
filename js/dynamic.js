function showCatName(){
	window.alert(document.catname.value);
}

var data = ""

$.ajax({
  url: "https://montanaflynn-cat-overflow.p.mashape.com/?limit=9&offset=1",
  headers: {
  	'X-Mashape-Key': 'tF8OhNKhTKmshvP35EC7XIn3VD6dp15x49WjsnW1DpioGWoPQA',
  	'Content-Type': 'text/plain'
  },
  method: 'GET',
  success: function(response){
  	data = response;
  	console.log(response);
  	var cat_images = data.split('\n');	
	cat_images.forEach(parseCatImages)
  }
});

function parseCatImages(cat_image, index, cat_images){
	console.log(cat_image)
	$("#image_" + index).attr("src", String(cat_image));
}