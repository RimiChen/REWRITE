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
    var load_story_assertions = function(filePath) {
        var result_text="";
        $.ajax({
            async: false,
            dataType : 'json',
            url: filePath,
            type : 'GET',
            success: function(data) {
                var assertion_count = 0;
                for(var key in data){ 
                    //here do your logic and assign value for code varable   
                    each_story_settings.assert_pool[assertion_count] = data[key];
                    result_text = result_text+ "{"+data[key]['r']+", "+data[key]['relation']+", "+data[key]['l']+"}\n"; 
                    assertion_count++;
                }
            }
        });
   
        return result_text;
    }  
	function create_assertions_row(r_value, rela_value, l_value, result_text){
		//console.log(r_value+", "+ rela_value+", "+ l_value);
		result_text = result_text+"{"+r_value+", "+rela_value+", "+l_value+"}.\n";
		return result_text;
	}     
    return {
        add_div_background_image:add_div_background_image,
		load_story_text: load_story_text,
		load_story_assertions: load_story_assertions
    }
})();