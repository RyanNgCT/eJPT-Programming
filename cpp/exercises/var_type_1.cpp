#include <iostream>

using namespace std;

int main(){
	int a = 2;
	int b = 3;
	int sum = a + b;
	
	cout << "The output of the sum of the two values is: " << sum << endl;
	
	a = 100;
	
	sum = a + b;
	
	cout << "The output of the sum of the two values (with a updated) is: " << sum << endl;
	
	system("PAUSE");
	cin.ignore();
	return 0;
}
