package main

import (
  "fmt"
)

func bubbleSort(input []int) ([]int, int) {
  steps := 0
  output := make([]int, len(input))
  copy(output, input)
  length := len(output)
  index := 0
  for index != length - 1 {
    current := output[index]
    next := output[index + 1]
    if current > next {
      output[index] = next;
      output[index + 1] = current;
      index = 0
    } else {
      index += 1
    }
    steps += 1
  }
  return output, steps
}

func main() {
  data := []int{1, 2, 5, 2, 3, 1, 2, 3, -2, 10, 100, 12, 1, 5, 6, 100, 12, 35, 55, 55, 3, 222}
  sortedData, steps := bubbleSort(data)
  fmt.Printf("%v\n", data);
  fmt.Printf("%v %d\n", sortedData, steps);
}
