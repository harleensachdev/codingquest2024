#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <limits.h>
using namespace std;
int main() {
  
    string input = "AAA: Seat 9997\nBBB: Discount 2886\nDDD: Luggage 3500\nAAA: Tax 156\nCCC: Fee 9468\nBBB: Fee 9378\nAAA: Discount 3103\nDDD: Rebate 967";

    unordered_map <string, int> companyCosts;
  stringstream ss(input);
  string line;
  while(getline(ss,line)) {
    stringstream lineStream(line);
    string company, detail;
    int value;
    lineStream >>company>>detail>>value;

    if (detail == "Seat" || detail == "Meals" || detail == "Luggage" || detail == "Fee" || detail == "Tax" ){
      companyCosts[company] += value;
  } else if (detail == "Discount" || detail == "Rebate") {
    companyCosts[company] -= value;
  }


  }
  int minCost = INT_MAX;
  for (auto& entry: companyCosts) {
    minCost = min(minCost, entry.second);

  }
  cout << "Final cost of the cheapest option: " << minCost << endl;

  return 0;
}
