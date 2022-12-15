#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

enum rps { Rock = 0, Paper = 1, Scissors = 2 };
enum result { Loose = 0, Draw = 1, Win = 2 };

class Entry {
  private:
    rps opponentThrow;
    result provResult;

  public:
    Entry(string line);

    int getScore();
};

Entry::Entry(string line) {
    char oppThrowChar = line[0];
    char myThrowChar = line[2];

    this->opponentThrow = static_cast<rps>(oppThrowChar - 'A');
    this->provResult = static_cast<result>(myThrowChar - 'X');
}

int Entry::getScore() {
    int score = 0;

    if (opponentThrow == Rock) {
        if (provResult == Loose) {
            // Choose Scissors and Loose
            score = 3;
        } else if (provResult == Draw) {
            // Choose Rock and Draw
            score = 4;
        } else if (provResult == Win) {
            // Choose Paper and Win
            score = 8;
        }
    } else if (opponentThrow == Paper) {
        if (provResult == Loose) {
            // Choose Rock and Loose
            score = 1;
        } else if (provResult == Draw) {
            // Choose Paper and Draw
            score = 5;
        } else if (provResult == Win) {
            // Choose Scissors and Win
            score = 9;
        }
    } else if (opponentThrow == Scissors) {
        if (provResult == Loose) {
            // Choose Paper and Loose
            score = 2;
        } else if (provResult == Draw) {
            // Choose Scissors and Draw
            score = 6;
        } else if (provResult == Win) {
            // Choose Rock and Win
            score = 7;
        }
    }

    return score;
}

int main() {

    ifstream infile;
    infile.open("input.txt");

    int totalScore = 0;

    string curLine;
    while (getline(infile, curLine)) {
        auto curEntry = Entry(curLine);
        totalScore += curEntry.getScore();
    }

    printf("Total score: %d\n", totalScore);
}