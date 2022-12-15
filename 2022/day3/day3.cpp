#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

class Rucksack {
  private:
    string sack;
    string firstCompartment;
    string secondCompartment;

  public:
    Rucksack(string line);

    int priority();
    string getSack() { return sack; }
};

Rucksack::Rucksack(string line) {
    sack = line;
    firstCompartment = line.substr(0, line.length() / 2);
    secondCompartment = line.substr(line.length() / 2, line.length() / 2);
}

int Rucksack::priority() {

    for (char &c : firstCompartment) {
        if (secondCompartment.find(c) != string::npos) {
            if (islower(c)) {
                return (c - 'a') + 1;
            } else {
                return (c - 'A') + 27;
            }
        }
    }

    return 0;
}

int main() {

    ifstream infile;
    infile.open("input.txt");

    int totalPriority = 0;

    vector<Rucksack> sacks;

    string curLine;
    while (getline(infile, curLine)) {
        auto curSack = Rucksack(curLine);
        sacks.push_back(curSack);
    }

    for (int i = 0; i < sacks.size(); i += 3) {
        for (char &c : sacks[i].getSack()) {
            if (sacks[i + 1].getSack().find(c) != string::npos) {
                if (sacks[i + 2].getSack().find(c) != string::npos) {
                    // printf("For group:\n\t%s\n\t%s\n\t%s\n\tFound: %c\n",
                    //        sacks[i].getSack().c_str(), sacks[i + 1].getSack().c_str(),
                    //        sacks[i + 2].getSack().c_str(), c);
                    if (islower(c)) {
                        totalPriority += (c - 'a') + 1;
                    } else {
                        totalPriority += (c - 'A') + 27;
                    }
                    break;
                }
            }
        }
    }

    printf("Total priority: %d\n", totalPriority);
}