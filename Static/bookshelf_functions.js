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
                    conosle.log("==System: add new story.");
                    break;
                default:
                    console.log("no element name");
            }	
        }); 	
    }  
    
    /*returned visible functions*/
    var initialize_frames = function() {
        console.log("==System: loading bookshelf layers.");
        //start here
        clickAllCanvas("#bs_add_story");
        
    };
  
    return {
        initialize_frames:initialize_frames
    }
})();
