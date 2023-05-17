package za.co.wethinkcode.fizzbuzz;

import java.util.ArrayList;
import java.util.List;

public class FizzBuzz {
    public String checkNumber(int number) {
        boolean divisibleBy3 = number % 3 == 0;
        boolean divisibleBy5 = number % 5 == 0;
            if (divisibleBy3 && divisibleBy5) {
                return "FizzBuzz";
            }else if (divisibleBy3) {
                return "Fizz";
            }else if (divisibleBy5) {
                return "Buzz";
            }
        return String.valueOf(number);
    }

    public String countTo(int number) {
        List<String> newlist = new ArrayList<String>(); 
        for (int i = 1; i <= number; i++) {
            newlist.add(checkNumber(i));
        }
        return newlist.toString();
    }
}
