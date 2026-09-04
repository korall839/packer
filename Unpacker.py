from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import threading,sys,ast,os,signal

def Packer(whole1):
        agents=[]
        beckup={}
        agentsNumber=[1,0,0]
        def agent(number,whole,thisAgent,r,l,i):
            new_agent=[]
            if not(whole is None) and len(whole) >= i:
                print("эээ 67?")
                for y in range(i,len(whole)):
                        print(1)
                        if len(r) % 2 == 1:
                            if str(whole)[y] != " " or y == 1:
                                r+=str(whole)[y]
                                if not(r in thisAgent):
                                    thisAgent.append(r)
                                if l[-1] == '|' or l[-1] == '_':
                                    pass
                                else:
                                    l+=','
                                k=0
                                for i in range(len(thisAgent)):
                                    if k == 1:
                                        pass
                                    elif thisAgent[i] == r:
                                        l+=str(i+1)
                                        k=1
                            else:
                                def agent1(number,whole,thisAgent,r,l,i):
                                    if not(whole is None) and len(whole) >= i:
                                        print("эээ 67?")
                                        for y in range(i,len(whole)):
                                            if i+20 >= y:
                                                t.append(len(thisAgent)+len(thisAgent[-1])-1)
                                                break
                                            if len(r) % 2 == 1:
                                                r+=str(whole)[y]
                                                if not(r in thisAgent):
                                                    thisAgent.append(r)
                                                if l[-1] == '|':
                                                    pass
                                                else:
                                                    l+=','
                                                k=0
                                                for i in range(len(thisAgent)):
                                                    if k == 1:
                                                        pass
                                                    elif thisAgent[i] == r:
                                                        l+=str(i+1)
                                                        k=1
                                            else:
                                                r+=str(whole)[y]
                                            print("номер агента: ",number)
                                            print("целое: ",whole)
                                            print("Len: ",thisAgent)
                                            print("Num: ",l)
                                            print("буфер: ",r)
                                            print("интерация: ",y)
                                        if r != "":
                                            y+=1
                                            r+=" "
                                            thisAgent.append(r)
                                            l+=','
                                            k=0
                                            for i in range(len(thisAgent)):
                                                if k == 1:
                                                    pass
                                                elif thisAgent[i] == r:
                                                    l+=str(i+1)
                                                    k=1
                                            l+="-"
                                        r=l
                                        thisAgent.append(r)
                                    print(f"агент {number} завершил работу")
                                    t.append(len(thisAgent)+len(thisAgent[-1])-1)
                                t=[]
                                if len(whole) >= y+2:
                                    agentsNumber[0]+=1
                                    q=[whole[:],thisAgent[:],l,r]
                                    beckup[number-1]=q
                                    new_thisAgent=thisAgent[:]
                                    k=0
                                    for i in range(len(thisAgent)):
                                        if k == 1:
                                                pass
                                        elif thisAgent[i] == str(whole)[y-1]+str(whole)[y+1]:
                                            l2=str(i//2+1)
                                            k=1
                                    if not(str(whole)[y-1]+str(whole)[y+1] in thisAgent):
                                        new_thisAgent.append(str(whole)[y-1]+str(whole)[y+1])
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,thisAgent,r,l,y)))
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},{len(new_thisAgent)}_{len(new_thisAgent)}",y+2)))
                                        new_agent[-1].start()
                                        new_agent[-2].start()
                                        for i in range(len(new_agent)):
                                            new_agent[i].join()
                                        q=beckup[number-1]
                                        whole=q[0][:]
                                        thisAgent=q[1][:]
                                        l=q[2]
                                        r=q[3]
                                        if t[-1] > t[-2]:
                                            l=f"{l},{len(thisAgent)}_"
                                            r+=str(whole)[y]
                                        else:
                                            r+=str(whole)[y]
                                    else:
                                        new_thisAgent.append(str(whole)[y+1]+str(whole)[y+2])
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,thisAgent,r,l,y)))
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},{l2}_{l2}",y+2)))
                                        new_agent[-1].start()
                                        new_agent[-2].start()
                                        for i in range(len(new_agent)):
                                            new_agent[i].join()
                                        q=beckup[number-1]
                                        whole=q[0][:]
                                        thisAgent=q[1][:]
                                        l=q[2]
                                        r=q[3]
                                        if t[-1] > t[-2]:
                                            l=f"{l},{l2}_"
                                            r+=str(whole)[y]
                                        else:
                                            r+=str(whole)[y]
                                if not(r in thisAgent):
                                    thisAgent.append(r)
                                if l[-1] == '|' or l[-1] == '_':
                                    pass
                                else:
                                    l+=','
                                k=0
                                for i in range(len(thisAgent)):
                                    if k == 1:
                                        pass
                                    elif thisAgent[i] == r:
                                        l+=str(i+1)
                                        k=1
                            r=""
                        else:
                            if str(whole)[y] != " " or y == 0:
                                r+=str(whole)[y]
                            else:
                                def agent1(number,whole,thisAgent,r,l,i):
                                    if not(whole is None) and len(whole) >= i:
                                        print("эээ 67?")
                                        for y in range(i,len(whole)):
                                            if i+20 == y:
                                                t.append(len(thisAgent)+len(thisAgent[-1])-1)
                                                break
                                            if len(r) % 2 == 1:
                                                r+=str(whole)[y]
                                                if not(r in thisAgent):
                                                    thisAgent.append(r)
                                                if l[-1] == '|':
                                                    pass
                                                else:
                                                    l+=','
                                                k=0
                                                for i in range(len(thisAgent)):
                                                    if k == 1:
                                                        pass
                                                    elif thisAgent[i] == r:
                                                        l+=str(i+1)
                                                        k=1
                                            else:
                                                r+=str(whole)[y]
                                            print("номер агента: ",number)
                                            print("целое: ",whole)
                                            print("Len: ",thisAgent)
                                            print("Num: ",l)
                                            print("буфер: ",r)
                                            print("интерация: ",y)
                                        if r != "":
                                            y+=1
                                            r+=" "
                                            thisAgent.append(r)
                                            l+=','
                                            k=0
                                            for i in range(len(thisAgent)):
                                                if k == 1:
                                                    pass
                                                elif thisAgent[i] == r:
                                                    l+=str(i+1)
                                                    k=1
                                            l+="-"
                                        r=l
                                        thisAgent.append(r)
                                    print(f"агент {number} завершил работу")
                                    t.append(len(thisAgent)+len(thisAgent[-1])-1)
                                t=[]
                                if len(whole) >= y+3:
                                    agentsNumber[0]+=1
                                    q=[whole[:],thisAgent[:],l,r]
                                    beckup[number-1]=q
                                    new_thisAgent=thisAgent[:]
                                    k=0
                                    for i in range(len(thisAgent)):
                                        if k == 1:
                                                pass
                                        elif thisAgent[i] == str(whole)[y+1]+str(whole)[y+2]:
                                            l2=str(i//2+1)
                                            k=1
                                    if not(str(whole)[y+1]+str(whole)[y+2] in thisAgent):
                                        new_thisAgent.append(str(whole)[y+1]+str(whole)[y+2])
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,thisAgent,r,l,y)))
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},_{len(new_thisAgent)}",y+3)))
                                        new_agent[-1].start()
                                        new_agent[-2].start()
                                        for i in range(len(new_agent)):
                                            new_agent[i].join()
                                        q=beckup[number-1]
                                        whole=q[0][:]
                                        thisAgent=q[1][:]
                                        l=q[2]
                                        r=q[3]
                                        if t[-1] > t[-2]:
                                            if l == "\n":
                                                l=f"{l}~,_"
                                            else:
                                                l=f"{l},_"
                                            r+=str(whole)[y]
                                        else:
                                            r+=str(whole)[y]
                                    else:
                                        new_thisAgent.append(str(whole)[y+1]+str(whole)[y+2])
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,thisAgent,r,l,y)))
                                        new_agent.append(threading.Thread(target=agent1, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},_{l2}",y+3)))
                                        new_agent[-1].start()
                                        new_agent[-2].start()
                                        for i in range(len(new_agent)):
                                            new_agent[i].join()
                                        q=beckup[number-1]
                                        whole=q[0][:]
                                        thisAgent=q[1][:]
                                        l=q[2]
                                        r=q[3]
                                        if t[-1] > t[-2]:
                                            if l == "\n":
                                                l=f"{l}~,_"
                                            else:
                                                l=f"{l},_"
                                            r+=str(whole)[y]
                                        else:
                                            r+=str(whole)[y]
                        print("номер агента: ",number)
                        print("целое: ",whole)
                        print("Len: ",thisAgent)
                        print("Num: ",l)
                        print("буфер: ",r)
                        print("интерация: ",y)
                if agents == []:
                        agentsNumber[1]=number
                if r != "":
                    y+=1
                    r+=" "
                    thisAgent.append(r)
                    l+=','
                    k=0
                    for i in range(len(thisAgent)):
                        if k == 1:
                            pass
                        elif thisAgent[i] == r:
                            l+=str(i+1)
                            k=1
                    l+="-"
                r=l
                thisAgent.append(r)
                agents.append(thisAgent)
            print(f"агент {number} завершил работу")
            if new_agent != []:
                for i in range(len(new_agent)):
                    new_agent[i].join()
        agent(1,whole1,[],'','|',0)
        print('пул агентов:',agents)
        print('всего агентов:',agentsNumber[0])
        print('результат от агента №',agentsNumber[1])
        print('агентов закончевших принудительно:',agentsNumber[2])
        print('ожидаемый результат:',agents[0])
        return agents[0]
def Unpacker(whole):
    print(len(whole))
    per_len,per_int=whole[:-1] , whole[-1]
    strs= per_len
    nums= per_int.replace('|','').split(",")
    print(strs)
    print(nums)
    print(per_int)
    result =[]
    for num in nums:
        if "_" in num:
            if num[0] == "_":
                if num[-1] == "-" or (num[-1] == "~" and num[-2] == "-"):
                    whole=strs[int(num.replace("-","").replace("_","").replace("~",""))-1]
                    if num[-1] == "~":
                        lens=whole[0]
                        lens=whole[1]
                    else:
                        lens=whole[0]
                    result.append(" "+lens)
                elif num[-1] == "+" or (num[-1] == "~" and num[-2] == "+"):
                    whole=strs[int(num.replace("+","").replace("_","").replace("~",""))-1]
                    if num[-1] == "~":
                        lens=whole[1]
                        lens=whole[2]
                    else:
                        lens=whole[1]
                    result.append(" "+lens)
                else:
                    result.append(" "+strs[int(num.replace("_",""))-1])
            else:
                lens1,crop1=num.split("_")
                if lens1[-1] == "+" or (lens1[-1] == "~" and lens1[-2] == "+"):
                    whole1=strs[int(lens1.replace("+","").replace("~",""))-1]
                    if lens1[-1] == "~":
                        lens2=whole1[1]
                        lens2=whole1[2]
                    else:
                        lens2=whole1[1]
                else:
                    whole1=strs[int(lens1.replace("-","").replace("~",""))-1]
                    if lens1[-1] == "~":
                        lens2=whole1[0]
                        lens2=whole1[1]
                    else:
                        lens2=whole1[0]
                if crop1[-1] == "-":
                    whole2=strs[int(crop1.replace("-","").replace("~",""))-1]
                    if crop1[-1] == "~":
                        crop2=whole2[0]
                        crop2=whole2[1]
                    else:
                        crop2=whole2[0]
                else:
                    whole2=strs[int(crop1.replace("+","").replace("~",""))-1]
                    if crop1[-1] == "~":
                        crop2=whole2[1]
                        crop2=whole2[2]
                    else:
                        crop2=whole2[1]
                result.append(lens2+" "+crop2)
        else:
            if num[-1] == "-":
                    whole=strs[int(num.replace("-",""))-1]
                    lens=whole[0]
                    result.append(lens)
            elif num[-1] == "+":
                    whole=strs[int(num.replace("+",""))-1]
                    lens=whole[1]
                    result.append(lens)
            else:
                print(num)
                result.append(strs[int(num)-1])
    return "".join(result)
class MainScreen(App):
    def bysya_shitaet_file(self,window,file_path,x,y):
        if os.path.splitext(file_path.decode('utf-8'))[1] == '.lenu':
            path_str=file_path.decode('utf-8')
            self.d=path_str
            with open(path_str,'r') as r:
                local=ast.literal_eval(r.read())
                print(type(local))
                print(local)
                self.c=str(Unpacker(local))
                print(self.c)
                self.a.text=str((str(self.c)).encode("utf-8"))
        else:
            path_str=file_path.decode('utf-8')
            self.d=path_str
            with open(path_str,'r') as r:
                local=r.read()
                self.c=str(local)
                print(self.c)
                self.a.text=self.c
    def bysya_zapisuvaet_file(self,*args):
        if os.path.splitext(self.d)[1] == '.lenu':
            with open(os.path.splitext(self.d)[0],'wb') as r:
                r.write(bytes(self.c.encode('utf-8')))
        else:
            output_pyt=self.d+".lenu"
            with open(output_pyt,'w') as a:
                a.write(str(Packer(self.c)))
    def build(self):
        super().build()
        root=FloatLayout()
        self.a=Label(
            text="",
            pos_hint={'x':0.45,'y':0.45},
            size_hint=(0.1,0.1)
        )
        self.b=Button(
            text="сохранить на диск",
            pos_hint={'x':0.45,'y':0.2},
            size_hint=(0.1,0.1)
        )
        self.c=''
        self.d=''
        root.add_widget(self.a)
        root.add_widget(self.b)
        if len(sys.argv) > 1:
            path_str=sys.argv[1]
            self.d=path_str
            with open(path_str,'rb') as r:
                local=ast.literal_eval(r.read().strip())
                self.c=str(Unpacker(local))
                print(self.c)
                self.a.text=self.c.encode('latin-1')
        Window.bind(on_drop_file=self.bysya_shitaet_file)
        self.b.bind(on_press=self.bysya_zapisuvaet_file)
        return root
MainScreen().run()
pid=os.getpid()
os.system(f"taskkill /F /PID {pid}")
