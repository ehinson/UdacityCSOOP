
def reverse_string(s):
    r_string = reversed(s)
    new_string = ""
    for char in r_string:
        new_string+= char
    print new_string

print reverse_string("a")

print reverse_string("The quick brown fox jumped over the lazy dog.")
