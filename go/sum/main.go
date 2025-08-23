package main

import "fmt"

func recursion_sum(n int) int {
	if (n == 1) {
		return 1
	} else {
		return n + recursion_sum(n-1)
	}
}

func sum(n int) int {
	result := 0
	for i := range n+1 {
		result += i
	}
	return result
}

func main() {
	fmt.Println(sum(3))
	fmt.Println(recursion_sum(3))
}
