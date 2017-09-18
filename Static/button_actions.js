var button_actions = (function () {
        //return result_text;
    var listen_button =  function(button_name){
        //TODO: move all button check in here
        //var elementName = "#get_tag_from_text";
        
        $(document).ready(function(){
            switch(button_name) {
                case "#story_to_assertions":
                    $(button_name).click(function(){
                        var current_story = JSON.parse(localStorage.getItem("R_rewrite_chosen_story"));
                        console.log(current_story);
                        story_2_assertions.story_become_assertions(current_story.name);
                    });
                    break;
                case "#assertions_to_story":
                    $(button_name).click(function(){
                        var current_story = JSON.parse(localStorage.getItem("R_rewrite_chosen_story"));
                        story_2_assertions.assertions_become_story(current_story.name);
                    });
                    break;	       	                
                default:
                    console.log("no element name");
            }	
        }); 	
      }
    return {
        listen_button: listen_button
    }
})();