#Examples
nums = [10,20,30]
mix  = ["Dev", 22, True, 99.9]

#Accessong List Items(Indexing & Slicing)
#Indexing
nums = [10, 20, 30, 40]
print(nums[0])  #10
print(nums[2])  #30
print(nums[-3]) #20
print(nums[-1]) #40

#Slicing

print(nums[1:3]) #[20, 30]
print(nums[:2])  #[10,20]
print(nums[::2]) #[10, 30]
print(nums[::1]) #[10, 20, 30, 40]
print(nums[::3]) #[10, 40]
print(nums[::-3]) #[40, 10]
print(nums[::-2]) #[40, 20]
print(nums[::-1]) #[40, 30, 20, 10]

#List is Mutable
nums = [1, 2, 3]
nums[0] = 100
print(nums) #[100, 2, 3]

#List Manipulation
nums.append(50)
print(nums)

#Insert by index
nums.insert(1, 999)
print(nums)

#Extend the list
nums.extend([60, 70])
print(nums)

#Remove by item on list
nums = [10, 20, 30, 40]
nums.remove(20)
print(nums)


#Pop by Index
nums.pop(2)
print(nums)

#delete by index
del nums[1]

#clear list
nums.clear()
print(nums)

#Other list Methods

n = [90, 75, 47, 99, 20]

#Sort
n.sort()
print(n)

#Reverse
n.reverse()
print(n)

#Count
n.count(90)

#Index
n.index(75)

#List Comprehension

squares = [x*x for x in range(5)]
print(squares) # [0, 1, 4, 9, 16]

cubes = [x*x*x for x in range(6)]
print(cubes)

#fibonacci
n = 10
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
print(fib)


