import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(10000000):
        res += i+i**2+i**3
    q.put(res) # queue

def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
#     print('multicore:' , res1+res2)

def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i+i**2+i**3
#     print('normal:', res)

def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
#     print('multithread:', res1+res2)

def job2(x):
    return x*x

def multicore2():
    # pool可以直接返回,指定核的个数
    pool = mp.Pool(processes=2)
    res = pool.map(job2,range(10))
    print(res)
    res = pool.apply_async(job2,(2,))
    print(res.get())
# 这个不能迭代
#     res = pool.apply_async(job,(2,3,4,5))
    multi_res = [pool.apply_async(job2,(i,)) for i in range(10)]
    print([res.get() for res in multi_res])
    
def job3(v,num,l):
    l.acquire()
    time.sleep(2)
    v.value += num
    print(v.value)
    l.release()
    
def multicore3():
    l = mp.Lock()
        # 共享内存
    v = mp.Value('i',0)
#     array = mp.Array('i', [1,2,3])
    # pool可以直接返回,指定核的个数
    p1 = mp.Process(target=job3,args=(v,1,l))
    p2 = mp.Process(target=job3,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
if __name__ == '__main__':
    flag = '锁'
    if flag == '池化':
        multicore2()
    elif flag =='比较':     
        st = time.time()
        normal()
        st1= time.time()
        print('normal time:', st1 - st)
        multithread()
        st2 = time.time()
        print('multithread time:', st2 - st1)
        multicore()
        print('multicore time:', time.time()-st2)
    elif flag == '锁':
        multicore3()
