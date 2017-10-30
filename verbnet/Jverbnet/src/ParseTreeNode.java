import java.util.ArrayList;
import java.util.List;

public class ParseTreeNode {
	String target_object;
	//predicate, 
	String type;
	String name;
	ParseTreeNode parent;
	List<ParseTreeNode> child;
	
	public ParseTreeNode(ParseTreeNode current_parent){
		parent = current_parent;
		child = new ArrayList<ParseTreeNode>();
		target_object = "";
		type = "";
		name = "";
	}
}
