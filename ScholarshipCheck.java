public class ScholarshipCheck {
    public static void main(String[] args) {
        boolean passedInternal = true;  // assume input
        double cgpa = 8.5;              // assume input

        if (passedInternal) {
            if (cgpa >= 8.0) {
                System.out.println("🎉 Eligible for scholarship!");
            } else {
                System.out.println("Passed internal, but CGPA below 8. Not eligible.");
            }
        } else {
            System.out.println("Not eligible. Did not pass internal.");
        }
    }
}
