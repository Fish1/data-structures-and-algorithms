package main

import "fmt"

type indexCount struct {
	index int
	Count int
}

func main() {

	m := make(map[rune]indexCount)
	s := "minimum"

	for index, value := range s {
		if entry, ok := m[value]; ok {
			entry.Count += 1
		} else {
			m[value] = indexCount{index: index, Count: 1}
		}
	}

	result := 'a'
	lowest := len(s)

	for key, value := range m {
		if value.Count == 1 && value.index < lowest {
			result = key
			lowest = value.index
		}
	}

	fmt.Printf("%s", string(result))
}