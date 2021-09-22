// https://www.hackerrank.com/challenges/encryption/problem

#include <bits/stdc++.h>

using namespace std;

// Complete the encryption function below.
string encryption(string s) {
    float size = sqrt(s.size());
    int rows = floor(size), cols = ceil(size);
    rows = (rows * cols < s.size()) ? cols : rows;
    vector<vector<char>> table = {};
    string encrypted = "";
    int idx = 0, jdx = 0, run = 0;
    for(idx = 0; idx < rows; idx++) {
        table.push_back({});
        for(jdx = 0; jdx < cols; jdx++) {
            if(run < s.size())
                table[idx].push_back(s[run++]);
            else
                table[idx].push_back('0');
        }
    }
    for(idx = 0; idx < cols; idx++) {
        for(jdx = 0; jdx < rows; jdx++)
            if(table[jdx][idx] != '0')
                encrypted += table[jdx][idx];
        encrypted += " ";
    }
    return encrypted;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = encryption(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
