package main

import "fmt"

func containsX(a string) bool {
	foundX := false

	for index := 0; index < len(a); index += 1 { 
		if a[index] == 'X' {
			foundX = true
			break
		}
	}

	return foundX
}

func main() {
	a := "difojfiAsodf"
	result := containsX(a)
	fmt.Printf("%s %t\n", a, result)
}