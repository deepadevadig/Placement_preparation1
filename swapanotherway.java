public class swapanotherway{


    public static void swap(int[] numbers){
        int temp=numbers[0];
        numbers[0]=numbers[1];
        numbers[1]=temp;
        System.out.println("number[0]" + numbers[0] + "numbers[1]"+ numbers[1]);

    }
    public static void main (String[] args){
        int input1 = 56;
        int input2 = 78;
        int[] input3={input1 , input2};
        
        swap(input3);







    }
    
}