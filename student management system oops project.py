#creating course, batch , student doing crud on that
'''Initialisation of lists contsin objs'''
courses=[]
batches=[]
students=[]
class Course:
    def __init__(self,cid, cname, cduration):
        self.cid=cid
        self.cname=cname
        self.cduration=cduration
    def cdisplay(self):
        print(f'course id:{self.cid} , course name:{self.cname} and course duration:{self.cduration}')

class Batch:
    def __init__(self, bid, bname, btime):
        self.bid=bid
        self.bname=bname
        self.btime=btime
        self.cid=[]
    def bdisplay(self):
        print(f'Batch {self.bid} Details of course {self.cid.cname} \n with Batch id: {self.bid}, Batch name: {self.bname} and Timing of batch: {self.btime} of course_id:- {self.cid.cid} course name:- {self.cid.cname} and course duration:- {self.cid.cduration}')
        
class Student:
    def __init__(self ,sid, sname):
        self.sid=sid
        self.sname=sname
        self.bid=[]
    def sdisplay(self):
        print(f'STudent Details of Batch{self.bid.bname} \n student id/rn {self.sid}, student name {self.sname} of their batch id:- {self.bid.bid} batch name :- {self.bid.bname} and batch timing:- {self.bid.btime} \n with her enrolled course course id:- {self.bid.cid.cid}, course name:- {self.bid.cid.cname} and course duration:- {self.bid.cid.cduration}')




def add_course():
    print('-------Course ADD SECTION--------')
    a=int(input('enter course id '))
    b=input('enter course name ')
    c=input('enter course duration ')
    cobj=Course(cid=a, cname=b, cduration=c)
    courses.append(cobj)
    print(f'{b} Course Added Successfully !........... Thanks for adding COurse')
    print()
    
def read_course():
    print('-------Course READ/SEARCH SECTION--------')
    rd_ch=int(input('enter Ur choice 1.Full Read \t 2.Particular Read :-\n'))
    #print('cobj',cobj)
    if rd_ch==1:
        print('All courses are displaying.....!')
        for cobj in courses:
            cobj.cdisplay()
        
    
    elif rd_ch==2:
        print('Particular courses are displaying....!')
        prtu_rd_ch=int(input('enter Ur choice To Read COurses 1.Course id \t 2.Course name \t 3.Course Duration :-\n'))
        if prtu_rd_ch==1:
            print('Searching By COurse Id..')
            user_cid=int(input('enter Id Of courses Want TO search '))
            for cobj in courses:
                if user_cid==cobj.cid:
                    cobj.cdisplay()
                    return
                #else:
            #print(f'{user_cid} course id not exist \n plz enter valid Course id')
        elif prtu_rd_ch==2:
            print('Searching By COurse name..')
            user_cname=input('enter name Of courses Want TO search ')
            for cobj in courses:
                if user_cname==cobj.cname:
                    cobj.cdisplay()
                    return
                #else:
            #print(f'{user_cname} course name not exist \n plz enter valid Course name')
        elif prtu_rd_ch==3:
            print('Searching By COurse duration..')
            user_cduration=input('enter duration Of courses Want TO search ')
            for cobj in courses:
                if user_cduration==cobj.cduration:
                    cobj.cdisplay()
                    return
                #else:
            #print(f'{user_cduration} course duration not exist \n plz enter valid Course duration')

def update_course():
    print()
    print('-------Course UPDATE SECTION--------')
    print('courses are Updating by name, duration.....!')
    user_up_cid=int(input('enter Id Of courses Update'))
    for cobj in courses:
        if user_up_cid==cobj.cid:
            #a=int(input('enter course id '))
            cobj.cname=input('enter course name ')
            cobj.cduration=input('enter course duration ')
            print(f'{cobj.cname} course updated successfully !')
            #cobj=Course(cid=a, cname=b, cduration=c)
        #else:
    #print(f'{user_up_cid} Id does not exist...... plz enter valid ID' )
        
            
def delete_course():
    print()
    print('-------Course DELETE SECTION--------')
    prtu_del_ch=int(input('enter Ur choice To Delete COurses 1.Course id \t 2.Course name \t 3.Course Duration :-\n'))
    if prtu_del_ch==1:
        print('Deleting By COurse Id..')
        user_cid=int(input('enter Id Of courses Want TO Delete '))
        for cobj in courses:
            if user_cid==cobj.cid:
                cobj.cdisplay()
                print('this course will be deleted....')
                courses.remove(cobj)
                #del cobj
                #cobj.cdisplay()
                print('Course DEleted Successfully !')
                return
                
            #else:
             #   print(f'{user_cid} course id not exist \n plz enter valid Course id')
    elif prtu_del_ch==2:
        print('Deleting By COurse name..')
        user_cname=input('enter name Of courses Want TO Delete ')
        for cobj in courses:
            if user_cname==cobj.cname:
                courses.remove(cobj)
                print('Course DEleted Successfully !')
                return
                #del cobj
                #cobj.cdisplay()
            #else:
              #  print(f'{user_cname} course name not exist \t plz enter valid Course name')
    elif prtu_del_ch==3:
        print('Deleting By COurse duration..')
        user_cduration=input('enter duration Of courses Want TO Delete ')
        for cobj in courses:
            if user_cduration==cobj.cduration:
                cobj.cdisplay()
                print('this course will be deleted....')
                #del cobj
                #cobj.cdisplay()
                courses.remove(cobj)
                print('Course DEleted Successfully !')
                return
                #cobj.cdisplay()
            #else:
                #print(f'{user_cduration} course duration not exist \t plz enter valid Course duration')

    
#BATCHES ---------   -----------------------------------------------------------------       ---- BATCHES ----- ALL BATCHES

def add_batch():
    print()
    print()
    print("WELCOMES TO BATCHES OF SKILLS ACADEMY")
    print('-------BATCH ADD SECTION--------')
    #print('BATCH 
    print('Plz, Enter the valid batch details to Add new Batch:- ')
    a=int(input('enter batch id '))
    b=input('enter batch name ')
    c=input('enter batch time ')
    bobj=Batch(bid=a, bname=b, btime=c)
    batches.append(bobj)
    print(f'{bname} Batch Added Successfully !........... Thanks for adding Batch')
    print()
def read_course():
    print('-------BATCH READ/SEARCH SECTION--------')
    rd_bh=int(input('enter Ur choice 1.Full Read \t 2.Particular Read :-\n'))
    #print('cobj',cobj)
    if rd_bh==1:
        print('All Batches are displaying.....!')
        for bobj in batches:
            Bobj.bdisplay()
    
    elif rd_bh==2:
        print('Particular batches are displaying....!')
        prtu_rd_bh=int(input('enter Ur choice To Read Batch 1.Batch id \t 2.Batch name \t 3.Batch Timing :-\n'))
        if prtu_rd_bh==1:
            print('Searching By Batch Id..')
            user_bid=int(input('enter Id Of Batch Want TO search '))
            for bobj in batches:
                if user_bid==bobj.bid:
                    bobj.bdisplay()
                    return
                #else:
            #print(f'{user_cid} course id not exist \n plz enter valid Course id')
        elif prtu_rd_bh==2:
            print('Searching By Batch name..')
            user_bname=input('enter name Of Batch Want TO search ')
            for bobj in batches:
                if user_bname==bobj.bname:
                    bobj.bdisplay()
                    return
                
            #print(f'{user_cname} course name not exist \n plz enter valid Course name')
        elif prtu_rd_bh==3:
            print('Searching By Batch Timing..')
            user_btiming=input('enter Timing Of Batch Want TO search ')
            for bobj in batches:
                if user_btiming==bobj.btime:
                    bobj.bdisplay()
                    return
                #else:
            #print(f'{user_cduration} course duration not exist \n plz enter valid Course duration')

def update_batch():
    print()
    print('-------BATCH UPDATE SECTION--------')
    #print('batches are Updating by name, timing.....!')
    user_up_bid=int(input('enter Id Of batch Update'))
    for bobj in batches:
        if user_up_bid==bobj.bid:
            #a=int(input('enter course id '))
            bobj.bname=input('enter batch name ')
            bobj.btime=input('enter batch timing ')
            print(f'{bobj.bname} batch updated successfully !')
            #cobj=Course(cid=a, cname=b, cduration=c)
        #else:
    #print(f'{user_up_cid} Id does not exist...... plz enter valid ID' )
        
            
def delete_batch():
    print()
    print('-------BATCH DELETE SECTION--------')
    prtu_del_bh=int(input('enter Ur choice To Delete Batches 1.Batch id \t 2.Batch name \t 3.Batch Timing :-\n'))
    if prtu_del_bh==1:
        print('Deleting By Batch Id..')
        user_bid=int(input('enter Id Of batch Want TO Delete '))
        for bobj in batches:
            if user_bid==bobj.bid:
                bobj.bdisplay()
                print('this batch will be deleted....')
                batches.remove(bobj)
                #del cobj
                #cobj.cdisplay()
                print('batch DEleted Successfully !')
                return
                
            #else:
             #   print(f'{user_cid} course id not exist \n plz enter valid Course id')
    elif prtu_del_bh==2:
        print('Deleting By Batch name..')
        user_bname=input('enter name Of Batch Want TO Delete ')
        for bobj in batches:
            if user_bname==bobj.bname:
                batches.remove(bobj)
                print('batch DEleted Successfully !')
                return
                #del cobj
                #cobj.cdisplay()
            #else:
              #  print(f'{user_cname} course name not exist \t plz enter valid Course name')
    elif prtu_del_bh==3:
        print('Deleting By Batch timing..')
        user_btiming=input('enter timing Of batch Want TO Delete ')
        for bobj in batches:
            if user_btiming==bobj.btime:
                bobj.bdisplay()
                print('this batch will be deleted....')
                #del cobj
                #cobj.cdisplay()
                batches.remove(bobj)
                print('batch DEleted Successfully !')
                return
                #cobj.cdisplay()
            #else:
                #print(f'{user_cduration} course duration not exist \t plz enter valid Course duration')

    
def add_student():
    print()
    print()
    print('WELCOMES TO SKILLS ACADEMY')
    print('------- ADD SECTION--------')
    a=int(input('enter student id:- '))
    b=input(' enter student name:- ')
    sobj=Student(sid=a, sname=b)
    students.append(sobj)
    print(b,'Student Added Sucessfully..!')
    print()
def read_student():
    print('------- READ/SEARCH SECTION--------')
    rd_sh=int(input('1. Full Read \t 2. Particular Read \n Enter Your choice To Read Students:- '))
    if rd_sh==1:
        for sobj in students:
            sobj.display()
    elif rd_sh==2:
        pr_rd_sh==int(input('enter your choice to search students by 1. student ID 2. Students Name:-\n '))
        if pr_rd_sh==1:
            print('Access student by its ID...')
            user_sid=int(input('enter student id want to search:- '))
            for sobj in students:
                if user_id==sobj.sid:
                    sobj.display()
        elif pr_rd_sh==2:
            print('Access student by its NAME')
            user_sname=input('enter student name wAnt to search:- ')
            for sobj in students:
                if user_sname==sobj.sname:
                    sobj.display()
        else:
            print("ENter VALID choice To read STudents")

def update_student():
    print()
    print('------- UPDATE SECTION--------')
    print('updating students by name')
    user_up_sid=int(input(' Enter Students id want to update:- '))
    for sobj in studets:
        if user_up_sid==sobj.sid:
            sobj.name=input('enter Updated Student Name:- ')
            print('The updated student name is ',sobj.name)
def delete_student():
    print()
    print('-------STUDENT DELETE SECTION--------')
    prtu_del_sh=int(input('enter choice want to delete student by 1. student id 2. student name:- '))
    if prtu_del_sh==1:
        print('delete by student id')
        for sobj in students:
            user_sid=int(input('enter student id want to delete:- '))
            if user_sid==sobj.sid:
                students.remove(sobj)
                print('Student deleted Successfully....!')
                print()
                
    elif prtu_del_sh==2:
        print('delete by student name')
        user_sname=input('enter student name want to delete')
        for sobj in students:
            if user_sname==sobj.sname:
                students.remove(sobj)
            print('Student Deleted Successfully..!')
            print()
            
    else:
        print('enter valid choice to delete')
        print()
            
            


print("Welcome TO Student Managemnt System ")
username=input('Enter username :- ')
password=input('enter Password :- ')
if username=="admin" and password=="Admin@123":
    print('Welcome ADMIN to Student managemnt system of SKIILS ACADEMY \n')
    ad_ch=int(input('1. Courses \t 2. Batches \t 3. Students \t 4. Exit \n Enter CHoice want to continue WIth..:- '))
    if ad_ch==1:
        print("COURSES Section OF SKILLS ACADEMY")
        ad_course_ch=int(input('1. Add Courses \t 2. Read courses \t 3. Update Courses \t 4. Delete Courses \n Enter CHoice want to continue WIth..:- '))
        if ad_course_ch==1:
            add_course()
        elif ad_course_ch==2:
            read_course()
        elif ad_course_ch==3:
            update_course()
        elif ad_course_ch==4:
            delete_course()
        else:
            print('invalid choice! \t Enter the valid choice')
        
    elif ad_ch==2:
        print("BATCHES Section OF SKILLS ACADEMY")
        ad_batch_bh=int(input('1. Add batch \t 2. Read batches \t 3. Update batches \t 4. Delete batches \n Enter CHoice want to continue WIth..:- '))
        if ad_batch_bh==1:
            add_batch()
        elif ad_batch_bh==2:
            read_batch()
        elif ad_batch_bh==3:
            update_batch()
        elif ad_batch_bh==4:
            delete_batch()
        else:
            print('invalid choice! \t Enter the valid choice')
    elif ad_ch==3:
        print("STUDENTS Section OF SKILLS ACADEMY")
        ad_student_sh=int(input('1. Add STudents \t 2. Read Students \t 4. Delete Students \n Enter CHoice want to continue WIth..:- '))
        if ad_student_sh==1:
            add_student()
        elif ad_student_sh==2:
            read_student()
        #elif ad_student_sh==3:
           # update_student()
        elif ad_student_sh==4:
            delete_student()
        else:
            print('invalid choice! \t Enter the valid choice')

    elif ad_ch==4:
        print('Exiting from Application ....!')
        break
        
    else:
        print('Enter valid choice!!!!')


#------------------------------------------------------------------------------------------------------------
        
else:
    print('Welcome Students to Student managemnt system of SKIILS ACADEMY \n')
    stud_ch=int(input('1. Courses \t 2. Batches \t 3. Students \n Enter CHoice want to continue WIth..:- '))
    if stud_ch==1:
        print("COURSES SECTION OF SKILLS ACADEMY")
        stud_course_ch=int(input('1. Read courses \n Enter CHoice want to continue WIth..:- '))
        if stud_course_ch==1:
            read_course()
        else:
            print('invalid choice! \t Enter the valid choice')
        
    elif ad_ch==2:
        print("BATCHES SECTION OF SKILLS ACADEMY")
        stud_batch_bh=int(input('1. Read batches \n Enter CHoice want to continue WIth..:- '))
        if stud_batch_bh==1:
            read_batch()
        else:
            print('invalid choice! \t Enter the valid choice')
    elif ad_ch==3:
        print("STUDENTS SECTION OF SKILLS ACADEMY")
        stud_student_sh=int(input('1. Read Students \t 2. Update Students \n Enter CHoice want to continue WIth..:- '))
        #if stud_student_sh==1:
         #   add_student()
        if stud_student_sh==1:
            read_student()
        elif stud_student_sh==2:
            update_student()
        #elif stud_student_sh==4:
         #   delete_student()
        else:
            print('invalid choice! \t Enter the valid choice')
        
    else:
        print('Enter valid choice!!!!') 
    
        
'''while True:
    user_while_choice=int(input('1. 1. add course \t   \n enter ur choice:- ')
    add_course()
    add_course()
    
    read_course()
    
    update_course()
    read_course()
    
    delete_course()
    delete_course()


while True:
    add_batch()
    add_batch()
    
    read_batch()
    
    update_batch()
    read_batch()
    
    delete_batch()
    delete_batch()'''
    

