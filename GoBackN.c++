#include<bits/stdc++.h>
#include<ctime>
#define ll long long int

using namespace std;

void transmission(ll &i,ll &N, ll &tf, ll &tt)
{
    while(i<=tf)
    {
        int z=0;
        for(int k=i;k<i+N&&k<=tf;k++)
        {
            cout<<"Sending frame "<<k<<"...."<<endl;
            tt++;
        }

        for(int k=i;k<i+N&&k<=tf;k++)
        {
            int f=rand()%2;
            if(!f)
            {
                cout<<"Acknoledgement for frame "<<k<<"...."<<endl;
                z++;
            }
            else
            {
                cout<<"Timeout! Frame number "<<k<<" not rcieved"<<endl;
                cout<<"Retransmitting Window ...."<<endl;
                break;
            }
        }

        cout<<endl;
        i+=z;
    }
}

int main()
{
    ll tf,N,tt=0;
    srand(time(NULL));

    cout<<"Enter the total number of frames : ";
    cin>>tf;
    cout<<"enter the window size : ";
    cin>>N;
    ll i=1;

    transmission(i,N,tf,tt);

    cout<<"Total number of frames which were sent and resent are : "<<tt<<endl;

    return 0;
}