public class URLify{
    public static void main(String[]args){
        String str = "Mr John Smith     ";
        char [] str1 = str.toCharArray();
        replaceSpaces(str1, 13);
        System.out.println(str1);

    }
    public static void replaceSpaces(char[] str, int length){
        int spaceCount = 0;
        int newLength = 0;
        //Count the number of spaces
        for(int i = 0; i < length; i++){
            if(str[i] == ' '){
                spaceCount++;
            }
        }
        newLength = length + spaceCount*2;
        System.out.println(newLength);
        str[newLength] = '\0';
        for(int i = length - 1; i >= 0; i--){
            if(str[i] == ' '){
                str[newLength-1] = '0';
                str[newLength-2] = '2';
                str[newLength-3] = '%';
                newLength = newLength - 3;
            }
            else{
                str[newLength - 1] = str[i];
                newLength = newLength - 1;
            }
        }
    }
}
