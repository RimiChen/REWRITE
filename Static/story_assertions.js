var story_2_assertions = (function () {        //return result_text;
    var story_become_assertions = function(story_name){
        console.log("==System: transform story to assertions");
        //recomputing assertions
        //save the story to txt 
        
        var story_path = "Storys/"+story_name+".txt";
        var story_content = $("#"+"story_content_text").text();
        //console.log(story_content);

        $.post( "/post_save_story", {
            story_path: story_path,
            story_content: story_content
        });

        // call rensa to generate a new file
        
        $.post( "/post_rensa", {
            javascript_data: story_name
        });

        shared_methods.load_story_assertions("Storys/"+story_name+".json"); 
        shared_methods.link_synonym();
        
        $("#"+"story_content_right").contents().remove();
        for(var item in each_story_settings.assert_pool){
            //create 3 blocks for r, relation, l
            //console.log(item);
            story_editing.create_assertion_row(
                each_story_settings.assert_pool[item]['r'],
                each_story_settings.assert_pool[item]['relation'],
                each_story_settings.assert_pool[item]['l'],
                item,
                each_story_settings.assert_pool[item]['index'],
                each_story_settings.assert_pool[item]['sentence'],
                each_story_settings.assert_pool[item]['weight']
            );
        }
        //window.location.href='/story_editing';
        //reload rensa


    }
    var assertions_become_story = function(story_name){
        console.log("==System: transform assertions to story");

    }
    return {
        story_become_assertions: story_become_assertions,
        assertions_become_story: assertions_become_story
    }
})();