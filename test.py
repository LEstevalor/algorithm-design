import random
import time

def testall():
    testone(20, 1, 200, 1, 30, 1, 50, 1, 50)


def testone(N, capacity_min, capacity_max, item_count_min, item_count_max, weight_min, weight_max, value_min, value_max):
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0

    item_count = random.randint(item_count_min, item_count_max)

    for i in range(N):
        w = [random.randint(weight_min, weight_max) for _ in range(item_count)]  # 物品重量
        v = [random.randint(value_min, value_max) for _ in range(item_count)]  # 物品价值
        C = random.randint(capacity_min, capacity_max)  # 背包容量

        start_time = time.time()
        dp(C, w, v)
        end_time = time.time()
        result1 += (end_time - start_time)

        start_time = time.time()
        greedy(C, w, v)
        end_time = time.time()
        result2 += (end_time - start_time)

        start_time = time.time()
        backtrack(C, w, v, 0, 0)
        end_time = time.time()
        result3 += (end_time - start_time)

        start_time = time.time()
        dp_v(C, w, v)
        end_time = time.time()
        result4 += (end_time - start_time)

    print("测试次数：{}次".format(N))
    print("DP运行时间：{}ms".format(int(result1 * 1000)))
    print("贪心运行时间：{}ms".format(int(result2 * 1000)))
    print("回溯运行时间：{}ms".format(int(result3 * 1000)))
    print("优化DP运行时间：{}ms".format(int(result4 * 1000)))


def testoa(N, capacity_min, capacity_max, item_count_min, item_count_max, weight_min, weight_max, value_min, value_max, method):
    result1 = 0
    item_count = random.randint(item_count_min, item_count_max)

    for i in range(N):
        w = [random.randint(weight_min, weight_max) for _ in range(item_count)]  # 物品重量
        v = [random.randint(value_min, value_max) for _ in range(item_count)]  # 物品价值
        C = random.randint(capacity_min, capacity_max)  # 背包容量

        start_time = time.time()
        if method == 'dpplus':
            dp_v(C, w, v)
        elif method == 'dp':
            dp(C, w, v)
        elif method == 'greedy':
            greedy(C, w, v)
        elif method == 'backtrack':
            backtrack(C, w, v, 0, 0)
        else:
            raise Exception("方法错误")
        end_time = time.time()
        result1 += (end_time - start_time)

    return int(result1 * 1000)


def test():
    start_time = time.time()
    print("动态规划结果：" + str(dp(4, [1, 3, 4], [15, 20, 30])))
    end_time = time.time()
    print("方法运行时间：%.9f秒" % (end_time - start_time))

    start_time = time.time()
    print("贪心算法结果：" + str(greedy(4, [1, 3, 4], [15, 20, 30])))
    end_time = time.time()
    print("方法运行时间：%.9f秒" % (end_time - start_time))

    start_time = time.time()
    print("回溯法结果：" + str(backtrack(4, [1, 3, 4], [15, 20, 30], 0, 0)))
    end_time = time.time()
    print("方法运行时间：%.9f秒" % (end_time - start_time))

    start_time = time.time()
    print("优化DP结果：" + str(dp_v(4, [1, 3, 4], [15, 20, 30])))
    end_time = time.time()
    print("方法运行时间：%.9f秒" % (end_time - start_time))


def dp(capacity, w, v):
    """动态规划解决0-1背包
    :arg
        capacity: 背包容量
        w: 物体重量
        v: 物体体积

    :returns 容量capacity下背包装入物品最优解
        Integer
    """
    # 物品数
    n = len(w)
    # dp[i][j]中i代表第几个背包（显然这里i = 0无意义），j代表当前重量
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # 遍历，从前往后、从左到右
    # 外层：遍历n个物品
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= w[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]


def dp_v(capacity, w, v):
    """动态规划解决0-1背包
    :arg
        capacity: 背包容量
        w: 物体重量
        v: 物体体积

    :returns 容量capacity下背包装入物品最优解
        Integer
    """
    # 物品数
    n = len(w)
    # dp[i][j]中i代表第几个背包（显然这里i = 0无意义），j代表当前重量
    dp = [0 for _ in range(capacity + 1)]

    # 遍历，从前往后、从左到右
    # 外层：遍历n个物品
    for i in range(1, n + 1):
        for j in range(capacity, 0, -1):
            if j >= w[i - 1]:
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])

    return dp[capacity]


def greedy(capacity, w, v):
    """贪心算法解决0-1背包
    :arg
        capacity: 背包容量
        w: 物体重量
        v: 物体体积

    :returns 容量capacity下背包装入物品贪心解
        Integer
    """
    # 以价值向量v为依据排序，w随之索引位移动
    # 先创建一个索引数值
    indexs = list(range(len(v)))
    # 然后按以v为依据，对应索引数组变动
    indexs.sort(key=lambda x: v[0] - v[x])  # v[x]-v[0]则从小到大

    result = 0  # 记录结果
    for index in indexs:
        if capacity >= w[index]:
            capacity -= w[index]
            result += v[index]

    return result


def backtrack(capacity, w, v, index, result):
    """回溯法解决0-1背包
    :arg
        capacity: 背包容量
        w: 物体重量
        v: 物体体积
        index: 当前索引
        result: 上一个索引传递过来的结果值

    :returns 容量capacity下被使用容量的背包装入物品的价值
        Integer
    """
    cur_result = result
    for i in range(index, len(w) - 1):
        if capacity >= w[index]:
            cur_result = max(cur_result,
                             backtrack(capacity - w[index], w, v, i + 1, result + v[i]))

    return cur_result
