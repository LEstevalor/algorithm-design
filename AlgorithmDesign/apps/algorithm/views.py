from rest_framework.response import Response
from rest_framework.views import APIView
from test import testoa, dp, dp_v, greedy, backtrack
import ast


# Create your views here.
class CaculateView(APIView):
    """
    计算方法
    """
    def post(self, request, method):
        capacity = int(request.data["capacity"])
        value = request.data["value"]
        number = int(request.data["number"])
        weight = request.data["weight"]
        value = ast.literal_eval("[" + value + "]")
        weight = ast.literal_eval("[" + weight + "]")
        # print(weight)
        # print(value)
        # print(number)
        # print(len(weight))
        # print(len(value))
        # print(type(weight))
        # print(len(weight) != len(value))
        # print(len(weight) != number)

        if len(weight) != len(value) or len(weight) != number:
            raise Exception("数据传入有误")

        if method == 'dpplus':
            res = dp_v(capacity, weight, value)
        elif method == 'dp':
            res = dp(capacity, weight, value)
        elif method == 'greedy':
            res = greedy(capacity, weight, value)
        elif method == 'backtrack':
            res = backtrack(capacity, weight, value, 0, 0)
        else:
            raise Exception("方法错误")

        print(res)

        return Response({"res": res})


class CaculateTestView(APIView):
    """
    测试运行时间
    """
    def post(self, request, method):
        testNumber = int(request.data["testNumber"])
        capacityMax = int(request.data["capacityMax"])
        capacityMin = int(request.data["capacityMin"])
        valueMax = int(request.data["valueMax"])
        valueMin = int(request.data["valueMin"])
        numberMax = int(request.data["numberMax"])
        numberMin = int(request.data["numberMin"])
        weightMin = int(request.data["weightMin"])
        weightMax = int(request.data["weightMax"])

        if weightMin > weightMax or numberMin > numberMax or valueMin > valueMax or capacityMin > capacityMax:
            raise Exception("数据传入有误")

        res = testoa(testNumber, capacityMin, capacityMax, numberMin, numberMax,
                      weightMin, weightMax, valueMin, valueMax, method)

        return Response({"res": "测试次数：{}次，运行时间为{}ms".format(testNumber, res)})
