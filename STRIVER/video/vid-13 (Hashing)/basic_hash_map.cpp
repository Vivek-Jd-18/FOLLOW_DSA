# include <bits/stdc++.h>
using namespace std;

// N = 5
// arr = {1,2,1,2,3}

int main()
{
    // get array from user
    int n;
    cout<<"Enter Length"<<endl;
    cin>>n;

    int arr[n];

    cout<<"Enter "<<n<<" elements"<<endl;
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }

    // compute
    map <int, int> mp;
    for(int i = 0; i < n; i++){
        mp[arr[i]]++;                
    }


    // fetch
    int f;
    cout<<"Enter a number to fetch frequency of: "<<endl;
    cin>>f; 
    while(f--){
        int num;
        cin>>num;
        cout<<"Frequency of number '"<<num<<"' is: "<<mp[num]<<endl;
    }

}