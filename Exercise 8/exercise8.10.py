def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)


texts = [
    "Halo, apa kabar?",
    "Jangan lupa tugas Python hari ini.",
    "Nanti malam belajar bareng, ya.",
]
sent_messages = []

send_messages(texts, sent_messages)

print("\nList pesan asli:")
print(texts)

print("\nList pesan terkirim:")
print(sent_messages)