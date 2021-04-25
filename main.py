import json
with open("input.lrc", encoding="utf-8") as f:
    lrcfile = f.read().splitlines()
outputjson = []
count = 0
for line in lrcfile:
    i = 0
    while i < len(line):
        if line == "":
            break
        elif line[i] == "[":
            i += 1
            if line[i] + line[i+1] == "ti":
                name = line.split(":")[-1].replace("]", "")
                break
            elif line[i] + line[i+1] == "ar":
                artist = line.split(":")[-1].replace("]", "")
                break
            elif line[i] + line[i+1] == "la":
                language = line.split(":")[-1].replace("]", "")
                break
            elif line[i] + line[i+1] == "re":
                creator = line.split(":")[-1].replace("]", "")
                break
            elif line[i] + line[i+1] == "ve":
                version = line.split(":")[-1].replace("]", "")
                break
            elif line[i].isdigit() == True:
                words = line.split("  ")
                o = i
                l = 0
                b = False
                while l < len(words):
                    textwithtime = words[l]
                    timefromlrc = textwithtime[o:o+8]
                    timelist = timefromlrc.split(":")
                    minute = int(timelist[0])
                    second = int(timelist[-1].split(".")[0])
                    millisecond = int(timelist[-1].split(".")[-1])
                    finaltime = (minute * 60000) + (second * 1000) + millisecond
                    try:
                        outputjson[-1]["duration"] = finaltime - int(outputjson[-1]["time"])
                    except IndexError:
                        duration = 0
                    if textwithtime[o+8] == "]":
                        shit = True
                    else:
                        shit = False
                    if words[-1] == textwithtime:
                        isLineEnding = 1
                        if shit == True:
                            text = textwithtime.split("]")[-1]
                        else:
                            text = textwithtime.split(">")[-1]
                    else:
                        isLineEnding = 0
                        if shit == True:
                            text = textwithtime.split("]")[-1] + " "
                        else:
                            text = textwithtime.split(">")[-1] + " "
                    lyric = {
                        "time": finaltime,
                        "duration": duration,
                        "text": text,
                        "isLineEnding": isLineEnding
                    }
                    outputjson.append(lyric)
                    l += 1
                    count += 1
                i+=len(line)
            else:
                break
            i += 1
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(outputjson, f)
try:
    print("Name: " + name)
except Exception:
    print("Name: Unknown")
try:
    print("Artist: " + artist)
except Exception:
    print("Artist: Unknown")
try:
    print("Language: " + language)
except Exception:
    print("Language: Unknown")
try:
    print("Creator: " + creator)
except Exception:
    print("Creator: Unknown")
try:
    print("Version: " + version)
except Exception:
    print("Version: Unknown")