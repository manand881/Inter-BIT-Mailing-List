# Written by Anand Mahesh 
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib
import time 

my_email_id="jhondoe@gmail.com"
password="a really good password"
f=open("message","r")

course_prefix="mca"
number_prefix_list=['250','400','450','100']
number_prefix=str()
email_list=list()
year=20  

for z in range(19,21):
    year=z

    for y in number_prefix_list:
        number_prefix=y
        iterator=1

        for x in range (50):

            if len(str(iterator))==1:
                temp=course_prefix+number_prefix+str(0)+str(iterator)+"."+str(year)+"@bitmesra.ac.in"
                email_list.append(temp)
                iterator+=1

            if len(str(iterator))==2:
                temp=course_prefix+number_prefix+str(iterator)+"."+str(year)+"@bitmesra.ac.in"
                email_list.append(temp)
                iterator+=1


# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(my_email_id, password) 
  
# message to be sent
subject="Request to Join the INTER BIT Telegram Group"
text_message=f.readlines()
text_message=''.join(text_message)
message = 'subject: {}\n\n{}'.format(subject, text_message)

for reciever_email_id in email_list:
    # sending the mail
    try:
        s.sendmail(my_email_id, reciever_email_id, message)
        print("sent to:",reciever_email_id)
        time.sleep(2)
    except Exception as e:
        print(e,reciever_email_id) 
  
# terminating the session 
s.quit()
print("Sent To All") 
                                                    