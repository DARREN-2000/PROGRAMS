import java.io.*;
import java.net.*;
import java.util.*;
class Clientrarp
{
            public static void main(String args[])
            {
            try
            {         
                        BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
                        Socket clsct=new Socket("127.0.0.1",3000);

                        DataInputStream din=new DataInputStream(clsct.getInputStream());
                        DataOutputStream dout=new DataOutputStream(clsct.getOutputStream());
                        System.out.println("Enter the Physical Addres (MAC):");
                        String str1=in.readLine();
                        dout.writeBytes(str1+'\n');
                        String str=din.readLine();
                        System.out.println("The Logical address is(IP): "+str);                     
                        clsct.close();
            }
            catch (Exception e)
            {
            System.out.println(e);
            }
            }
}
