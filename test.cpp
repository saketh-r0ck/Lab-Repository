
int x = 10

int call_by_value(int a){
    a = a+2;
    print(a);
    return 0;
}

int call_by_reference(int &a){
    a = a+ 2;
    print(a);
    return 0;
}

call_by_value(x);
call_by_refrence(*x);
