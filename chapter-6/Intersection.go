package main

import (
	"fmt"
)

func intersection(a []int, b []int) []int {
	m := map[int]bool{}

	for _, valueA := range a {
		for _, valueB := range b {
			if valueA == valueB {
				m[valueA] = true
				break
			}
		}
	}

	output := []int{}
	for key := range m {
		output = append(output, key)
	}

	return output
}

func main() {
	arr1 := []int{1, 3, 5, 6}
	arr2 := []int{5, 6, 7, 1, 5, 9}
	inter := intersection(arr1, arr2)
	fmt.Printf("%v\n", inter)

}