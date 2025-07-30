public class isnumber {

    public static boolean isnumber(String input) {
        boolean result = true;

        for (int index = 0; index < input.length(); index++) {
            char character = input.charAt(index);
            if (character < '0' || character > '9') {
                result = false;
                break;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String input = "fghjghjdfg";

        boolean isNum = isnumber(input);

        if (isNum) {
            System.out.println(input + " is a number.");
        } else {
            System.out.println(input + " is NOT a number.");
        }
    }
}
