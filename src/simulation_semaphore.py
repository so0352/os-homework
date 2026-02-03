from Fork import Fork
from Philosopher import Philosopher
import threading
from Semaphore import Semaphore

# 全員が揃うまで待機するバリア
barrier = threading.Barrier(5)

# 哲学者が同時に食事できる人数を管理する
can_eat_philosopher_num = Semaphore(4)


def simulation(philosopher_id: int, fork: Fork, philosopher: Philosopher):
    left_fork, right_fork = philosopher.get_fork_number_to_use(philosopher_id)

    print(f"哲学者{philosopher_id}: 準備完了、他の哲学者を待っています...")

    # 全員が揃うまで待機
    barrier.wait()

    # 考え事(think_task)がある間繰り返す
    while True:
        # 思考する
        philosopher.think(philosopher_id)

        # 考え事が残っているか確認
        if philosopher.get_think_task() == 0:
            print(f"哲学者{philosopher_id}: 考え事がなくなった、終了")
            break
        # 食事できるかセマフォに確認
        can_eat_philosopher_num.P(philosopher_id=philosopher_id)

        # 左のフォークを取る
        print(f"哲学者{philosopher_id}: フォーク{left_fork}を取ろうとしている...")
        fork.use_fork(left_fork)
        print(f"哲学者{philosopher_id}: フォーク{left_fork}の取得完了")

        # 右のフォークを取る
        print(f"哲学者{philosopher_id}: フォーク{right_fork}を取ろうとしている...")
        fork.use_fork(right_fork)
        print(f"哲学者{philosopher_id}: フォーク{right_fork}の取得完了")

        # 食事する
        print(f"哲学者{philosopher_id}: 食事中...")
        philosopher.eat(philosopher_id)

        print(f"哲学者{philosopher_id}: 食事終了")

        # 右のフォークを置く
        print(f"哲学者{philosopher_id}: フォーク{right_fork}を置く")
        fork.release_fork(right_fork)
        print(f"哲学者{philosopher_id}: フォーク{right_fork}を置けた")

        # 左のフォークを置く
        print(f"哲学者{philosopher_id}: フォーク{left_fork}を置く")
        fork.release_fork(left_fork)
        print(f"哲学者{philosopher_id}: フォーク{left_fork}を置けた")

        # セマフォを解放
        can_eat_philosopher_num.V(philosopher_id=philosopher_id)
