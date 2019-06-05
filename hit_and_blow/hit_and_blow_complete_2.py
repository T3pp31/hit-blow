import random      
import tkinter as tk       
import tkinter.messagebox as tmsg    

def ButtonClick():
    b=editboxl.get()
    
    isok=False
    if len(b)!=4:
        tmsg.showerror("エラー","4桁の数字を入力してください")
    else:
        kazuok=True
        for i in range(4):
            if b[i]<"0" or b[i]>"9" :
                tmsg.showerror("エラー","数字ではありません")
                kazuok=False
                break
        if kazuok:
            isok=True
    
    if isok:
        hit=0
        for i in range(4):
            if a[i]==int(b[i]):
                hit=hit+1
                
        blow=0
        for j in range(4):
            for i in range(4):
                if int(b[j])==a[i] and a[i]!= int(b[i]) and a[j]!=int(b[j]):
                    blow=blow+1
                    break
                
        if hit==4:
            tmsg.showinfo("当たり","おめでとうございます。正解です")
            root.destroy()
        else:
            tmsg.showinfo("ヒント","ヒット"+str(hit)+"/"+"ブロー"+str(blow))
            rireki.insert(tk.END,b+"/H:"+str(hit)+"B:"+str(blow)+"\n")
            
a=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
#ウィンドウ作成
root=tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")
#ラベル作成
labell=tk.Label(root,text="数を入力してください→", font=("Helvetica",10))
labell.place(x=20,y=20)

editboxl=tk.Entry(width=9,font=("Helventica",14))
editboxl.place(x=175,y=20)
#ボタン作成&応答
button1=tk.Button(root,text="チェック",font=("Helvetica",10), command=ButtonClick)
button1.place(x=275,y=20)
#履歴表の作成
rireki=tk.Text(root,font=("Helventica",14))
rireki.place(x=400,y=0,width=200,height=400)






root.mainloop()