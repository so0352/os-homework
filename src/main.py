# 食事をする哲学者問題
from Fork import Fork
from Philosopher import Philosopher
import threading
#from simulation_deadlock import simulation
from simulation_semaphore import simulation


if __name__ == "__main__":

    fork = Fork()

    threads = []
    for i in range(5):
        philosopher = Philosopher()
        t = threading.Thread(target=simulation, args=(i, fork, philosopher))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
