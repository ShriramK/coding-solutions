//Problem C
import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args)
	{
		try
		{
			Scanner keyboard = new Scanner(new File("C-large-practice.in"));
			int size = Integer.parseInt(keyboard.next());//Integer.parseInt(keyboard.nextLine());
			PrintWriter outFile = new PrintWriter(new File("C-large-practice.out")); 
			for( int i = 0; i < size; i++ )
			{
				String a = keyboard.next();
				String b = keyboard.next();
				int answer = 0;
				if( b.length() != 1 )
				{
					int limit = Integer.parseInt(b);
					for( int j = Integer.parseInt(a); j < limit; j++ )
					{
						answer += cyclicStrings(j, limit);
					}
				}
				outFile.print("Case #" + (i+1) + ": " + answer + "\n");
			}
			keyboard.close();
			outFile.close();
		}
		catch(IOException e)
		{
		}
	}

	public static int cyclicStrings( int value, int limit )
	{
		int cnt = 0;
		String valueString = Integer.toString(value);
		String temp = valueString;
		int pos = 0;
		int end = Integer.toString(limit).length();
		Stack<Integer> nums = new Stack<Integer>();
		while( pos < end - 1)
		{
			temp = temp.substring(temp.length() - 1) + temp.substring(0, temp.length() - 1);
			int newValue = Integer.parseInt(temp);
			if( value < newValue && newValue <= limit )
			{
				if( nums.search(newValue) == -1 )
				{
					nums.push(newValue);
					cnt += 1;
				}
			}
			pos += 1;
		}
		return cnt;
	}
}