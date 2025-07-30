public class swap{

    public static void getswap(int number1,int number2)

    {
        
        int temp=number1;
        number1=number2;
        number2=temp;
        System.out.println("number1="+number1 +" " + "number2="+number2);


    }


public static void main(String[] args){
    getswap(23,78);



}


}