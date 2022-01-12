#include <bits/stdc++.h>
using namespace std;

using ll = long long int;
#define endl '\n'

void solve(ll &tc)
{
    ll a, b;
    cin >> a >> b;
    cout << a + b << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll tc = 1;
    cin >> tc;
    for(ll i = 1; i <= tc; i++) {
        solve(i);
    }
    return 0;
}