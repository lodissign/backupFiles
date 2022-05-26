# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys, select, tty, termios
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    key_pub=rospy.Publisher('keys', String, queue_size=1)
        # 이름: keys, 메세지 type: String 인 Publisher를 만듦.
    rospy.init_node("keyboard_driver")
        # 이름: keyboard_driver 인 노드를 생성.
    rate=rospy.Rate(100)
    old_attr=termios.tcgetattr(sys.stdin)
        # 현재 설정 값(콘솔은 전체 텍스트 줄을 버퍼에 넣어 사용자가 엔터 키를 누를 때 프로그램으로
        # 보내 준다.)을 old_attr에 저장.
    tty.setcbreak(sys.stdin.fileno())
        # 누르자마자 곧바로 프로그램의 표준 입력 스트림으로 키를 받도록 설정 변경.
    print ("Publishing keystrokes. Press Ctrl-C to exit...")
    while not rospy.is_shutdown():
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
        # old_attr 에 저장된 원래 설정 값으로 되돌려 줌.