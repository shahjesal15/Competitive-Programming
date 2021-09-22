// https://www.hackerrank.com/challenges/extra-long-factorials/problem

#include <bits/stdc++.h>

using namespace std;

// Complete the extraLongFactorials function below.
#define MAX 500

int multiply(int x, int res[], int res_size) {
    int carry = 0;
    for(int idx = 0; idx < res_size; idx++) {
        int result = res[idx] * x + carry;
        res[idx] = result % 10;
        carry = result / 10;
    }
    while(carry) {
        res[res_size] = carry % 10;
        carry /= 10;
        res_size++;
    }
    return res_size;    
}

void extraLongFactorials(int n) {
    int res[MAX];
    res[0] = 1;
    int res_size = 1;
    
    for(int idx = 2; idx <= n; idx++)
        res_size = multiply(idx, res, res_size);
    
    for(int idx = res_size - 1; idx >= 0; idx--)
        cout << res[idx];
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    extraLongFactorials(n);

    return 0;
}
