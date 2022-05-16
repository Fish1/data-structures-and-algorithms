package main

import "fmt"

func intersection(a []int, b []int) []int {
	m := make(map[int]bool)
	var big []int
	var small []int

	if len(a) >= len(b) {
		big = a
		small = b
	} else {
		big = b
		small = a
	}

	for _, value := range big {
		m[value] = true
	}

	m2 := make(map[int]bool)

	for _, value := range small {
		if m[value] {
			m2[value] = true
		}
	}

	result := []int{}

	for key := range m2 {
		result = append(result, key)
	}

	return result
}

func main() {
	a := []int{1, 2, 3, 4, 5, 100, 101}
	b := []int{0, 2, 100, 4, 6, 8, 5}
	c := intersection(a, b)

	fmt.Printf("%v", c)
}