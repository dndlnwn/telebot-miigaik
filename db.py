import sqlite3 as sq
import sys
name = ""
bak =''
spec = ''
with sq.connect("db.db") as con:
    cur = con.cursor()
    all_spec = ' '
    cur.execute("""CREATE TABLE IF NOT EXISTS bakalavr (
        name_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        prof_link TEXT,
        examinations TEXT,
        budgetary_place INTEGER,
        contract_place INTEGER,
        coast INTEGER
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS sprciality (
        name_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        prof_link TEXT,
        examinations TEXT,
        budgetary_place INTEGER,
        contract_place INTEGER,
        coast INTEGER
    )""")
    cur.execute("SELECT * FROM bakalavr")
    all_rezults_bak = cur.fetchall()
    cur.execute("SELECT * FROM sprciality")
    all_rezults_spec = cur.fetchall()
    #for i in range(0,3):
        #bak_2 = all_rezults_bak[i][1]+ "\n " + all_rezults_bak[i][2]+ "\n " + all_rezults_bak[i][3]+ "\n " + str(all_rezults_bak[i][4])+ "\n " + str(all_rezults_bak[i][5])+ "\n " + str(all_rezults_bak[i][6])+ "\n "
    #for i in range(2):
        #bak_2 = all_rezults_bak[i][1]+ "\n " + all_rezults_bak[i][2]+ "\n " + all_rezults_bak[i][3]+ "\n " + str(all_rezults_bak[i][4])+ "\n " + str(all_rezults_bak[i][5])+ "\n " + str(all_rezults_bak[i][6])+ "\n "
    with sq.connect('db.db') as db:
        cur = db.cursor()
        querty = """ SELECT * FROM bakalavr"""
        cur.execute(querty)
        for res in cur:
            if res == '(':
                res = '' + bak
            elif res == ')':
                res='' + bak
            elif res==',':
                res='' + bak
            else:
                bak = bak + str(res) + "\n"
        result_bak = ''
        res_bak = bak.replace('(', '') 
        res_bak = res_bak.replace(')', '') 


        specquerty = """ SELECT * FROM sprciality"""
        cur.execute(specquerty)
        for i in cur:
            if i == '(':
                i = '' + bak
            elif i == ')':
                i = '' + bak
            elif i == ',':
                i = '' + bak
            else:
                spec = spec + str(i) + "\n"
        result_spec = ''
        result_spec = spec.replace('(', '') 
        result_spec = result_spec.replace(')', '') 
    print (res_bak)

