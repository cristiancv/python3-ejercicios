dic1 = {'a' : 1, 'b' : 12, 'c' : 13 , 'd' : 4}
print("dic 1:",dic1)
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
print("dic 2:",dic2)
dic3=dic1
print("dic 3: ", dic3)
dic3.update(dic2)
print("dic 3: ", dic3)
#dic1 → {‘a’ : 1, ’b’ : 5, ‘c’ : 6 , ‘d’ : 4 , ‘e’ : 9 , ‘f’ : 10}
print("dic 1:",dic1)
print("dic 2:",dic2)
print("dic 3: ", dic3)