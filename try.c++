#include<iostream>
using namespace std;
int main(){
    int arr[8]={1,2,5,10,20,50,100,200};
    int query;
    cin>>query;
    int total=0;
    int ans=0;
    for(int i=7;i>=0;i--){
        if(arr[i]+ans>query){
            continue;
        }
        if(query==arr[i]+ans){
            total+=1;
            break;
        }
        if(query>arr[i]+ans){
            total+=1;
            ans+=arr[i];
            i+=1;
        }
    }
    cout<<total;
}
