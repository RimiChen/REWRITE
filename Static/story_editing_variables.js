//variables for storys
var current_settings ={
    current_story: "",
    take_actor_actions: false
}
var each_story_settings = {
    story_id: -1,
    story_name: "",
    assert_pool: {},
    total_story_text: "",
    assertion_frame_width: 0,
    assertion_frame_hieght: 100,
    actor_pool: {}
}
var assertion_dictionary = {
    //each assertion is a list
    //object: [{assertion index, assertion status}]
    showed_assertions: {}
}
var first_order_logic = {
    synonym_group: {}
    
}