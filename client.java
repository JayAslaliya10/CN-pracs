import java.io.*;
import java.net.*;

public class myClient{
    public static void main(String[] args){
        try{
            Socket s = new Socket("localhost",8080);
            DataInputStream din = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            BufferReader bfr = new BufferReader(new InputStreamReader(System.in));
            System.out.println("Enter the number : ");
            String str = bfr.readline();
            dout.writeUTF(str);

            String str2 = din.readUTF();
            System.out.println("The factorial of number is : "+str2);
            dout.flush();
            dout.close();
            s.close();

        }catch(Exception e){
            System.out.println(e);
        }
    }
}