#include<iostream>
using namespace std;

int main() {
    int a;
    cout << "Enter first number:";
    cin >> a;
    int b;
    cout << "Enter second number:";
    cin >> b;
    int result = a / b;
    if(a % b != 0){
        cout << "the result is " << result << " and the reminder is " << a % b << endl;
    }
    else{
        cout << "the result is " << result << endl;
    }
}