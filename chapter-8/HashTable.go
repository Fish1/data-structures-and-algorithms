package main

import "fmt"

func hash(value string, limit int) int {
	result := 1
	for _, element := range value {
		result *= int(element - ('0' - 1))
	}
	return result % limit
}

func main() {
	hashmap := []int{}
	fmt.Printf("%d\n", hash("test"))
	fmt.Printf("%d\n", hash("test1"))
}