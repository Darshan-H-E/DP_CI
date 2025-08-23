package main

import "fmt"

type Node struct {
	val   int
	left  *Node
	right *Node
}


func efficient_inorder(node *Node) {
	if node == nil {
		return
	}

	if node.left != nil {
		efficient_inorder(node.left)
	}
	fmt.Printf("%d\n", node.val)

	if node.right != nil {
		efficient_inorder(node.right)
	}
}

func main() {
	root := &Node{
		val: 2,
		left:  &Node{val: 1},
		right: &Node{val: 3},
	}

	efficient_inorder(root)
}

// Time Complexity: O(n)
//
//     Every node is visited exactly once.
//
//     So for n nodes, total work done = O(n).
//
//  Space Complexity:
//
//     Best case (balanced tree): O(log n) – recursion stack grows with tree height.
//
//     Worst case (skewed tree): O(n) – if the tree is a straight line (all left or all right children).
//     So, space complexity is O(h), where h is the height of the tree.
