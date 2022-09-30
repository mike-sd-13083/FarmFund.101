import RPi.GPIO as GPIO 
import dht11 
import time 
import datetime 
import Adafruit_GPIO.SPI as SPI 
import Adafruit_MCP3008 
import MySQLdb 
import sys 
#import timedelta from datetime 
#import timedelta, datetime 
import datetime 
from twilio.rest import Client

account_sid = 'AC9d774678f99e46725cb49150' #put your twillio account user id and token here
auth_token = 'fb60e45227f53d8a1d343f238f5' # Found on Twilio Console Dashboard

def whatsapp():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body='change',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+91******'

                          )

    print(message.sid)


def whatsapp():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body='Need water Supply',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+918*******'

#                              to='whatsapp:+91********'
                          )

    print(message.sid)
def whatsapp3():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body='since last two days tempacture is fewareable',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+91********'

#                              to='whatsapp:+9196*******'
                          )

    print(message.sid)

def parameter():
    
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    print("Moister level is: %d " %  moi)
    sql = ("""INSERT INTO agriculcture (date_time,temperature,humidity,moister,light) VALUES (%s,%s,%s,%s,%s)""",(datetime.datetime.now(),result.temperature,result.humidity,moi,light))
    cur.execute(*sql)
    db.commit()
    print "Write Complete"
    temp = int(result.temperature)	                    
    time.sleep(1)

def water_level():


    p1=y-1
    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(p1,))
    d2 = cur.fetchall()
    for i in d2:
        m2=(i[0])

    print("privious 1 day %d" % m2) #privious1
		    	
    p2=y-2
    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(p2,))
    d3 = cur.fetchall()
    for i in d3:
        m3=(i[0])
			   
    print("privious 2nd day %d" % m3) #privious2

    p3=y-3
    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(p3,))
    d4 = cur.fetchall()
    for i in d4:
        m4=(i[0])
    print("privious 3rd day %d" % m4) #privious3

    p4=y-4
    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(p4,))
    d5 = cur.fetchall()
    for i in d5:
        m5=(i[0])
    print("privious 4th day %d " % m5) #privious4
		 
    p5=y-5
    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(p5,))
    d6 = cur.fetchall()
    for i in d6:
        m6=(i[0])
    print("privious 5th day %d " % m6) #privious5

    p6=y-6
    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(p6,))
    d7 = cur.fetchall()
    for i in d7:
        m7=(i[0])
    print("privious 6 days %d" % m7) #privious6

    if(m2>800 or m3>850 or m4>900 or m5>1000 or m6>1000 or m7>1000):
        print("Soil is Dry since last 7 days")



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
CLK  = 18 # board 12
MISO = 23  # board 16
MOSI = 24 # board 18
CS   = 25 # board 22
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# read data using pin 14
instance = dht11.DHT11(pin=14)
db = MySQLdb.connect(host="", user="",passwd="", db="") #use your database connectivity here  
cur = db.cursor()
x= datetime.datetime.now()
y1 = (x.strftime("%d"))
y=int(y1)
print(y)
m = (x.strftime("%m"))
mi = (x.strftime("%M"))
h= (x.strftime("%H"))
s = x.strftime("%S")
hour = int (h)
min = int(mi)
month= int(m)
sec = int(s)


while(1):
    result = instance.read()
    select = mcp.read_adc(0)
    moi = mcp.read_adc(1)
    light= mcp.read_adc(2)
    val = int(select)
    
    #whatsapp3()
    print(val)

    
    if(val> 0 and val < 200):
	print("crop is groundnut")        
        if result.is_valid():
            print(y)
            print(x)
	    if (moi < 10):
                #set = y +4
	    	set = min + 1
#	    if(y == set):
	    if(min == set):
		print("wapsa condition occur")
            if(hour==11 and min==33):
                    print("hour and min matched")
                   # whatsapp()
    #		break
		 #--------------------------
                    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(y,))
                    h1 = cur.fetchall()
                    for i in h1:
                            m_p=(i[0])
                    print(m_p)
                   
                   
                    
                    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(b,))
                    h2 = cur.fetchall()
                    for i in h2:
                            m_t=(i[0])
                    print(m_t)
                    
                    if(m_p>800 and m_t>800):
                            print("Water level in soil is less")
                    
                            whatsapp()
#-------------------------------------------------------
                   
                    water_level()
		#--------------------------------
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(y,))
                    
                    d = cur.fetchall()
                    for i in d:
                            p_f=(i[0])
                            print(p_f)
                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(y,))
                    e = cur.fetchall()
                    for i in e:
                            p_t=(i[0])
                    print(p_t)
                    dif = p_f -p_t
                    print("diffrance is %d" % dif)
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(b,))
                    d = cur.fetchall()
                    for i in d:
                            t_f=(i[0])
                            print(t_f)

                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(b,))
                    e = cur.fetchall()
                    for i in e:
                            t_t=(i[0])
                    print(t_t)
                    y_dif= t_f - t_t
                    print("yestrdays diffrance %d" % y_dif)
                    if(t_t>=30):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Fuliar Fungle Disease occure and temp is high")
                    if(t_f<=20):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Fuliar Fungle Disease occure and temp is low")           
                        
                    else:
                            print("fevarable condition")
                            
            month= int(m)
            z =int (y)
            b=z-(1)
            parameter()
#--------------------------------2nd Crop----------------------------------------------------------------------------
    if(val> 201 and val < 400):
	print("crop is Whist Chilli")        
        if result.is_valid():
            print(y)
            print(x)
	    if (moi < 10):
                #set = y +4
	    	set = min + 1
#	    if(y == set):
	    if(min == set):
		print("wapsa condition occur")
            if(hour==11 and min==33):
                    print("hour and min matched")
                   # whatsapp()

             cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(y,))
                    h1 = cur.fetchall()
                    for i in h1:
                            m_p=(i[0])
                    print(m_p)
                   
                   
                    
                    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(b,))
                    h2 = cur.fetchall()
                    for i in h2:
                            m_t=(i[0])
                    print(m_t)
                    
                    if(m_p>800 and m_t>800):
                            print("Water level in soil is less")
                    
                            whatsapp()
#-------------------------------------------------------
                    water_level()

		    		#--------------------------------
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(y,))
                    
                    d = cur.fetchall()
                    for i in d:
                            p_f=(i[0])
                            print(p_f)
                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(y,))
                    e = cur.fetchall()
                    for i in e:
                            p_t=(i[0])
                    print(p_t)
                    dif = p_f -p_t
                    print("diffrance is %d" % dif)
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(b,))
                    d = cur.fetchall()
                    for i in d:
                            t_f=(i[0])
                            print(t_f)

                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(b,))
                    e = cur.fetchall()
                    for i in e:
                            t_t=(i[0])
                    print(t_t)
                    y_dif= t_f - t_t
                    print("yestrdays diffrance %d" % y_dif)
                    if(t_t>=30):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Temp is high amd Disease may occure")
                    if(t_f<=15):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print(" Temp is low and Disease may occure")           
                        
                    else:
                            print("fevarable condition")
                            
            month= int(m)
            z =int (y)
            b=z-(1)
            parameter()
#-----------------------------3rd crop-----------------------------------------------------------            
    if(val> 401 and val < 600):
	print("crop is Gram")        
        if result.is_valid():
	    if (moi < 10):
                #set = y +4
	    	set = min + 1
#	    if(y == set):
	    if(min == set):
		print("wapsa condition occur")
            if(hour==11 and min==33):
                    print("hour and min matched")
                   # whatsapp()

             cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(y,))
                    h1 = cur.fetchall()
                    for i in h1:
                            m_p=(i[0])
                    print(m_p)
                   
                   
                    
                    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(b,))
                    h2 = cur.fetchall()
                    for i in h2:
                            m_t=(i[0])
                    print(m_t)
                    
                    if(m_p>800 and m_t>800):
                            print("Water level in soil is less")
                    
                            whatsapp()
#-------------------------------------------------------
                   
                    water_level()

		    		#--------------------------------
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(y,))
                    
                    d = cur.fetchall()
                    for i in d:
                            p_f=(i[0])
                            print(p_f)
                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(y,))
                    e = cur.fetchall()
                    for i in e:
                            p_t=(i[0])
                    print(p_t)
                    dif = p_f -p_t
                    print("diffrance is %d" % dif)
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(b,))
                    d = cur.fetchall()
                    for i in d:
                            t_f=(i[0])
                            print(t_f)

                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(b,))
                    e = cur.fetchall()
                    for i in e:
                            t_t=(i[0])
                    print(t_t)
                    y_dif= t_f - t_t
                    print("yestrdays diffrance %d" % y_dif)
                    if(t_t>=23):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Gram Wilt Disease occure and temp is high")
                    if(t_f<=12):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Temp is low")           
                        
                    else:
                            print("fevarable condition")
                            
            month= int(m)
            z =int (y)
            b=z-(1)
            parameter()
#----------------------------------4th crop------------------------------------------------------
    if(val> 601 and val < 800):
	print("crop is Watermalon")        
        if result.is_valid():
	    if (moi < 10):
                #set = y +4
	    	set = min + 1
#	    if(y == set):
	    if(min == set):
		print("wapsa condition occur")
            if(hour==11 and min==33):
                    print("hour and min matched")
                   # whatsapp()

             cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(y,))
                    h1 = cur.fetchall()
                    for i in h1:
                            m_p=(i[0])
                    print(m_p)
                   
                   
                    
                    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(b,))
                    h2 = cur.fetchall()
                    for i in h2:
                            m_t=(i[0])
                    print(m_t)
                    
                    if(m_p>800 and m_t>800):
                            print("Water level in soil is less")
                    
                            whatsapp()
#-------------------------------------------------------
                   
                    water_level()

                    
		    		#--------------------------------
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(y,))
                    
                    d = cur.fetchall()
                    for i in d:
                            p_f=(i[0])
                            print(p_f)
                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(y,))
                    e = cur.fetchall()
                    for i in e:
                            p_t=(i[0])
                    print(p_t)
                    dif = p_f -p_t
                    print("diffrance is %d" % dif)
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(b,))
                    d = cur.fetchall()
                    for i in d:
                            t_f=(i[0])
                            print(t_f)

                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(b,))
                    e = cur.fetchall()
                    for i in e:
                            t_t=(i[0])
                    print(t_t)
                    y_dif= t_f - t_t
                    print("yestrdays diffrance %d" % y_dif)
                    if(t_t>=32):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Anthracnose Disease occure and temp is high")
                    if(t_f<=24):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Temp is low")           
                        
                    else:
                            print("fevarable condition")
                            
            month= int(m)
            z =int (y)
            b=z-(1)
            parameter()
#--------------------------------------------------------5th crop-------------------------------
 if(val> 801 and val < 1000):
	print("crop is Sorghum")        
        if result.is_valid():
	    if (moi < 10):
                #set = y +4
	    	set = min + 1
#	    if(y == set):
	    if(min == set):
		print("wapsa condition occur")
            if(hour==11 and min==33):
                    print("hour and min matched")
                   # whatsapp()

             cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(y,))
                    h1 = cur.fetchall()
                    for i in h1:
                            m_p=(i[0])
                    print(m_p)
                   
                   
                    
                    cur.execute("""select MIN(demo) from agri2 where date_time='%s'""",(b,))
                    h2 = cur.fetchall()
                    for i in h2:
                            m_t=(i[0])
                    print(m_t)
                    
                    if(m_p>800 and m_t>800):
                            print("Water level in soil is less")
                    
                            whatsapp()
#-------------------------------------------------------
                   
                    water_level()
		    
		#--------------------------------
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(y,))
                    
                    d = cur.fetchall()
                    for i in d:
                            p_f=(i[0])
                            print(p_f)
                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(y,))
                    e = cur.fetchall()
                    for i in e:
                            p_t=(i[0])
                    print(p_t)
                    dif = p_f -p_t
                    print("diffrance is %d" % dif)
                    cur.execute("""select MAX(temp) from agri2 where date_time='%s'""",(b,))
                    d = cur.fetchall()
                    for i in d:
                            t_f=(i[0])
                            print(t_f)

                    cur.execute("""select MIN(temp) from agri2 where date_time='%s'""",(b,))
                    e = cur.fetchall()
                    for i in e:
                            t_t=(i[0])
                    print(t_t)
                    y_dif= t_f - t_t
                    print("yestrdays diffrance %d" % y_dif)
                    if(t_t>=25):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Loose smut Disease occure and temp is high")
                    if(t_f<=20):
                        if(dif<=3 and y_dif<=3):
                            #whatsapp call
                            print("Temp is low")           
                        
                    else:
                            print("fevarable condition")
                            
            month= int(m)
            z =int (y)
            b=z-(1)
            parameter()