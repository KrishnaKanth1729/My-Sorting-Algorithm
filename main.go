package main

import (
	"fmt"
	"os"
)

func checkSort(array []int) bool {
	iteration := 0
	var count int
	for i := 0; i < len(array)-1; i++ {
		iteration += 1
		if array[i] <= array[i+1] {
			count += 1
		}
	}
	return count == len(array)-1
}

func sort(nums []int) []int {
	res := checkSort
	result := res(nums)
	if result == true {
		fmt.Println("List is already sorted")
		os.Exit(0)
	}
	count := 0
	size := len(nums)
	running := true
	for running {
		for i := 0; i < size-1; i++ {
			count += 1
			elem := nums[i]
			if elem <= nums[i+1] {
				continue
			} else {
				nums[i], nums[i+1] = nums[i+1], nums[i]

			}
		}
		res := checkSort(nums)
		if res == true {
			running = false
			break

		} else {
			continue
		}
	}
	return nums
}

func main() {
	var sample_array []int = []int{5, 6, 78, 12, 30, 67, 43, 21}
	fmt.Println(sort(sample_array))
}
