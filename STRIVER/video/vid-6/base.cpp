// C++ STL divided into:
// 1)Algorithms
// 2)Containers
// 3)Functions
// 4)Iterators

#include <bits/stdc++.h>
using namespace std;

bool comp(pair<int, int> p1, pair<int, int> p2)
{
    if (p1.first > p2.first)
        return true;
    if (p1.first < p2.first)
        return false;

    if (p1.second < p2.second)
        return true;
    return false;
}

int main()
{

    // CONTAINERS AND ITERATORS

    // // pairs ------------------------------------------------------------------------------------------------
    // pair <int, int> p = {1,2};
    // cout << p.first << p.second <<endl;

    // // nested pairs
    // pair <int, pair <int, int>> p2 = {1,{2,3}};
    // cout << p2.first << p2.second.first << p2.second.second << endl;

    // // pair array
    // pair<int, int> arr[] = {{1,2},{1,2},{1,2}};
    // cout << arr[0].first << arr[1].second << arr[2].first <<endl;

    // Container : 1)Vectors
    // vector<int> v1;
    // v1.push_back(1);
    // v1.emplace_back(2);

    // vector<pair<int, int>> v2;
    // v2.push_back({1,2});
    // v2.emplace_back(3,4);

    // vector<int> v3(5,10);

    // vector<int> v4 = {1,2,3,4,5};

    // vector<int> v5(v4);

    // // cout<<v1[0]<<endl;

    // // Iterators with Vector ------------------------------------------------------------------------------------------------
    // // Iterator is nothing but a point to the memroy where the elememt lies

    // vector<int>::iterator it = v4.begin();
    // it++;
    // // cout<< *(it) <<endl;
    // vector<int>::iterator it2 = v4.end();
    // // cout<< *(it2) <<endl;

    // // loop the iterator
    // // for(vector<int>::iterator i = v4.begin(); i!=v4.end(); i++){
    // //     cout << *(i)<<endl;
    // // }

    // // "auto" is used for a datatype to automatically assign according to the data
    // // for(auto i = v4.begin(); i!=v4.end(); i++){
    // //     cout << *(i)<<endl;
    // // }

    // // Erase
    // v4.erase(v4.begin()+1,v4.begin()+3);

    // // for(auto i : v4){
    // //     cout << i << endl;
    // // }

    // // Insert
    // // vector<int> vx(2,100);
    // // vx.insert(vx.begin()+1,120);

    // // for(auto i : vx){
    // //     cout << i << endl;
    // // }

    // // vector<int> vx(2,100);
    // // vx.insert(vx.begin()+1,120);

    // // vector<int> vnew = {1,2,3,4};
    // // vnew.insert(vnew.begin(),vx.begin(),vx.end());

    // // vnew.pop_back();
    // // cout << "Vector size: " << vnew.size() << endl;

    // // // vnew.swap(v4);

    // // vnew.clear();
    // // for(auto i : vnew){
    // //     cout << i << endl;
    // // }

    // List  ---------------------------------------------------------------------------------------------
    // list<int> l1;
    // l1.push_back(1);
    // l1.push_back(2);
    // l1.push_front(3);
    // l1.push_back(4);

    // for (auto i : l1)
    // {
    //     cout << i << endl;
    // }

    // Deque - has the same functions as List so leave it -----------------------------------------------------

    // // Stack - is LIFO ----------------------------------------------------------------------------------------

    // stack<int> st, st1;
    // st.push(1);
    // st.push(2);
    // st.push(3);
    // st.push(4);

    // cout << st.top() << endl;
    // st.pop();
    // cout << st.size() << endl;
    // cout << st.empty() << endl;

    // st.swap(st1);

    // // Queue - is FIFO ----------------------------------------------------------------------------------------

    // queue<int> qu, qu1;
    // qu.push(1);
    // qu.push(2);
    // qu.push(3);
    // qu.push(4);

    // cout << qu.back() << qu.front() << endl;
    // qu.pop();
    // cout << qu.size() << endl;
    // cout << qu.empty() << endl;

    // qu.swap(qu1);

    // Priority Queue - is FIFO ----------------------------------------------------------------------------------------

    // max heap pq
    // priority_queue<int> pq, pq1;
    // pq.push(1);
    // pq.push(4);
    // pq.push(3);
    // pq.push(2);

    // cout << pq.top() << endl;
    // pq.pop();
    // cout << pq.size() << endl;
    // cout << pq.empty() << endl;

    // pq.swap(pq1);

    // min heap pq

    // priority_queue<int, vector<int>, greater<int>> pq;
    // pq.push(4);
    // pq.push(1);
    // pq.push(3);
    // pq.push(2);
    // cout << pq.top() << endl;

    // // Set - Sorted and unique -----------------------------------------------------------------------------------------------
    // set<int> st;
    // st.insert(2);
    // st.emplace(3);
    // st.insert(5);
    // st.insert(4);
    // st.insert(1);
    // st.insert(2);

    // auto it1 = st.find(2);
    // auto it2 = st.find(2);
    // st.find(2);

    // st.erase(it1,it2);
    // cout<<*(it1)<<endl;

    // // MultiSet - similar to Set but duplicates are allowd -------------------------------------------------------------------------------
    // multiset<int> mst;
    // mst.insert(2);
    // mst.emplace(3);
    // mst.insert(5);
    // mst.insert(4);
    // mst.insert(1);
    // mst.insert(2);

    // auto it1 = mst.find(2);
    // auto it2 = mst.find(2);
    // mst.find(2);

    // mst.erase(it1,it2);
    // cout<<*(it1)<<endl;

    // // UnorderedSet - similar to Set but unordered -------------------------------------------------------------------------------
    // unordered_set<int> ust;
    // ust.insert(2);
    // ust.emplace(3);
    // ust.insert(5);
    // ust.insert(4);
    // ust.insert(1);
    // ust.insert(2);

    // auto it1 = ust.find(2);
    // auto it2 = ust.find(2);
    // ust.find(2);

    // ust.erase(it1,it2);
    // cout<<*(it1)<<endl;

    // // Map - key value sort of ---------------------------------------------------------------------------------------------

    // map<int, int> m1;
    // m1[1] = 11;
    // m1[2] = 22;
    // m1[4] = 44;
    // m1[3] = 33;

    // for(auto i : m1){
    //     cout <<"Key: "<< i.first <<"  Value: " <<i.second <<endl;
    // }

    // Multi Map - simimlar to map , only diff is you can store duplicate keys ----------------------------------------------------

    // Unordered  Map - simimlar to map , only diff is you can store in unordered manner -------------------------------------------

    // ALGORITHMS

    // sort

    int n = 5;
    int a[] = {2, 4, 1, 3, 6, 5};

    // sort(a, end(a));
    // sort(a, a+n, greater<int>);

    // customized ordering

    pair<int, int> p1[] = {{1, 2}, {2, 3}, {4, 3}, {1, 3}};

    sort(a, a + 2, comp);
    // sort()
    for (auto i : a)
    {
        cout << i << endl;
    }

    return 0;
}