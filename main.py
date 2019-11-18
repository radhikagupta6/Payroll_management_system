import time
import datetime
from tkinter import*
from tkinter import messagebox

root= Tk()
root.title("Payroll management system")
root.geometry("1500x650+0+0")
heads = Frame(root, width=1500, height=70, bd=5, relief="raise")
heads.pack(side= TOP)
f1=Frame(root, width=400, height=500, bd=5, relief="raise")
f1.pack(side=LEFT)
f2=Frame(root, width=100, height=500, bd=5, relief="raise")
f2.pack(side=RIGHT)
f1a=Frame(f1, width=500, height=200, bd=5, relief="raise")
f1a.pack(side=TOP)
f1b=Frame(f1, width=500, height=200, bd=5, relief="raise")
f1b.pack(side=TOP)
lbl1= Label(heads, font=('arial',55,'bold'),text="PAYROLL MANAGEMENT SYSTEM", bd=20)
lbl1.grid(row=0, column=0)
#====================================================================functions======================================================================================================
def quitt():
        quesquitt=messagebox.askyesno("PAYROLL MANAGEMENT SYSTEM","Would you like to quit ?")
        if quesquitt>0:
                root.destroy()
                return
def resetit():
        Name.set("")
        Address.set("")
        Employer.set("")
        HoursWorked.set("")
        WagesHour.set("")
        NINumber.set("")
        Payable.set("")
        NetPayable.set("")
        Taxable.set("")
        OvertimeHours.set("")



def EnterInfo():
        txtt1.insert(END,"\t\tPAY SLIP\n\n")
        txtt1.insert(END,"Name: \t\t"+Name.get()+"\n\n")
        txtt1.insert(END,"Address: \t\t"+Address.get()+"\n\n")
        txtt1.insert(END,"Employer: \t\t"+Employer.get()+"\n\n")
        txtt1.insert(END,"Hours Worked: \t\t"+HoursWorked.get()+"\n\n")
        txtt1.insert(END,"Wages per hour: \t\t"+WagesHour.get()+"\n\n")
        txtt1.insert(END,"NI number: \t\t"+NINumber.get()+"\n\n")
        txtt1.insert(END,"Payable: \t\t"+Payable.get()+"\n\n")
        txtt1.insert(END,"Net Payable: \t\t"+NetPayable.get()+"\n\n")
        txtt1.insert(END,"Tax Paid: \t\t"+Taxable.get()+"\n\n")

def Salaryy():
        Hrsworked=float(HoursWorked.get())
        wagesperhrs=float(WagesHour.get())
        paydue=Hrsworked*wagesperhrs
        paymentdue="INR",str('%.2f'%(paydue))
        Payable.set(paymentdue)
        
        tax=paydue*0.2
        taxablee="INR",str('%.2f'%(tax))
        Taxable.set(taxablee)

        netpay=paydue-tax
        netpays="INR",str('%.2f'%(netpay))
        NetPayable.set(netpays)

        if Hrsworked>40:
                OvertimeHourss=(Hrsworked-40)+wagesperhrs*1.5
                ovrtimehrs="INR",str('%.2f'%(OvertimeHourss))
                OvertimeHours.set(ovrtimehrs)

        elif Hrsworked <=40:
                overtimepayy=(Hrsworked-40)+wagesperhrs*1.5
                ovrtimehrs="INR",str('%.2f'%(overtimepayy))
                OvertimeHours.set(ovrtimehrs)

        return



#=================================================================variables=======================================================      

Name=StringVar()
Address=StringVar()
Employer=StringVar()
HoursWorked=StringVar()
WagesHour=StringVar()
NINumber=StringVar()
Payable=StringVar()
NetPayable=StringVar()
Taxable=StringVar()
OvertimeHours=StringVar()
DateofOrder=StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))
#====================================================================labels=======================================================================
label1=Label(f1a, text='Name', font=('arial',16,'bold'),bd=20).grid(row=0,column=0)
label2=Label(f1a, text='Address', font=('arial',16,'bold'),bd=20).grid(row=0,column=2)
label3=Label(f1a, text='Employer', font=('arial',16,'bold'),bd=20).grid(row=1,column=0)
label4=Label(f1a, text='NI Number', font=('arial',16,'bold'),bd=20).grid(row=1,column=2)
label5=Label(f1a, text='Hours Worked', font=('arial',16,'bold'),bd=20).grid(row=2,column=0)
label6=Label(f1a, text='Hourly Rate', font=('arial',16,'bold'),bd=20).grid(row=2,column=2)
label7=Label(f1a, text='Tax', font=('arial',16,'bold'),bd=20).grid(row=3,column=0)
label8=Label(f1a, text='OverTime', font=('arial',16,'bold'),bd=20).grid(row=3,column=2)
label9=Label(f1a, text='Gross Pay', font=('arial',16,'bold'),bd=20).grid(row=4,column=0)
label10=Label(f1a, text='Net Pay', font=('arial',16,'bold'),bd=20).grid(row=4,column=2)
#=====================================================Entry blocks==========================================================================================

txt1=Entry(f1a,textvariable=Name, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=0, column=1)
txt2=Entry(f1a,textvariable=Address, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=0, column=3)
txt3=Entry(f1a,textvariable=Employer, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=1, column=1)
txt4=Entry(f1a,textvariable=HoursWorked, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=2, column=1)
txt5=Entry(f1a,textvariable=WagesHour, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=2, column=3)
txt6=Entry(f1a,textvariable=NINumber, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=1, column=3)
txt7=Entry(f1a,textvariable=Payable, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=4, column=1)
txt8=Entry(f1a,textvariable=NetPayable, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=4, column=3)
txt9=Entry(f1a,textvariable=Taxable, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=3, column=1)
txt10=Entry(f1a,textvariable=OvertimeHours, font=('arial',16,'bold'),bd=16, width=22, justify='left').grid(row=3, column=3)
#=======================text widget for the pay slip================================================================================================================================================
lbl2=Label(f2, textvariable=DateofOrder, font=('arial',15,'bold')).grid(row=0, column=0)
txtt1=Text(f2,height=22, width=34, bd=5, font=('arial',12,'bold'))
txtt1.grid(row=1,column=0)
#=====================================buttons===================================================================================================================================================
btn1=Button(f1b, text='Weekly Salary', command=Salaryy,padx=12, pady=12, bd=8, fg='black', font=('arial',16,'bold'),width=10, height=1).grid(row=0, column=0)
btn2=Button(f1b, text='Reset', command= resetit,  padx=12, pady=12, bd=8, fg='black', font=('arial',16,'bold'),width=10, height=1).grid(row=0, column=1)
btn3=Button(f1b, text='Generate Slip',command=EnterInfo, padx=12, pady=12, bd=8, fg='black', font=('arial',16,'bold'), width=10,height=1).grid(row=0, column=2)
btn4=Button(f1b, text='Exit System',  command= quitt,padx=12, pady=12, bd=8, fg='black', font=('arial',16,'bold'),width=10,height=1).grid(row=0, column=3)
btn5=Button(f1b, text='Slip Reset',command=lambda: txtt1.delete('1.0', END),padx=12, pady=12, bd=8, fg='black', font=('arial',16,'bold'),width=10,height=1).grid(row=0, column=4)

root.mainloop()