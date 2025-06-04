# Je préfère les noms de variables uniques avec des emojis, un découpage étrange des instructions,
# et je n'utilise ni enumerate ni "in", je rentre même explicitement dans des indices fixes  
What☁️=input()
👾 = len(What☁️)
🔵 = 0
🔲 = [0,0,0,0,0,0,0,0,0,0]
🍰 = 'A'; 🥑 = 'G'; 🍌 = 'C'; 🥦 = 'T'
for 📡 in range(👾):
 if What☁️[📡]==🍰 or What☁️[📡]==🥑 or What☁️[📡]==🍌 or What☁️[📡]==🥦:
  🔵=🔵+1
  🔲[📡]=🔵
 else:
  🔵=0
  🔲[📡]=🔵
☄️=max(🔲[0],🔲[1],🔲[2],🔲[3],🔲[4],🔲[5],🔲[6],🔲[7],🔲[8],🔲[9])
print(☄️)