import random
import linecache

def LuckyDraw(cnt):
    Randomlist = []
    LuckyDogList = []

    people = int(input("请输入中奖人数:"))
    Randomlist = random.sample(range(1, cnt), people)  # 从[1 ~ 总数]中随机抽people个人，不重复
    # print(Randomlist)
    for i in Randomlist:
        LuckyDogList.append(linecache.getline('./抽奖池.txt', i))
    # pprint.pprint(LuckyDogList)
    with open('./中奖人员名单.txt', 'w', encoding='utf-8') as f:
        for index in LuckyDogList:
            f.write('UID: ' + ''.join(index))
    print("---抽奖结束---")

if __name__ == "__main__":
    count = len(open(r'./抽奖池.txt', 'r', encoding='utf-8').readlines())
    # print(count)
    LuckyDraw(count)
