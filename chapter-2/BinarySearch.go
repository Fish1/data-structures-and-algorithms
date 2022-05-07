package main

import (
  "fmt"
)

func binarySearch(data []int, search int) (int, int) {
  steps := 0
  lower := 0
  upper := len(data) - 1

  for lower <= upper {
    steps += 1
    middle := (upper + lower) / 2
    value := data[middle]
    if search == value {
      return middle, steps
    }

    if search > value {
      lower = middle + 1
    } else if search < value {
      upper = middle - 1
    }
  }
  return -1, steps
}

func linearSearch(data []int, search int) (int, int) {
  length := len(data)
  for index := 0; index < length; index += 1 {
    if data[index] == search {
      return index, index
    }
  }
  return -1, length
}

func execute(data []int, search int) {
  index, steps := binarySearch(data, search)
  fmt.Printf("Binary Search: %d in %d ? %d ... found in %d steps\n", search, data, index, steps);
  index, steps = linearSearch(data, search)
  fmt.Printf("Linear Search: %d in %d ? %d ... found in %d steps\n\n", search, data, index, steps);
}

func main() {
  arr := []int{1, 2, 5, 6, 7, 9, 10}
  for index := 1; index <= 10; index += 1 {
    execute(arr, index);
  }
}
