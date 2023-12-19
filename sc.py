import time
def scroll_text(text, speed):
for char in text:
print(char, end='', flush=True)
time.sleep(speed)
if __name__== "__main__":
file_path = "/path/to/text/faile.txt"
speed = 0.1
with open(fail_path, 'r') as file:
text = file.read()
scroll_text(text, speed)