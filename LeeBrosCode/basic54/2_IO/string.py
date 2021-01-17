import sys

# input
# 1 <= len(s) <= 100
s = sys.stdin.readline()

# output
sys.stdout.write(s)

'''
#include <iostream>
#include <string>  // string이 아니라 char로 선언하니까 Wrong Answer 돌아옴.
using namespace std;

int main()
{
    // declare var s
    string s;
    
    // input
    cin >> s;
    
    // output
    cout << s <<endl;
}
'''