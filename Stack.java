// Java program for reversing the linked list
import java.io.*;
import java.util.*;

class Stackdemo {
    
	public static void main(String[] args)
	{
		 Stack<String> st = new Stack<String>();
		 Stack<String> st1 = new Stack<String>();
		 st.push("hey");
		 st.push("how");
		 st.push("you");
		 st.push("doing");
		 System.out.println(st+"\n");
		 while(!st.empty()){
		     //System.out.print(st.peek()+"\n");
		     st1.push(st.peek());
		     System.out.print(st.pop()+"\n");
		 }
		 System.out.println(st1+"\n");
	}
}
