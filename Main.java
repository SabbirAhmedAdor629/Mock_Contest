import java.util.*;  
class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    for (int i=0; i<10; i++){
      long number = in.nextLong();
      if(number == 0){
        continue;
      }
      if(number%17 == 0){
        System.out.println(1);
      }
      else{
        System.out.println(0);
      }
    }
    
    
  }
}