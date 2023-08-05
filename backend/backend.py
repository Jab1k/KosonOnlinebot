
import mysql.connector
import requests as r
res = {}
def getgroup(name: str):
    if name == '🛒Gulmira Market':
        db = mysql.connector.connect(
            host='176.96.243.56',
            user='easytrade',
            database='gulmira_db',
            port='3306',
            password='masterkey'
        )
        mycrsor = db.cursor()
        mycrsor.execute("""
                select dir_goods.gd_name, dir_groups.grp_name from dir_goods left join dir_groups on dir_goods.gd_group = dir_groups.grp_id
                	""")
        datas = mycrsor.fetchall()
        for m in datas:
            r = res.get(m[1], [])
            r.append(m[0])
            res[m[1]] = r
        return res
    elif name == "🍔Bursa HALLAL FOOD":
        db = mysql.connector.connect(
            host='176.96.243.56',
            user='easytrade',
            database='bursa_db',
            port='3306',
            password='masterkey'
        )
        mycrsor = db.cursor()
        mycrsor.execute("""
                select dir_goods.gd_name, dir_groups.grp_name from dir_goods left join dir_groups on dir_goods.gd_group = dir_groups.grp_id
                	""")
        datas = mycrsor.fetchall()
        for m in datas:
            if m[1] == 'Корневая группа' or m[1] == "BURSA":
                continue
            else:
                r = res.get(m[1], [])
                r.append(m[0])
                res[m[1]] = r
        return res

    else:
        return {"kechirasiz":0}
def checkmahs(name: str):
    db = mysql.connector.connect(
    	host = '176.96.243.56',
	user='easytrade',
	database='gulmira_db',
	port='3306',
	password='masterkey'
	)
    mycrsor = db.cursor()
    mycrsor.execute("""
select dir_goods.gd_name, dir_prices.prc_value from dir_goods LEFT JOIN dir_prices ON dir_goods.gd_id = dir_prices.prc_good
	""")
    datas = mycrsor.fetchall()
    print(name)
    for i in range(len(datas)):
        if datas[i][0][0:18] == name:
            return datas[i][1]

    # -------------------------------
    db = mysql.connector.connect(
        host='176.96.243.56',
        user='easytrade',
        database='bursa_db',
        port='3306',
        password='masterkey'
    )
    mycrsor = db.cursor()
    mycrsor.execute("""
    select dir_goods.gd_name, dir_prices.prc_value from dir_goods LEFT JOIN dir_prices ON dir_goods.gd_id = dir_prices.prc_good
    	""")
    datas = mycrsor.fetchall()
    print(name)
    for i in range(len(datas)):
        if datas[i][0][0:18] == name:
            return datas[i][1]
    return 'Topilmadi!'
