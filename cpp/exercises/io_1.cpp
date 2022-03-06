#include <iostream>

using namespace std;


int main(){
	
	int uservalue;
	
	cout << "This program adds 10 to your input " << endl;
	cout << "Please enter an integer " << endl;
	
	cin >> uservalue;
	
	if (int(uservalue))
		cout << "The input value is " << uservalue << " and the updated value is " << uservalue + 10 << endl;
	else 
		cout << "Invalid integer value entered. Please enter an integer! Quitting..." << endl;
	
	cin.ignore();
	cout << " Press Enter to Exit..." << endl;
	cin.ignore();
	return 0;
}
