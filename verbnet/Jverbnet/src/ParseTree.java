//implement parse tree functions
public class ParseTree {
	public ParseTree(){
		
	}
	public ParseTreeNode createParseTree(String semantic){
		System.out.println(semantic);
		ParseTreeNode root = new ParseTreeNode(null);
		//"(", ")", ","
		int end_index = semantic.indexOf(")");
		int current_layer = 0;
		//while(end_index >= 0){
		int temp_index_left ;
		int temp_index_comma ;
		int temp_index_right ;
			
		String[] tokens = semantic.split("\\(|\\)|\\,");
		System.out.println(tokens);
			//break;

		//}
		
		return root;
	}
}
