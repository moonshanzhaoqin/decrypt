import sys

# from py import *
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
    print "start"
    output = open('data.txt', 'w')
    # gameIdList=["1","2","3","4","5","6","11","12","13","16","17","18","19","20","23","24","25","28","29","30"]
    gameIdList = ["18", "19", "20", "23", "24", "25", "28", "29", "30"]
    for i in range(31, 74):
        gameIdList.append(str(i))
    for i in range(75, 88):
        gameIdList.append(str(i))
    print gameIdList

    gameIdList = ["17"]
    newInstallsSQL = "select (facebookId) from goc_oplog.log_playerdailylogin where userregisterdate='2014-01-15 00:00:00' and clienttype=0 and p_date='2014-01-15'"
    newInstallsResult = hiveExe(newInstallsSQL)
    newInstallsCount = len(newInstallsResult)
    print "newInstallsCount", newInstallsCount

    facebookIdList = str(newInstallsResult)
    facebookIdList = facebookIdList.replace("[", "(")
    facebookIdList = facebookIdList.replace("]", ")")

    arr = []
    for gameId in gameIdList:
        output.write('---------gameId----------:')
        output.write(gameId)
        output.write('\n')
        print "---------gameId----------", gameId
        # GameDAU,spin Count,Coins Played
        gameInfoSQL = "select count(distinct facebookId),count(*),sum(bet) from goc_oplog.log_gamehistory where facebookId in "
        gameInfoSQL += facebookIdList
        gameInfoSQL += " and gameid='"
        gameInfoSQL += gameId
        gameInfoSQL += "' and p_date='2014-01-15'"
        gameInfoResult = hiveExe(gameInfoSQL)

        print 'gameDAUResult,spinCountSQLResult,CoinsPlayedSQLResult:', gameInfoResult
        string2 = 'gameDAUResult,spinCountSQLResult,CoinsPlayedSQLResult:'
        string2 += str(gameInfoResult)

        output.write(string2)
        output.write('\n')
    output.close()
    print "end"