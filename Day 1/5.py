list = []
import pandas as pd
for i in range(5):
    person = {}
    person['name'] =input("Enter your name: ")
    person['city'] = input("Enter your city : ")
    person['collge'] = input("Enter your phone college: ")
    person['email']= input("Enter your email: ")
    person['insta'] = input("Enter your insta id: ")
    list.append(person)
    print(type(person))
print(type(list)) 
df = pd.DataFrame(list)
print(type(df))
print(df)

print(df.loc[:,['name','email']])
print(df.loc[[2,4],['insta','name']])

findman = input("Enter name")
print(df.loc[df['name']==findman])