import java.io.*; 
import java.net.*; 
import java.util.*; 
class Server
{
	public static void main(String args[])
	{
		try
		{
			ServerSocket obj=new ServerSocket(139); 
			Socket obj1=obj.accept();
			while(true)
			{
				DataInputStream din=new DataInputStream(obj1.getInputStream()); 						DataOutputStream dout=new DataOutputStream(obj1.getOutputStream());
				String str=din.readLine();
				String ip[]={"165.165.80.80","165.165.79.1"};
				String mac[]={"6A:08:AA:C2","8A:BC:E3:FA"};
				for(int i=0;i<ip.length;i++)
				{	
					if(str.equals(ip[i]))
					{ 
						dout.writeBytes(mac[i]+'\n'); 
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
