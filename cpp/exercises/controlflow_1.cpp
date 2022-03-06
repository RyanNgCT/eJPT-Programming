#include <iostream>
#include <limits.h> // check int overflow

using namespace std;

int main(){
	
// for (initialization, end_condition, increment/step){
// 			statement/ operation
// }

int value;
int a;
int b;

// similar to while
for (;;){
	cout << " 1 -> Addition\n 2 -> Subtraction\n Enter an option: ";
	cin >> value;
	
	if (value == 1){
	
		cout << "Enter 2 numbers to be summed with a space as a delimiter: " << endl;
		// ref: https://stackoverflow.com/questions/7425318/multiple-inputs-on-one-line
		cin >> a;
		cin >> b;
		
		// check int overflow (values entered > int_size or combined value > int_size) 
		if ((a < INT_MAX) && (b < INT_MAX) && ((a+b) < INT_MAX))
			cout << "The resultant value is " << a+b << endl;
		else
			cout << "Code value results in Integer Overflow... Quitting..." << endl;
			break;
	}
	else if (value == 2){
		cout << "Enter 2 numbers to be subtracted with a space as a delimiter: " << endl;
		cin >> a;
		cin >> b;
		
		// check int overflow (values entered > int_size)
		if ((a < INT_MAX) && (b < INT_MAX)) 
			if (a >= b)
				cout << "The resultant value is " << a-b << endl;
			else 
				cout << "The resultant value is " << b-a << endl;
		else
			cout << "Code value results in Integer Overflow... Quitting..." << endl;
			break;
	}
	else
		cout << "Invalid option selected! Please try again!" << endl;
	}

	cin.ignore();
	return 0;
}
