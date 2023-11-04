# recursion_str_reversal function accepts string and returns reversed string

def recursion_str_reversal (string):
    if len(string) == 1:
        return string
    return string[-1] + recursion_str_reversal(string[:-1])


print(recursion_str_reversal('reverse'))
