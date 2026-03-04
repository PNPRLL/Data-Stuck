import json

def findStations(stations, cities_needed):
    # แปลงรายชื่อเมืองที่ต้องการเป็น Set เพื่อให้ตัดเมืองที่ซ้ำออกได้ง่าย
    needed = set(cities_needed)
    final_stations = []
    
    # ทำไปเรื่อยๆ จนกว่าเราจะครอบคลุมครบทุกเมือง
    while len(needed) > 0:
        best_station = None
        covered_cities = set()
        
        # วนลูปหาสถานีที่ครอบคลุมเมืองที่เรากำลังต้องการ ได้จำนวนมากที่สุด
        for name, cities in stations.items():
            # ใช้ intersection เพื่อหาว่า สถานีนี้ คลุมเมืองที่เราต้องการได้กี่เมือง
            can_cover = needed.intersection(set(cities))
            # ถ้าคลุมได้เยอะกว่าสถานีที่ดีที่สุดในรอบนี้ ให้จดจำสถานีนี้ไว้
            if len(can_cover) > len(covered_cities):
                best_station = name
                covered_cities = can_cover

        # ถ้าไม่เหลือสถานีไหนที่คลุมเมืองที่เหลือได้แล้ว ให้หยุด
        if best_station is None:
            break
        # อัปเดตข้อมูล: หักเมืองที่คลุมไปแล้วออก และเก็บสถานีนี้เข้าคำตอบ
        needed -= covered_cities
        final_stations.append(best_station)

        # ลบสถานีที่เลือกไปแล้วออกจากตัวเลือก จะได้ไม่ต้องวนเช็คซ้ำให้เสียเวลา
        del stations[best_station]

    # เรียงลำดับชื่อสถานีแบบ A-Z โดยใช้ Bubble Sort
    n = len(final_stations)
    for i in range(n):
        for j in range(0, n - 1):
            if final_stations[j] > final_stations[j + 1]:
                # สลับตำแหน่งถ้าตัวหน้ามาก่อนตัวหลัง
                final_stations[j], final_stations[j + 1] = final_stations[j + 1], final_stations[j]
    return final_stations

def main():
    cities_input = json.loads(input())
    num_stations = int(input())
    # รับข้อมูลสถานีวิทยุทีละบรรทัด เก็บลง Dictionary
    stations_dict = {}
    for _ in range(num_stations):
        data = json.loads(input())
        # กำหนด Key คือชื่อสถานี และ Value คือลิสต์ของเมือง
        stations_dict[data["Name"]] = data["Cities"]
    result = findStations(stations_dict, cities_input)
    print(result)

main()