import java.io.*;
import java.net.*;
import java.util.*;
class Serverrarp
{
            public static void main(String args[])
            {
            try
            {
                        ServerSocket obj=new ServerSocket(3000);
                        Socket obj1=obj.accept();
                        while(true)
                        {
                                    DataInputStream din=new DataInputStream(obj1.getInputStream());
                                    DataOutputStream dout=new DataOutputStream(obj1.getOutputStream());
                                    String str=din.readLine();
                                    String ip[]={"165.165.80.80","165.165.79.1"};
                                    String mac[]={"6A:08:AA:C2:B3:F8","8A:BC:E3:FA:6D:C3"};
                                    for(int i=0;i<mac.length;i++)
                                    {
                                                if(str.equals(mac[i]))
                                                {
                                                            dout.writeBytes(ip[i]+'\n');
                                                            break;
                                                }
                                    }                     
                                    obj.close();
                        }
                       
            }
            catch(Exception e)
            {
                        System.out.println(e);
            }
            }
}
