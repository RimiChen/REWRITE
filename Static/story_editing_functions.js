/*
Style:
visible functions are returned variables
inner functions are 
*/

var story_editing = (function () {
    /*inner functions*/
    var story_assertions = {};
    var result_assertion_text = "";
    function test_json_assign(input){
        console.log("JSON: ");
        console.log(input);
    }
    function load_story_assertions(filePath){
        //console.log(result_assertion_text);
        $(document).ready(function () {
            $.getJSON(filePath, function(data){
                var assertion_count = 0;
                $.each(data, function (key, value) {
                    story_assertions[assertion_count] = data[key];
                    //console.log("---"+"{"+data[key]['r']+", "+data[key]['relation']+", "+data[key]['l']+"}");
                    result_assertion_text = result_assertion_text+ "{"+data[key]['l']+", "+data[key]['relation']+", "+data[key]['r']+"}\n"; 
                    assertion_count ++;
                });
                //console.log(result_assertion_text);

                return result_assertion_text;
            });
            //console.log(result_assertion_text);
        }); 
    }
    function query_by_key(key_word){
        result_list = []
        console.log("query "+key_word.toLowerCase());
        for(var item in each_story_settings.assert_pool){
            if(each_story_settings.assert_pool[item]['l'].toLowerCase() == key_word.toLowerCase()){
                result_list.push( each_story_settings.assert_pool[item]);
            }
        }
        
        return result_list;
    }
    function query_by_value(key_word){
        result_list = []
        console.log("query "+key_word.toLowerCase());
        for(var item in each_story_settings.assert_pool){
            if(each_story_settings.assert_pool[item]['r'].toLowerCase() == key_word.toLowerCase()){
                result_list.push( each_story_settings.assert_pool[item]);
            }
        }
        
        return result_list;
    } 
             
    var create_assertion_row = function(l_text, relation_text, r_text, index, index_text, sentence, weight){
        //out frame
		//get parent frame position
		var target_frame_id = "story_content_right";
		var target_frame = document.getElementById(target_frame_id);    

		var parent_frame = "#"+target_frame_id;
        var reference_base = $(parent_frame);
        var weight_shift = 50;
        var parent_frame_width = reference_base.width() - weight_shift;
		var reference_base_position = reference_base.offset();
		var left_offset = reference_base_position.left;
		var top_offset = reference_base_position.top;
		
		//append bookshelf top
		var new_frame = document.createElement("div");
		new_frame.id = "assertion_out_frame_"+index;
		new_frame.class = "assertion_out_frame";
        target_frame.appendChild(new_frame);
        
        each_story_settings.assertion_frame_width = parent_frame_width;
		//console.log("x = "+ 0+", y = "+(0+index*(each_story_settings.assertion_frame_hieght+2)));
		$("#"+new_frame.id).css({
			top: (0+index*(each_story_settings.assertion_frame_hieght+2))+"px",
			left: 0+"px",
			position:'absolute',
			height: each_story_settings.assertion_frame_hieght+"px",
            width: each_story_settings.assertion_frame_width+"px",
            zIndex: 4,
           //backgroundColor:  "rgba(0, 255, 255, 0.5)",
            display: "inline-block"
        });	
    

        if(sentence.split(' ').length < 100){
            var new_frame = document.createElement("div");
            new_frame.id = "assertion_sentence_"+index;
            new_frame.class = "assertion_sentence";
            target_frame.appendChild(new_frame);
            
            each_story_settings.assertion_frame_width = parent_frame_width;
            //console.log("x = "+ 0+", y = "+(0+index*(each_story_settings.assertion_frame_hieght+2)));
            $("#"+new_frame.id).css({
                top: (each_story_settings.assertion_frame_hieght+index*(each_story_settings.assertion_frame_hieght+2))+"px",
                left: 0+"px",
                position:'absolute',
                height:  each_story_settings.assertion_frame_height+"px",
                width: each_story_settings.assertion_frame_width+"px",
                zIndex: 7,
                backgroundColor:  "rgba(0, 255, 255, 0.8)",
                display: "none"
            });	
            

            $("#"+"assertion_out_frame_"+index).mouseover(function() {
                $("#"+"assertion_sentence_"+index).css({
  
                    display: "inline-block"
                });	                
                $("#"+"assertion_sentence_"+index).text(sentence);
            }).mouseout(function() {

                $("#"+"assertion_sentence_"+index).css({
                    display: "none"
                });	                
                $("#"+"assertion_sentence_"+index).text("");
            });
        }
  

		target_frame_id = "assertion_out_frame_"+index;
        target_frame = document.getElementById(target_frame_id);  
        
        var index_pos_shift = 30;
        //index block
        new_frame = document.createElement("div");
		new_frame.id = "assertion_index_"+index;
		new_frame.class = "assertion_index";
        target_frame.appendChild(new_frame);
        
		$("#"+new_frame.id).css({
			top: 0+"px",
			left: 0+"px",
			position:'absolute',
			height: index_pos_shift+"px",
            width: index_pos_shift+"px",
            zIndex: 5,
            backgroundColor:  "rgba(0, 0, 0, 1)",
            display: "inline-block",
            verticalAlign: "center",
            Align: "center",
            color: "rgba(255, 255, 255, 1)"
        });	
        $("#"+"assertion_index_"+index).text(index_text);
		var current_index_button = document.getElementById("assertion_index_"+index);
		current_index_button.addEventListener('click', function(event){
            var string_index = g_story_settings.story_pool[current_settings.current_story].content.indexOf(sentence);
            var tempString = g_story_settings.story_pool[current_settings.current_story].content.substring(0, index); 
            var lineNumber = tempString.split('\n').length;
            console.log("assertion #"+index+" in line #"+lineNumber);
        });        


        target_frame_id = "assertion_out_frame_"+index;
        target_frame = document.getElementById(target_frame_id);  

      
        
        
        //left
  

        new_frame = document.createElement("div");
		new_frame.id = "assertion_left_"+index;
		new_frame.class = "assertion_left";
        target_frame.appendChild(new_frame);
        
		$("#"+new_frame.id).css({
			top: 0+"px",
			left: Math.floor(parent_frame_width/3*0+index_pos_shift)+"px",
			position:'absolute',
			height: (each_story_settings.assertion_frame_hieght/2-2)+"px",
            width: Math.floor(parent_frame_width/3-5)+"px",
            zIndex: 5,
            backgroundColor:  "rgba(255, 0, 255, 0.5)",
            display: "inline-block",
            verticalAlign: "center",
            Align: "center"
        });	      
        
        var text_target_frame_id = "assertion_left_"+index;
        text_target_frame = document.getElementById(text_target_frame_id);  

        var new_text_area = document.createElement("textarea"); 
		new_text_area.id = "assertion_left_text_"+index;
		new_text_area.class = "assertion_left_text";
        text_target_frame.appendChild(new_text_area);
		$("#"+ text_target_frame.id).css({
            height: "100%",
            width: "100%",
            webkitBoxSizing: "border-box", /* Safari/Chrome, other WebKit */
            mozBoxSizing: "border-box",   /* Firefox, other Gecko */
            boxSizing: "border-box",
            backgroundColor: "rgba(0,0,0,0)", 
            borderColor:"rgba(0,0,0,0)",
            color:  "rgba(0, 0, 0, 1)", 
            verticalAlign: "center",
            Align: "center",
            zIndex: 6
        });
        $("#"+"assertion_left_text_"+index).text(r_text);


        //middle
        new_frame = document.createElement("div");
		new_frame.id = "assertion_middle_"+index;
		new_frame.class = "assertion_middle";
        target_frame.appendChild(new_frame);

		$("#"+new_frame.id).css({
			top: 0+"px",
			left: Math.floor(parent_frame_width/3*1+index_pos_shift)+"px",
			position:'absolute',
			height: (each_story_settings.assertion_frame_hieght/2-2)+"px",
            width: Math.floor(parent_frame_width/3-5)+"px",
            zIndex: 5,
            backgroundColor:  "rgba(0, 0, 0, 1)",
            color:"rgba(255, 255, 255, 1)",
            display: "inline-block",
            verticalAlign: "center",
            Align: "center"
        });
        $("#"+"assertion_middle_"+index).text(relation_text);   

        //right
        new_frame = document.createElement("div");
		new_frame.id = "assertion_right_"+index;
		new_frame.class = "assertion_right";
        target_frame.appendChild(new_frame);

		$("#"+new_frame.id).css({
			top: 0+"px",
			left: Math.floor(parent_frame_width/3*2+index_pos_shift)+"px",
			position:'absolute',
			height: (each_story_settings.assertion_frame_hieght/2-2)+"px",
            width: Math.floor(parent_frame_width/3-5)+"px",
            zIndex: 5,
            backgroundColor:  "rgba(255, 255, 0, 0.5)",
            display: "inline-block"
        });
        
        text_target_frame_id = "assertion_right_"+index;
        text_target_frame = document.getElementById(text_target_frame_id);  

        new_text_area = document.createElement("textarea"); 
		new_text_area.id = "assertion_right_text_"+index;
		new_text_area.class = "assertion_right_text";
        text_target_frame.appendChild(new_text_area);
		$("#"+ text_target_frame.id).css({
            height: "100%",
            width: "100%",
            webkitBoxSizing: "border-box", /* Safari/Chrome, other WebKit */
            mozBoxSizing: "border-box",   /* Firefox, other Gecko */
            boxSizing: "border-box",
            backgroundColor: "rgba(0,0,0,0)", 
            borderColor:"rgba(0,0,0,0)",
            color:  "rgba(0, 0, 0, 1)", 
            verticalAlign: "center",
            Align: "center",
            zIndex: 6 
        });
        $("#"+"assertion_right_text_"+index).text(l_text);        


    
        //weight
        new_frame = document.createElement("div");
		new_frame.id = "assertion_weight_"+index;
		new_frame.class = "assertion_weight";
        target_frame.appendChild(new_frame);
        
		$("#"+new_frame.id).css({
			top: (each_story_settings.assertion_frame_hieght/2+2)+"px",
			left:0+"px",
			position:'absolute',
			height: index_pos_shift+"px",
            width: index_pos_shift+"px",
            zIndex: 5,
            backgroundColor:  "rgba(0, 0, 255, 1)",
            display: "inline-block",
            verticalAlign: "center",
            Align: "center",
            color: "rgba(255, 255,0, 1)"
        });	
        $("#"+"assertion_weight_"+index).text(weight);
		var current_weight_button = document.getElementById("assertion_weight_"+index);
		current_index_button.addEventListener('click', function(event){
            var string_index = g_story_settings.story_pool[current_settings.current_story].content.indexOf(sentence);
            var tempString = g_story_settings.story_pool[current_settings.current_story].content.substring(0, index); 
            var lineNumber = tempString.split('\n').length;
            console.log("assertion #"+index+" in line #"+lineNumber);
        });
        text_target_frame_id = "assertion_weight_"+index;
        text_target_frame = document.getElementById(text_target_frame_id);  

        new_text_area = document.createElement("textarea"); 
		new_text_area.id = "assertion_weight_text_"+index;
		new_text_area.class = "assertion_weight_text";
        text_target_frame.appendChild(new_text_area);
		$("#"+ text_target_frame.id).css({
            height: "100%",
            width: "100%",
            webkitBoxSizing: "border-box", /* Safari/Chrome, other WebKit */
            mozBoxSizing: "border-box",   /* Firefox, other Gecko */
            boxSizing: "border-box",
            backgroundColor: "rgba(0,0,0,0)", 
            borderColor:"rgba(0,0,0,0)",
            color:  "rgba(0, 0, 0, 0)", 
            verticalAlign: "center",
            Align: "center",
            zIndex: 6 ,
            resize: "none"
        });
        $("#"+"assertion_weight_text_"+index).text(weight);                  
        $("#"+"assertion_weight_text_"+index).change(function() {
            $("#"+"assertion_weight_text_"+index).text($("#"+"assertion_weight_text_"+index).val());
            //change weight here
        });      
    }

    var initialize_editing_interface = function() {
        console.log("==System: loading story editing interface.");
        
        //start here
        var frame_id = "story_text_left";
        shared_methods.add_div_background_image(frame_id, "Materials/paper.png");      
        var frame_id = "story_text_right";
        shared_methods.add_div_background_image(frame_id, "Materials/paper_reverse.png"); 
        var frame_id = "story_to_assertions";
        shared_methods.add_div_background_image(frame_id, "Materials/right_arrow.png"); 
        var frame_id = "assertions_to_story";
        shared_methods.add_div_background_image(frame_id, "Materials/left_arrow.png"); 		


        //add story text to left part, add assertions to right part
        var current_story = JSON.parse(localStorage.getItem("R_rewrite_chosen_story"));
        //console.log(current_story);
        //console.log(current_story.name);
        g_story_settings.story_pool[current_story.name] = current_story;
        current_settings.current_story = current_story.name;
        //shared_methods.load_story_text("Storys/"+current_story.name+".txt", current_story.name); 
        $("#story_content_text").text(g_story_settings.story_pool[current_story.name].content);
        
        each_story_settings.story_name = current_story.name; 
        each_story_settings.total_story_text = shared_methods.load_story_assertions("Storys/"+current_story.name+".json"); 
        
        shared_methods.link_synonym();
        
        // clean display
        $("#"+"story_content_right").contents().remove();
        console.log(each_story_settings.assert_pool);
        temp_assertion_pool = [];
        
        for(var item in each_story_settings.assert_pool){
            //create 3 blocks for r, relation, l
            //console.log(item);
            temp_assertion_pool.push( each_story_settings.assert_pool[item]);
        }
        temp_assertion_pool.sort(sort_by('storypoints', true, parseInt));
        
        for(var item in temp_assertion_pool){
            //create 3 blocks for r, relation, l
            //console.log(item);
            create_assertion_row(
                temp_assertion_pool[item]['r'],
                temp_assertion_pool[item]['relation'],
                temp_assertion_pool[item]['l'],
                item,
                temp_assertion_pool[item]['index'],
                temp_assertion_pool[item]['sentence'],
                temp_assertion_pool[item]['weight']
            );
        } 
        
        console.log(temp_assertion_pool);
        //query in here
        console.log("Test query: Glass-blower")
        console.log(query_by_key("Glass-blower"));
        //console.log(shared_methods.query_related_subject("Glass-blower"));
        //$("#story_assertion_text").text(each_story_settings.total_story_text);
        $("#story_content_text").change(function() {
            $("#story_content_text").text($("#story_content_text").val());
            current_story.content = $("#story_content_text").text();
            localStorage.setItem("R_rewrite_chosen_story",  JSON.stringify(current_story));
        });


        //use java function to get verbnet information
        ///// implement in here
        
        //listen to button reactions:
        button_actions.listen_button("#story_to_assertions");
        button_actions.listen_button("#assertions_to_story");
        
    };
    var sort_by = function(field, reverse, primer){
        
           var key = primer ? 
               function(x) {return primer(x[field])} : 
               function(x) {return x[field]};
        
           reverse = !reverse ? -1 : 1;
        
           return function (a, b) {
               return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
             } 
    }
    return {
        initialize_editing_interface:initialize_editing_interface,
        create_assertion_row :create_assertion_row,
        sort_by: sort_by
    }
})();
