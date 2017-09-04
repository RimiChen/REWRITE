var shared_methods = (function () {
    var add_div_background_image = function(div_name, image_path){
		//$('selector').css({'background-image':'url(images/example.jpg)'});
		$("#"+div_name).css({'background-image':'url('+image_path+')', "background-size": "100% 100%"});
    } 
	var load_story_text = function(filePath, story_name){
		var story_content = "";
		file_path = filePath;
		$.get(filePath, function(data){
			story_content = data;
			//console.log(data);
			g_story_settings.story_pool[story_name].content = data;
			//return data;
		});
	}       
    
    return {
        add_div_background_image:add_div_background_image,
        load_story_text: load_story_text
    }
})();