// Java program for reversing the linked list

class LinkedList {

	static Node head;

	static class Node {

		int data;
		Node next;

		Node(int d)
		{
			data = d;
			next = null;
		}
	}

	Node itterativereverse(Node node)
	{
	    Node prev=null;
	    Node current=node;
	    Node ahead=null;
	    while(current!=null){
	        ahead=current.next;
	        current.next=prev;
	        prev=current;
	        current=ahead;
	    }
		return prev;
	}
	
	Node recursivereverse(Node head)
	{
	    //basecases
	    if(head==null||head.next==null){
	        return head;
	    }
	    
	    Node rhead=recursivereverse(head.next);
	    head.next.next=head; 
	    head.next=null;
	    return rhead;
		
	}

	void printList(Node node)
	{
		while (node != null) {
			System.out.print(node.data + " ");
			node = node.next;
		}
	}

	
	public static void main(String[] args)
	{
		LinkedList list = new LinkedList();
		list.head = new Node(5);
		list.head.next = new Node(10);
		list.head.next.next = new Node(15);
		list.head.next.next.next = new Node(20);

		list.printList(head);
		head = list.recursivereverse(head);
		System.out.println("");
		System.out.println("Reversed linked list ");
		list.printList(head);
		head = list.itterativereverse(head);
		System.out.println("");
		System.out.println("Reversed Reversed linked list ");
		list.printList(head);
	}
}
