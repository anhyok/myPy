#1. '틀렸으면' 단어를 모은다

#2. 모아둔 '틀린단어' list가 5개 이상?

#3. '틀린단어' list로 한 게임 더
# - 해당 코드 Copy & Paste?
# - 또는 함수?

#4. 잘 되면 Set()으로 중복제거
# - 필요하면, 다시 list()를 이용하여 리스트로 바꿀 수 있음

# ** 1번에서 중복 아닌 것만 넣으면
# ** 4번은 안해도 됨


import random
import time

#w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
w = [
    'the','be','and','of','a','in','to','have','it','I','that','for','you','he','with','on','do','say','this','they','at','but','we','his','from','not','by','she','or','as','what','go','their','can','who','get','if','would','her','all','my','make','about','know','will','up','one','time','there','year','so','think',
    'when','which','them','some','me','people','take','out','into','just','see','him','your','come','could','now','than','like','other','how','then','its','our','two','more','these','want','way','look','first','also','new','because','day','use','no','man','find','here','thing','give','many','well','only','those',
    'tell','very','even','back','any','good','woman','through','us','life','child','work','down','may','after','should','call','world','over','school','still','try','last','ask','need','too','feel','three','state','never','become','between','high','really','something','most','another','much','family','own','leave',
    'put','old','while','mean','keep','student','why','let','great','same','big','group','begin','seem','country','help','talk','where','turn','problem','every','start','hand','might','American','show','part','against','place','such','again','few','case','week','company','system','each','right','program','hear',
    'question','during','play','government','run','small','number','off','always','move','night','live','Mr','point','believe','hold','today','bring','happen','next','without','before','large','million','must','home','under','water','room','write','mother','area','national','money','story','young','fact','month',
    'different','lot','study','book','eye','job','word','though','business','issue','side','kind','four','head','far','black','long','both','little','house','yes','since','provide','service','around','friend','important','father','sit','away','until','power','hour','game','often','yet','line','political','end',
    'among','ever','stand','bad','lose','however','member','pay','law','meet','car','city','almost','include','continue','set','later','community','name','five','once','white','least','president','learn','real','change','team','minute','best','several','idea','kid','body','information','nothing','ago','lead',
    'social','understand','whether','watch','together','follow','parent','stop','face','anything','create','public','already','speak','others','read','level','allow','add','office','spend','door','health','person','art','sure','war','history','party','within','grow','result','open','morning','walk','reason',
    'low','win','research','girl','guy','early','food','moment','himself','air','teacher','force','offer','enough','education','across','although','remember','foot','second','boy','maybe','toward','able','age','policy','everything','love','process','music','including','consider','appear','actually','buy','probably',
    'human','wait','serve','market','die','send','expect','sense','build','stay','fall','oh','nation','plan','cut','college','interest','death','course','someone','experience','behind','reach','local','six','remain','effect','yeah','suggest','class','control','raise','care','perhaps','late','hard','field',
    'else','pass','former','sell','major','sometimes','require','along','development','themselves','report','role','better','economic','effort','decide','rate','strong','possible','heart','drug','leader','light','voice','wife','whole','police','mind','finally','pull','return','free','military','price','less',
    'according','decision','explain','son','hope','develop','view','relationship','carry','town','road','drive','arm','TRUE','federal','break','difference','thank','receive','value','international','building','action','full','model','join','season','society','tax','director','position','player','agree','especially',
    'record','pick','wear','paper','special','space','ground','form','support','event','official','whose','matter','everyone','center','couple','site','project','hit','base','activity','star','table','court','produce','eat','teach','oil','half','situation','easy','cost','industry','figure','street','image','itself',
    'phone','either','data','cover','quite','picture','clear','practice','piece','land','recent','describe','product','doctor','wall','patient','worker','news','test','movie','certain','north','personal','simply','third','technology','catch','step','baby','computer','type','attention','draw','film','Republican',
    'tree','source','red','nearly','organization','choose','cause','hair','century','evidence','window','difficult','listen','soon','culture','billion','chance','brother','energy','period','summer','realize','hundred','available','plant','likely','opportunity','term','short','letter','condition','choice','single',
    'rule','daughter','administration','south','husband','Congress','floor','campaign','material','population','economy','medical','hospital','church','close','thousand','risk','current','fire','future','wrong','involve','defense','anyone','increase','security','bank','myself','certainly','west','sport','board',
    'seek','per','subject','officer','private','rest','behavior','deal','performance','fight','throw','top','quickly','past','goal','bed','order','author','fill','represent','focus','foreign','drop','blood','upon','agency','push','nature','color','recently','store','reduce','sound','note','fine','near','movement',
    'page','enter','share','common','poor','natural','race','concern','series','significant','similar','hot','language','usually','response','dead','rise','animal','factor','decade','article','shoot','east','save','seven','artist','scene','stock','career','despite','central','eight','thus','treatment','beyond',
    'happy','exactly','protect','approach','lie','size','dog','fund','serious','occur','media','ready','sign','thought','list','individual','simple','quality','pressure','accept','answer','resource','identify','left','meeting','determine','prepare','disease','whatever','success','argue','cup','particularly','amount',
    'ability','staff','recognize','indicate','character','growth','loss','degree','wonder','attack','herself','region','television','box','TV','training','pretty','trade','election','everybody','physical','lay','general','feeling','standard','bill','message','fail','outside','arrive','analysis','benefit',
    'forward','lawyer','present','section','environmental','glass','skill','sister','PM','professor','operation','financial','crime','stage','ok','compare','authority','miss','design','sort','act','ten','knowledge','gun','station','blue','strategy','clearly','discuss','indeed','truth','song','example',
    'check','environment','leg','dark','various','rather','laugh','guess','executive','prove','hang','entire','rock','forget','claim','remove','manager','enjoy','network','legal','religious','cold','final','main','science','green','memory','card','above','seat','cell','establish','nice','trial','expert','spring',
    'firm','radio','visit','management','avoid','imagine','tonight','huge','ball','finish','yourself','theory','impact','respond','statement','maintain','charge','popular','traditional','onto','reveal','direction','weapon','employee','cultural','contain','peace','pain','apply','measure','wide','shake',
    'fly','interview','manage','chair','fish','particular','camera','structure','politics','perform','bit','weight','suddenly','discover','candidate','production','treat','trip','evening','affect','inside','conference','unit','style','adult','worry','range','mention','deep','edge','specific','writer','trouble',
    'necessary','throughout','challenge','fear','shoulder','institution','middle','sea','dream','bar','beautiful','property','instead','improve','stuff','detail','method','somebody','magazine','hotel','soldier','reflect','heavy','bag','heat','marriage','tough','sing','surface','purpose','exist','pattern',
    'whom','skin','agent','owner','machine','gas','ahead','generation','commercial','address','cancer','item','reality','coach','Mrs','yard','beat','violence','total','tend','investment','discussion','finger','garden','notice','collection','modern','task','partner','positive','civil','kitchen','consumer','shot',
    'budget','wish','painting','scientist','safe','agreement','capital','mouth','nor','victim','newspaper','threat','responsibility','smile','attorney','score','account','interesting','audience','rich','dinner','vote','western','relate','travel','debate','prevent','citizen','majority','none','front','born','admit',
    'senior','assume','wind','key','professional','mission','fast','alone','customer','suffer','speech','successful','option','participant','southern','fresh','eventually','forest','video','global','Senate','reform','access','restaurant','judge','publish','relation','release','bird','opinion','credit','critical',
    'corner','concerned','recall','version','stare','safety','effective','neighborhood','original','troop','income','directly','hurt','species','immediately','track','basic','strike','sky','freedom','absolutely','plane','nobody','achieve','object','attitude','labor','refer','concept','client','powerful','perfect',
    'nine','therefore','conduct','announce','conversation','examine','touch','please','attend','completely','variety','sleep','involved','investigation','nuclear','researcher','press','conflict','spirit','replace','British','encourage','argument','camp','brain','feature','afternoon','AM','weekend','dozen',
    'possibility','insurance','department','battle','beginning','date','generally','African','sorry','crisis','complete','fan','stick','define','easily','hole','element','vision','status','normal','Chinese','ship','solution','stone','slowly','scale','university','introduce','driver','attempt','park','spot','lack',
    'ice','boat','drink','sun','distance','wood','handle','truck','mountain','survey','supposed','tradition','winter','village','Soviet','refuse','sales','roll','communication','screen','gain','resident','hide','gold','club','farm','potential','European','presence','independent','district','shape','reader','Ms',
    'contract','crowd','Christian','express','apartment','willing','strength','previous','band','obviously','horse','interested','target','prison','ride','guard','terms','demand','reporter','deliver','text','tool','wild','vehicle','observe','flight','facility','understanding','average','emerge','advantage','quick',
    'leadership','earn','pound','basis','bright','operate','guest','sample','contribute','tiny','block','protection','settle','feed','collect','additional','highly','identity','title','mostly','lesson','faith','river','promote','living','count','unless','marry','tomorrow','technique','path','ear','shop','folk',
    'principle','survive','lift','border','competition','jump','gather','limit','fit','cry','equipment','worth','associate','critic','warm','aspect','insist','failure','annual','French','Christmas','comment','responsible','affair','procedure','regular','spread','chairman','baseball','soft','ignore','egg','belief',
    'demonstrate','anybody','murder','gift','religion','review','editor','engage','coffee','document','speed','cross','influence','anyway','threaten','commit','female','youth','wave','afraid','quarter','background','native','broad','wonderful','deny','apparently','slightly','reaction','twice','suit','perspective',
    'growing','blow','construction','intelligence','destroy','cook','connection','burn','shoe','grade','context','committee','hey','mistake','location','clothes','Indian','quiet','dress','promise','aware','neighbor','function','bone','active','extend','chief','combine','wine','below','cool','voter','learning','bus',
    ] # ref: https://www.wordfrequency.info/  #1

def rand_question(w): #2
    n = 1
    wrong = [] #2 틀린 단어용 빈 리스트
    q = random.choice(w)
    while n <= 5:
        print("*문제", n)
        print(q)
        x = input()
        if q == x:
            print("통과!")
            n = n + 1
            q = random.choice(w)
        else:
            print("오타, 다시 도전")
            wrong.append(q) #2
    return wrong #2 틀린 단어 리스트


best_et = 0 #1 최단 기록이 0초라면 아직 최단 기록이 없다고 가정
wrong_set = set() #2 전체 틀린 단어용 빈 집합(중복 제거)
while True: #1
    print("[타자 게임] 준비되면 엔터! (q: 종료)") #1
    ready = input() #1
    if ready == 'q': #1
        break #1

    start = time.time()
    wrong_w = rand_question(w) #2: 다섯 번 질문 함수
    wrong_set.update(wrong_w) #2
    end = time.time()

    et = end - start
    if best_et == 0: #1 첫 기록
        best_et = et #1
    elif best_et > et: #1
        best_et = et #1
    print("타자 시간 :", format(et, ".2f"), "초")
    print("최단 시간 :", format(best_et, ".2f"), "초") #1
    if(len(wrong_set)>0):
        print("전체 틀린 단어: ", wrong_set) #2
    print("=====================") #1

    if (len(wrong_set) >= 5): #2 전체 틀린 단어 갯수가 일정 이상되면
        print("*** 틀린단어 복습 ***") #2
        wrong_w = rand_question(list(wrong_set)) #2
        wrong_set = set(wrong_w) #2
        print("*** 틀린단어 복습 끝!! ***") #2

print("Good bye!") #1
