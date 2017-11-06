import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class VerbNetDictionary {
	//direct to a right dictionary
	public static Map<String, String> verbnet_reference;
	public static Map<String, String> predicate_reference;
	public static Map<String, String> role_reference;
	public static Map<String, String> role_short_reference;
	
	public static List<Map<String, List<Map<String, String>>>> jsonDictionary;
	public static Map<String, List<String>> attributesDictionary;
	public static Map<String, List<String>> attributeCollectDictionary;
	
	//public static Map<String, String> verbnet_reference;
	public VerbNetDictionary(){
		verbnet_reference = new TreeMap<String, String>();
		predicate_reference = new TreeMap<String, String>();
		initialPredicate();
		System.out.println("predicate refereces: "+predicate_reference.size());
		
		role_reference = new TreeMap<String, String>();
		initialRole_general();
		//same as general
		//initialRole_NP();
		System.out.println("role refereces: "+role_reference.size());

		role_short_reference = new TreeMap<String, String>();
		jsonDictionary = new ArrayList<Map<String, List<Map<String, String>>>>();
		
		Map<String, String> semanticMap = new TreeMap<String, String>();
		List<Map<String, String>> itemMap = new ArrayList<Map<String, String>>();
		itemMap.clear();
		itemMap.add(semanticMap);
		Map<String, List<Map<String, String>>> assertionMap = new TreeMap<String, List<Map<String, String>>>();
		assertionMap.put("First", itemMap);
		jsonDictionary.add(assertionMap);
		
		attributesDictionary = new TreeMap<String, List<String>>() ;
		attributeCollectDictionary = new TreeMap<String, List<String>>();
		
		
		
	}
	//initialize
	private void initialRole_general(){
		//addShort("E", "empty");
		//addShort("T", "theme");
		//addShort("L", "location");
		addRole("Agent","Agent");
		addRole("Asset","Asset");
		addRole("Attribute","Attribute");
		addRole("Beneficiary","Beneficiary");
		addRole("Cause","Cause");
		addRole("Co-Agent","Co-Agent");
		addRole("Co-Patient","Co-Patient");
		addRole("Co-Theme","Co-Theme");
		addRole("Destination","Destination");
		addRole("Experiencer","Experiencer");
		addRole("Extent","Extent");
		addRole("Goal","Goal");
		addRole("Initial_Location","Initial_Location");
		addRole("Instrument","Instrument");
		addRole("Location","Location");
		addRole("Material","Material");
		addRole("Patient","Patient");
		addRole("Pivot","Pivot");
		addRole("Predicate","Predicate");
		addRole("Product","Product");
		addRole("Recipient","Recipient");
		addRole("Reflexive","Reflexive");
		addRole("Result","Result");
		addRole("Source","Source");
		addRole("Stimulus","Stimulus");
		addRole("Theme","Theme");
		addRole("Time","Time");
		addRole("Topic","Topic");
		addRole("Trajectory","Trajectory");
		addRole("Value","Value");
		
	}
	private void initialRole_NP(){
		//addShort("E", "empty");
		//addShort("T", "theme");
		//addShort("L", "location");
		
	}	
	private void initialPredicate(){
		addPredicate("Adv","Adv");
		addPredicate("Pred","Pred");
		addPredicate("Prep","Prep");
		addPredicate("about","about");
		addPredicate("abstain","abstain");
		addPredicate("adjust","adjust");
		addPredicate("admit","admit");
		addPredicate("adopt","adopt");
		addPredicate("agree","agree");
		addPredicate("alive","alive");
		addPredicate("allow","allow");
		addPredicate("amount_changed","amount_changed");
		addPredicate("apart","apart");
		addPredicate("appear","appear");
		addPredicate("apply_heat","apply_heat");
		addPredicate("apply_material","apply_material");
		addPredicate("approve","approve");
		addPredicate("assess","assess");
		addPredicate("attached","attached");
		addPredicate("attempt","attempt");
		addPredicate("avoid","avoid");
		addPredicate("base","base");
		addPredicate("begin","begin");
		addPredicate("believe","believe");
		addPredicate("benefit","benefit");
		addPredicate("body_motion","body_motion");
		addPredicate("body_process","body_process");
		addPredicate("body_reflex","body_reflex");
		addPredicate("calculate","calculate");
		addPredicate("capacity","capacity");
		addPredicate("cause","cause");
		addPredicate("change_value","change_value");
		addPredicate("characterize","characterize");
		addPredicate("command","command");
		addPredicate("concentrate","concentrate");
		addPredicate("conclude","conclude");
		addPredicate("confined","confined");
		addPredicate("conflict","conflict");
		addPredicate("confront","confront");
		addPredicate("consider","consider");
		addPredicate("conspire","conspire");
		addPredicate("contact","contact");
		addPredicate("continue","continue");
		addPredicate("convert","convert");
		addPredicate("cooked","cooked");
		addPredicate("cooperate","cooperate");
		addPredicate("cope","cope");
		addPredicate("correlate","correlate");
		addPredicate("cost","cost");
		addPredicate("covered","covered");
		addPredicate("created_image","created_image");
		addPredicate("declare","declare");
		addPredicate("dedicate","dedicate");
		addPredicate("defend","defend");
		addPredicate("degradation_material_integrity","degradation_material_integrity");
		addPredicate("delay","delay");
		addPredicate("depend","depend");
		addPredicate("describe","describe");
		addPredicate("designated","designated");
		addPredicate("desire","desire");
		addPredicate("destroyed","destroyed");
		addPredicate("different","different");
		addPredicate("direction","direction");
		addPredicate("disappear","disappear");
		addPredicate("discomfort","discomfort");
		addPredicate("discover","discover");
		addPredicate("emit","emit");
		addPredicate("emotional_state","emotional_state");
		addPredicate("end","end");
		addPredicate("enforce","enforce");
		addPredicate("ensure","ensure");
		addPredicate("equals","equals");
		addPredicate("exceed","exceed");
		addPredicate("exert_force","exert_force");
		addPredicate("exist","exist");
		addPredicate("experience","experience");
		addPredicate("express","express");
		addPredicate("filled_with","filled_with");
		addPredicate("financial_relationship","financial_relationship");
		addPredicate("flinch","flinch");
		addPredicate("forbid","forbid");
		addPredicate("force","force");
		addPredicate("free","free");
		addPredicate("future_possession","future_possession");
		addPredicate("give_birth","give_birth");
		addPredicate("group","group");
		addPredicate("harmed","harmed");
		addPredicate("has_possession","has_possession");
		addPredicate("help","help");
		addPredicate("hold","hold");
		addPredicate("in","in");
		addPredicate("in_reaction_to","in_reaction_to");
		addPredicate("indicate","indicate");
		addPredicate("involuntary","involuntary");
		addPredicate("involve","involve");
		addPredicate("license","license");
		addPredicate("limit","limit");
		addPredicate("linger","linger");
		addPredicate("location","location");
		addPredicate("made_of","made_of");
		addPredicate("manner","manner");
		addPredicate("masquerade","masquerade");
		addPredicate("meets","meets");
		addPredicate("mingled","mingled");
		addPredicate("motion","motion");
		addPredicate("necessitate","necessitate");
		addPredicate("neglect","neglect");
		addPredicate("nonagentive_cause","nonagentive_cause");
		addPredicate("occur","occur");
		addPredicate("path","path");
		addPredicate("perceive","perceive");
		addPredicate("perform","perform");
		addPredicate("physical_form","physical_form");
		addPredicate("position","position");
		addPredicate("promote","promote");
		addPredicate("property","property");
		addPredicate("relate","relate");
		addPredicate("renege","renege");
		addPredicate("risk","risk");
		addPredicate("rotational_motion","rotational_motion");
		addPredicate("rush","rush");
		addPredicate("search","search");
		addPredicate("seem","seem");
		addPredicate("sleep","sleep");
		addPredicate("social_interaction","social_interaction");
		addPredicate("spend","spend");
		addPredicate("state","state");
		addPredicate("subjugated","subjugated");
		addPredicate("successful_in","successful_in");
		addPredicate("suffocate","suffocate");
		addPredicate("supplicate","supplicate");
		addPredicate("suspect","suspect");
		addPredicate("take_care_of","take_care_of");
		addPredicate("take_in","take_in");
		addPredicate("together","together");
		addPredicate("transfer","transfer");
		addPredicate("transfer_info","transfer_info");
		addPredicate("understand","understand");
		addPredicate("urge","urge");
		addPredicate("use","use");
		addPredicate("value","value");
		addPredicate("via","via");
		addPredicate("visible","visible");
		addPredicate("wear","wear");
		addPredicate("weather","weather");
		addPredicate("yield","yield");

	}
	
	
	//basic functions
	private void addRole(String key, String value){
		role_reference.put(key, value);
	}
	private void addPredicate(String key, String value){
		predicate_reference.put(key, value);
	}
	private void addShort(String key, String value){
		role_short_reference.put(key, value);
	}
}
