package main

import (
	"fmt"
	"strconv"
)

func invertList(_list []int) []int {
	length := len(_list)
	counter := length/2

	for i := 0; i < int(counter); i++ {
		fmt.Println(i)
		toCut := i+1
		number, _ := strconv.ParseInt(fmt.Sprintf("%d", length-toCut), 10, 64)
		fmt.Printf(" \n %v \n", number)

		_list[i], _list[number] = _list[number], _list[i]
		
	}

	return _list
}

func main() {
	fmt.Println(invertList([]int{2, 4, 1, 1, 3, 5, 21, 45}))
}
