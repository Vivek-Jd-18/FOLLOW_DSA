#include <iostream>
#include <vector>
using namespace std;

int countPrimes(int N) {
    if (N <= 2) return 0;
    vector<bool> arr(N, true);
    cout<<sizeof(arr)<<" size "<<endl;
    int primes = 0; 
    int i = 2;

    while(i*i <= N){
        if(arr[i] == true){
            for(int j = i*i; j<N; j+=i){
                arr[j] = false;
            }
        }
        i++;
    }


    for(int i = 2; i < N; i++){
        cout<<"index: "<<i<<"element: "<< arr[i] <<endl;
        if(arr[i] == true){
            primes++;
        }
    }

    return primes;
}

int main() {
    int n = 10;
    cout << countPrimes(n) << endl;  // Outputs: 4 (primes are 2, 3, 5, 7)
    return 0;
}
