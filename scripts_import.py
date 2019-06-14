from app.models import Season, Title, Item
import  copy
from collections import defaultdict

file_list = []
speaker_list = []

file = open("手動で[]外す[]削除発話者付加発話者かぶり消すS1だけ.txt", "r", encoding="utf-8_sig")

for i, f in enumerate(file):
    splited_text = f.split()
    if "発話者" in splited_text:
        season = splited_text[1]
        title = splited_text[2]
        progress= splited_text[3]
        temp_speaker_list = splited_text[4:]
        speaker = " ".join(temp_speaker_list)
        line_dict = {
            "season": season,
            "title": title,
            "percent": progress,
            "speaker": speaker,
        }
        file_list.append(line_dict)
    else:
        if splited_text:
            dict = file_list[-1]
            if "line" not in dict:
                dict["line"] = []
            dict["line"].append(splited_text)

    speaker_list.clear()

season_name = file_list[0]['season']
season = season = Season.objects.create(season=season_name)

title_list = []
for f in file_list:
    t = f["title"]
    if t not in title_list:
        title_list.append(t)

for ti in title_list:
    title_object = Title(season=season, title=ti)
    title_object.save()

for f in file_list:
    t = f["title"]
    t_django = Title.objects.get(title=t)
    s = f["speaker"]
    line_list = f["line"]
    p = f["percent"]
    cast_number = int(p[:2])
    new_list = []
    for l in line_list:
        new_list += l
    row_text = " ".join(new_list)


    item_object = Item(
        title=t_django,
        progress=cast_number,
        speaker=s,
        script=row_text
    )
    item_object.save()

