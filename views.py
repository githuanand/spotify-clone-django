from django.shortcuts import render

def index(request):
    songs = [
        {
            "id": 1,
            "title": "Let Me Love You",
            "artist": "DJ Snake",
            "file": "songs/let_me_love_you.mp3",
            "cover": "images/let_me_love_you_image.jpg"
        },
        {
            "id": 2,
            "title": "Piya Aaye Na",
            "artist": "KK",
            "file": "songs/piya_aaye_na_aashiqui.mp3",
            "cover": "images/piya_aaye_na_image.jpeg"
        },
        {
            "id": 3,
            "title": "Tere Bin Bas Ek Pal",
            "artist": "Atif Aslam",
            "file": "songs/tere_bin_bas_ek_pal.mp3",
            "cover": "images/bus_Ek_pal.jpeg"
        },
    ]
    return render(request, "music/index.html", {"songs": songs})
