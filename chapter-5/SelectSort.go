package main

import (
  "fmt"
)

func selectSort(input []int) ([]int, int) {
  steps := 0
  output := make([]int, len(input))
  copy(output, input)
  length := len(input)
  for indexA := 0; indexA < length; indexA += 1 {
    leastIndex := indexA
    for indexB := indexA + 1; indexB < length; indexB += 1 {
      steps += 1
      if output[indexB] < output[leastIndex] {
        leastIndex = indexB
      }
    }
    steps += 1
    current := output[indexA]
    least := output[leastIndex]
    output[indexA] = least
    output[leastIndex] = current
  }
  return output, steps
}

func main() {
  data := []int{1, 2, 5, 2, 3, 1, 2, 3, -2, 10, 100, 12, 1, 5, 6, 100, 12, 35, 55, 55, 3, 222}
  fmt.Printf("%v\n", data);
  sortedData, steps := selectSort(data)
  fmt.Printf("%v %d\n", sortedData, steps);
}
