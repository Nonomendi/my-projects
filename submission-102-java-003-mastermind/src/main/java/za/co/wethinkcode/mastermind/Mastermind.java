package za.co.wethinkcode.mastermind;

public class Mastermind {
    private final String code;
    private final Player player;



    public Mastermind(CodeGenerator generator, Player player){
        this.code = generator.generateCode();
        this.player = player;
    }
    public Mastermind(){
        this(new CodeGenerator(), new Player());
    }

    public void runGame(){
        // System.out.println(code);
    
        System.out.println("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.");
      int turns = 12;
     
      while (turns >0 ){
        int correct_digits = 0;
        int incorrect_digits = 0;
        turns--;
        String guess = this.player.getGuess();
        if (guess == "bye"){
            break;
        }
        
        for (int i = 0; i < 4; i++) {
            if (guess.charAt(i) == code.charAt(i)) {
                correct_digits++;
              } else if (code.indexOf(guess.charAt(i)) != -1) {
                incorrect_digits++;
            }
        }
        System.out.println("Number of correct digits in correct place: " + correct_digits);
        System.out.println("Number of correct digits not in correct place: " + incorrect_digits);
        
        if(turns == 0){
            System.out.println("No more turns left.\nThe code was: " + code);
                break;

        }

        if (correct_digits == 4) {
            System.out.println("Congratulations! You are a codebreaker!\nThe code was: " + code);
            break;

                
            }
        if(guess != code){
                System.out.println("Turns left: "+ turns);
                
            }
        
      
        
    }
   
        
        }

    public static void main(String[] args){
        Mastermind game = new Mastermind();
        game.runGame();
    }
}
