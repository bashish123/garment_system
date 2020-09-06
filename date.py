# import sqlite3
# #backend db
#
# def Received_Challan():
#     con=sqlite3.connect("Received_Challan.db")
#     cursor=con.cursor()
#     command1 = """CREATE TABLE IF NOT EXISTS Received(id INTEGER PRIMARY KEY,DateTime Text,StyleNo TEXT,PartyName TEXT,Quantity INTEGER,PchallanNo INTEGER,LaundryName TEXT,ProgrammStatus TEXT, \
#                     Note TEXT)"""
#     cursor.execute(command1)
#     con.commit()
#     con.close()
#
# def addreceived_record(DateTime,StyleNo,PartyName,Quantity,PchallanNo,LaundryName,ProgrammStatus,Note):
#     con=sqlite3.connect("Received_Challan.db")
#     cur=con.cursor()
#     cur.execute("INSERT INTO Received_Challan VALUES (NULL, ?,?,?,?,?,?,?,? )",DateTime,StyleNo,PartyName,Quantity,PchallanNo,LaundryName,ProgrammStatus,Note)
#     con.commit()
#     con.close()

