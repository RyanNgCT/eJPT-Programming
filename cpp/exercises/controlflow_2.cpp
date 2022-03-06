#include <iostream>
#include <limits.h> // check int overflow

using namespace std;

//globals
int value;
int a;
int b;

int main(){

while (value!= 3)
{
	cout << " 1 -> Addition\n 2 -> Subtraction\n 3 -> Exit Program\n Enter an option: ";
	cin >> value;
	
	switch (value)
	{
		case 1:
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
				
		case 2:
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
				
	 	case 3:
			cout << "Exitting!" << endl;
			break;
	}
	cout << "Invalid option selected! Please try again!" << endl;
}
	cin.ignore();
	return 0;
}
