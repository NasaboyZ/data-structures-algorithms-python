# # O(n)
def print_items(n):
    for i in range (n):
        print(i)


print_items(10)


# # drop Const
def print_items(n):
    for i in range (n):
        print(i)
    for j in range (n):
        print(j)

print_items(10)

# # O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print (i,j)
print_items(10)

# Drop non Dominants
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_items(10)

#Big O(1)

def add_items(n):
    return n + n + n

