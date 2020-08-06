#include<iostream>
using namespace std;

#define ONEFEN    1
#define FIVEFEN    5
#define TENFEN    10
#define TWENTYFINEFEN 25

int main()
{
    int cur_money=41;
    int num_25=0,num_10=0,num_5=0,num_1=0;

    //Try different denominations
    while(cur_money>=TWENTYFINEFEN){ 
        num_25++;
        cur_money -=TWENTYFINEFEN;
    }
    
    while(cur_money>=TENFEN){
        num_10++;
        cur_money -=TENFEN;
    }
    
    while(cur_money>=FIVEFEN){
        num_5++;
        cur_money -=FIVEFEN;
    }
    
    while(cur_money>=ONEFEN){
        num_1++;
        cur_money -=ONEFEN;
    }

    //output
    cout<< "25 cents："<<num_25<<endl;
    cout<< "10 cents："<<num_10<<endl;
    cout<< "5 cents："<<num_5<<endl;
    cout<< "1 cents："<<num_1<<endl;

    return 0;
}