'''
Created on Mar 13, 2015

@author: moon.shan
'''

if __name__ == '__main__':
    facebookId = [];
    buyFacebookId = [];

    f = file(r'D:\DBFacebook.txt')
    f2 = file(r'D:\buyFacebook.txt')
    f3 = open(r'D:\noBuy.txt', 'a')
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0:  # Zero length indicates EOF
            break
        facebookId.append(line.strip('\n'))

        # Notice comma to avoid automatic newline added by Python
    f.close()  #
    #     print facebookId,
    #     print len(facebookId)

    while True:
        line2 = f2.readline()
        if len(line2) == 0:
            break
        buyFacebookId.append(line2.strip('\n'))

    f.close()
    #     print facebookId
    #
    #     print len(facebookId)
    #     print buyFacebookId
    #
    #     print len(buyFacebookId)

    nobuy = []
    for buyid in facebookId:
        if buyid in buyFacebookId:
            continue
        else:
            nobuy.append(buyid)
            f3.write(buyid + '\n')
    f3.close()


