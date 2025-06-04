# Importation des modules nécessaires
import os          # Permet d'interagir avec le système d'exploitation, ici pour compiler et exécuter des fichiers
import tempfile    # Utilisé ici pour créer un fichier temporaire de manière sécurisée

# Définition d'une variable contenant le code source C++ sous forme de chaîne de caractères, délimitée par trois guillemets pour permettre du texte multiligne.
code = """
#include <bits/stdc++.h>
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

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}

template<typename Tuple>
void print_tuple(ostream&,const Tuple&){}
template<typename Car,typename... Cdr,typename Tuple>
void print_tuple(ostream& os,const Tuple& t){
	print_tuple<Cdr...>(os,t);
	os<<(sizeof...(Cdr)?",":"")<<get<sizeof...(Cdr)>(t);
}
template<typename... Args>
ostream& operator<<(ostream& os,const tuple<Args...>& t){
	print_tuple<Args...>(os<<'(',t);
	return os<<')';
}

template<typename Ch,typename Tr,typename C,typename=decltype(begin(C()))>
basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>& os,const C& c){
	os<<'[';
	for(auto i=begin(c);i!=end(c);++i)
		os<<(i==begin(c)?"":" ")<<*i;
	return os<<']';
}

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

# Création d'un fichier temporaire
# La fonction mkstemp retourne un tuple (file descriptor, chemin du fichier)
# Le suffixe ".cpp" indique qu'il s'agit d'un fichier source C++
(_, filename) = tempfile.mkstemp(".cpp")

# Ouverture du fichier temporaire en mode écriture (par défaut, c'est du texte)
f = open(filename, "w")
# On écrit le contenu de la variable 'code' (donc le code source C++) dans le fichier temporaire
f.write(code)
# On ferme le fichier pour s'assurer que toutes les données sont vraiment écrites sur disque
f.close()

# Compilation du fichier source C++ à l'aide du compilateur 'g++' en spécifiant le fichier source et l'exécutable résultant
# L'option -std=c++0x exige au compilateur d'utiliser au minimum la norme C++11 (c++0x était une notation préliminaire)
os.system("g++ -std=c++0x {} -o ./a.out".format(filename))
# Exécution du programme compilé, le fichier exécutable est './a.out'
os.system("./a.out")