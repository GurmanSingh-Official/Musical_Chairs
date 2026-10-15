import random 
import time 
import pygame 

song = "Music for game.mp3"

def main():
    print("WELCOME TO MUSICAL CHAIRS!")
    time.sleep(0.5)
    print("LETS PLAY MUSICAL CHAIRS, GET READY!")
    print("STARTING IN 10 SECONDS")
    time.sleep(10)

    t1, t2 = timer()
    print("LETSS PLAYYYY!")
    time.sleep(1)
    song_management(t1, t2)

    print("THANKU EVERYONE FOR YOUR CORPORATION!")
    print("IT WAS FUN PLAYING WITH YOU ALL!")
    print("MEET YOU ALL SOON!")

def timer():
    play_time = random.randint(20, 60)
    pause_time = random.randint(10, 20)
    return play_time, pause_time

def song_management(t1, t2):
    pygame.mixer.init()
    pygame.mixer.music.load(song)

    pygame.mixer.music.play()

    while True:
        time.sleep(t1)

        pygame.mixer.music.pause()
        time.sleep(t2)

        pygame.mixer.music.unpause()

        song_status = pygame.mixer.music.get_busy()

        if song_status:
            continue 
        else:
            break
    
    pygame.mixer.music.stop()
    return 

main()