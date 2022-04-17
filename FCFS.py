# 선입선처리(FCFS) 스케줄링 알고리즘

def fcfs(bursts, arrivals):
    wait_time = [] # 대기 시간
    turn_time = [] # 반환 시간

    # 대기 시간 = n-1 까지의 실행 시간 - n의 도착 시간
    wait_time.append(0) # 첫 프로세스는 대기시간이 0초
    turn_time.append(bursts[0]) # 첫 프로세스의 반환 시간(=실행 시간) 추가
    for i in range(1, len(bursts)):
        count = i
        result = 0
        while count > 0:
            result += bursts[count - 1]
            count -= 1
        wait_time.append(result - arrivals[i])
    # 반환 시간 = n의 실행 시간 + 대기 시간 (= n까지의 실행 시간 - n의 대기 시간)
        turn_time.append(bursts[i] + (result - arrivals[i]))

    return wait_time, turn_time


if __name__ == '__main__':
    processes = [1, 2, 3, 4, 5] # process id
    burst_time = [10, 28, 6, 4, 14] # 실행 시간
    arrival_time = [0, 1, 2, 3, 4] # 도착 시간

    n = len(processes)

    w, t = fcfs(burst_time, arrival_time)
    print(f"process ID\t\t: {processes}")
    print(f"Burst_시간\t\t: {burst_time}")
    print(f"Waiting_시간\t\t: {w}")
    print(f"Turn_Around_시간\t: {t}")
    print(f"평균 waiting 시간\t: {sum(w) / n}")
    print(f"평균 turn around 시간\t: {sum(t) / n}")