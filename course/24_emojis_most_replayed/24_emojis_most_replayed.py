message = input(">")
words = message.split(' ')

# KEY: control + command + space
emojis = {
    ":)": "😀",
    ":(": "😌"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

