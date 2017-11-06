import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.lang.reflect.Type;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
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
        //initialize dictionary
        VerbNetDictionary.jsonDictionary.clear();
		
        
		for (Assertion assertion : assertionList) {
			Map<String, List<Map<String, String>>> assertionMap = new TreeMap<String, List<Map<String, String>>>();
			
			//Map<String, String> semanticMap = new TreeMap<String, String>();
			//List<Map<String, String>> itemMap = new ArrayList<Map<String, String>>();
			
			//Map<String, String> indexEmptyMap = new TreeMap<String, String>();
			List<Map<String, String>> indexList = new ArrayList<Map<String, String>>();
			//indexMap.add(indexEmptyMap);
			
			//Map<String, String> rEmptyMap = new TreeMap<String, String>();
			List<Map<String, String>> rList = new ArrayList<Map<String, String>>();
			//rMap.add(rEmptyMap);

			//Map<String, String> relationEmptyMap = new TreeMap<String, String>();
			List<Map<String, String>> relationList = new ArrayList<Map<String, String>>();
			//relationMap.add(relationEmptyMap);
			
			//Map<String, String> lEmptyMap = new TreeMap<String, String>();
			List<Map<String, String>> lList = new ArrayList<Map<String, String>>();
			//lMap.add(lEmptyMap);

			///Map<String, String> semanticEmptyMap = new TreeMap<String, String>();
			List<Map<String, String>> semanticList = new ArrayList<Map<String, String>>();
			//semanticMap.add(semanticEmptyMap);

			
			

			
			
			
			//itemMap.clear();
			//itemMap.add(semanticMap);
					
			//assertionMap.put("First", itemMap);
			//jsonDictionary.add(assertionMap);        
	        
			
			/*
			System.out.println(test.index);
			System.out.println(test.r);
			System.out.println(test.l);
			System.out.println(test.relation);
			System.out.println(test.sentence);
			*/
			//System.out.println(assertion.relation);
			if(assertion.relation.equals("action")==true){
				Map<String, String> indexEmptyMap = new TreeMap<String, String>();
				indexEmptyMap.put("index", Integer.toString(assertion.index));
				indexList.add(indexEmptyMap);

				Map<String, String> rEmptyMap = new TreeMap<String, String>();
				rEmptyMap.put("subject", assertion.r);
				rList.add(rEmptyMap);				
				
				
				Map<String, String> relationEmptyMap = new TreeMap<String, String>();
				relationEmptyMap.put("relation", assertion.relation);
				relationList.add(relationEmptyMap);	
				
				
				Map<String, String> lEmptyMap = new TreeMap<String, String>();
				lEmptyMap.put("object", assertion.l);
				lList.add(lEmptyMap);	
				
				
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
						
						Map<String, String> semanticEmptyMap = new TreeMap<String, String>();
						semanticEmptyMap.put("predicate", child.name);
						
						List<ISemanticArgType> arguments = part.getArgumentTypes();
						for(ISemanticArgType argument: arguments){
							
							ParseTreeNode arg_child = new ParseTreeNode(child);
							arg_child.name = argument.getID();
							String theme = VerbNetDictionary.role_reference.get(arg_child.name);
							
							
							if(theme != null ){
								//semanticEmptyMap.put(argument.getID(), theme);
								//System.out.println(semanticEmptyMap);
								//semanticList.add(semanticEmptyMap);

								//exist
								if(theme == "Patient" || theme == "Theme" || theme =="Experiencer"){
									arg_child.target_object = assertion.l;
									semanticEmptyMap.put(argument.getID(), arg_child.target_object);
									//System.out.println(semanticEmptyMap);
									semanticList.add(semanticEmptyMap);
									
									if(VerbNetDictionary.attributesDictionary.get(arg_child.target_object) == null){
										List<String> newAttribute = new ArrayList<String>();
										newAttribute.add(argument.getID());
										VerbNetDictionary.attributesDictionary.put(arg_child.target_object, newAttribute);
									}
									else{
										VerbNetDictionary.attributesDictionary.get(arg_child.target_object).add(argument.getID());
									}
									
									if(VerbNetDictionary.attributeCollectDictionary.get(argument.getID()) == null){
										List<String> newAttribute = new ArrayList<String>();
										newAttribute.add(arg_child.target_object);
										VerbNetDictionary.attributeCollectDictionary.put(argument.getID(), newAttribute);
									}
									else{
										VerbNetDictionary.attributeCollectDictionary.get(argument.getID()).add(arg_child.target_object);
									}
									
									
								}
								else if(theme == "Location"){
									arg_child.target_object = "some where";
									semanticEmptyMap.put(argument.getID(), arg_child.target_object);
									//System.out.println(semanticEmptyMap);
									semanticList.add(semanticEmptyMap);
									
									if(VerbNetDictionary.attributesDictionary.get(arg_child.target_object) == null){
										List<String> newAttribute = new ArrayList<String>();
										newAttribute.add(argument.getID());
										VerbNetDictionary.attributesDictionary.put(arg_child.target_object, newAttribute);
									}
									else{
										VerbNetDictionary.attributesDictionary.get(arg_child.target_object).add(argument.getID());
									}
									
									if(VerbNetDictionary.attributeCollectDictionary.get(argument.getID()) == null){
										List<String> newAttribute = new ArrayList<String>();
										newAttribute.add(arg_child.target_object);
										VerbNetDictionary.attributeCollectDictionary.put(argument.getID(), newAttribute);
									}
									else{
										VerbNetDictionary.attributeCollectDictionary.get(argument.getID()).add(arg_child.target_object);
									}
									
									
								}
								else{
									//System.out.println("This theme is not intrpreable: "+theme);
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
				
				assertionMap.put("index", indexList);
				assertionMap.put("r", rList);
				assertionMap.put("relation", relationList);
				assertionMap.put("l", lList);
				assertionMap.put("semantic", semanticList);
				VerbNetDictionary.jsonDictionary.add(assertionMap);
				//System.out.println(VerbNetDictionary.jsonDictionary);
			}
			//System.out.println(assertionMap);

		}
		//System.out.println("????");
		//System.out.println(MyObject myObject = new MyObject();

		
		//System.out.println(gsonResult.toJson(VerbNetDictionary.jsonDictionary));
		
		try (Writer writer = new FileWriter("Output.json")) {
		    //Gson gson = new GsonBuilder().create();
		    //gson.toJson(users, writer);
			Gson gsonResult = new GsonBuilder().setPrettyPrinting().serializeNulls().create();
			
		    gsonResult.toJson(VerbNetDictionary.jsonDictionary, writer);
		}
		catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
		}
		try (Writer writer = new FileWriter("Output2.json")) {
		    //Gson gson = new GsonBuilder().create();
		    //gson.toJson(users, writer);
			Gson gsonResult = new GsonBuilder().setPrettyPrinting().serializeNulls().create();
			
		    gsonResult.toJson(VerbNetDictionary.attributesDictionary, writer);
		}
		catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
		}			
		try (Writer writer = new FileWriter("Output3.json")) {
		    //Gson gson = new GsonBuilder().create();
		    //gson.toJson(users, writer);
			Gson gsonResult = new GsonBuilder().setPrettyPrinting().serializeNulls().create();
			
		    gsonResult.toJson(VerbNetDictionary.attributeCollectDictionary, writer);
		}
		catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
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

