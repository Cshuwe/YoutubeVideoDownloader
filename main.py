import pytube
import time
import tqdm


def videocn():
    video_url = input("Please enter the url:")

    youtube = pytube.YouTube(video_url)

    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for _ in tqdm.tqdm(mylist):
        time.sleep(1)

    print("Please be patient video converting is in progress.")
    print("")
    time.sleep(1)

    video = youtube.streams.first()

    video.download(r'c:\\YoutubeVideos')
    print("Download complete please check C:\YoutubeVideos")
    print("")
    print("Would you like to download another movie?")
    print("")
    print("If yes please press y if not press n")
    print("")
    yes = input("")
    if yes == "y":
        videocn()
    else:
        time.sleep(2)
        print("Thank you!")
    exit()


videocn()
