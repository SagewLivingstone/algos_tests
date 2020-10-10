#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::endl;
using std::vector;
using std::string;

int main()
{
    vector<string> msg {"hello", "i", "am", "testing", "vscode"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}