// Given two strings, write a method to decide if one is a permutation of the other

/* Date structure to use: Hashtable to record character numbers
   Big-O complexity: running time O(n)
*/


import java.util.Hashtable; 
import java.util.Set;


public class CheckPermutation{

	public static boolean isPermutation(String s1, String s2){
		// length different 
		if(s1.length() != s2.length()){
			return false;
		}

		Hashtable<Character,Integer> ht = new Hashtable<Character,Integer>();

		// count characters
		char[] s1_arr = s1.toCharArray();
		for(int i =0; i< s1_arr.length; i++){
			if(ht.containsKey(s1_arr[i])){
				int tmp = ht.get(s1_arr[i])+ 1;
				ht.put(s1_arr[i],tmp);
			}
			else{
				ht.put(s1_arr[i],1);
			}
		}

		char[] s2_arr = s2.toCharArray();
		for(int j =0; j< s2_arr.length;j++){
			// contain same key
			if(ht.containsKey(s2_arr[j])){
				int val = ht.get(s2_arr[j]);
				// if no chars in existing hash table
				if(val == 0){
					return false;
				}
				else{
					val--;
					ht.put(s2_arr[j],val);
				}
			}
			// no key found
			else{
				return false;
			}
		} // finish looping second char array

		// check if s1 has char doesn't exist in s2
		Set<Character> keys = ht.keySet();
		for(char key: keys){
			int v = ht.get(key);
			if(v != 0){
				return false;
			}
		}

		return true;
	}


	public static void main(String args[]){
		String s1 = "abc";
		String s2 = "bac";
		System.out.println("abc and bac anagram "+ isPermutation(s1,s2));
		s1 = "ABC ";
		s2 = "CBA";
		System.out.println("ABC  and CBA anagram "+ isPermutation(s1,s2));
		s1 = "AABBCC";
		s2 = "ABCABC";
		System.out.println("AABBCC and ABCABC anagram "+ isPermutation(s1,s2));

	}
}