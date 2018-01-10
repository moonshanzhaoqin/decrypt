import sys

reload(sys)
import MySQLdb
import datetime

import sys

sys.path.append('D://hive-0.10.0-bin//lib//py')
from hive_service import ThriftHive
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

hive_server_ip = '54.215.228.50'
# hive_server_ip = '10.0.1.10'
hive_server_port = 10000


def hiveExe(sql):
    try:
        transport = TSocket.TSocket(hive_server_ip, hive_server_port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = ThriftHive.Client(protocol)

        transport.open()

        client.execute(sql)

        # print "The return value is : "
        result = client.fetchAll()
        #         print result
        #         print "............",len(result)
        transport.close()
        return result
    except Thrift.TException, tx:
        print '%s' % (tx.message)


if __name__ == '__main__':

    # strSQL = sys.argv[1]
    # strFileName = sys.argv[2]
    # strSQL = "select firstName,lastName,facebookId,sex,language,registerDate,lastLoginDate from player";
    strFileName = 'D://Facebookid.txt'
    file = open(strFileName, 'r')
    try:
        arrFacebookId = file.readlines()

    finally:
        file.close()

    arrInfo = []
    for fbId in arrFacebookId:
        sumRewardSQL = "select sum(amount/100),activitydetails from goc_oplog.log_playerbalanceactivity where facebookid="
        sumRewardSQL += str(fbId)
        sumRewardSQL += "and activityname='Reward' and p_date>'2014-08-05' and P_date<'2015-02-03' group by activitydetails"
        # select sum(amount/100),activitydetails from goc_oplog.log_playerbalanceactivity where facebookid=100002293496767 and activityname='Reward' and p_date>'2014-08-05' and P_date<'2015-02-03' group by activitydetails;
        print sumRewardSQL;
        newInstallsResult = hiveExe(sumRewardSQL)
        print "sumRewardSQL", newInstallsResult
        arrInfo.append(newInstallsResult)

        newInstallsCount = len(newInstallsResult)
        print "sumRewardSQL", newInstallsCount

        facebookIdList = str(newInstallsResult)
        facebookIdList = facebookIdList.replace("[", "(")
        facebookIdList = facebookIdList.replace("]", ")")

        print arrInfo

    result = open('d://fbInfo.txt', 'w')
    for arr in arrInfo:
        result.write(arr)
        result.write("\n")
    result.close()