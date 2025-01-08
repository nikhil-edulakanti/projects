package Quiz;
import java.util.Scanner;

public class QuestionService {
    

    Questions [] questions = new Questions[5];
    

    public QuestionService() {
        questions[0] = new Questions(1, "size of int", "2", "6", "4", "8", "4");
        questions[1] = new Questions(2, "size of double", "2", "6", "4", "8", "8");
        questions[2] = new Questions(3, "size of char", "2", "6", "4", "8", "2");
        questions[3] = new Questions(4, "size of long", "2", "6", "4", "8", "8");
        questions[4] = new Questions(5, "size of boolean", "1", "2", "4", "8", "1");

    }

    public void playQuiz()
    {   
        Scanner sc = new Scanner(System.in);
        System.out.println("Welcome to the quiz!");
        System.out.println("Please do type the answer when prompted!");
        for(Questions q : questions)
        {
            System.out.println(q.getId() +  ") " + q.getQuestion());
            System.out.println(q.getOpt1() + " | " + q.getOpt2() + " | " + q.getOpt3() + " | " + q.getOpt4());
            String answer = sc.nextLine();
            if(answer.equals(q.getAnswer()))
            {
                System.out.println("Thats correct");
            }
            else{
                System.out.println("Wrong answer!");
            }

        }

    }

}
