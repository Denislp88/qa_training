pip install transformers
pip install sentencepiece

git clone https://github.com/argosopentech/argos-translate.git
cd argos-translate
python3 -m pip install .

argospm update
argospm search
argospm install translate-en_ru
argospm install translate-ru_en

import torch, re
from argostranslate import package, translate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Расскомментируйте чтобы установить модели из файлов
# Файлы можно скачать тут: https://www.argosopentech.com/argospm/index/
package.install_from_path('ru_en.argosmodel')
package.install_from_path('en_ru.argosmodel')

installed_languages = translate.get_installed_languages()

for lang in installed_languages:
    print(str(lang))

installed_languages = translate.load_installed_languages()

# Замените индексы установленных языков с 0 и 1 на те которые соответствуют русскому и английскому
translation_en_ru = installed_languages[0].get_translation(installed_languages[1])
translation_ru_en = installed_languages[1].get_translation(installed_languages[0])

device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained("bigscience/T0_3B")
model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0_3B").to(device)


while True:

    vopros = input('Введи вопрос: ')

    vopros = translation_ru_en.translate(vopros + '?')

    otvet = tokenizer.decode(model.generate(tokenizer.encode(vopros, return_tensors="pt").to(device))[0])

    otvet = re.sub(r'(\<(/?[^>]+)>)', '', otvet)

    print(translation_en_ru.translate(otvet))