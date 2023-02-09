
# 10
# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
print("!!!TASK 10!!!")
def uniques(elements):
    uniques = dict(())
    for elem in elements:
        if(elem not in uniques.keys()):
            uniques[elem] = 0
    return uniques.keys()

nums = list(map(int, input().split()))
print(uniques(nums))
