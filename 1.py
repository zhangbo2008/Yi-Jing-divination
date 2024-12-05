# 刷成结构化数据:
with open('易经全文.txt') as f:
     tmp=f.readlines()
tmp=[i.strip() for i in tmp if i.strip()]     


tmp2=[i[i.find('《')+1:i.find('》')] for i in tmp  if '卦：《' in i]  # 挂名

tmp3=[i for i in tmp if '【白话】' in i and '《象》' not in i]




gua=[]
suoyin=[]
jieguo=[]
for i in range(len(tmp)):
    j=tmp[i]
    if  '卦：《'  in j:
        gua.append(j)
        suoyin.append(i)
for i in range(len(gua)-1):
    jieguo.append(tmp[suoyin[i]:suoyin[i+1]])
    pass
jieguo.append(tmp[suoyin[len(gua)-1]:])
guaci=[i[2] for i in jieguo ]


# 一句古文, 下面2个白话.
yaoci=[]
for i in jieguo:
    tmp=[]
    for j in i:
       if '【白话】' in j:
          tmp.append(j)
    tmp=tmp[2:][1::2]
    yaoci.append(tmp)
pass
  
  
#   拿到所有的资源
yongjiu=yaoci[0][-1]
yongliu=yaoci[1][-1]
yaoci[0]=yaoci[0][:-1]
yaoci[1]=yaoci[1][:-1]


#===========用这五个来算卦即可.
yongjiu
yongliu
guaci
guaming=tmp2
guaming=[i.replace('卦','') for  i in guaming]
yaoci
# 两个特例, 用九, 用六:
# 朱熹说“遇此卦而六爻皆变者即此占之”，就是说如果筮得六个九，六爻都变的时候，就用“用九”爻来占断吉凶。如果是六爻纯阴的《坤》卦，道理相同，就是“用六”了。
  
#========一个字典. 挂名和编码的对应.
# 乾就是111111
# 坤就是000000


bianma={
  
'乾':'111111'
,'坤':'000000'
,'剥':'000001'
,'比':'000010'
,'观':'000011'
,'豫':'000100'
,'晋':'000101'
,'萃':'000110'
,'否':'000111'
,'谦':'001000'
,'山':'001001'
,'蹇':'001010'
,'渐':'001011'
,'小过':'001100'
,'旅':'001101'
,'咸':'001110'
,'遯':'001111'
,'师':'010000'
,'蒙':'010001'
,'水':'010010'
,'涣':'010011'
,'解':'010100'
,'未济':'101010'
,'困':'010110'
,'讼':'010111'
,'升':'011000'
,'蛊':'011001'
,'井':'011010'
,'风':'011011'
,'恒':'011100'
,'鼎':'011101'
,'大过':'011110'
,'姤':'011111'
,'复':'100000'
,'颐':'100001'
,'屯':'100010'
,'益':'100011'
,'雷':'100101'
,'噬嗑':'100101'
,'随':'100110'
,'无妄':'100111'
,'明夷':'101000'
,'贲':'101001'
,'既济':'101010'
,'家人':'101011'
,'豊':'101100'
,'离':'101101'
,'革':'101110'
,'同人':'101111'
,'临':'110000'
,'损':'110001'
,'节':'110010'
,'中孚':'110011'
,'归妹':'110100'
,'睽':'110101'
,'泽':'110110'
,'履':'110111'
,'泰':'111000'
,'大畜':'111001'
,'需':'111010'
,'小畜':'111011'
,'大壮':'111100'
,'大有':'111101'
,'夬':'111110'
}
# 注意这个编码是从1手到6手的.
# 我们这个按照图来. 改成从6手到1手的.

for i in bianma:
   bianma[i]=bianma[i][::-1]

def geibianmafanhuigua(a):
    for i in bianma:
       if bianma[i]==a:
          return i
  
print(geibianmafanhuigua('111111'))
print(geibianmafanhuigua('010000'))
  
  
print(1)    








import gradio as gr




with gr.Blocks() as demo:

    gr.Markdown(
    """
 <h1 align="center">周易:金钱摇卦系统</h1>
 <h5 align="center">摇六次硬币, 每次三个硬币,通过结果给出周易解释.</h5>

    """)
    # 添加行，里面的元素横向添加
    with gr.Column():
        with gr.Row():
          a1=gr.Button('第一次')
          a2=gr.Text(label=None,show_label=False)
        with gr.Row():
          a3=gr.Button('第二次')
          a4=gr.Text(label=None,show_label=False)
        with gr.Row():
          a5=gr.Button('第三次')
          a6=gr.Text(label=None,show_label=False)
        with gr.Row():
          a7=gr.Button('第四次')
          a8=gr.Text(label=None,show_label=False)
        with gr.Row():
          a9=gr.Button('第五次')
          a10=gr.Text(label=None,show_label=False)     
        with gr.Row():
          a11=gr.Button('第六次')
          a12=gr.Text(label=None,show_label=False)   
        with gr.Row():
          qingkong=gr.Button('重置',scale=0.1)
          
        with gr.Row():
          qingkong2=gr.Button('根据硬币结果进行解释',scale=0.1)  
          jieshi=gr.Text(label=None,show_label=False,value=""*100)   
import random        
def f1():
    out=''
    a1=random.random()>0.5
    a2=random.random()>0.5
    a3=random.random()>0.5
    for i in [a1,a2,a3]:
      if i:
        out+='正'
        out+=' '
      else:
        out+='反'
        out+=' '     
    return out    
with demo: # 触发函数都写这里.s
     
  a1.click(fn=f1, inputs=[], outputs=a2)
  a3.click(fn=f1, inputs=[], outputs=a4)
  a5.click(fn=f1, inputs=[], outputs=a6)
  a7.click(fn=f1, inputs=[], outputs=a8)
  a9.click(fn=f1, inputs=[], outputs=a10)
  a11.click(fn=f1, inputs=[], outputs=a12)
  def f2(a,b,c,d,e,f):
     return  '','','','','',''
    
  qingkong.click(fn=f2, inputs=[a2,a4,a6,a8,a10,a12], outputs=[a2,a4,a6,a8,a10,a12])
  
  
  
  def f3(a,b,c,d,e,f): #最核心的算卦函数!!!!!!!!!!!!!!!!!!!!!!
    
    # 我们正挂用0,1编码 1阳, 0阴. 然后按照 第六手.... 第一手的顺序排列. 所以是2的6次幂.也就是64挂.
    
    zhenggua=[] # 正挂
    for i in [f,e,d,c,b,a]:
         if  i.count('正')%2==1:
            zhenggua.append(1)
         else:
            zhenggua.append(0)
    bianyaodeshuliang=0 # bianyao数量
    for i in [f,e,d,c,b,a]:
         if  i.count('正')==0 or i.count('正')==3:
            bianyaodeshuliang+=1

    biangua=[]  # 变卦.
    for i in [f,e,d,c,b,a]:
         if  i.count('正')==1 or i.count('正')==0:
            biangua.append(1)
         else:
            biangua.append(0)     
    zhenggua=[str(i) for i in zhenggua]
    biangua=[str(i) for i in biangua]
    
    benguaguaming=geibianmafanhuigua(''.join(zhenggua))
    bianguaguaming=geibianmafanhuigua(''.join(biangua))
    # 根据便要数量来判断.
    if bianyaodeshuliang==0:
       celue='没有变爻：在《易经》中查出本卦的卦辞，根据这个卦词的意思来解释你算的这一卦。'
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==benguaguaming:
              guaindex=i
              break
       jieshi2=guaci[guaindex]
    if bianyaodeshuliang==1:
       celue='一个变爻：在《易经》中查出本卦的变爻的爻辞，根据这个爻词的意思来解释你算的这一卦。'
       
       tmp4=[f,e,d,c,b,a]
       bianyaoindex=0
       for i in range(len(tmp4)):
         j=tmp4[i]
         if  j.count('正')==0 or j.count('正')==3:
            bianyaoindex=i
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==benguaguaming:
              guaindex=i
              break
       jieshi2=yaoci[guaindex][bianyaoindex]
       
    if bianyaodeshuliang==2:
       celue='二个变爻：在《易经》中查出本卦的两个变爻的爻辞，根据这两个爻的爻词的意思来解释这一卦，但是要以上爻的爻词为主。'
       
       tmp4=[f,e,d,c,b,a]
       bianyaoindex=[]
       for i in range(len(tmp4)):
         j=tmp4[i]
         if  j.count('正')==0 or j.count('正')==3:
            bianyaoindex.append(i)
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==benguaguaming:
              guaindex=i
              break
      # 如果2个解释,那么我们用6个空格分开  主解释    次要解释.
       jieshi2=yaoci[guaindex][bianyaoindex[0]]+'   ---   '+yaoci[guaindex][bianyaoindex[1]]
    if bianyaodeshuliang==3:
       celue='在《易经》中分别查出本卦和变卦的卦辞，以本卦的卦词为主，变卦的卦词为辅，综合解释你算的这一卦。'
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==benguaguaming:
              guaindex=i
              break
       guaindex2=0
       for i in range(len(guaming)):
           if guaming[i]==bianguaguaming:
              guaindex2=i
              break
            
            
       jieshi2=guaci[guaindex]+'   ---  '+guaci[guaindex2]
    
    if bianyaodeshuliang==4:
       celue='四个变爻：在《易经》中查出本卦中两个没变的爻的爻词，根据这两个爻词的意思，以下爻的爻词为主来解释你算的这一卦。'
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==benguaguaming:
              guaindex=i
              break
       tmp4=[f,e,d,c,b,a]
       bianyaoindex=[]
       for i in range(len(tmp4)):
         j=tmp4[i]
         if  j.count('正')==0 or j.count('正')==3:
            bianyaoindex.append(i)
       bubianindex=[]
       for i in range(len(tmp4)):
          if i not in bianyaoindex:
             bubianindex.append(i)

      # 如果2个解释,那么我们用6个空格分开  主解释    次要解释.
       jieshi2=yaoci[guaindex][bubianindex[-1]]+'   ---   '+yaoci[guaindex][bubianindex[0]]
    
    
    if bianyaodeshuliang==5:
       celue='五个变爻：在《易经》中查出这个本卦的变卦，然后用变卦中不变的那个爻的爻词来解释你算的这一卦。'
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==bianguaguaming:
              guaindex=i
              break
       tmp4=[f,e,d,c,b,a]
       bianyaoindex=[]
       for i in range(len(tmp4)):
         j=tmp4[i]
         if  j.count('正')==0 or j.count('正')==3:
            bianyaoindex.append(i)
       bubianindex=[]
       for i in range(len(tmp4)):
          if i not in bianyaoindex:
             bubianindex.append(i)

      # 如果2个解释,那么我们用6个空格分开  主解释    次要解释.
       jieshi2=yaoci[guaindex][bubianindex[-1]]
    
    if bianyaodeshuliang==6:
       celue='六爻皆变：在《易经》中查出这个本卦的变卦，根据这个变卦卦词的意思来解释你算的这一卦。'
       guaindex=0
       for i in range(len(guaming)):
           if guaming[i]==bianguaguaming:
              guaindex=i
              break


      # 如果2个解释,那么我们用6个空格分开  主解释    次要解释.
       jieshi2=       guaci[guaindex]
    
    
    
    
    
    
    return  '本挂编码:'+''.join(zhenggua)+'  变卦编码:'+''.join(biangua) + '  本卦挂名:' + benguaguaming+ '  变卦挂名:' + bianguaguaming + '  变爻数量:' + str(bianyaodeshuliang) + '策略: '+celue + '解释:'+ jieshi2
  
  
  qingkong2.click(fn=f3, inputs=[a2,a4,a6,a8,a10,a12], outputs=[jieshi])

  demo.launch()












