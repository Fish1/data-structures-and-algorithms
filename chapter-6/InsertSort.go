package main

import (
	"fmt"
)

func insertSort(input []int) ([]int, int) {
	steps := 0
	output := make([]int, len(input))
	copy(output, input)
	length := len(input)
	for indexA := 1; indexA < length; indexA += 1 {
		valueA := output[indexA]
		openIndex := indexA
		for indexB := indexA - 1; indexB >= 0; indexB -= 1 {
			/* comparison */
			steps += 1
			valueB := output[indexB]
			if valueA < valueB {
				/* shift */
				steps += 1
				output[indexB + 1] = valueB
				openIndex = indexB
			} else {
				break
			}
		}
		output[openIndex] = valueA
	}

	return output, steps
}

func main() {
  data := []int{1, 8 ,2, 7, 3, 6, 4, 5}
  fmt.Printf("%v\n", data);
  sortedData, steps := insertSort(data)
  fmt.Printf("%v %d\n\n", sortedData, steps);

  data = []int{1, 2, 3, 4, 5, 6, 7, 8}
  fmt.Printf("%v\n", data);
  sortedData, steps = insertSort(data)
  fmt.Printf("%v %d\n\n", sortedData, steps);
	
  data = []int{8, 7, 6, 5, 4, 3, 2, 1}
  fmt.Printf("%v\n", data);
  sortedData, steps = insertSort(data)
  fmt.Printf("%v %d\n", sortedData, steps);
}