// variables which are going to be saved in local storage should have "R_rewrite_" prefix

var g_story_settings = {
	// category name, layer #
	category_layer_list : {},
	// category, number of stories
	category_number_story: {},
	// initialize with -1, and will be changed according to category numbers
	last_layer_number: 0,
	// story_name, story object
	story_pool: {},
	total_story_number: 0,
	last_story_name: ""

}
var bookshelf_variables = {
	total_width: 847,
	top_height:29,
	layer_height:274,
	layer_left_width:85,
	layer_right_width:82,
	layer_middle_width:679
}