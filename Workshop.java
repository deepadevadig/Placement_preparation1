public class Workshop {
    public  static int getSum(int number1,int number2)
    {
        return number1+number2;
    }
    public static  void invoke()
    {
        int result= getSum (1000,70);
        System.out.println("sum="+result);
    }

    public static void main(String[] args)
    {

       invoke();
    }

    
}
