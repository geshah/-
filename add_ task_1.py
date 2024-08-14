grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
os_0=(grades[0])
os_1=(grades[1])
os_2=(grades[2])
os_3=(grades[3])
os_4=(grades[4])
sr_0 = float(sum(os_0)/len(os_0))
sr_1 = float(sum(os_1)/len(os_1))
sr_2= float(sum(os_2)/len(os_2))
sr_3= float(sum(os_3)/len(os_3))
sr_4= float(sum(os_4)/len(os_4))
list_izm = list(students)
res = list_izm.sort()
print(list_izm)
new_students={list_izm[0]:sr_0,list_izm[1]:sr_1,list_izm[2]:sr_2,list_izm[3]:sr_3,list_izm[4]:sr_4}
print(new_students)
