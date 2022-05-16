package main

import "fmt"

func main() {

	a := []string{"a", "b", "c", "d", "c", "e", "b"}

	m := make(map[string]bool)

	var result string

	for _, value := range a {

		if m[value] {
			result = value
			break
		}
		
		m[value] = true
	}

	fmt.Printf("%s", result)
}