#include <stdio.h>
#include <iostream>
using namespace std;
bool FINISH_FLAG = false;


string snow(int n){
    if ((n/2)<=1 && (n%2)<=1)
        return (to_string(n/2) +to_string(n%2) + to_string(n/2));
    else
        
};

int main(){
    
    int n, l, r;
    string new_num, a;
    
    scanf("%d%d%d",&n,&l,&r);
    string ohshit=to_string(n);
    int count = 0;
    while(true){
        if ( count == 3)
            break;
        for (int i = 0; i< ohshit.length();i++){
            if (int(ohshit.at(i)) >1)
                break;
            if (i ==ohshit.length()-1)
                 FINISH_FLAG = true;
            
        }
        
        if (FINISH_FLAG == true)
                   break;
        if (stoi(ohshit) == n){
            ohshit = snow(stoi(ohshit));
        }
        else{
            a = ohshit.at(0);
            new_num = snow(stoi(a));
            
            ohshit = new_num + ohshit.substr(ohshit.length()/2) + new_num;
            
        }
        cout << ohshit<<endl;
        count++;
        
        
    }
    
    
    
    
    
    
}
