import os
from imaplib import Commands

import pygame


def main():
    """
    The main function which runs the program
    """

    ...


def load_mp3_files(folder_path):
    """
    Args:
        folder_path(string) : The folder directory
    Returns:
        List(List of strings): The filenames if the directory and the files exist
    """
    if not os.path.exists(folder_path):
        print(f"Check the folder '{folder_path}' again because it does not exists.")
        return None
    songs_list = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]
    return songs_list

    # fix a edge case where i need to check file name using lower as it will not check files with .MP3


def display_menu(songs_list):
    """
    Args:
        songs_list(List of strings): The songs list
    Returns:
        Nothing just prints the menu
    """
    os.system("clear")
    print("---Music Player---")
    for index, song_name in enumerate(songs_list, start=1):
        print(f"{index}. {song_name}")


def play_session(file_path):
    """
    Args:
        file_path(string): The full path to the specific song selected
    Returns:
        Nothing, plays the songs and waits for inputs
    """
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    song_name = os.path.basename(file_path)
    print(f"Playing: {song_name}!")
    while True:
        command = input("P for Pause, R for Resume, S for Stop!").upper().strip()
        if command == "P":
            pygame.mixer.music.pause()
            print("Paused!")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed!")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped!")
            return
        else:
            print("Please enter correct command!")


if __name__ == "__main__":
    main()
