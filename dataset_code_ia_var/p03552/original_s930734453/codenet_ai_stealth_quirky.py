import sys
exec('G=lambda:map(int,sys.stdin.readline().split());Q,P,S=G();Y=[*G()];print(max(abs(Y[Q-1]-S),abs(Y[Q-1]-Y[Q-2])))')