#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
// Create a text string, which is used to output the text file
string floor_commands;
// Read from the text file
ifstream file("Day1.txt");
// Use a while loop together with the getline() function to read the file line by line
while (getline(file, floor_commands)){}
// Close the file
file.close();

bool basementFound = false;
//Part 1

int floor = 0;

for (int i = 0; i < floor_commands.length(); i++) {
    if (floor_commands[i] == '(') {
        floor += 1;
    }
    else if (floor_commands[i] == ')') {
        floor -= 1;
    }

    if (floor == -1 && !basementFound) {
        cout<< i + 1<< endl;
        basementFound = true;
    }
}
cout<< floor<< endl;
}
