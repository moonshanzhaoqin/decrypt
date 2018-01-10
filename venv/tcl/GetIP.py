class GetIP:

    u = "http://172.18.188.152:8080/pegasusmanager/jsp/awardsManager/freeTicketsList.jsp";
    print(u.replace("http://", ""));
    for i in range(0,5):
        print(u.replace("http://", "").split("/")[i]);
