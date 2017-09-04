/*
Style:
visible functions are returned variables
inner functions are 
*/

var story_editing = (function () {
    /*inner functions*/
    
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
        var current_story = localStorage.getItem("R_rewrite_chosen_story");
        console.log(current_story);
        g_story_settings.story_pool[current_story.name] = current_story;
        //shared_methods.load_story_text("Storys/"+current_story.name+".txt", current_story.name); 

        //// story content in here
        //g_story_settings.story_pool[story_name].content
        $("#story_content_text").text(g_story_settings.story_pool[current_story.name].content);
        console.log(g_story_settings.story_pool[current_story.name].content);
    };
    
    return {
        initialize_editing_interface:initialize_editing_interface
    }
})();
