var shared_methods = (function () {
    var add_div_background_image = function(div_name, image_path){
		//$('selector').css({'background-image':'url(images/example.jpg)'});
		$("#"+div_name).css({'background-image':'url('+image_path+')', "background-size": "100% 100%"});
	}    
    
    return {
        add_div_background_image:add_div_background_image
    }
})();