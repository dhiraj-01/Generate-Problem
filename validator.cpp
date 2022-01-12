#include <bits/stdc++.h>
using namespace std;

using ll = long long int;
#define endl '\n'

template <typename T1, typename T2, typename T3>
void ok(T1 l, T2 r, T3 n) {
    assert(((T3)(l)) <= n and n <= ((T3)(r)));
}

void solve(ll &tc)
{
    ll t;
    cin >> t;
    ok(1, 10, t);
    for(ll rep = 0; rep < t; rep++)
    {
        ll a, b;
        cin >> a >> b;
        ok(1, 10, a);
        ok(1, 10, b);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll tc = 1;
    for(ll i = 1; i <= tc; i++) {
        solve(i);
    }
    return 0;
}