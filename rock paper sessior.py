import random 
cpu_choice = random.randint(0,2)

user_chose= input('enter your choise\n')
if(cpu_choice== 0):
        cpu_chose= ('rock')
elif(cpu_choice==1):
    cpu_chose= ('paper')
elif(cpu_choice==2):
     cpu_chose= ('sessior')

print(('cpu choose\t'+cpu_chose)+ ('\nyou choose\t'+user_chose))

if(user_chose=='rock'):
    if(cpu_chose=='rock'):
         print('oops!! TIEEEEEE๐๐๐๐')
    elif(cpu_chose=='paper'):
        print('You loose๐ฅ๐ฅ๐ฅ')
    elif(cpu_chose=='sessior'):
        print('You win๐๐')


elif(user_chose=='paper'):
    if(cpu_chose=='paper'):
        print('oops!! TIEEEEEE๐๐๐๐')
    elif(cpu_chose=='rock'):
        print('You win๐๐')
    elif(cpu_chose=='sessior'):
        print('You loose๐ฅ๐ฅ๐ฅ')


elif(user_chose=='sessior'):
    if(cpu_chose=='sessior'):
        print('oops!! TIEEEEEE๐๐๐๐')
    elif(cpu_chose=='paper'):
        print('You win๐๐')
    elif(cpu_chose=='rock'):
        print('You loose๐ฅ๐ฅ๐ฅ')
    