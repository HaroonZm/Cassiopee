code="""
#include <iostream>
#include <algorithm>
#include <array>
#include <vector>
using namespace std;

#define dump(...) cout<<"# "<<#__VA_ARGS__<<'='<<(__VA_ARGS__)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

constexpr int INF=1e9;
constexpr int MOD=1e9+7;
constexpr double EPS=1e-9;

int dfs(const vvi& g,int u)
{
	int res=1<<u;
	for(int v:g[u]) res|=dfs(g,v);
	return res;
}

int main()
{
	for(int n,m;cin>>n>>m && n|m;){
		array<int,20> cs;
		vvi g(n);
		rep(i,n){
			cin>>cs[i];
			int k; cin>>k;
			rep(j,k){
				int r; cin>>r;
				g[i].push_back(r);
			}
		}

		array<int,20> bs;
		rep(i,n) bs[i]=dfs(g,i);

		static array<int,1<<20> sums; sums.fill(0);

		rep(i,n) sums[1<<i]=cs[i];
		rep(i,1<<n) sums[i]=sums[i&-i]+sums[i-(i&-i)];

		int res=INF;
		rep(i,1<<n) if(__builtin_popcount(i)<res){
			int b=0;
			rep(j,n) b|=(i>>j&1)*bs[j];
			if(sums[b]>=m) res=min(res,__builtin_popcount(b));
		}
		cout<<res<<endl;
	}
}
"""

import os,tempfile
(_,filename)=tempfile.mkstemp(".cpp")

f=open(filename,"w")
f.write(code)
f.close()

os.system("g++ -std=c++0x {} -o ./a.out".format(filename))
os.system("./a.out")