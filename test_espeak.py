import subprocess
string_to_speak = "Hello my friend. I am currently talking to you."

speaking_subprocess = subprocess.run(["espeak", string_to_speak, "--stdout", "|", "aplay"])