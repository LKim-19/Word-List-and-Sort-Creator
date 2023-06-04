fname = "romeo.txt"

fh = open(fname)
lst = list()

# For loop to split the lines up into individual words
# In the file
for line in fh:
    x = line.split()
    # For loop to loop through the words list
    for y in x:
        # If the word is not in the list it will
        # Append to the list. If already exists doesn't append.
        if y not in lst:
            lst.append(y)

lst.sort()

print(lst)
