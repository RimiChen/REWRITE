// story object
function Story(story_name, story_category, story_index){
	this.name = story_name;
	this.category = story_category;
	
	//generate random, if not exist
	story_identify = Math.floor(Date.now());
	this.id = "story"+story_identify;
	this.content = {};
	
	random_r = Math.floor(Math.random() * (255 - 0) + 0);
	random_g = Math.floor(Math.random() * (255 - 0) + 0);
	random_b = Math.floor(Math.random() * (255 - 0) + 0);
	
	this.book_cover_color= "rgba("+random_r+","+random_g+","+random_b+", 1)";
	
	random_h = Math.floor(Math.random() * (230 - 180) + 180);
	this.book_size_height= random_h;
	this.book_size_width= 30;
	this.story_index= story_index;
}