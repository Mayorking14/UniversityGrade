import java.util.Scanner;

public class TypingSpeedTest {
	public static void main(String[] args) {

Scanner scanner = new Scanner(System.in);

	System.out.println("Typing Speed Test (Java)");
	System.out.println("Type this sentence exactly and press Enter when done:");

	System.out.println();
	String sentence = "The end is near, Jesus is coming soon";
	System.out.println(sentence);
	System.out.println();

	System.out.println("When you're ready, press Enter to start...");
	scanner.next(); 

	System.out.println("Start typing now and press Enter when finished:");
	long start = System.nanoTime();           
	String typedSentence = scanner.next();
	long end = System.nanoTime();

	double timeSeconds = (end - start) / 1_000_000_000.0; 
        double minutes = timeSeconds / 60.0;
	int numberOfWords = typedSentence.split("\\s+").length;

	double wordPerMinute = numberOfWords / minutes;

       System.out.println("Time taken in seconds is: " + timeSeconds);

	 System.out.println("Word per minute is: " + wordPerMinute);


}
}