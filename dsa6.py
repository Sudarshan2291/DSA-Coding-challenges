""" Encoded message only small case
1) swap 1st with 2nd and 3rd with 4th character and so on if length is odd dont swap
2)replace a by z and b by y and c by x,etc,and z by a """

def encode_str(s):
    l = len(s)
    lst1 = s.split()
    lst2 = []
    if l%2 == 0:
        for i in range(0,l-1,2):
            lst1[i],lst1[i+1] = lst1[i+1],lst1[i]

        for char in lst1:
            if 'a' <= char <= 'z':
                lst2.append(chr(ord('z') - (ord(char) - ord('a'))))

    else:
        for char in s:
            if 'a' <= char <= 'z':
                lst2.append(chr(ord('z') - (ord(char) - ord('a'))))
    
    return ''.join(lst2)



s = input("Enter the string")
res = encode_str(s)
print(res)
