account1='qiyu'
password1='123456'
print('please input account')
account2=input()
print('please input password')
password2=input()
user_account=account2
user_password=password2
if account1==account2:
    if password1==password2:
        print('successs!')
    else:
        print('fall!')

else:
    print('fall!')
