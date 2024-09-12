#include<bits/stdc++.h>
using namespace std;
int main() {
  int a[] = {1,2,4};
  unordered_map < int, int > mpp;
  for (int i = 0; i < 8; i++) {
    mpp[a[i]]++;
  }
  int maxFreq = INT_MIN;
  int minFreq = INT_MAX;
  int maxEle = -1, minEle = -1;
  for (auto & e: mpp) {
    if (e.second > maxFreq) {
      maxEle = e.first;
      maxFreq = e.second;
    }
    if (e.second < minFreq) {
      minEle = e.first;
      minFreq = e.second;
    }
  }
  cout << maxEle << " " << minEle;
}