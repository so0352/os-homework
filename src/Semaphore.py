import threading


class Semaphore:
    """セマフォ（カウンティングセマフォ）"""

    def __init__(self, value: int = 1):
        self._value = value
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)

    def P(self, philosopher_id: int = None):
        """P操作（wait操作）: セマフォの値を1減らす。0なら待機"""
        with self._condition:
            while self._value == 0:
                self._condition.wait()
            self._value -= 1
            if philosopher_id is not None:
                print(
                    f"哲学者{philosopher_id}: セマフォ取得 (制御セマフォ値: {self._value})"
                )

    def V(self, philosopher_id: int = None):
        """V操作（signal操作）: セマフォの値を1増やす。待機中のスレッドを起こす"""
        with self._condition:
            self._value += 1
            if philosopher_id is not None:
                print(
                    f"哲学者{philosopher_id}: セマフォ解放 (制御セマフォ値: {self._value})"
                )
            self._condition.notify()

    @property
    def value(self):
        """現在のセマフォの値を取得"""
        with self._lock:
            return self._value
