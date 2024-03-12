# Check whether one string is a rotation of another

def check_rotation(str1,str2):

    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return "Not rotation"
    i = 0

    while i < len1:
        if str1[i:] in str2:   # Find out index of substring of first string in second string
            break_at = i
            break
        i += 1
    if i == len1:
        return "Not rotation"
    if str1[:i-1] in str2:      # Check remaining of first string is also in first string
        return "Rotation"
    else:
        return "Not rotation"



str1 = "JavaJ2eeStrutsHibernate"
str2 = "“StrutsHibernateJavaJ2ee”"

print(check_rotation(str1,str2))