def my_find_outlier(integers):
    arr = list(map(lambda x: x % 2 == 0, integers))
    idx = arr.index(False) if arr.count(True) > arr.count(False) else arr.index(True)
    return integers[idx]

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

# 베스트가 훨씬 보기 깔끔하다.