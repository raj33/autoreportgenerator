from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question
from bs4 import BeautifulSoup
import requests
dict = {'86': 'Complaints regarding Schools', '84': 'Complaints regarding voter list', '85': 'Inclusion, delection of correction in the voter list','37': 'Maintenance of Parks','38': 'Maintenance of Playground','26': 'Obstruction of water flow','45': 'Poor quality of work','17': 'Pot hole fill up/Repairs to the damage surface','40': 'Repairs to Centre Median','20': 'Repairs to existing footpath','39': 'Repairs to Flyovers/ bridges/ Culverts','23': 'Repairs to the SWD','41': 'Repairs to Traffic Island','31': 'Replacement of Cover for Manholes','44': 'Stoppage of Civil Works','130': 'UGD Over Flow','132': 'Unauthorised Road cutting','53': 'Absenteesim of door to door garbage collector','52':'Absenteesim of sweepers','56':'Bio Medical waste/Health hazard waste removal','78':'Broken Bin','65':'Burning of garbage','143':'Community Toilets','141':'Complaint Regarding School Toilets','58':'Complaints regarding burial ground','61':'Complaints regarding Dispensary','133':'Complaints regarding function Halls','59':'Complaints regarding public toilets','60':'Complaints regarding restaurants / Function halls','74':'Death of Stray Animals','24':'Desilting of Drain','29':'Disposal of removed silt on the Road','64':'Dog menace','89':'Fevers - Dengue/Malaria/ Gastro-enteritis','90':'Food adulteration: Road Side Eateries','79':'Garbage lorry with out Net','35':'Illegal draining of sewage to SWD/Open site','72':'Illegal slaughtering','77':'Improper Sweeping','91':'Issues relating to vacant lands','63':'Mosquito menace','57':'Obstruction of road by Trees branches','142':'Open defecation- free (ODF)','49':'Over flowing of garbage bins','140':'Poor maintenance of Public toilets at Fuel stations','51':'Provision of garbage bin','54':'Removal of Debris','30':'Removal of fallen trees','48':'Removal of garbage','62':'Request for Anti Larval operations - to prevent  Dengue /Malaria etc','50':'Shifting of garbage bin','144':'Silt by the side of dividers','81':'Spilling of Garbage from lorry','28':'Stagnation of water','70':'Stray cattle','73':'Stray Pigs','80':'Transfer Station  Smell','69':'Unauthorised sale of meat and meat product','42':'Unauthorised tree Cutting','134':'Unclaimed Dead Bodies','68':'Unhygeinic conditions because of Slaughter House','76':'Unhygienic and improper transport of meat and livestock','67':'Unsanitary conditions on the road','83':'Complaints related to issue of all types of license','82':'Complaints related to property tax','136':'Double Assessments','135':'Errors in demand Notice','99':'New Property Tax Fixation','100':'New vacant Land tax Fixation','102':'Property Tax Bifurcation','103':'Revision Petition on Property Tax','104':'Transfer of Title of property','105':'vacancy Remission','14':'Electric Shock due to street light','131':'Hanging of Streetlight Wires','11':'Non Burning of Street Lights', '34':'Encroachment on the public property','108':'Issues relating to Advertisement Boards','36':'Misuse of Community Hall','47':'Over head cable Wires running in Hapazard manner','43':'Parking Issue','21':'Removal of shops in the footpath','88':'Unauthorised Advt. Boards','32':'Unauthorised / Illegal construction','33':'violation of DCR/Building bye laws','121':'Complaints regarding all Sanctioned loans','139':'Disputes in SSG / SLF / TLF','115':'Non Receipt of Pensions (Disabled/ Old age/ Widow)','137':'Non Sanction of Bank Linkage to the group','138':'Provision of Placement after Training under ESTP','116':'Sanction of Gas Connection Under Deepam Scheme','113':'vaddi Leni Runalu','122':'Contamination of Water','124':'Issues Related to Drinking Water Supply','128':'Repair Bore wells','129' : 'Water pipe leakage'}
def st(n,nn):
    url = "http://"+str(n)+".emunicipal.ap.gov.in/pgr/complaint/view/"+str(nn)
   
    r  = requests.get(url)
    arr=[]
    data = r.text
    #print(data)
    

    soup = BeautifulSoup(data)
    #print(soup)
    
    for link in soup.find_all('div',{'class':'col-sm-2 col-xs-12 add-margin'}):
       
         arr.append(link.text)
    print(arr[2].replace(' ',''))
    return(arr[2].replace(' ',''))
    #print('1')
def index(request):
    latest_question_list = Question.objects.order_by()
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
anantapur=['anantapur','dharmavaram','gooty','guntakal','hindupur','kadiri','kalyanadurgam','madakasira','pamidi','puttaparthy','rayadurg','tadipatri']
chittoor=['chittoor','madanapalle','nagari','palamaner','punganur','puttur','srikalahasti','tirupati']
eastgodavari=['amalapuram','gollaprolu','kakinada','mandapet','mummidivaram','peddapuram','pithapuram','rajahmundry','ramachandrapuram','samalkot','tuni','yeleswaram']
krishna=['gudivada','jaggaiahpet','machilipatnam','nandigama','nuzividu','pedana','tiruvuru','vijayawada','vuyyuru']
kurnool=['adoni','allagadda','atmakur','dhone','gudur','kurnool','nandikotkur','nandyal','yemmiganur']
prakasam=['addanki','cheemakurthy','chirala','giddalur','kandukur','kanigiri','markapur','ongole']
nellore=['atmakur','gudur','kavali','naidupet','nellore','sullurpeta','venkatagiri']
srikakulam=['amudalavalasa','ichapuram','palakonda','palasakasibugga','rajam','srikakulam']
visakhapatnam=['narsipatnam','visakhapatnam','yelamanchili','bheemili','anakapalli']
vizianagaram=['bobbili','nellimarla','parvathipuram','saluru','vijayanagaram']
westgodavari=['bhimavaram','eluru','jangareddygudem','kovvur','narasapur','nidadavole','palakol','tadepalligudem','tanuku']
kadapa=['budwel','jammalamadugu','kadapa','mydukur','proddatur','pulivendula','rajampet','rayachoty','yerraguntla'] 
guntur=['bapatla','chilakaluripet','guntur','macherla','mangalagiri','narasaraopet','piduguralla','ponnur','repalle','sattenapalle','tadepalli','tenali','vinukonda']
def status(request):
    response = Question.objects.filter(status="Pending")
    noo=[]
    for i in response:
          
          print(i.crn)
          input('22')
          noo.append(i.crn)
          n=i.ulbname
          nn=i.crn 
          print(st(n,nn))       
          i.status=st(n,nn)
          i.save()
          input('1111111111')
    return HttpResponse(response)
@csrf_exempt    
def detail(request, question_id):
    dist=''
    data=question_id.split('@')
    inn=data[3]
    datav=dict[inn]
    data1=data[4]
    for i in anantapur:
        if data1==i:
            dist=data1
    for i in chittoor:
        if data1==i:
            dist=data1 
    for i in eastgodavari:
        if data1==i:
            dist=data1
    for i in krishna:
        if data1==i:
            dist=data1
    for i in kurnool:
        if data1==i:
            dist=data1
    for i in prakasam:
        if data1==i:
            dist=data1
    for i in nellore:
        if data1==i:
            dist=data1   
    for i in srikakulam:
        if data1==i:
            dist=data1
    for i in visakhapatnam:
        if data1==i:
            dist=data1
    for i in vizianagaram:
        if data1==i:
            dist=data1  
    for i in westgodavari:
        if data1==i:
            dist=data1
            print('sssssss')
    for i in kadapa:
        if data1==i:
            dist=data1     
    for i in guntur:
        if data1==i:
            dist=data1                                 

                                                       
    que=Question(name=data[0],phone=data[1],category=data[2],typee=datav,crn=data[5],ulbname=data[4],distr=dist)
    
    que.save()
    #return HttpResponse("You're looking at question %s." % que.question_text)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
