# is_palindrome function. Accepts any datatype, tries to convert it into str, returns false if str is not palindrome.
# Trows an error with description is an error occurs.

def is_palindrome (string):
    try:
        try_string = str(string)
        if len(try_string) < 2:
            return False
        forward_cnt = 0
        backward_cnt = -1
        while forward_cnt < len(try_string) // 2:
            if try_string[forward_cnt] != try_string[backward_cnt]:
                return False
            else:
                forward_cnt += 1
                backward_cnt -= 1
        return True
    except Exception as e:
        print("Something went wrong:", e)


print(is_palindrome("hahah"))
