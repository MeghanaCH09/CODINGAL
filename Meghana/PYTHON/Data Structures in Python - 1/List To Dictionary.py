def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result
    
students=[[1, 'name1', 'Grade5'], [2, 'name2', 'Grade6'], [3, 'name3', 'Grade7'], [4, 'name4', 'Grade8'], [5, 'name5', 'Grade9']]

print("The Original Value ")
print(students)

print("Converting it to Dictionary Form")
print(test(students))
