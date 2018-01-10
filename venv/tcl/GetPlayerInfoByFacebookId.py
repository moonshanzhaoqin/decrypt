import sys

reload(sys)
import MySQLdb
import datetime

DBhost_Production = "goc-production.cq7aluezktzp.us-west-1.rds.amazonaws.com"
DBhost_Testing = "testingdb.grandorientcasino.com"
DBuser = "root"
DBpasswd = "aspectqa"


class CDataBase:
    def __init__(self, host, user, passwd, dbname=""):
        try:
            self.conn = MySQLdb.connect(host, user, passwd, dbname, charset="utf8", use_unicode=1)
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def query(self, sql):
        lt = []
        n = self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            lt.append(row)
        return lt

    def execute(self, sql):
        n = self.cursor.execute(sql)
        self.conn.commit()
        return True

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':

    # strSQL = sys.argv[1]
    # strFileName = sys.argv[2]
    strSQL = "select firstName,lastName,facebookId,sex,language,registerDate,lastLoginDate from player";
    strFileName = 'd://fb.txt'
    file = open(strFileName, 'r')
    try:
        arrFacebookId = file.readlines()
        # print partFacebookId
    finally:
        file.close()

    arrInfo = []
    for fbId in arrFacebookId:
        temp = int(fbId) % 1024
        index = temp / 128
        index += 1
        dbNgame = "GOC_onlinegame" + str(index)
        # print "onlineDbGame:",dbNgame
        db = CDataBase(host=DBhost_Production, user=DBuser, passwd=DBpasswd, dbname=dbNgame)

        # sql = "select firstName,lastName,facebookId,sex,registerDate,lastLoginDate from player where facebookId="
        sql = strSQL
        sql += " where facebookId="
        sql += fbId

        # print "SQL:",sql
        lt = db.query(sql)
        if lt == None:
            continue
        for row in lt:
            info = ""
            for r in row:
                info += str(r)
                info += ","
            # print info
            arrInfo.append(info)

        db.close()

    # print arrInfo
    result = open('d://fbInfo.txt', 'w')
    for arr in arrInfo:
        result.write(arr)
        result.write("\n")
    result.close()

