import random
s=["stone","paper","scissor"]
t=True
c=0
b=0
while t:
  e=int(input("0 for stone,1 for paper ,2 for scissor   "))
  print(s[e])
  r=random.randint(0,2)
  print(s[r])
  if(s[e]==s[1] and s[r]==s[0]):
    b=b+1
  elif(s[e]==s[0] and s[r]==s[2]):
    b=b+1
  elif(s[e]==s[2] and s[r]==s[1]):
    b=b+1
  elif(s[e]==s[1] and s[r]==s[2]):
    c=c+1
  elif(s[e]==s[0] and s[r]==s[1]):
    c=c+1
  elif(s[e]==s[2] and s[r]==s[0]):
    c=c+1
  elif(s[e]==s[r]):
    c=c+0
    b=b+0
  else:
    print("invalid input")
 
  i=int(input("enter 1 to continue "))
  if i!=1:
    t=False
print(f"your score {b}")
print(f"computers score {c}")


