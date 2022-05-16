package main

import "fmt"

func main() {

	s := "the quick brown box jumps over a lazy dog"

	m := make(map[rune]bool)

	for _, value := range s {
		m[value] = true
	}

	var result rune
	for r := 'a'; r < 'z'; r += 1 {
		if m[r] == false {
			result = r
			break
		}
	}

	fmt.Printf("%s", string(result))
}