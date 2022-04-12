# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/12 20:33

goods = [(60 ,10) ,(100 ,20) ,(120 ,30)]    # （价格，重量）
goods.sort(key=lambda x: x[0]/x[1] ,reverse = True)     # 根据商品单价排序

def fraction_backpack(goods, w):
    m =[0 for _ in range(len(goods))]
    total_v = 0
    for i,(price,weight) in enumerate(goods):
        if weight < w:
            m[i] = 1
            total_v += price
            w -= weight
        else:
            m[i] = w / weight
            total_v += price * m[i]
            break
    return m ,total_v

print(fraction_backpack(goods,50))