import pygame

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print("Error playing audio: ", str(e))

    pygame.mixer.quit()
    pygame.quit()

# Example usage
audio_file = "path_to_your_audio_file.mp3"
play_audio("output.wav")
