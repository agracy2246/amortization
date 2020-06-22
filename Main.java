import java.io.*;
public class Main{
    public static void main(String[] args){
        Amortization am = new Amortization(113000, .03, 30);
        try{
            am.saveReport("test.txt");
            System.out.println(am.mInterest);
           
        }catch(Exception ex){}
    }
}
