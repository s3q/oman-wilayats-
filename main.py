import json
from googletrans import Translator

translator = Translator()
data = {}
trans = {}

with open("names_ar.json", "r", encoding="utf-8") as f:
    trans = f.read()
    trans = json.loads(trans)



with open("gadm.json", "r", encoding="utf-8") as f:
    djson = json.load(f)
    allwilayat = djson["features"]

    for w in allwilayat:
        gov = w["properties"]["NAME_1"]
        if data.get(gov) is None:
            data[gov] = {
                "ar": trans[gov],
                "wilayat": {}
            }

        wilaya = w["properties"]["NAME_2"]
        data[gov]["wilayat"][wilaya] = {
            "ar": trans[wilaya],
            "geozone": w["geometry"]["coordinates"][0][0]
        }

# حفظ النتيجة
with open("geo_oman.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Done, translations saved in test.json")
