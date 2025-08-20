package main

import "fmt"

type Node struct {
	val int
	next *Node
}

func headTraverse(head *Node) {
	if (head != nil) {
		headTraverse(head.next)
		fmt.Printf("%d\n", head.val)
	}
}

func tailTraverse(head *Node) {
	if (head != nil) {
		fmt.Printf("%d\n", head.val)
		tailTraverse(head.next)
	}
}

func main() {
	ll := &Node{1, &Node{2, &Node{3, nil}}}

	headTraverse(ll)
	fmt.Println("--------------------------")
	tailTraverse(ll)
}
