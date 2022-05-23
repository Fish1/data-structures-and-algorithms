package main

import "fmt"

func sum_array(data []int) int {
	length := len(data)

	/* Edge case */
	if length == 0 {
		return 0
	}

	/* Base case */
	if length == 1 {
		return data[0]
	}

	/* Ruturn first element plus sum of remaining */
	return data[0] + sum_array(data[1:]);
}

func main() {
	data := []int{1, 2, 3, 4, 5}
	sum := sum_array(data)
	fmt.Println(sum)
}