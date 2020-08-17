#Emoji Cnverter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    "<3": "💖",
    ";)": "😉",
    ":D": "😃",
    ":/": "😕"
}
op = ""
for word in words:
    op += emojis.get(word, word) + " "
print(op)
