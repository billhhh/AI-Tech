#include<iostream>
using namespace std;

int main ()
{
  int f[105], i, cur_money, cost;

  cur_money = 15;
  f[0] = 0;

  for (i = 1; i <= cur_money; i++)
    {
      cost = 99999;
      if (i - 1 >= 0) cost = min (cost, f[i - 1] + 1);
      if (i - 5 >= 0) cost = min (cost, f[i - 5] + 1);
      if (i - 11 >= 0) cost = min (cost, f[i - 11] + 1);
      f[i] = cost;
      printf ("f[%d]=%d\n", i, f[i]);
    }

  return 0;
}
