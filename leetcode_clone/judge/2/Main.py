def linearsearch(nums, target):
	for i in nums:
		if i == target:
			return True
	return False

def main():
	T = int(input())
	while T > 0:
		n = int(input())
		nums = list(map(int, input().split()))
		target = int(input())
		print(linearsearch(nums, target))
		T -= 1

main()
