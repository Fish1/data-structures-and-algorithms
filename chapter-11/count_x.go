package main

import "fmt"

func countX(s string) int {
	if len(s) == 0 {
		return 0
	}

	if s[0] == 'x' {
		return 1 + countX(s[1:])
	} else {
		return countX(s[1:])
	}
}

func main() {
	data := "axaxaxaxx"
	fmt.Println(countX(data))
}