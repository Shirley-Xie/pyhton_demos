from multiprocessing import Process
import os

"""
多进程：multiprocessing
    Unix/Linux: fork()调用1次返回2次，将当前进程（父进程：返回子进程的ID）复制一份（子进程：返回0，调用getppid()拿到父进程ID）
    父进程fork很多子进程，像一个树干分出很多树杈，每个树杈都有ID
"""
# 很凌乱
# print('1,Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('1,I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('1,I (%s) just created a child process (%s).' % (os.getpid(), pid))

print('-------------------------------------------------------------------')

"""
跨平台：multiprocessing模块提供了一个Process类来代表一个进程对象
启动一个子进程并等待其结束
"""


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def starting():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

starting()