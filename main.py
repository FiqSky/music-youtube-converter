from pytube import YouTube
import shutil


def main():
    url = input("Enter Link Youtube Video: ")
    print("Converting...")

    movie = YouTube(url).streams\
        .filter(progressive=True, file_extension='mp4')\
        .get_highest_resolution()\
        .download()

    shutil.move(movie, r"C:/Users/fiqih/Desktop/")
    print("Video Downloaded!")


main()
