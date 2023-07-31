
classes_hexCode_dict = {
    'reception_desk': '5f52a0', 
    'table': 'eb6100', 
    'sofa': 'f39800', 
    'stand sign': 'fff100', 
    'first door': '8fc31f',   
    'the second door': '77a21a',
    '第三扇门': '5c7e14',
    '第四扇门': '46600f',
     
    'plant': '22ac38', 
    'railing': '009944', 
    'column3': '003734', 
    'column1': '009e96', 
    'column2': '006661', 
    
    'shelving': '00a0e9', 
    'desk': '00479d', 
    'wall': '1d2088', 
    'bucket': 'b28850', 
    'chair': '6a3906', 
    'computer': 'f6b37f', 
    # 'void': '000000',
    
}


to_list = {
    'reception_desk': '5f52a0', 
    'table': 'eb6100', 
    'sofa': 'f39800', 
    'stand sign': 'fff100', 
    'first door': '8fc31f',   
    'the second door': '77a21a',
    '三号门': '5c7e14',
    '第四扇门': 'fourth door,the fourth door,四号门',
     
    'plant': '22ac38', 
    'railing': '009944', 
    'column3': '003734', 
    'column1': '009e96', 
    'column2': '006661', 
    
    'shelving': '00a0e9', 
    'desk': '00479d', 
    'wall': '1d2088', 
    'bucket': 'b28850', 
    'chair': '6a3906', 
    'computer': 'f6b37f', 
    # 'void': '000000',
    
}

dict2list=[(key,value) for key,value in classes_hexCode_dict]




hx_json={
    {"usr_instr":"找张华把我的新杯子拿来","api":["取货任务.txt"]},
    {"usr_instr":"检查一下第一扇门","api":["前往某个地点.txt"]},
    {"usr_instr":"去第二扇门那里等我三分钟","api":["前往某个地点.txt","等待.txt"]},
    {"usr_instr":"去李红那里把我的面包拿给张华","api":["取货任务.txt","送货任务.txt"]},
    {"usr_instr":"我手机在沙发上吗？","api":["前往某个地点.txt"]},
    
    {"usr_instr":"去看看离第四扇门最近的植物","api":["前往某个地点.txt"]},
    {"usr_instr":"等待5分钟","api":["等待.txt"]},
    {"usr_instr":"清洁大厅","api":["清洁活动.txt"]},
    {"usr_instr":"送货到前台","api":["送货任务.txt"]},
    {"usr_instr":"去货架找李红取货送到前台张华那里","api":["取货任务.txt","送货任务.txt"]},
    
    {"usr_instr":"从货架找李红取货送到前台张华那里,等待5分钟;重复3次","api":["取货任务.txt","送货任务.txt","等待.txt","取货任务.txt","送货任务.txt","等待.txt","取货任务.txt","送货任务.txt","等待.txt"]},
    {"usr_instr":"去栏杆等待10分钟,然后去沙发等待5分钟","api":["前往某个地点.txt","等待.txt","前往某个地点.txt","等待.txt"]},
    {"usr_instr":"在第一扇门和第三扇门之间巡逻两次","api":["前往某个地点.txt","前往某个地点.txt","前往某个地点.txt","前往某个地点.txt",]},
    {"usr_instr":"去货架找李红取2件货,分别送到门口和沙发,然后返回前台","api":["取货任务.txt","送货任务.txt","送货任务.txt","前往某个地点.txt"]},
    {"usr_instr":"随机去2个地点(沙发、栏杆、门口、茶几等),然后回前台","api":["前往某个地点.txt","前往某个地点.txt","前往某个地点.txt"]},
}
        
    
    
    

