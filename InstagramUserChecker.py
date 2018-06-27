#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python: 2
# Version: 1.0
# Cyber_Soldiers_Security_Team: CSST
# link: https://t.me/CyberSoldiersST
# Github: github.com/SarbazVatan
# Coded By @Soldier_of iran

import threading, Queue, requests, sys, re
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

print '''



      :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+      
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`   
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'  
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@, 
 @@@@#  << Instagram-User-Checker >> .@@@@ 
 @@@#                           #@@@@.`@@@'
:@@@              * CSST *     :@@@@@@ @@@@
@@@@                           :@@@@@@ .@@@
@@@@                .::`       :@@@@@@  @@@
@@@@            ,@@@@@@@@@'    :@@@@@@  @@@
@@@@          `@@@@@@@@@@@@@+  :@@@@@@  @@@
@@@@         #@@@@@@@@@@@@@@@@  @@@@@:  @@@
@@@@        @@@@@@.      #@@@@@         @@@
@@@@       #@@@@`          @@@@@        @@@
@@@@      `@@@@             #@@@@       @@@
@@@@@@@@@@@@@@      :++`     @@@@@@@@@@@@@@
@@@@@@@@@@@@@`      ,@@@@`    @@@@@@@@@@@@@
@@@@@@@@@@@@@         @@@@.   :@@@@@@@@@@@@
@@@@@@@@@@@@.         #@@@@    @@@@@@@@@@@@
@@@@@@@@@@@@          ;@@@@+   @@@@@@@@@@@@
@@@@@@@@@@@@   :,     @@@@@@   +@@@@@@@@@@@
@@@@@@@@@@@@   +@    .@@@@@@   ;@@@@@@@@@@@
@@@@@@@@@@@@   +@@#;@@@@@@@@   +@@@@@@@@@@@
@@@@@@@@@@@@   `@@@@@@@@@@@@   @@@@@@@@@@@@
@@@@@@@@@@@@    @@@@@@@@@@@    @@@@@@@@@@@@
@@@@@@@@@@@@#   `@@@@@@@@@#   `@@@@@@@@@@@@
@@@@@@@@@@@@@    .@@@@@@@#    @@@@@@@@@@@@@
@@@@@@@@@@@@@@     +@@@@     :@@@@@@@@@@@@@
@@@@@@@@@@@@@@#             `@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@           :@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@,       `@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@+;+@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
 `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# 
  '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   
     '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     
        [By]: Sarbaz_Vatan
'''
def check(q):
    while 1:
        user = q.get()
        if user != None:
            try:
                url = "http://instagram.com/"+user
                source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'})
                if source.status_code == 200:
                    bs = BeautifulSoup(source.text, 'lxml')
                    allmeta = bs.find_all("meta")
                    spliter = str(allmeta[12]['content']).split(' ')
                    checked.append('{USER} | {FOLLOWERS} | {FOLLOWINGS} | {POSTS}'.format(USER=user, FOLLOWERS=spliter[0], FOLLOWINGS=spliter[2], POSTS=spliter[4]))
                    print '\n\n[Username]: {0}\n[Followers]: {1}\n[Followings]: {2}\n[Posts]: {3}'.format(user, spliter[0], spliter[2], spliter[4])
                    q.task_done()
                else:
                    print "\n[-]Check your connection and try again..."
            except:
                print '\n\n[Timeout]'
                q.task_done()
        else:
            q.task_done()

def sort(i):
    for x in checked:
        if i == 1:
            users_by_sort[x] = int(str(x.split(' | ')[1]).replace(',', '').replace('.', '').replace('k', '0'*3).replace('m', '0'*6))
        elif i == 2:
            users_by_sort[x] = int(str(x.split(' | ')[2]).replace(',', '').replace('.', '').replace('k', '0'*3).replace('m', '0'*6))
        elif i == 3:
            users_by_sort[x] = int(str(x.split(' | ')[3]).replace(',', '').replace('.', '').replace('k', '0'*3).replace('m', '0'*6))
    LIST_1 = users_by_sort.values()
    for n in range(len(LIST_1)):
        max_number = max(LIST_1)
        for k in users_by_sort.keys():
            if users_by_sort[k] == max_number:
                final.append(k)
        LIST_1.remove(max_number)
    save_checks(final)


def save_checks(LIST):
    with open('results.txt', 'a') as rs:
        for x in LIST:
            rs.write('\n'+str(x))
    rs.close()

def start_thread():
    global input_queue
    global checked
    global final
    global users_by_sort
    for x in range(thread):
        aa = threading.Thread(target=check, args=(input_queue,))
        aa.setDaemon(True)
        aa.start()
    for xx in open(user_list, 'r').readlines():
        input_queue.put(str(xx).strip())
    input_queue.put(None)
    input_queue.join()

if __name__ == "__main__":
    input_queue = Queue.Queue()
    checked = []
    users_by_sort = {}
    final = []
    user_list = raw_input("\a\n[#]UsersList: ")
    thread = int(raw_input("[+]Thread: "))
    print '''\n[*]Sort by:\n\t[1]Followers\n\t[2]Followings\n\t[3]Posts'''
    num = input(">>> ")
    save_results = open('results.txt', 'a')
    save_results.write('\n\n\n<<< Username | Followers | Followings | Posts >>>\n\n')
    save_results.close()
    start_thread()
    sort(num)
    raw_input("\n\n\a[~]Job Finished :D")

