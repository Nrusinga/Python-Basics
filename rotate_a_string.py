str1 = 'charan'


def rotate_right(s):
    return s[-1] + s[:-1]  


for i in range(5):
    str1 = rotate_right(str1)
    print(f"After rotation {i+1}: {str1}")
