#include <iostream>
#include <string>
using namespace std;

int main() {
    int number1;
    int number2;
    string op;

    cout << "Taschenrechner" << endl;
    cout << "number 1: " << endl;
    cin >> number1;
    cout << "operator: " << endl;
    cin >> op;
    cout << "number 2: " << endl;
    cin >> number2;
    

    if (op == "+") {
        cout << number1 + number2;
    } else if (op == "-") {
        cout << number1 - number2;
    } else if (op == "*") {
        cout << number1 * number2;
    } else if (op == "/") {
        cout << number1 / number2;
    } else {
        cout << "Invalid operator!"; 
    }

    return 0;
}
