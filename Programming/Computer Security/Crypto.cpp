#include<bits/stdc++.h>
using namespace std;

 long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0)
    {
        if(b & 1)
            res = res * a % m;
        a = a * a %m;
        b >>= 1;

    }
    return res;

}

int main() {

   #ifndef ONLINE_JUDGE

		freopen("input.txt", "r", stdin);

		freopen("output.txt", "w", stdout);

	#endif

    long long p, q, a;
    cin>>p >> q;

   long long n = p * q;
   long long z = (p-1) * (q-1), d, e;

   for(long long i = 2;  ; i++){
    if(__gcd(i, z) == 1) {
        d = i;
        break;
    }

   }
   for(long long i = 2; ; i++) {
    if((i*d) % z == 1){
        e = i;
        break;
    }
   }
  
  cout<<p<<endl;
  cout<<q<<endl;
  cout<<n<<endl;
  cout<<z<<endl;
  cout<<d<<endl;
  cout<<e<<endl;

    long long plain = 26;

    long long c = binpow(plain, e, n);
  cout<<"value of c " <<c<<endl;

    long long org = binpow(c, d, n);
    cout<<"orginal value " << org<<endl;


}
