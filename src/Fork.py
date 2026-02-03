from Semaphore import Semaphore


class Fork:
    def __init__(self):
        self._forks = [Semaphore(1) for _ in range(5)]

    def use_fork(self, fork_number: int):
        self._forks[fork_number].P()
        return f"フォーク{fork_number}取得完了"

    def release_fork(self, fork_number: int):
        self._forks[fork_number].V()
        return f"フォーク{fork_number}を手放した"
