import pandas as pd
import folium
tiles = "https://map.pstatic.net/nrb/styles/basic/1694139974/{z}/{x}/{y}.png?mt=bg.ol.ts.lko"
# 속성 설정
attr = "Navvvver"
# 지도 객체 생성
m = folium.Map(location = [37.55,126.98],
               zoom_start = 13,               
               attr = attr)
folium.Marker(location = [37.55,126.98]).add_to(m)





m.save('mmmm.html')