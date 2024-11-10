#imports needed
from tkinter import * 
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests

#main window functions
def f3() : 
	mw.withdraw()
	aw.deiconify()
def f6() : 
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0, END)	
	con = None
	try : 
		con = connect("lms.db")
		cursor = con.cursor()
		sql = "select * from books"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data : 
			info = info + "Id:" + str(d[0]) + " |" +" Name:" + str(d[1] + " |" + " Price:"+ str(d[2])+ " Count:"+ str(d[3])+ "\n")
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
def f8() : 
	mw.withdraw()
	uw.deiconify()
def f11() : 
	mw.withdraw()
	dw.deiconify()
def f14() : 
	mw.withdraw()
	gw.deiconify()
	
#add window functions
def f4() : 
	con = None
	try : 
		con = connect("lms.db")
		cursor = con.cursor()
		sql = "insert into books values('%d', '%s', '%f', '%d')"
		Id = int(aw_ent_id.get())
		if Id<1:   		# only id greater then 0 allowed start from 1
			raise Exception("Id should contain positive Integer only")
		name = aw_ent_name.get()
		if not(name.isalpha()) :	#in name no other then alphabet/letter allowed
			raise Exception("Name should contain letters only")
		elif len(name)<2 :		#length of name 2 minimum complusory
			raise Exception("Name should contain atleast 2 letters")
		price = float(aw_ent_price.get())	
		if price<=0 : 
			raise Exception("price cannot be empty or 0")
		copies = int(aw_ent_copies.get())
		if copies<0:   		
			raise Exception("Copies of book cannot be negative")
		cursor.execute(sql%(Id, name, price, copies))
		con.commit()
		showinfo("Success", "Record Created")
	except ValueError:		#id&salary cannot be empty
		con.rollback()
		showerror("Issue", "Field cannot be empty")
	except Exception as e :
		con.rollback()
		showerror("Issue", e)
	finally:
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_price.delete(0,END)
		aw_ent_copies.delete(0,END)
		aw_ent_id.focus()
		if con is not None:
			con.close()
def f5() : 
	aw.withdraw()
	mw.deiconify()

#view window function
def f7() : 
	vw.withdraw()
	mw.deiconify()

#update window function
def f9() : 
	con = None
	try : 
		con = connect("lms.db")
		cursor = con.cursor()
		sql = "update books set name='%s', price='%f', copies='%d' where id='%d'"
		Id = int(uw_ent_id.get())
		if Id<1:   		# only id greater then 0 allowed start from 1
			raise Exception("Id should contain positive Integer only")
		name = uw_ent_name.get()
		if not(name.isalpha()) :	#in name no other then alphabet/letter allowed
			raise Exception("Name should contain letters only")
		elif len(name)<2 :		#length of name 2 minimum complusory
			raise Exception("Name should contain atleast 2 letters")
		price = float(uw_ent_price.get())	
		if price<=0 : 
			raise Exception("salary cannot be empty or 0")
		copies = int(uw_ent_copies.get())
		if copies<0:   		
			raise Exception("Copies of book cannot be negative")		
		cursor.execute(sql%(name, price, copies,Id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Updated")
		else:
			showinfo("Failure", id," Does not exists")
	except ValueError:
		con.rollback()
		showerror("Issue", "Field cannot be empty")
	except Exception as e :
		con.rollback()
		showerror("Issue", e)
	finally:
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_price.delete(0,END)
		uw_ent_copies.delete(0,END)
		uw_ent_id.focus()
		if con is not None:
			con.close()		
def f10() : 
	uw.withdraw()
	mw.deiconify()

#delete window function
def f12() : 
	con = None
	try : 
		con = connect("lms.db")
		cursor = con.cursor()
		sql = "delete from books where id='%d'"
		Id = int(dw_ent_id.get())
		if Id<1:
			raise Exception("Id should contain positive Integer only")
		cursor.execute(sql%(Id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Deleted")
		else:
			showinfo("Failure", id," Does not exists")
	except ValueError :
            con.rollback()
            showerror("Issue", "Field cannot be empty")
	except Exception as e :
            con.rollback()
            showerror("Issue", e)
	finally:
            dw_ent_id.delete(0,END)
            dw_ent_id.focus()
            if con is not None:
                con.close()
def f13() : 
	dw.withdraw()
	mw.deiconify()

#MAIN WINDOW
mw = Tk()
mw.title("  L . M . S  ")
mw.geometry("900x650+50+50")
mw.configure(bg="lightgreen")
f = ("Courier", 18, "bold")
mw_lbl = Label(mw, text ="  Library Management System  ", font=f, bg="lightgreen", width=50)
mw_btn_add = Button(mw, text="ADD DETAILS", font=f, width=20, command=f3)
mw_btn_view = Button(mw, text="VIEW DETAILS", font=f, width=20, command=f6)
mw_btn_update = Button(mw, text="UPDATE DETAILS", font=f, width=20, command=f8)
mw_btn_delete = Button(mw, text="DELETE DETAILS", font=f, width=20, command=f11)
mw_lbl_loc = Label(mw, text ="Location : ", font=f, bg="lightgreen", width=20)
mw_ent_loc = Entry(mw,font=f)
mw_lbl_temp = Label(mw, text ="Temperature : ", font=f,  bg="lightgreen", width=20)
mw_ent_temp = Entry(mw, font=f)
mw_lbl.place(x=50, y = 30)
mw_btn_add.place(x=100, y = 140)
mw_btn_view.place(x=500, y = 140)
mw_btn_update.place(x=100, y = 270)
mw_btn_delete.place(x=500, y = 270)
mw_lbl_loc.place(x=100, y = 530)
mw_ent_loc.place(x=100, y = 570)
mw_lbl_temp.place(x=500, y = 530)
mw_ent_temp.place(x=500, y = 570)
#Location
try:
    wa = "https://ipinfo.io"
    res = requests.get(wa)
    data = res.json()
    city = data["city"]
    state = data["region"]
    mw_ent_loc.insert(15, str(city))
except Exception as e :
    showerror("Issue",e)
#Temperature 
try:
    a1 = "https://api.openweathermap.org/data/2.5/weather"
    a2 = "?q=" + city
    a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
    a4 = "&units=" + "metric"
    wa = a1 + a2 + a3 + a4
    res = requests.get(wa)
    data = res.json()
    temp = data["main"]["temp"]
    mw_ent_temp.insert(15, str(temp))
except Exception as e:
    showerror("Issue",e)

#ADD WINDOW
aw = Toplevel(mw)
aw.title("Create Book Record")
aw.geometry("900x650+50+50")
aw.configure(bg="lightblue")
aw_lbl_id = Label(aw, text="Enter Book Id :", font=f, bg="lightblue")
aw_ent_id = Entry(aw, font=f)
aw_lbl_name = Label(aw, text="Enter Book Name :", font=f, bg="lightblue")
aw_ent_name = Entry(aw, font=f)
aw_lbl_price = Label(aw, text="Enter Book Price :", font=f, bg="lightblue")
aw_ent_price = Entry(aw, font=f)
aw_lbl_copies = Label(aw, text="Enter Book copies :", font=f, bg="lightblue")
aw_ent_copies = Entry(aw, font=f)
aw_btn_save = Button(aw, text="Save", font=f, width=15, command=f4)
aw_btn_back = Button(aw, text="Back", font=f, width=15, command=f5)
aw_lbl_id.place(x=80,y=130)
aw_ent_id.place(x=500,y=130)
aw_lbl_name.place(x=80,y=230)
aw_ent_name.place(x=500,y=230)
aw_lbl_price.place(x=80,y=330)
aw_ent_price.place(x=500,y=330)
aw_lbl_copies.place(x=80,y=430)
aw_ent_copies.place(x=500,y=430)
aw_btn_save.place(x=130,y=550)
aw_btn_back.place(x=600,y=550)
aw.withdraw()

#VIEW WINDOW
vw = Toplevel(mw)
vw.title("View Book Record")
vw.geometry("900x650+50+50")
vw.configure(bg="lightgrey")
vw_st_data = ScrolledText(vw, width=45, height=13, font=f)
vw_btn_back = Button(vw, text="Back", font=f, width=15, command=f7)
vw_st_data.place(x=50, y = 50)
vw_btn_back.place(x=570, y= 530)
vw.withdraw()

#UPDATE WINDOW
uw = Toplevel(mw)
uw.title("Update Book Record")
uw.geometry("900x650+50+50")
uw.configure(bg="khaki1")
uw_lbl_id = Label(uw, text="Enter Book Id :", font=f, bg="khaki1")
uw_ent_id = Entry(uw, font=f)
uw_lbl_name = Label(uw, text="Enter Book Name :", font=f, bg="khaki1")
uw_ent_name = Entry(uw, font=f)
uw_lbl_price = Label(uw, text="Enter Book Price :", font=f, bg="khaki1")
uw_ent_price = Entry(uw, font=f)
uw_lbl_copies = Label(uw, text="Enter Book Copies :", font=f, bg="khaki1")
uw_ent_copies = Entry(uw, font=f)
uw_btn_save = Button(uw, text="Save", font=f, width=15, command=f9)
uw_btn_back = Button(uw, text="Back", font=f, width=15, command=f10)
uw_lbl_id.place(x=80,y=130)
uw_ent_id.place(x=500,y=130)
uw_lbl_name.place(x=80,y=230)
uw_ent_name.place(x=500,y=230)
uw_lbl_price.place(x=80,y=330)
uw_ent_price.place(x=500,y=330)
uw_lbl_copies.place(x=80,y=430)
uw_ent_copies.place(x=500,y=430)
uw_btn_save.place(x=130,y=550)
uw_btn_back.place(x=600,y=550)
uw.withdraw()

#DELETE WINDOW
dw = Toplevel(mw)
dw.title("Delete Book Record")
dw.geometry("900x650+50+50")
dw.configure(bg="orange")
dw_lbl_id = Label(dw, text="Enter Book Id :", font=f, bg="orange")
dw_ent_id = Entry(dw, font=f)
dw_btn_delete = Button(dw, text="Delete", font=f, width=15, command=f12)
dw_btn_back = Button(dw, text="Back", font=f, width=15, command=f13)
dw_lbl_id.place(x=80,y=170)
dw_ent_id.place(x=500,y=170)
dw_btn_delete.place(x=130,y=450)
dw_btn_back.place(x=600,y=450)
dw.withdraw()

def confirmExit() : 
	if askyesno('Confirm Exit', 'Are you sure you want to exit'):
		mw.destroy()
mw.protocol('WM_DELETE_WINDOW', confirmExit)
mw.mainloop()