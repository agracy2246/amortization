public class Regex {
	public static void main(String[] args) {
		Pattern pattern;
		
		StringBuilder[] v = {
			new StringBuilder("075.0"),
			new StringBuilder("074.0"),
			new StringBuilder("073.0"),
			new StringBuilder("074.0.a"),
			new StringBuilder("074.0.b"),
			
			new StringBuilder("075.0.a-CP-43E"),
			
			new StringBuilder("1.8.c"),
			new StringBuilder("075.0_SpaceC2_v0.6")						
		};
		
		for(StringBuilder x : v) {
			// First check if the string matches without alteration
			if(x.toString().matches("[0-9]{3}\\.[0-9]{1}(\\.[0-9A-Za-z_]{1,15})?")) {
				System.out.println("Matches without alteration");
				continue; // for purposes of the loop
			}
			// Check if the first "block" is a match of ###.#.
			else if(x.toString().matches("[0-9]{3}\\.[0-9]{1}\\.(.*)?")) {
				System.out.println("First Block matches: " + x);
				// change any non-alphanumeric digit after the first block to a _
				for(int i = 6; i < x.length(); ++i) {
					if(!isAlphaNumeric(String.valueOf(x.charAt(i)))) {
						x.setCharAt(i, '_');
					}
				}
			}
			// Need to get the first block to match
			else if(x.toString().matches("[0-9]{3}\\.[0-9]{1}(.*)?")) {
				x.insert(5, '.');
				// change any non-alphanumeric digit after the first block to a _
				for(int i = 6; i < x.length(); ++i) {
					if(!isAlphaNumeric(String.valueOf(x.charAt(i)))) {
						x.setCharAt(i, '_');
					}
				}
			}
			// Nothing in the string matches, need to build our own
			else {
				for(int i = 0; i < x.length(); ++i) {
					if(!isAlphaNumeric(String.valueOf(x.charAt(i)))) {
						x.setCharAt(i, '_');
					}
				}
				x.insert(0,"00.0.");
			}
			
		}
		
		
	}
	public static boolean isAlphaNumeric(String s) {
		return s != null && s.matches("^[a-zA-Z0-9]*$");
	}
}