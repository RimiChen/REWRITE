/*
Style:
visible functions are returned variables
inner functions are 
*/

var bookshelf_functions = (function () {
    /*inner functions*/
    function clickAllCanvas(elementName){
        $(document).ready(function(){
            switch(elementName) {
                case "#bs_add_story":
					$(elementName).click(function(){
						console.log("==System: add new story. with category and story name.");
						//// in current version we don't take input from users
						// temporary testing variables
						temp_story_name = "THE_BOX_OF_ROBBERS";
						temp_story_category = "Fantacy"
						create_empty_story(temp_story_name, temp_story_category);
						shared_methods.load_story_text("Storys/"+temp_story_name+".txt", temp_story_name); 
						//console.log(g_story_settings.story_pool[temp_story_name].content);
						
						temp_story_name = "THE_ENCHANTED_TYPES";
						temp_story_category = "FairyTale"
						create_empty_story(temp_story_name, temp_story_category);
						shared_methods.load_story_text("Storys/"+temp_story_name+".txt", temp_story_name); 
						//console.log(g_story_settings.story_pool[temp_story_name].content);
							
						temp_story_name = "THE_GIRL_WHO_OWNED_A_BEAR";
						temp_story_category = "Advanture"
						create_empty_story(temp_story_name, temp_story_category);
						shared_methods.load_story_text("Storys/"+temp_story_name+".txt", temp_story_name); 
						//console.log(g_story_settings.story_pool[temp_story_name].content);

						temp_story_name = "THE_GLASS_DOG";
						temp_story_category = "Fantacy"
						create_empty_story(temp_story_name, temp_story_category);
						shared_methods.load_story_text("Storys/"+temp_story_name+".txt", temp_story_name); 
						//console.log(g_story_settings.story_pool[temp_story_name].content);
							
						temp_story_name = "THE_QUEEN_OF_QUOK";
						temp_story_category = "Advanture"
						create_empty_story(temp_story_name, temp_story_category);
						shared_methods.load_story_text("Storys/"+temp_story_name+".txt", temp_story_name); 

						temp_story_name = "TEST_STORY";
						temp_story_category = "Fantacy"
						create_empty_story(temp_story_name, temp_story_category);
						shared_methods.load_story_text("Storys/"+temp_story_name+".txt", temp_story_name); 
						//console.log(g_story_settings.story_pool[temp_story_name].content);
						
						console.log(g_story_settings.story_pool);
					});				
                    break;
                default:
                    console.log("no element name");
            }	
        }); 	
    }
	/* create an empty story*/
	function create_empty_story(story_name, story_category){
		//check if the story exist
		//if the category not exist, add new category
		if(g_story_settings.story_pool[story_name]){
			//story exist
			console.log("==System: this story exist!");
		}
		else{
			//create story
			console.log("==System: add new story!");
			if(g_story_settings.category_number_story[story_category]){
				story_index = g_story_settings.category_number_story[story_category]+1;
			}
			else{
				story_index = 1;
			}
			var new_story = new Story(story_name, story_category, story_index);
			g_story_settings.story_pool[story_name] = new_story;
			
			//update local storage
			g_story_settings.last_story_name = story_name;


			//create bookshelf
			update_bookshelf();
		
		}
		
	}
	function create_bookshelf_first_layer(){
		console.log("==System: createh the first empty layer");
		//get parent frame position
		var target_frame_id = "bookshelf";
		var target_frame = document.getElementById(target_frame_id);    

		var parent_frame = "#"+target_frame_id;
		var reference_base = $(parent_frame);
		var reference_base_position = reference_base.offset();
		var left_offset = reference_base_position.left;
		var top_offset = reference_base_position.top;
		
		//append bookshelf top
		var new_frame = document.createElement("div");
		new_frame.id = "bookshelf_top";
		new_frame.class = "bookshelf_frame_top";
		target_frame.appendChild(new_frame);
		
		$("#"+new_frame.id).css({
			top: top_offset+"px",
			left: left_offset+"px",
			position:'absolute',
			height: bookshelf_variables.top_height+"px",
			width: bookshelf_variables.total_width+"px",
			backgroundColor: "rgba(255,0,255, 1)"
		});	
		shared_methods.add_div_background_image(new_frame.id, "Materials/Bookshelf_top.png");
		
		create_a_bookshelf_layer(1);
	}
	function create_category_board(category_name){
		target_layer = g_story_settings.category_layer_list[category_name];
		//create a board
		console.log("==System: create category board");
		//get parent frame position
		var target_frame_id = "bookshelf_overlay";
		var target_frame = document.getElementById(target_frame_id);    

		var parent_frame = "#"+target_frame_id;
		var reference_base = $(parent_frame);
		var reference_base_position = reference_base.offset();
		var left_offset = reference_base_position.left;
		var top_offset = reference_base_position.top;
		
		//append bookshelf top
		var new_frame = document.createElement("div");
		new_frame.id = "bookshelf_board_"+category_name;
		new_frame.class = "bookshelf_board";
		target_frame.appendChild(new_frame);
		
		$("#"+new_frame.id).css({
			top: (bookshelf_variables.top_height*0.2+bookshelf_variables.layer_height*(target_layer-1))+"px",
			left: (bookshelf_variables.total_width*0.4)+"px",
			position:'absolute',
			height: Math.floor(bookshelf_variables.top_height*0.6)+"px",
			width: Math.floor(bookshelf_variables.total_width*0.2)+"px",
			backgroundColor: "rgba(0,0,0, 1)",
			color: "rgba(255,255,255, 1)",
			zIndex:3,
			textAlign: "center"
		});	
		$("#"+new_frame.id).text(category_name);
		shared_methods.add_div_background_image(new_frame.id,  "Materials/Bookshelf_board.png");
	}
	function create_a_bookshelf_layer(current_layer_index){
		//console.log("==System: create other layers");
		//create bookshelf
		//get parent frame position
		var target_frame_id = "bookshelf";
		var target_frame = document.getElementById(target_frame_id);    

		var parent_frame = "#"+target_frame_id;
		var reference_base = $(parent_frame);
		var reference_base_position = reference_base.offset();
		var left_offset = reference_base_position.left;
		var top_offset = reference_base_position.top;

		$("#bookshelf_overlay").css({
			top: top_offset+"px",
			left: left_offset+"px",
			position:'absolute',
			height:
			(
				bookshelf_variables.top_height
				+(bookshelf_variables.layer_height*current_layer_index)
			)
			+"px",
			width: bookshelf_variables.total_width+"px"
		});	
		
		
		new_frame = document.createElement("div");
		new_frame.id = "bookshelf_body_left_"+current_layer_index;
		new_frame.class = "bookshelf_frame_left";
		target_frame.appendChild(new_frame);
		$("#"+new_frame.id).css({
			top: (top_offset+(bookshelf_variables.top_height)+(bookshelf_variables.layer_height*current_layer_index))+"px",
			left: left_offset+"px",
			position:'absolute',
			height: bookshelf_variables.layer_height+"px",
			width: bookshelf_variables.layer_left_width+"px",
			backgroundColor: "rgba(0,255,0, 1)"
		});	
		
		
		//DEBUG:
		/*
		y_coord =
			(
				top_offset
				+(bookshelf_variables.top_height)
				+(bookshelf_variables.layer_height*(current_layer_index-1))
			);

		console.log("y: "+y_coord);
		*/
		
		// left frame
		new_frame = document.createElement("div");
		new_frame.id = "bookshelf_body_left_"+current_layer_index;
		new_frame.class = "bookshelf_frame_left";
		target_frame.appendChild(new_frame);
		$("#"+new_frame.id).css({
			top: 
			(
				top_offset
				+(bookshelf_variables.top_height)
				+(bookshelf_variables.layer_height*(current_layer_index-1))
			)
			+"px",
			
			left: left_offset+"px",
			
			position:'absolute',
			height: bookshelf_variables.layer_height+"px",
			width: bookshelf_variables.layer_left_width+"px",
			backgroundColor: "rgba(0,255,0, 1)"
		});	
		shared_methods.add_div_background_image(new_frame.id,"Materials/Bookshelf_left.png");

		
		//middle frame
		new_frame = document.createElement("div");
		new_frame.id = "bookshelf_body_middle_"+current_layer_index;
		new_frame.class = "bookshelf_frame_middle";
		target_frame.appendChild(new_frame);
		$("#"+new_frame.id).css({
			top: 
			(
				top_offset
				+(bookshelf_variables.top_height)
				+(bookshelf_variables.layer_height*(current_layer_index-1))
			)
			+"px",
			
			left: 
			(
				left_offset
				+bookshelf_variables.layer_left_width
			)
			+"px",
			
			position:'absolute',
			height: bookshelf_variables.layer_height+"px",
			width: bookshelf_variables.layer_middle_width+"px",
			backgroundColor: "rgba(0,255,255, 1)"
		});			
		shared_methods.add_div_background_image(new_frame.id, "Materials/Bookshelf_middle.png");

		//right frame
		new_frame = document.createElement("div");
		new_frame.id = "bookshelf_body_right_"+current_layer_index;
		new_frame.class = "bookshelf_frame_right";
		target_frame.appendChild(new_frame);
		$("#"+new_frame.id).css({
			top: 
			(
				top_offset
				+(bookshelf_variables.top_height)
				+(bookshelf_variables.layer_height*(current_layer_index-1))
			)
			+"px",
			
			left: 
			(
				left_offset
				+bookshelf_variables.layer_left_width
				+bookshelf_variables.layer_middle_width
			)
			+"px",
			
			position:'absolute',
			height: bookshelf_variables.layer_height+"px",
			width: bookshelf_variables.layer_right_width+"px",
			backgroundColor: "rgba(0,0,255, 1)"
		});	
		shared_methods.add_div_background_image(new_frame.id, "Materials/Bookshelf_right.png");
		
	}

	function add_story_book_button(story_name){
		console.log("==System: draw book "+story_name);
		var target_frame_id = "bookshelf_overlay";
		var target_frame = document.getElementById(target_frame_id);    

		var parent_frame = "#"+target_frame_id;
		var reference_base = $(parent_frame);
		var reference_base_position = reference_base.offset();
		var left_offset = reference_base_position.left;
		var top_offset = reference_base_position.top;
		
		//append bookshelf top
		var new_frame = document.createElement("div");
		story_object = g_story_settings.story_pool[story_name];
		category_name = story_object.category;
		category_layer = g_story_settings.category_layer_list[category_name];
		
		new_frame.id = "book_"+story_name;
		new_frame.class = "story_book";
		new_frame.addEventListener('click', function(event){
			console.log("==System: story "+story_name+" was clicked.");
			alert(g_story_settings.story_pool);
			
			localStorage.setItem("R_rewrite_chosen_story", JSON.stringify(g_story_settings.story_pool[story_name]));
			$.post( "/post_rensa", {
				javascript_data: story_name
			});
			//// this will generate .json file
			//add loading here?
			window.location.href='/story_editing';
		});
		target_frame.appendChild(new_frame);
		
		$("#"+new_frame.id).css({
			top: 
			(
				(bookshelf_variables.layer_height*category_layer)
				-story_object.book_size_height
			)
			+"px",
			left: 
			(
				bookshelf_variables.top_height
				+story_object.book_size_width*(story_object.story_index-1)
			)+"px",
			position:'absolute',
			height: story_object.book_size_height+"px",
			width: story_object.book_size_width+"px",
			backgroundColor: story_object.book_cover_color,
			zIndex: 4,
			textAlign: "center"
			//transform: "rotate(90deg)",
			//transformOrigin: "center center 0"
		});	
		$("#"+new_frame.id).text(story_name);
		console.log(story_name+", "+story_object.book_cover_color+", (w,h) = "+story_object.book_size_width+","+story_object.book_size_height);
	
	}
	function update_bookshelf(){
		//go over story pool
		old_story_pool = localStorage.getItem("R_rewrite_story_pool");
		//console.log("===");
		console.log(old_story_pool);
		if(old_story_pool === null){
			// no story
					//not exist
			story_name = g_story_settings.last_story_name;
			category_name = g_story_settings.story_pool[story_name].category;
			
			g_story_settings.last_layer_number = g_story_settings.last_layer_number +1;
			g_story_settings.category_layer_list[category_name] = 
				Object.keys(g_story_settings.category_layer_list).length + 1;
						
			g_story_settings.category_number_story[category_name] = 1;
			create_a_bookshelf_layer(g_story_settings.last_layer_number);
			create_category_board(category_name);
			
			//draw book
			add_story_book_button(story_name);
		}
		else{
			for(story_name in g_story_settings.story_pool){
				//console.log("---"+g_story_settings.story_pool[story_name].category+", "+g_story_settings.story_pool[story_name].name);
				category_name = g_story_settings.story_pool[story_name].category;
				if(story_name == g_story_settings.last_story_name){
					//the newest story
					if(g_story_settings.category_layer_list[category_name]){
						//the category exist
						g_story_settings.category_number_story[category_name] 
							= g_story_settings.category_number_story[category_name]+1;
						console.log(category_name+", "+g_story_settings.category_number_story[category_name]);
					}
					else{
						//category not exist
						g_story_settings.last_layer_number = g_story_settings.last_layer_number +1;
						g_story_settings.category_layer_list[category_name] = 
							Object.keys(g_story_settings.category_layer_list).length + 1;
						g_story_settings.category_number_story[category_name] = 1;
						
						create_a_bookshelf_layer(g_story_settings.last_layer_number);
						create_category_board(category_name);
					}
					//draw book
					add_story_book_button(story_name);
				}

			}

			console.log(g_story_settings.category_layer_list);
			console.log(g_story_settings.category_number_story);
		
		}
		localStorage.setItem("R_rewrite_story_pool", g_story_settings.story_pool);		
		
	}
	function clean_local_storage(){
		localStorage.removeItem("R_rewrite_story_pool");
		localStorage.removeItem("R_rewrite_catergory_pool");
	}
	/*returned visible functions*/
    var initialize_frames = function() {
        console.log("==System: loading bookshelf layers.");
        //start here
        image_source.initialize_image_pool();
		//// listen to button functions
        clickAllCanvas("#bs_add_story");
        
		
		//// initialize
		//funciton menu
		shared_methods.add_div_background_image("bs_add_story", "Materials/add_more_story.png")
		/*
		read varaibles from web storage
		*/
		//// clean all of local storages
		clean_local_storage();
		//// create bookshlef top frame
		create_bookshelf_first_layer();
		//// default will have first layer

		if(localStorage.getItem("R_rewrite_story_pool")=== null){
			console.log("==System: no previous story data.");
			g_story_settings.total_story_number = 0;
			// don't need to add more layer
		}
		else{
			console.log("==System: get story data.");
			
			g_story_settings.story_pool 
			= localStorage.getItem("R_rewrite_story_pool");
			
			g_story_settings.total_story_number 
			= Object.keys(g_story_settings.story_pool).length;
			
			//if any story exists, category must not be empty 
			g_story_settings.category_number_story 
			= localStorage.getItem("R_rewrite_catergory_pool") 
			
			//var category_number = Object.keys(g_story_settings.category_number_story).length;
			var category_number = 5;
			for(bookshelf_iter = 2; bookshelf_iter<=category_number; bookshelf_iter++){
				// create remaining layers
				console.log("==System: create layer #"+bookshelf_iter);
				create_a_bookshelf_layer(bookshelf_iter);
			}
			
			//// go over story pool
			
		}
		
    };
  
    return {
        initialize_frames:initialize_frames
    }
})();
