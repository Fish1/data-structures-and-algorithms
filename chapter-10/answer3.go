package main

import "fmt"

func sum(low int, high int) int {
	if high < low {
		return 0
	}

	return high + sum(low, high - 1)
}

func main() {
	fmt.Println("Hello")
	fmt.Println(sum(1, 10))
	fmt.Println(sum(1, 12))
}