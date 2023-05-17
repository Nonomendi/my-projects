package za.co.wethinkcode.mastermind;

import java.io.InputStream;
// import java.text.BreakIterator;
import java.util.Scanner;

// import org.junit.platform.commons.util.StringUtils;


public class Player {
    private final Scanner inputScanner;

    public Player(){
        this.inputScanner = new Scanner(System.in);
    }

    public Player(InputStream inputStream){
        this.inputScanner = new Scanner(inputStream);
    }

    /**
     * Gets a guess from user via text console.
     * This must prompt the user to re-enter a guess until a valid 4-digit string is entered, or until the user enters `exit` or `quit`.
     *
     * @return the value entered by the user
     */
    public String getGuess(){
        Scanner input = this.inputScanner;
        String user_input ;

        while (true){
            System.out.println("Input 4 digit code:");
            user_input = input.nextLine();

            if (user_input.equals("exit")|| user_input.equals("quit")){
                return "bye";
            }

            if (user_input.length()!= 4 ||! user_input.matches("[1-8]+")){
                System.out.println("Please enter exactly 4 digits (each from 1 to 8).");                
            }else{
                break;
            }
        }

        return user_input;
    }
}
