package main

import "fmt"

func towerOfHanoi(s, d, e string, n int) {
	if n <= 0 {
		return
	}
	towerOfHanoi(s, e, d, n-1)
	fmt.Printf("Move disk - %d from %s to %s\n", n, s, d)
	towerOfHanoi(e, d, s, n-1)
}

func main() {
	towerOfHanoi("A", "B", "C", 3)
}
