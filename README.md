# 食事をする哲学者問題（Dining Philosophers Problem） シミュレーション

## 概要

5人の哲学者が円卓を囲み、思考と食事を繰り返すシミュレーションです。
各哲学者は左右のフォークを両方取得しないと食事ができません。

## ファイル構成

```
src/
├── main.py                 # エントリーポイント
├── Philosopher.py          # 哲学者クラス
├── Fork.py                 # フォーク管理クラス
├── Semaphore.py            # セマフォ実装
├── simulation_deadlock.py  # デッドロック発生版シミュレーション
├── simulation_semaphore.py # セマフォによるデッドロック回避版
└── run.sh                  # 繰り返し実行スクリプト
```

## 実行方法

```bash
cd src
python3 main.py
```

100回繰り返し実行する場合：

```bash
cd src
bash run.sh
```

## デッドロックの切り替え

[src/main.py](src/main.py) のインポート文を変更することで、デッドロック版とセマフォ版を切り替えできます：

```python
# デッドロック版
from simulation_deadlock import simulation

# セマフォによるデッドロック回避版
from simulation_semaphore import simulation
```

## デッドロック回避の仕組み

[src/simulation_semaphore.py](src/simulation_semaphore.py) では、同時に食事できる哲学者の数をセマフォで4人に制限することで、循環待機を防ぎデッドロックを回避しています。

## デッドロック発生例

[deadlock.txt](deadlock.txt) にデッドロックが発生した際のログが記録されています。
全員が左のフォークを取得した後、右のフォークを待ち続けて停止します。
