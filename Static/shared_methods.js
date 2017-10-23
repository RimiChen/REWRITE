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
        //var result_text="";
        each_story_settings.assert_pool = {};
        $.ajax({
            async: false,
            dataType : 'json',
            url: filePath,
            type : 'GET',
            success: function(data) {
                var assertion_count = 0;
                for(var key in data){ 
                    console.log(assertion_count);
                    //here do your logic and assign value for code varable   
                    each_story_settings.assert_pool[assertion_count] = data[key];
                    //initial assertions
                    each_story_settings.assert_pool[assertion_count]['weight'] = 1;
                    each_story_settings.assert_pool[assertion_count]['status'] = true;

                    each_story_settings.assert_pool[assertion_count]['current_l'] = each_story_settings.assert_pool[assertion_count]['l'];
                    each_story_settings.assert_pool[assertion_count]['current_r'] = each_story_settings.assert_pool[assertion_count]['r'];
                    each_story_settings.assert_pool[assertion_count]['storypoints'] = each_story_settings.assert_pool[assertion_count]['storypoints'];
                    
                    //first check if it is an action
                    if(current_settings.take_actor_actions == true){
                        //use actor's action
                        feach_story_settings.assert_pool[assertion_count]['current_l']
                    }
                    else{

                    }

                    if(assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']]){
                        // a list of properties
                        // same subject have different properties
                        if(assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']][each_story_settings.assert_pool[assertion_count]['index']]){
                            //come from same assertion index
                            assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']][each_story_settings.assert_pool[assertion_count]['index']].push(each_story_settings.assert_pool[assertion_count]['r']);
                        }
                        else{
                            //not from same assertion   -->  status change
                            //find a previous action
                            
                            
                            assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']][each_story_settings.assert_pool[assertion_count]['index']] = [];
                            assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']][each_story_settings.assert_pool[assertion_count]['index']].push(each_story_settings.assert_pool[assertion_count]['r']);
                        }
                    }
                    else{
                        //different subject
                        assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']] = {};
                        assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']][each_story_settings.assert_pool[assertion_count]['index']] = [];
                        assertion_dictionary[each_story_settings.assert_pool[assertion_count]['l']][each_story_settings.assert_pool[assertion_count]['index']].push(each_story_settings.assert_pool[assertion_count]['r']);
                        
                    }

                    //result_text = result_text+ "{"+data[key]['r']+", "+data[key]['relation']+", "+data[key]['l']+"}\n"; 
                    assertion_count++;
                }
                console.log(assertion_dictionary);
                console.log(each_story_settings.assert_pool);
            }
        });
   
        //return result_text;
    }
    var link_synonym = function(){
        same_value_pool = {};
        if(Object.keys(each_story_settings.assert_pool).length == 0){
            console.log("==System: no assertions");
        }
        else{
            for(item in each_story_settings.assert_pool){
                value =  each_story_settings.assert_pool[item]['r'].toLowerCase();
                if(value != ""){
                    if(same_value_pool[value]){
                        
                        //exist
                        same_value_pool[value].push(each_story_settings.assert_pool[item]['l'].toLowerCase());
                        same_value_pool[value] = jQuery.unique(same_value_pool[value]);
                    }
                    else{
                        //not exist
                        same_value_pool[value] = [];
                        same_value_pool[value].push(each_story_settings.assert_pool[item]['l'].toLowerCase());
                    }
                }
            }
            console.log("Same value pool:");
            console.log(same_value_pool);
        }
        //first_order_logic.synonym_group

        for(item in same_value_pool){
            for(subject_index in same_value_pool[item]){
                //console.log("item: "+same_value_pool[item]);
                name = same_value_pool[item][subject_index];
                //console.log("subject: "+name);
                if(name != ""){
                    if(first_order_logic.synonym_group[name]){
                        first_order_logic.synonym_group[name].push.apply(first_order_logic.synonym_group[name], same_value_pool[item]);
                        first_order_logic.synonym_group[name] = jQuery.unique(first_order_logic.synonym_group[name]);
                    }
                    else{
                        first_order_logic.synonym_group[name] = [];
                        first_order_logic.synonym_group[name].push.apply(first_order_logic.synonym_group[name], same_value_pool[item]);
                    }
                }
            }
        }
        console.log("Similar subjects:");
        console.log(first_order_logic.synonym_group);


    } 
    var query_related_subject = function(key_word){

        result_list = []

        console.log("query "+key_word.toLowerCase()+" and related subjects");
        name_list = first_order_logic.synonym_group[key_word.toLowerCase()];
        console.log(name_list);
        for(var item in each_story_settings.assert_pool){
            if(name_list.indexOf(each_story_settings.assert_pool[item]['l'].toLowerCase())>=0){
                //console.log(each_story_settings.assert_pool[item]);
                result_list.push( each_story_settings.assert_pool[item]);
            }
        }
        
        return result_list;

    } 
	function create_assertions_row(r_value, rela_value, l_value, result_text){
		//console.log(r_value+", "+ rela_value+", "+ l_value);
		result_text = result_text+"{"+r_value+", "+rela_value+", "+l_value+"}.\n";
		return result_text;
	}     
    return {
        add_div_background_image:add_div_background_image,
		load_story_text: load_story_text,
        load_story_assertions: load_story_assertions,
        link_synonym: link_synonym,
        query_related_subject: query_related_subject
    }
})();