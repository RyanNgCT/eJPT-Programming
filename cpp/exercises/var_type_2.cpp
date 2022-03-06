#include <iostream>

using namespace std;

int global_var = 10;

int main(){
	
	cout << "The value of the global variable is: " << global_var << endl;
	
	// attempt to change global var
	int global_var = 100;
	// now it is set to local scope
	cout << "The value of the global variable is: " << global_var << endl;
	
	//system("PAUSE");
	cin.ignore();
	return 0;
}
