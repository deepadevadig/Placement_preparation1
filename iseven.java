public class iseven{
    public static boolean is_even(int number)
    {
        if (number % 2 == 0)
        {
             System.out.println("number is even");
            return true;
        
        }
        else{
             System.out.println("number is not even");
             return false;

        }
    }



    public static void main(String[] args)
    {
        is_even(18);

    }



}