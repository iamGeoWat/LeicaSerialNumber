#include <iostream>
#include <fstream>
using namespace std;

int main(){
    string a0 = "case ";
    string a1 = "<=SN && SN<=";
    string a2 = ": {type=\"";
    string a3 = "\";year=\"";
    string a4 = "\";pa=\"";
    string a5 = "\";}";
    fstream data;
    int i=0;

    data.open("leica.txt", ios::in);
    while (!data.eof()) {
        if (data.get() == ' ' && i == 0) {
            data.write(a0.c_str(), a0.size());
            i++;
            break;
        }
        if (data.get() == ' ' && i == 1) {
            data.write(a1.c_str(), a1.size());
            i++;
            break;
        }
        if (data.get() == ' ' && i == 2) {
            data.write(a2.c_str(), a2.size());
            i++;
            break;
        }
        if (data.get() == ' ' && i == 3) {
            data.write(a3.c_str(), a3.size());
            i++;
            break;
        }
        if (data.get() == ' ' && i == 4) {
            data.write(a4.c_str(), a4.size());
            i++;
            break;
        }
        if (data.get() == ' ' && i == 5) {
            data.write(a5.c_str(), a5.size());
            i++;
            i=0;
            break;
        }
    }
    data.close();
    return 0;
}
