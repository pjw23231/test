def ox_academic_system_copy():#학사제도
    ox_academic_system = [] 
    with open('text/quiz/ox_academic_system.txt', encoding='utf-8') as f:   # txt파일 열기
        while True:
            line = f.readline() # 줄 바꿈있을 때 까지 문자열 읽어 오기 열기
            if not line:
                break
            question = line[:-3]    # line 첫번째 부터 끝 3번째 줄까지 읽어오기
            answer = (line[-2:]).strip(' \n')   # line 끝 1번째에서 끝까지 읽어오기 
            if question[-1] != '.': # 끝에 마침표 없으면 
                question = question + '.'   # 마침표 추가
            line = [question, answer]    # 리스트로 만들어 변수 추가
            ox_academic_system.append(line) 
    ox1 = ox_academic_system.copy()
    return ox1

def ox_school_bus_copy():# 통학버스
    ox_school_bus = []
    with open('text/quiz/ox_school_bus.txt', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            question = line[:-3]
            answer = (line[-2:]).strip(' \n')
            if question[-1] != '.':
                question = question + '.'
            line = [question, answer]    
            ox_school_bus.append(line)
    ox2 = ox_school_bus.copy()
    return ox2

def ox_scholarship_on_campus_copy():    # 장학금
    ox_scholarship_on_campus = []
    with open('text/quiz/ox_scholarship_on_campus.txt', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            question = line[:-3]
            answer = (line[-2:]).strip(' \n')
            if question[-1] != '.':
                question = question + '.'
            line = [question, answer]    
            ox_scholarship_on_campus.append(line)
    ox3 = ox_scholarship_on_campus.copy()
    return ox3

def ox_campus_building_copy():  # 캠퍼스
    ox_campus_building = []
    with open('text/quiz/ox_campus_building.txt', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            question = line[:-3]
            answer = (line[-2:]).strip(' \n')
            if question[-1] != '.':
                question = question + '.'
            line = [question, answer]    
            ox_campus_building.append(line)
    ox4 = ox_campus_building.copy()
    return ox4

def ox_academic_system_commentary():    # 학사제도
    infile = open("text/commentary/academic_system_commentary.txt", "r", encoding='utf-8')
    academic_system_commentary = []
    for line in infile:
        t = []
        line = line.rstrip()    # 읽어올 때, 오른쪽 공백문자(\n) 제거
        t.append(line)
        academic_system_commentary.append(t)
    infile.close() 
    commentary1 = academic_system_commentary.copy()
    return commentary1

def ox_school_bus_commentary():
    infile = open("text/commentary/school_bus_commentary.txt", "r", encoding='utf-8')
    school_bus_commentary = []
    for line in infile:
        t = []
        line = line.rstrip()    # 읽어올 때, 오른쪽 공백문자(\n) 제거
        t.append(line)
        school_bus_commentary.append(t)
    infile.close() 
    commentary2 = school_bus_commentary.copy()
    return commentary2

def ox_scholarship_on_campus_commentary():
    infile = open("text/commentary/scholarship_on_campus_commentary.txt", "r", encoding='utf-8')
    scholarship_on_campus_commentary = []
    for line in infile:
        t = []
        line = line.rstrip()    # 읽어올 때, 오른쪽 공백문자(\n) 제거
        t.append(line)
        scholarship_on_campus_commentary.append(t)
    infile.close() 
    commentary3 = scholarship_on_campus_commentary.copy()
    return commentary3

def ox_campus_building_commentary():
    infile = open("text/commentary/campus_building_commentary.txt", "r", encoding='utf-8')
    campus_building_commentary = []
    for line in infile:
        t = []
        line = line.rstrip()    # 읽어올 때, 오른쪽 공백문자(\n) 제거
        t.append(line)
        campus_building_commentary.append(t)
    infile.close() 
    commentary4 = campus_building_commentary.copy()
    return commentary4