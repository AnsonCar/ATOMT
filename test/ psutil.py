import psutil

while (True):
    # CPU的使用情况
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f'CPU usage: {cpu_percent}%')

    # 内存使用情况
    mem_info = psutil.virtual_memory()
    print(f'Total memory: {mem_info.total / (1024**3):.2f} GB')
    print(f'Used memory: {mem_info.used / (1024**3):.2f} GB')
    print(f'Memory usage: {mem_info.percent}%')
    
    # 磁盘的使用情况
    disk_usage = psutil.disk_usage('/')
    print(f'Total disk space: {disk_usage.total / (1024**3):.2f} GB')
    print(f'Used disk space: {disk_usage.used / (1024**3):.2f} GB')
    print(f'Disk usage: {disk_usage.percent}%')
    
    # 系统中运行的所有进程的信息
    pids = psutil.pids()
    print(f'Total processes: {len(pids)}')
    
    
# 获取电脑整体的CPU、内存占用情况
def getMemory():
    data = psutil.virtual_memory()
    memory = str(int(round(data.percent))) + "%"
    print("系统整体memory占用:"+memory)
    return memory


def getCpu():
    cpu_list=psutil.cpu_percent(percpu=True)
    average_cpu = round(sum(cpu_list) / len(cpu_list),2)
    cpu=str(average_cpu) + "%"
    print("系统整体cpu占用:"+cpu)
    return cpu

# 获取指定进程的CPU和内存占用信息代码
def getMemSize(pid):
    # 根据进程号来获取进程的内存大小
    process = psutil.Process(pid)
    memInfo = process.memory_info()

    # rss: 该进程实际使用物理内存（包含共享库占用的全部内存）。
    # vms：该进程使用的虚拟内存总量。

    return memInfo.rss / 1024 / 1024

def getCpuPercent(pid):
    # 根据进程号来获取进程的内存大小
    p = psutil.Process(pid)
    p_cpu = p.cpu_percent(interval=0.1)
    cpu = round(p_cpu,2)
    return cpu

def getTotalM(processName):
    # 一个进程名对应的可能有多个进程
    # 进程号才是进程的唯一标识符，进程名不是
    totalM = 0
    for i in psutil.process_iter():
        if i.name() == processName:
            totalM += getMemSize(i.pid)
    print('进程占用内存：%.2f MB' % totalM)
    finalM=round(totalM,2)
    return finalM

def getTotalCPU(processName):
    # 一个进程名对应的可能有多个进程
    # 进程号才是进程的唯一标识符，进程名不是
    totalCPU = 0
    for i in psutil.process_iter():
        if i.name() == processName:
            totalCPU += getCpuPercent(i.pid)
    totalCPU_convert=round(totalCPU,2)
    finalCPU=str(totalCPU_convert)+'%'
    print("进程占用CPU："+finalCPU)
    return totalCPU_convert