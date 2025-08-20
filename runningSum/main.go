package main

import "fmt"

// Running Sum of 1d Array (LeetCode #1480)
// Problem statement: Given an integer array nums, the “running sum” at index i is the sum of all elements from nums[0] to nums[i].

// Input:  nums = [1, 2, 3, 4]
// Output: [1, 3, 6, 10]
// Explanation: runningSum[i] = sum(nums[0..i])

func sol(arr []int) {
	recursiveSol(arr, 0, 0)
}

func recursiveSol(arr []int, i int, sumSoFar int) int {
	if i >= len(arr) {
		return 0
	}
	arr[i] = arr[i] + sumSoFar
	recursiveSol(arr, i+1, arr[i])
	return arr[i]
}


func main() {
	arr := []int{1,2,3,4,5} 
	sol(arr)
	fmt.Println(arr)
}
