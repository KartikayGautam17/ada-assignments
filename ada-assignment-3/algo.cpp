#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int steps = 0;
int BinarySearch_r(vector<int> &v,int l,int r,int x){
    steps++;
    if (l > r) return -1;
    int mid = (l+r)/2;
    if (v[mid] == x) return x;
    else if (v[mid] < x) return BinarySearch_r(v,mid+1,r,x);
    else return BinarySearch_r(v,l,mid-1,x);
}

int main (){
    vector<int> inputs = {10,50,100,500,1000,5000};
    for (auto x:inputs){
        vector<int> temp(x);
        for (int i = 0;i<x;i++){
            temp[i] = i;
        }
        steps = 0;
        int avg_target = temp[rand()%x];
        cout << avg_target << endl;
        int best_target = temp[(x-1)/2];
        int worst_target = 0;
        cout << "size -: " << x << endl;
        BinarySearch_r(temp,0,x-1,best_target);
        cout << "best -: " << steps << endl;
        steps = 0;
        BinarySearch_r(temp,0,x-1,avg_target);
        cout << "avg -: " << steps << endl;
        steps = 0;
        BinarySearch_r(temp,0,x-1,worst_target);
        cout << "worst -: " << steps << endl;
    }
}