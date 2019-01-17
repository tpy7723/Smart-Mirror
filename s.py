from flask import Flask
from flask_socketio import SocketIO, emit
from bs4 import BeautifulSoup # 크롤링
import requests
import threading
import sys
import eventlet
eventlet.monkey_patch() # 비동기식 프로그래밍

app = Flask(__name__)
socketio = SocketIO(app)

global data
data = []

def sayhi():
    global data
    threading.Timer(1.0, sayhi).start() # 특정 함수를 지정된 시간 간격으로 재실행

    r = requests.get('https://www.acmicpc.net/status')
    soup = BeautifulSoup(r.text, 'html.parser') # r.text는 html 코드  / 
    table = soup.find('table')  #find_all(name, attrs, recursive, string, limit, **kwargs) 해당 조건에 맞는 모든 태그들을 가져온다.
                                #find(name, attrs, recursive, string, **kwargs) 해당 조건에 맞는 하나의 태그를 가져온다. 중복이면 가장 첫 번째 태그를 가져온다.
                                #table 태그만 가져온다
    data2 = []
    for tr in table.find_all('tr'):
        info = []
        for td in tr.find_all('td'):
            info.append(td.get_text())
        data2.append(info)
    data = data2
    print (data[1])        #['11409327', 'lalalalz', '13549', '틀렸습니다', '', '', 'C++14', '878', '2초 전']

    socketio.emit('mise', {'data': data}) # 데이터 전송

@socketio.on('mise') # 해당 데이터를 받으면 아래 함수 실행
def test_message():
    print ('start')
    socketio.emit('mise', {'data': data})
    

if __name__ == '__main__':
    sayhi()
    socketio.run(app)