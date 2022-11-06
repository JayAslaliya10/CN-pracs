import java.io.*;
import java.net.*;

public class MyServer{
    public static void main(String[] args){
        try{
            ServerSocket ss = new ServerSocket(8080);
            Socket s = ss.accept(); //establish connection
            DataInputStream din = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            
            String str = (String)din.readUTF();
            System.out.println("Number : "+str);

            int t = Integer.parseInt(str);
            int ans = 1;
            while(t>0){
                ans*=t;
                t--;
            }

            dout.writeUTF(Integer.toString(ans));
            dout.flush();
            dout.close();
            ss.close();

        }catch(Exception e){
            System.out.println(e);
        }
    }
}