import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#그래프 설정
fig = plt.figure()
ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000)) #x, y축 범위 설정

#공 만들기 (x좌표,y좌표), 공의 크기
ball= plt.Circle((0, 0), 20)

#초기 속도, 속도변화량 설정
vx = 10
vy = 25
ay = -0.5


def init():
    ax.add_patch(ball)
    return ball,

def animate(i):
    global vy
    
    (x, y) = ball.center #공의 중심 좌표를 x,y에 저장
    
    #속도와 속도 변화량 표현
    x = x + vx
    y = y + vy
    vy = vy + ay
    
    ball.center = (x, y) #변화된 x,y좌표를 공의 중심좌표로 저장

    return ball,

#애니메이션을 그리는 함수, interval값이 클수록 느리게 움직임
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=40, blit=True)
plt.show()