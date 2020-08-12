#include<iostream>
using namespace std;

#define ONECENT    1
#define FIVECENT    5
#define TENCENT    10
#define TWENTYFINECENT 25

int main()
{
    int cur_money=41;
    int num_25=0,num_10=0,num_5=0,num_1=0;

    //Try different denominations
    while(cur_money>=TWENTYFINECENT){
        num_25++;
        cur_money -=TWENTYFINECENT;
    }
    
    while(cur_money>=TENCENT){
        num_10++;
        cur_money -=TENCENT;
    }
    
    while(cur_money>=FIVECENT){
        num_5++;
        cur_money -=FIVECENT;
    }
    
    while(cur_money>=ONECENT){
        num_1++;
        cur_money -=ONECENT;
    }

    //output
    cout<< "25 cents："<<num_25<<endl;
    cout<< "10 cents："<<num_10<<endl;
    cout<< "5 cents："<<num_5<<endl;
    cout<< "1 cents："<<num_1<<endl;

    return 0;
}