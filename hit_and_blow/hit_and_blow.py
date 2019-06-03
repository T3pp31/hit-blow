import random
a=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]#4桁の数字を生成
print(str(a[0])+str(a[1])+str(a[2])+str(a[3])) #念のため答え表示（制作過程で必要なため、運用時は削除）
while True: #４桁の数字になっているかを判定。
    isok=False
    while isok==False:
        b=input("数をいれてね>")
        if len(b)!=4:
            print("４桁の数字を入力してください>")
        else:
            kazuok=True
            for i in range(4):
                if(b[i]<"0")or(b[1]>"9"):
                    print("数字ではありません")
                    kazuok=False
                    break
                if kazuok:
                    isok=True
    hit=0 #hitかblowかを判定。
    for i in range(4):
        if a[i]==int(b[i]):
            hit=hit+1
    blow=0
    for j in range(4):
        for i in range(4):
            if int(b[j]) ==a[i]and a[i]!=int(b[i]) and a[j]!=int(b[j]):
                blow=blow+1
                break
                
    print("ヒット"+str(hit))
    print("ブロー"+str(blow))
    
    if hit==4: #すべて当たったら終了
        print("あたり")
        break