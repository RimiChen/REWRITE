import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.lang.reflect.Type;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonIOException;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonSyntaxException;
import com.google.gson.reflect.TypeToken;

import edu.mit.jverbnet.data.semantics.IPredicateDesc;
import edu.mit.jverbnet.data.semantics.ISemanticArgType;

public class TestJS{
	public Map<String, String> tenseMapping;
	public Map<String, String> frameMapping;
	VerbData v_Data;
	public ParseTree tree;
	
    public TestJS() throws IOException{
    	System.out.println("Constucter to save information");
    	tree = new ParseTree();
    	v_Data = new VerbData(".\\verbnet\\");
        tenseMapping = new TreeMap<String, String>();
        /*
         *
went
cares
set
leaves
began
came
had
tying
ran
         */
        
        tenseMapping.put("went", "go");
        tenseMapping.put("cares", "care");
        tenseMapping.put("set", "set");
        tenseMapping.put("leaves", "leave");
        tenseMapping.put("began", "begin");
        tenseMapping.put("came", "come");
        tenseMapping.put("had", "have");
        tenseMapping.put("tying", "tie");
        tenseMapping.put("ran", "run");

        
        frameMapping = new TreeMap<String, String>();
        frameMapping.put("NN", "NP");
        frameMapping.put("VB", "V");
        frameMapping.put("VB", "V");
        frameMapping.put("JJ", "ADJ");
        
    
    }
    public void readJson(String filePath) throws JsonSyntaxException, JsonIOException, FileNotFoundException{
/*
    	Gson gson = new Gson();
    	JsonElement json = gson.fromJson(new FileReader("../../Storys/THE_GLASS_DOG.json"), JsonElement.class);
    	JsonArray jsonArray = json.getAsJsonArray();
    	System.out.println(json);
    	//System.out.println(jsonArray.spliterator());
    	List<JsonElement> assertionList = new ArrayList<JsonElement>();
    	assertionList.add(jsonArray);
    	System.out.println(assertionList.size());
*/
        Gson gson = new Gson();
        // or

        @SuppressWarnings("serial")
        Type collectionType = new TypeToken<List<Assertion>>() {
        }.getType();
        List<Assertion> assertionList = gson.fromJson(new FileReader("../../Storys/THE_GLASS_DOG.json"), collectionType);
  	
        //System.out.println(navigation);
        //mapping word

		for (Assertion assertion : assertionList) {
			/*
			System.out.println(test.index);
			System.out.println(test.r);
			System.out.println(test.l);
			System.out.println(test.relation);
			System.out.println(test.sentence);
			*/
			//System.out.println(assertion.relation);
			if(assertion.relation.equals("action")==true){
				System.out.println("=============");
				System.out.println("subject: "+assertion.l);
				System.out.println("old: "+assertion.r+", new: "+tenseMapping.get(assertion.r));
				List<IPredicateDesc> semantic = v_Data.getSemantic(tenseMapping.get(assertion.r));
				if(semantic.size() >0){
					System.out.println("list size:¡@"+semantic.size()+", list content: "+semantic);
					//create parse tree for this verb, as long as it has semantic
					ParseTreeNode root = new ParseTreeNode(null);
					for(IPredicateDesc part:semantic){
					//	tree.createParseTree(part.getValue().getID());
						ParseTreeNode child = new ParseTreeNode(root);
						child.name = part.getValue().getID();
						child.type = "predicate";
						
						List<ISemanticArgType> arguments = part.getArgumentTypes();
						for(ISemanticArgType argument: arguments){
							ParseTreeNode arg_child = new ParseTreeNode(child);
							arg_child.name = argument.getID();
							String theme = VerbNetDictionary.role_reference.get(arg_child.name);
							if(theme != null ){
								//exist
								if(theme == "Patient" || theme == "Theme" || theme =="Experiencer"){
									arg_child.target_object = assertion.l;
								}
								else if(theme == "Location"){
									arg_child.target_object = "some where";
								}
								else{
									System.out.println("This theme is not intrpreable: "+theme);
								}
							}

							arg_child.type = "role";
							child.child.add(arg_child);
						}
						root.child.add(child);
					//	System.out.println(part.getArgumentTypes());

					}
					System.out.println(root.child.size());
					for(int i = 0; i < root.child.size(); i++){
						System.out.println("-----");
						printTree(root, root.child.get(i), i);
					}
				}
			}
			
		}
    }
    public void printTree(ParseTreeNode parent, ParseTreeNode current, int index){
    	//TODO: debug the recursive
    	if(current.target_object !=""){
        	System.out.println("type: "+current.type+", name: "+current.name+", target_object: "+current.target_object);
    	}
    	else{
        	System.out.println("type: "+current.type+", name: "+current.name);    		
    	}

    	if(current.child.size() == 0){
    		//no child, return
        	if(parent != null){
        		//not root

        		if(index+1 < parent.child.size()){
            		//System.out.println("move to neighbor");
        			printTree(parent, parent.child.get(index+1), index+1);
        		}
        		else{
       			
        		}
        	}
        	else{
        		//root
        		if(index+1 < current.child.size()){
            		//System.out.println("move to root neighbor");
        			printTree(null, current.child.get(index+1), index+1);
        		} 
        	}
    	}
    	else{
    		//System.out.println("move to child");
			printTree(current, current.child.get(0), 0);
    	}
    }

}

