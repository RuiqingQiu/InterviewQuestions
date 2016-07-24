/* 1.6 String Compression: Implement a method to perform basic string
 compression using the counts of repeated characters. For example,
 the string aabcccccaaa would become a2b1c5a3. If the "compressed" string
 not become smaller than the original string, your method should return the
 original string. You can assume the string has only uppercase and lowercas    e
 (a-z).

 Input: aabccccccaaa
 Output: a2b1c5a3
 Input: abcd
 Output: abcd
*/

import java.lang.StringBuilder;

public class StringCompression{
	
	
	public static String compress(String s){
		String s_lower = s.toLowerCase(); 
		int char_count = 1;
		char[] arr = s_lower.toCharArray();
		char prev = arr[0];
		StringBuilder builder = new StringBuilder();

		// start from the second character till the end
		for(int i=1; i<arr.length;i++){
			char curr = arr[i];
			// current same as prev
			if(curr == prev){
				char_count++;
			}
			// build string
			else{
				builder.append(prev).append(char_count);
				char_count = 1; // reset counter
				prev = curr;
			}
		}
		String result = builder.append(prev).append(char_count).toString();
		
		// System.out.println("old" + s.length());
		// System.out.println("new" + result.length());


		if(result.length() >= s.length()){
			return s;
		}

		return result;

	}//end of the function*/

	public static void main(String[] args){
		System.out.println(compress("aabcccccaaa"));//a2b1c5a3
		System.out.println(compress("abcd"));//abcd
		System.out.println(compress("aAaaAbcd")); // aAaaAbcd
		System.out.println(compress("aAbCcccccCaaaA"));//a2b1c7a4

	}

} // end of class

