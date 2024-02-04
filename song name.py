"""
https://www.youtube.com/watch?v=W0DM5lcj6mw
             beliver
"""
"""
https://www.youtube.com/watch?v=QOUvmBggw_Y
            wakra wakra
"""
import urllib.request
import webbrowser

selected_song = input("")
selected_song = int(selected_song)
if selected_song == 1:
    print("beliver is selected")
    webbrowser.open("https://www.youtube.com/watch?v=W0DM5lcj6mw")
elif selected_song == 2:
    webbrowser.open("https://www.youtube.com/watch?v=QOUvmBggw_Y")
    print("wakrah wahrah is selected")
elif selected_song == 3:
    webbrowser.open("https://www.youtube.com/watch?v=jwNhhlkchwA")
    print("proggresive underground  is selected")
elif selected_song == 4:
    webbrowser.open("https://www.youtube.com/watch?v=_uUdJalMaF8")
    print("saki saki is selected")
elif selected_song == 5:
    webbrowser.open("https://www.youtube.com/watch?v=p1cEvNn88jM&list=PLMtpqbF01MkVhY0_Z4Afg1m3xCKa2kNBf&ab_channel=TaylorSwiftVEVO")
    print("long live is selected")
elif selected_song == 6:
    webbrowser.open("https://www.youtube.com/watch?v=q8gilwzNQEA")
    print("mere rashke qamar is selected")
elif selected_song == 7:
    webbrowser.open("https://www.youtube.com/watch?v=kw4tT7SCmaY")
    print("afareen is selected")
elif selected_song== 8:
    webbrowser.open("https://www.youtube.com/watch?v=2_7ZYtQ61yM&ab_channel=RafaelLucius")
    print("marshmellow is selected")
elif selected_song== 9:
    webbrowser.open("https://www.youtube.com/watch?v=xAG1uF9O1Is")
    print("best mix of popular songs  is selected")