package main

import "fmt"

func reverse(s string) string {
	/* Base case */
	if len(s) == 1 {
		return s
	}

	/* Data store */
	last := string(s[len(s) - 1])
	remaining := string(s[0:len(s) - 1])

	/* Increment */
	return last + reverse(remaining)
}

func main() {
	data := "Hello World"
	fmt.Println(data)
	fmt.Println(reverse(data))
}