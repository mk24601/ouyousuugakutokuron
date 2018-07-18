#!/usr/bin/env python
import random
V = 100 # 縦の長さ
W = 30 # 横の幅

answers = [0,0,0,1,1,1,0,1]#入力000〜111に対する返り値(rule184()内で使用)

def rule184(c1,c2,c3):
    binary = str(c1)+str(c2)+str(c3) # 入力された1/0を結合して文字列に
    return answers[int(binary,2)] # 2進数を10進数に変換し，該当するansweres[]の値を返す

if __name__ == '__main__' :
    cars = []

    # 枠を準備
    for i in range(V):
        cars.append([])

    # 初期値をランダムに設定
    for i in range(W):
        cars[0].append(random.randint(0, 1))

    
    for i in range(1,V):
        for j in range(W):
            if j == 0: # 左端のセルだった場合の処理
                cars[i].append(rule184(cars[i-1][W-1],cars[i-1][0],cars[i-1][1]))
            elif j == W-1: # 右端のセルだった場合の処理
                cars[i].append(rule184(cars[i-1][W-2],cars[i-1][W-1],cars[i-1][0]))
            else: # その他のセルだった場合の処理
                cars[i].append(rule184(cars[i-1][j-1],cars[i-1][j],cars[i-1][j+1]))
    
    # 結果の表示
    for i in range(V):
        for j in range(W):
            if j == W-1:
                print(str(cars[i][j]))
            else:
                print(str(cars[i][j])+",",end = "")