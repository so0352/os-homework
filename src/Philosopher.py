class Philosopher:
    def __init__(self):
        # 左フォーク、右フォークの番号の組み合わせ
        self._fork_number_to_use = [(0, 4), (1, 0), (2, 1), (3, 2), (4, 3)]
        # 考え事の数 => 0 になったら終了
        self._think_task = 3

    def get_fork_number_to_use(self, philosopher_num: int):
        return self._fork_number_to_use[philosopher_num]

    def get_think_task(self):
        return self._think_task

    # 哲学者がランダムな時間考えたあと、考え事の数を1つ減らす
    def think(self, philosopher_id):
        print(f"哲学者{philosopher_id}: 思考する")
        print(f"哲学者{philosopher_id}: 思考終了")
        self._think_task -= 1
        print(f"哲学者{philosopher_id}: 残り考え事数: {self._think_task}")

    # 哲学者がランダムな時間食事をする
    def eat(self, philosopher_id):
        print(f"哲学者{philosopher_id}: 食べる")
        print(f"哲学者{philosopher_id}: 食べ終わった")
