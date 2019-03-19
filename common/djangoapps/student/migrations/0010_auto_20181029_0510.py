# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_remove_early_level_of_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageproficiency',
            name='code',
            field=models.CharField(help_text='The ISO 639-1 language code for this language.', max_length=16, choices=[['aa', 'Afar'], ['ab', 'Abkhazian'], ['af', 'Afrikaans'], ['ak', 'Akan'], ['sq', 'Albanian'], ['am', 'Amharic'], ['ar', 'Arabic'], ['an', 'Aragonese'], ['hy', 'Armenian'], ['as', 'Assamese'], ['av', 'Avaric'], ['ae', 'Avestan'], ['ay', 'Aymara'], ['az', 'Azerbaijani'], ['ba', 'Bashkir'], ['bm', 'Bambara'], ['eu', 'Basque'], ['be', 'Belarusian'], ['bn', 'Bengali'], ['bh', 'Bihari languages'], ['bi', 'Bislama'], ['bs', 'Bosnian'], ['br', 'Breton'], ['bg', 'Bulgarian'], ['my', 'Burmese'], ['ca', 'Catalan'], ['ch', 'Chamorro'], ['ce', 'Chechen'], ['zh', 'Chinese'], ['zh_HANS', 'Simplified Chinese'], ['zh_HANT', 'Traditional Chinese'], ['cu', 'Church Slavic'], ['cv', 'Chuvash'], ['kw', 'Cornish'], ['co', 'Corsican'], ['cr', 'Cree'], ['cs', 'Czech'], ['da', 'Danish'], ['dv', 'Divehi'], ['nl', 'Dutch'], ['dz', 'Dzongkha'], ['en', 'English'], ['eo', 'Esperanto'], ['et', 'Estonian'], ['ee', 'Ewe'], ['fo', 'Faroese'], ['fj', 'Fijian'], ['fi', 'Finnish'], ['fr', 'French'], ['fy', 'Western Frisian'], ['ff', 'Fulah'], ['ka', 'Georgian'], ['de', 'German'], ['gd', 'Gaelic'], ['ga', 'Irish'], ['gl', 'Galician'], ['gv', 'Manx'], ['el', 'Greek'], ['gn', 'Guarani'], ['gu', 'Gujarati'], ['ht', 'Haitian'], ['ha', 'Hausa'], ['he', 'Hebrew'], ['hz', 'Herero'], ['hi', 'Hindi'], ['ho', 'Hiri Motu'], ['hr', 'Croatian'], ['hu', 'Hungarian'], ['ig', 'Igbo'], ['is', 'Icelandic'], ['io', 'Ido'], ['ii', 'Sichuan Yi'], ['iu', 'Inuktitut'], ['ie', 'Interlingue'], ['ia', 'Interlingua'], ['id', 'Indonesian'], ['ik', 'Inupiaq'], ['it', 'Italian'], ['jv', 'Javanese'], ['ja', 'Japanese'], ['kl', 'Kalaallisut'], ['kn', 'Kannada'], ['ks', 'Kashmiri'], ['kr', 'Kanuri'], ['kk', 'Kazakh'], ['km', 'Central Khmer'], ['ki', 'Kikuyu'], ['rw', 'Kinyarwanda'], ['ky', 'Kirghiz'], ['kv', 'Komi'], ['kg', 'Kongo'], ['ko', 'Korean'], ['kj', 'Kuanyama'], ['ku', 'Kurdish'], ['lo', 'Lao'], ['la', 'Latin'], ['lv', 'Latvian'], ['li', 'Limburgan'], ['ln', 'Lingala'], ['lt', 'Lithuanian'], ['lb', 'Luxembourgish'], ['lu', 'Luba-Katanga'], ['lg', 'Ganda'], ['mk', 'Macedonian'], ['mh', 'Marshallese'], ['ml', 'Malayalam'], ['mi', 'Maori'], ['mr', 'Marathi'], ['ms', 'Malay'], ['mg', 'Malagasy'], ['mt', 'Maltese'], ['mn', 'Mongolian'], ['na', 'Nauru'], ['nv', 'Navajo'], ['nr', 'Ndebele, South'], ['nd', 'Ndebele, North'], ['ng', 'Ndonga'], ['ne', 'Nepali'], ['nn', 'Norwegian Nynorsk'], ['nb', 'Bokm\xe5l, Norwegian'], ['no', 'Norwegian'], ['ny', 'Chichewa'], ['oc', 'Occitan'], ['oj', 'Ojibwa'], ['or', 'Oriya'], ['om', 'Oromo'], ['os', 'Ossetian'], ['pa', 'Panjabi'], ['fa', 'Persian'], ['pi', 'Pali'], ['pl', 'Polish'], ['pt', 'Portuguese'], ['ps', 'Pushto'], ['qu', 'Quechua'], ['rm', 'Romansh'], ['ro', 'Romanian'], ['rn', 'Rundi'], ['ru', 'Russian'], ['sg', 'Sango'], ['sa', 'Sanskrit'], ['si', 'Sinhala'], ['sk', 'Slovak'], ['sl', 'Slovenian'], ['se', 'Northern Sami'], ['sm', 'Samoan'], ['sn', 'Shona'], ['sd', 'Sindhi'], ['so', 'Somali'], ['st', 'Sotho, Southern'], ['es', 'Spanish'], ['sc', 'Sardinian'], ['sr', 'Serbian'], ['ss', 'Swati'], ['su', 'Sundanese'], ['sw', 'Swahili'], ['sv', 'Swedish'], ['ty', 'Tahitian'], ['ta', 'Tamil'], ['tt', 'Tatar'], ['te', 'Telugu'], ['tg', 'Tajik'], ['tl', 'Tagalog'], ['th', 'Thai'], ['bo', 'Tibetan'], ['ti', 'Tigrinya'], ['to', 'Tonga (Tonga Islands)'], ['tn', 'Tswana'], ['ts', 'Tsonga'], ['tk', 'Turkmen'], ['tr', 'Turkish'], ['tw', 'Twi'], ['ug', 'Uighur'], ['uk', 'Ukrainian'], ['ur', 'Urdu'], ['uz', 'Uzbek'], ['ve', 'Venda'], ['vi', 'Vietnamese'], ['vo', 'Volap\xfck'], ['cy', 'Welsh'], ['wa', 'Walloon'], ['wo', 'Wolof'], ['xh', 'Xhosa'], ['yi', 'Yiddish'], ['yo', 'Yoruba'], ['za', 'Zhuang'], ['zu', 'Zulu'], ['twq', 'Tasawaq'], ['sat-Deva', 'Santali (Devanagari)'], ['mfe', 'Morisyen'], ['zh-Hans', 'Chinese (Simplified)'], ['rof', 'Rombo'], ['zh-Hant', 'Chinese (Traditional)'], ['mni', 'Manipuri'], ['bm-Latn', 'Bamanankan (Latin)'], ['otq', 'Quer\xe9taro Otomi'], ['jv-Latn', 'Javanese (Latin)'], ['mww', 'Hmong Daw'], ['nso', 'Sesotho sa Leboa'], ['pa-Guru', 'Punjabi (Gurmukhi)'], ['byn', 'Blin'], ['ksf', 'Bafia'], ['dje', 'Zarma'], ['ksb', 'Shambala'], ['lkt', 'Lakota'], ['tzm-Tfng', 'Central Atlas Tamazight (Tifinagh)'], ['ksh', 'Colognian'], ['fil', 'Filipino'], ['haw', 'Hawaiian'], ['bin', 'Edo'], ['lrc', 'Northern Luri'], ['ssy', 'Saho'], ['ceb', 'Cebuano'], ['mgh', 'Makhuwa-Meetto'], ['mgo', "Meta'"], ['dav', 'Taita'], ['dyo', 'Jola-Fonyi'], ['pt-BR', 'Portuguese (Brazil)'], ['kkj', 'Kako'], ['bas', 'Basaa'], ['os-Latn', 'Ossetic (Latin)'], ['guz', 'Gusii'], ['sd-Deva', 'Sindhi (Devanagari)'], ['ses', 'Koyraboro Senni'], ['teo', 'Teso'], ['kde', 'Makonde'], ['arz', 'Arabic, Egyptian'], ['nus', 'Nuer'], ['ebu', 'Embu'], ['arn', 'Mapudungun'], ['seh', 'Sena'], ['wae', 'Walser'], ['jgo', 'Ngomba'], ['luy', 'Luyia'], ['sms', 'Skolt Sami'], ['smn', 'Inari Sami'], ['mua', 'Mundang'], ['smj', 'Lule Sami'], ['iu-Latn', 'Inuktitut (Latin)'], ['dsb', 'Lower Sorbian'], ['sma', 'Southern Sami'], ['luo', 'Luo'], ['hsb', 'Upper Sorbian'], ['sbp', 'Sangu'], ['ast', 'Asturian'], ['uz-Cyrl', 'Uzbek (Cyrillic)'], ['cgg', 'Chiga'], ['az-Cyrl', 'Azerbaijani (Cyrillic)'], ['nmg', 'Kwasio'], ['asa', 'Asu'], ['yue-Hant', 'Cantonese (Traditional)'], ['kea', 'Kabuverdianu'], ['ug-Arab', 'Uyghur (Arabic)'], ['pt-PT', 'Portuguese (Portugal)'], ['quc', 'K\u2019iche\u2019'], ['uz-Latn', 'Uzbek (Latin)'], ['iv', 'Invariant Language'], ['yua', 'Yucatec Maya'], ['ca-ES-valencia', 'Valencian'], ['nds', 'Low German'], ['chr-Cher', 'Cherokee (Cherokee)'], ['kfr', 'Kutchi'], ['ha-Latn', 'Hausa (Latin)'], ['brx', 'Bodo'], ['mer', 'Meru'], ['zgh-Tfng', 'Standard Moroccan Tamazight (Tifinagh)'], ['sah', 'Sakha'], ['mn-Mong', 'Mongolian (Traditional Mongolian)'], ['apc', 'Arabic, Levantine'], ['vai-Vaii', 'Vai (Vai)'], ['ks-Arab', 'Kashmiri (Perso-Arabic)'], ['kok', 'Konkani'], ['wal', 'Wolaytta'], ['dua', 'Duala'], ['swc', 'Congo Swahili'], ['yav', 'Yangben'], ['ks-Deva', 'Kashmiri (Devanagari)'], ['ff-Latn', 'Fulah'], ['ku-Arab', 'Central Kurdish'], ['sd-Arab', 'Sindhi (Arabic)'], ['tg-Cyrl', 'Tajik (Cyrillic)'], ['jmc', 'Machame'], ['shi-Tfng', 'Tachelhit (Tifinagh)'], ['fur', 'Friulian'], ['bem', 'Bemba'], ['tt-Cyrl', 'Tatar (Cyrillic)'], ['kln', 'Kalenjin'], ['bez', 'Bena'], ['vun', 'Vunjo'], ['os-Cyrl', 'Ossetic (Cyrillic)'], ['sr-Latn', 'Serbian (Latin)'], ['pa-Arab', 'Punjabi (Arabic)'], ['mn-Cyrl', 'Mongolian (Cyrillic)'], ['prg', 'Prussian'], ['prs', 'Dari'], ['nnh', 'Ngiemboon'], ['khq', 'Koyra Chiini'], ['qps', 'Pseudo'], ['saq', 'Samburu'], ['nqo', 'N\u2019Ko'], ['pap', 'Papiamento'], ['kmr-Arab', 'Northern Kurdish (Arabic)'], ['ewo', 'Ewondo'], ['bs-Cyrl', 'Bosnian (Cyrillic)'], ['afb', 'Arabic, Gulf'], ['xog', 'Soga'], ['naq', 'Nama'], ['nyn', 'Nyankole'], ['tig', 'Tigre'], ['tk-Latn', 'Turkmen (Latin)'], ['kab', 'Kabyle'], ['mas', 'Masai'], ['rwk', 'Rwa'], ['az-Latn', 'Azerbaijani (Latin)'], ['sr-Cyrl', 'Serbian (Cyrillic)'], ['lag', 'Langi'], ['tzm-Arab', 'Central Atlas Tamazight (Arabic)'], ['dgo', 'Dogri'], ['kam', 'Kamba'], ['syr', 'Syriac'], ['mai', 'Maithili'], ['mzn', 'Mazanderani'], ['shi-Latn', 'Tachelhit (Latin)'], ['vai-Latn', 'Vai (Latin)'], ['iu-Cans', 'Inuktitut (Canadian Aboriginal Syllabics)'], ['bs-Latn', 'Bosnian (Latin)'], ['gsw', 'Swiss German'], ['tzm-Latn', 'Central Atlas Tamazight (Latin)'], ['moh', 'Mohawk'], ['uz-Arab', 'Uzbek (Perso-Arabic)'], ['agq', 'Aghem']]),
        ),
    ]
