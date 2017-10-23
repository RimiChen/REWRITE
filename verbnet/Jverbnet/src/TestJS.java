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

public class TestJS{
	Map<String, String> tenseMapping;
	VerbData v_Data;
	
    public TestJS() throws IOException{
    	System.out.println("Constucter to save information");
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
				System.out.println("old: "+assertion.r+", new: "+tenseMapping.get(assertion.r));
				v_Data.getSemantic(tenseMapping.get(assertion.r));
			}
			
		}
    }

}

