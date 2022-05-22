package main

import (
	"errors"
	"fmt"
)

type Stack struct {
	data []rune
}

func push(s *Stack, v rune) {
	s.data = append(s.data, v)
}

func pop(s *Stack) (rune, error) {
	at := len(s.data) - 1
	if at < 0 {
		return 'a', errors.New("No Data")
	}
	result := s.data[at]
	s.data = s.data[0:at]
	return result, nil
}

func peek(s *Stack) (rune, error) {
	at := len(s.data) - 1
	if at < 0 {
		return '0', errors.New("No Data")
	}
	return s.data[len(s.data) - 1], nil
}

func main() {
	var mystack Stack
	mydata := "abcde"
	fmt.Println(mydata);

	for _, value := range mydata {
		push(&mystack, value)
	}

	mydata = ""
	for {
		val, err := pop(&mystack)
		if err != nil {
			break
		}
		mydata = mydata + string(val)
	}

	fmt.Println(mydata);
}