tsp_exact.pyは厳密解を，tsp_approximate.pyは近似解を求めるコードである。計算量の問題から，tsp_exact.pyはinput_3.csv（N＝64）以降は使えない （後で詳しく述べる）。

## 共通の関数

## read_input_file

input_{x}.csvファイルを読み込み，座標をcitiesという配列に入れる関数。

## write_output_file

output_{x}.csvファイルにノードを訪れる順番を書き込む関数。

## distance

2つのノード間の距離を求める関数。

## distance_matrix

```python
dist[i][j] = ノードiとノードjの間の距離
```
となるような配列を作る関数

---

# tsp_exact.py

## dfs

動的計画法を用いる。
```python
dp[S][city_now] = 部分集合Sに含まれるノードにすでに訪問済みであり，今city_nowにいる時，一周してノード0に戻るのに必要な残りの最短距離
```
この時，部分集合Sはbitで表す。n番目のbitが1ならこの部分集合はノードnを含むと考える。

例）
<img src="Google Step-9.jpg">

Sのn番目のbitが0ならノードnは未訪問なので，


## 

# tsp_approximate.py

近似解を求める。