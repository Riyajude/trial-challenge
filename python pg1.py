st='diya python123# riya'
a=0
sp=0
d=0
ch=0
print(st)
for i in st:
    if i.isalpha():
        a=a+1
        
    elif i.isspace():
        sp=sp+1
        
    elif i.isdigit():
        d=d+1
        
    else:
        ch=ch+1
print('no of alphabets:',a)
print('no of space:',sp)
print('digits',d)
print('sp ch',ch)
print(st.split())





    
    
