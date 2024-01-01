#include <iostream>
#include <fstream>
#include <string>

string floor_commands;

ifstream file("Day1.txt");
while (getline(file, floor_commands))
{
    cout << floor_commands;
}
MyReadFile.close();