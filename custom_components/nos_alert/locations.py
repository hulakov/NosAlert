"""
Official Ukrainian Administrative Locations database for alerts.in.ua.

Source:
Google Spreadsheet: https://docs.google.com/spreadsheets/d/1XnTOzcPHd1LZUrarR1Fk43FUyl8Ae6a6M7pcwDRjNdA/edit?gid=0#gid=0
Title: АДМІНІСТРАТИВНО-ТЕРИТОРІАЛЬНИЙ УСТРІЙ УКРАІНИ (alerts.in.ua UID список)
Total entries: 1622 (ієрархічна структура: Область → districts[] → hromadas[])
"""
try:
    from .location_helpers import LocationType, Hromada, District, Location
except ImportError:
    from location_helpers import LocationType, Hromada, District, Location

LOCATIONS: list[Location] = [
    {
        "uid": 31,
        "name": 'м. Київ',
        "type": LocationType.SPECIAL_CITY,
        "name_en": 'Kyiv',
    },
    {
        "uid": 30,
        "name": 'м. Севастополь',
        "type": LocationType.SPECIAL_CITY,
        "name_en": 'Sevastopol',
    },
    {
        "uid": 8,
        "name": 'Волинська область',
        "type": LocationType.OBLAST,
        "name_en": 'Volynska Oblast',
        "districts": [
            {
                "uid": 38,
                "name": 'Володимирський',
                "name_en": 'Volodymyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 255,
                        "name": 'м. Володимир та Володимирська',
                        "name_en": 'Volodymyr and Volodymyrska Hromada',
                    },
                    {
                        "uid": 256,
                        "name": 'Затурцівська',
                        "name_en": 'Zaturtsivska Hromada',
                    },
                    {
                        "uid": 257,
                        "name": 'Зимнівська',
                        "name_en": 'Zymnivska Hromada',
                    },
                    {
                        "uid": 259,
                        "name": 'Литовезька',
                        "name_en": 'Lytovezka Hromada',
                    },
                    {
                        "uid": 260,
                        "name": 'Локачинська',
                        "name_en": 'Lokachynska Hromada',
                    },
                    {
                        "uid": 261,
                        "name": 'м. Нововолинськ та Нововолинська',
                        "name_en": 'Novovolynsk and Novovolynska Hromada',
                    },
                    {
                        "uid": 262,
                        "name": 'Оваднівська',
                        "name_en": 'Ovadnivska Hromada',
                    },
                    {
                        "uid": 263,
                        "name": 'Павлівська',
                        "name_en": 'Pavlivska Hromada',
                    },
                    {
                        "uid": 264,
                        "name": 'Поромівська',
                        "name_en": 'Poromivska Hromada',
                    },
                    {
                        "uid": 265,
                        "name": 'Устилузька',
                        "name_en": 'Ustyluzka Hromada',
                    },
                    {
                        "uid": 258,
                        "name": 'Іваничівська',
                        "name_en": 'Ivanychivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 29,
        "name": 'Автономна Республіка Крим',
        "type": LocationType.OBLAST,
        "name_en": 'Autonomous Republic of Crimea',
        "districts": [
            {
                "uid": 41,
                "name": 'Камінь-Каширський',
                "name_en": 'Kamin-Kashyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 266,
                        "name": 'Камінь-Каширська',
                        "name_en": 'Kamin-Kashyrska Hromada',
                    },
                    {
                        "uid": 267,
                        "name": 'Любешівська',
                        "name_en": 'Liubeshivska Hromada',
                    },
                    {
                        "uid": 268,
                        "name": 'Маневицька',
                        "name_en": 'Manevytska Hromada',
                    },
                    {
                        "uid": 269,
                        "name": 'Прилісненська',
                        "name_en": 'Prylisnenska Hromada',
                    },
                    {
                        "uid": 270,
                        "name": 'Сошичненська',
                        "name_en": 'Soshychnenska Hromada',
                    },
                ],
            },
            {
                "uid": 40,
                "name": 'Ковельський',
                "name_en": 'Kovelskyi Raion',
                "hromadas": [
                    {
                        "uid": 232,
                        "name": 'Велимченська',
                        "name_en": 'Velymchenska Hromada',
                    },
                    {
                        "uid": 233,
                        "name": 'Велицька',
                        "name_en": 'Velytska Hromada',
                    },
                    {
                        "uid": 234,
                        "name": 'Вишнівська',
                        "name_en": 'Vyshnivska Hromada',
                    },
                    {
                        "uid": 235,
                        "name": 'Голобська',
                        "name_en": 'Holobska Hromada',
                    },
                    {
                        "uid": 236,
                        "name": 'Головненська',
                        "name_en": 'Holovnenska Hromada',
                    },
                    {
                        "uid": 237,
                        "name": 'Дубечненська',
                        "name_en": 'Dubechnenska Hromada',
                    },
                    {
                        "uid": 238,
                        "name": 'Дубівська',
                        "name_en": 'Dubivska Hromada',
                    },
                    {
                        "uid": 239,
                        "name": 'Заболоттівська',
                        "name_en": 'Zabolottivska Hromada',
                    },
                    {
                        "uid": 240,
                        "name": 'Забродівська',
                        "name_en": 'Zabrodivska Hromada',
                    },
                    {
                        "uid": 241,
                        "name": 'м. Ковель та Ковельська',
                        "name_en": 'Kovel and Kovelska Hromada',
                    },
                    {
                        "uid": 242,
                        "name": 'Колодяжненська',
                        "name_en": 'Kolodiazhnenska Hromada',
                    },
                    {
                        "uid": 243,
                        "name": 'Луківська',
                        "name_en": 'Lukivska Hromada',
                    },
                    {
                        "uid": 244,
                        "name": 'Люблинецька',
                        "name_en": 'Liublynetska Hromada',
                    },
                    {
                        "uid": 245,
                        "name": 'м. Любомиль та Любомльська',
                        "name_en": 'Liubomyl and Liubomlska Hromada',
                    },
                    {
                        "uid": 246,
                        "name": 'Поворська',
                        "name_en": 'Povorska Hromada',
                    },
                    {
                        "uid": 247,
                        "name": 'Ратнівська',
                        "name_en": 'Ratnivska Hromada',
                    },
                    {
                        "uid": 248,
                        "name": 'Рівненська',
                        "name_en": 'Rivnenska Hromada',
                    },
                    {
                        "uid": 249,
                        "name": 'Самарівська',
                        "name_en": 'Samarivska Hromada',
                    },
                    {
                        "uid": 250,
                        "name": 'Сереховичівська',
                        "name_en": 'Serekhovychivska Hromada',
                    },
                    {
                        "uid": 251,
                        "name": 'Смідинська',
                        "name_en": 'Smidynska Hromada',
                    },
                    {
                        "uid": 252,
                        "name": 'Старовижівська',
                        "name_en": 'Starovyzhivska Hromada',
                    },
                    {
                        "uid": 253,
                        "name": 'Турійська',
                        "name_en": 'Turiiska Hromada',
                    },
                    {
                        "uid": 254,
                        "name": 'м. Шацьк та Шацька',
                        "name_en": 'Shatsk and Shatska Hromada',
                    },
                ],
            },
            {
                "uid": 39,
                "name": 'Луцький',
                "name_en": 'Lutskyi Raion',
                "hromadas": [
                    {
                        "uid": 217,
                        "name": 'Берестечківська',
                        "name_en": 'Berestechkivska Hromada',
                    },
                    {
                        "uid": 218,
                        "name": 'Боратинська',
                        "name_en": 'Boratynska Hromada',
                    },
                    {
                        "uid": 219,
                        "name": 'Городищенська',
                        "name_en": 'Horodyshchenska Hromada',
                    },
                    {
                        "uid": 220,
                        "name": 'Горохівська',
                        "name_en": 'Horokhivska Hromada',
                    },
                    {
                        "uid": 221,
                        "name": 'Доросинівська',
                        "name_en": 'Dorosynivska Hromada',
                    },
                    {
                        "uid": 223,
                        "name": 'Колківська',
                        "name_en": 'Kolkivska Hromada',
                    },
                    {
                        "uid": 224,
                        "name": 'Копачівська',
                        "name_en": 'Kopachivska Hromada',
                    },
                    {
                        "uid": 222,
                        "name": 'Ківерцівська',
                        "name_en": 'Kivertsivska Hromada',
                    },
                    {
                        "uid": 225,
                        "name": 'м. Луцьк та Луцька',
                        "name_en": 'Lutsk and Lutska Hromada',
                    },
                    {
                        "uid": 226,
                        "name": "Мар'янівська",
                        "name_en": 'Marianivska Hromada',
                    },
                    {
                        "uid": 227,
                        "name": 'Олицька',
                        "name_en": 'Olytska Hromada',
                    },
                    {
                        "uid": 228,
                        "name": 'Підгайцівська',
                        "name_en": 'Pidhaitsivska Hromada',
                    },
                    {
                        "uid": 229,
                        "name": 'Рожищенська',
                        "name_en": 'Rozhyshchenska Hromada',
                    },
                    {
                        "uid": 230,
                        "name": 'Торчинська',
                        "name_en": 'Torchynska Hromada',
                    },
                    {
                        "uid": 231,
                        "name": 'Цуманська',
                        "name_en": 'Tsumanska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 4,
        "name": 'Вінницька область',
        "type": LocationType.OBLAST,
        "name_en": 'Vinnytska Oblast',
        "districts": [
            {
                "uid": 36,
                "name": 'Вінницький',
                "name_en": 'Vinnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 154,
                        "name": 'Агрономічна',
                        "name_en": 'Ahronomichna Hromada',
                    },
                    {
                        "uid": 156,
                        "name": 'Вороновицька',
                        "name_en": 'Voronovytska Hromada',
                    },
                    {
                        "uid": 155,
                        "name": 'м. Вінниця та Вінницька',
                        "name_en": 'Vinnytsia and Vinnytska Hromada',
                    },
                    {
                        "uid": 157,
                        "name": 'Гніванська',
                        "name_en": 'Hnivanska Hromada',
                    },
                    {
                        "uid": 159,
                        "name": 'Липовецька',
                        "name_en": 'Lypovetska Hromada',
                    },
                    {
                        "uid": 161,
                        "name": 'Лука-Мелешківська',
                        "name_en": 'Luka-Meleshkivska Hromada',
                    },
                    {
                        "uid": 160,
                        "name": 'Літинська',
                        "name_en": 'Litynska Hromada',
                    },
                    {
                        "uid": 162,
                        "name": 'Немирівська',
                        "name_en": 'Nemyrivska Hromada',
                    },
                    {
                        "uid": 163,
                        "name": 'Оратівська',
                        "name_en": 'Orativska Hromada',
                    },
                    {
                        "uid": 164,
                        "name": 'Погребищенська',
                        "name_en": 'Pohrebyshchenska Hromada',
                    },
                    {
                        "uid": 165,
                        "name": 'Стрижавська',
                        "name_en": 'Stryzhavska Hromada',
                    },
                    {
                        "uid": 166,
                        "name": 'Сутисківська',
                        "name_en": 'Sutyskivska Hromada',
                    },
                    {
                        "uid": 167,
                        "name": 'Тиврівська',
                        "name_en": 'Tyvrivska Hromada',
                    },
                    {
                        "uid": 168,
                        "name": 'Турбівська',
                        "name_en": 'Turbivska Hromada',
                    },
                    {
                        "uid": 169,
                        "name": 'Якушинецька',
                        "name_en": 'Yakushynetska Hromada',
                    },
                    {
                        "uid": 158,
                        "name": 'Іллінецька',
                        "name_en": 'Illinetska Hromada',
                    },
                ],
            },
            {
                "uid": 37,
                "name": 'Гайсинський',
                "name_en": 'Haisynskyi Raion',
                "hromadas": [
                    {
                        "uid": 185,
                        "name": 'Бершадська',
                        "name_en": 'Bershadska Hromada',
                    },
                    {
                        "uid": 186,
                        "name": 'Гайсинська',
                        "name_en": 'Haisynska Hromada',
                    },
                    {
                        "uid": 187,
                        "name": 'Дашівська',
                        "name_en": 'Dashivska Hromada',
                    },
                    {
                        "uid": 188,
                        "name": 'Джулинська',
                        "name_en": 'Dzhulynska Hromada',
                    },
                    {
                        "uid": 189,
                        "name": 'Краснопільська',
                        "name_en": 'Krasnopilska Hromada',
                    },
                    {
                        "uid": 190,
                        "name": 'Кунківська',
                        "name_en": 'Kunkivska Hromada',
                    },
                    {
                        "uid": 191,
                        "name": 'м. Ладижин та Ладижинська',
                        "name_en": 'Ladyzhyn and Ladyzhynska Hromada',
                    },
                    {
                        "uid": 192,
                        "name": 'Ободівська',
                        "name_en": 'Obodivska Hromada',
                    },
                    {
                        "uid": 193,
                        "name": 'Ольгопільська',
                        "name_en": 'Olhopilska Hromada',
                    },
                    {
                        "uid": 194,
                        "name": 'Райгородська',
                        "name_en": 'Raihorodska Hromada',
                    },
                    {
                        "uid": 195,
                        "name": 'Соболівська',
                        "name_en": 'Sobolivska Hromada',
                    },
                    {
                        "uid": 196,
                        "name": 'Теплицька',
                        "name_en": 'Teplytska Hromada',
                    },
                    {
                        "uid": 197,
                        "name": 'Тростянецька',
                        "name_en": 'Trostianetska Hromada',
                    },
                    {
                        "uid": 198,
                        "name": 'Чечельницька',
                        "name_en": 'Chechelnytska Hromada',
                    },
                ],
            },
            {
                "uid": 35,
                "name": 'Жмеринський',
                "name_en": 'Zhmerynskyi Raion',
                "hromadas": [
                    {
                        "uid": 177,
                        "name": 'Барська',
                        "name_en": 'Barska Hromada',
                    },
                    {
                        "uid": 178,
                        "name": 'Джуринська',
                        "name_en": 'Dzhurynska Hromada',
                    },
                    {
                        "uid": 179,
                        "name": 'м. Жмеринка та Жмеринська',
                        "name_en": 'Zhmerynka and Zhmerynska Hromada',
                    },
                    {
                        "uid": 180,
                        "name": 'Копайгородська',
                        "name_en": 'Kopaihorodska Hromada',
                    },
                    {
                        "uid": 181,
                        "name": 'Мурафська',
                        "name_en": 'Murafska Hromada',
                    },
                    {
                        "uid": 182,
                        "name": 'Северинівська',
                        "name_en": 'Severynivska Hromada',
                    },
                    {
                        "uid": 183,
                        "name": 'Станіславчицька',
                        "name_en": 'Stanislavchytska Hromada',
                    },
                    {
                        "uid": 184,
                        "name": 'Шаргородська',
                        "name_en": 'Sharhorodska Hromada',
                    },
                ],
            },
            {
                "uid": 33,
                "name": 'Могилів-Подільський',
                "name_en": 'Mohyliv-Podilskyi Raion',
                "hromadas": [
                    {
                        "uid": 170,
                        "name": 'Бабчинецька',
                        "name_en": 'Babchynetska Hromada',
                    },
                    {
                        "uid": 171,
                        "name": 'Вендичанська',
                        "name_en": 'Vendychanska Hromada',
                    },
                    {
                        "uid": 172,
                        "name": 'м. Могилів-Подільський та Могилів-Подільська',
                        "name_en": 'Mohyliv-Podilskyi and Mohyliv-Podilska Hromada',
                    },
                    {
                        "uid": 173,
                        "name": 'Мурованокуриловецька',
                        "name_en": 'Murovanokurylovetska Hromada',
                    },
                    {
                        "uid": 174,
                        "name": 'Чернівецька',
                        "name_en": 'Chernivetska Hromada',
                    },
                    {
                        "uid": 175,
                        "name": 'Ямпільська',
                        "name_en": 'Yampilska Hromada',
                    },
                    {
                        "uid": 176,
                        "name": 'Яришівська',
                        "name_en": 'Yaryshivska Hromada',
                    },
                ],
            },
            {
                "uid": 32,
                "name": 'Тульчинський',
                "name_en": 'Tulchynskyi Raion',
                "hromadas": [
                    {
                        "uid": 199,
                        "name": 'Брацлавська',
                        "name_en": 'Bratslavska Hromada',
                    },
                    {
                        "uid": 200,
                        "name": 'Вапнярська',
                        "name_en": 'Vapniarska Hromada',
                    },
                    {
                        "uid": 201,
                        "name": 'Городківська',
                        "name_en": 'Horodkivska Hromada',
                    },
                    {
                        "uid": 202,
                        "name": 'Крижопільська',
                        "name_en": 'Kryzhopilska Hromada',
                    },
                    {
                        "uid": 203,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 204,
                        "name": 'Студенянська',
                        "name_en": 'Studenianska Hromada',
                    },
                    {
                        "uid": 205,
                        "name": 'Томашпільська',
                        "name_en": 'Tomashpilska Hromada',
                    },
                    {
                        "uid": 206,
                        "name": 'Тульчинська',
                        "name_en": 'Tulchynska Hromada',
                    },
                    {
                        "uid": 207,
                        "name": 'Шпиківська',
                        "name_en": 'Shpykivska Hromada',
                    },
                ],
            },
            {
                "uid": 34,
                "name": 'Хмільницький',
                "name_en": 'Khmilnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 208,
                        "name": 'Глуховецька',
                        "name_en": 'Hlukhovetska Hromada',
                    },
                    {
                        "uid": 209,
                        "name": 'Жданівська',
                        "name_en": 'Zhdanivska Hromada',
                    },
                    {
                        "uid": 211,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 212,
                        "name": 'м. Козятин та Козятинська',
                        "name_en": 'Koziatyn and Koziatynska Hromada',
                    },
                    {
                        "uid": 213,
                        "name": 'Махнівська',
                        "name_en": 'Makhnivska Hromada',
                    },
                    {
                        "uid": 214,
                        "name": 'Самгородоцька',
                        "name_en": 'Samhorodotska Hromada',
                    },
                    {
                        "uid": 215,
                        "name": 'Уланівська',
                        "name_en": 'Ulanivska Hromada',
                    },
                    {
                        "uid": 216,
                        "name": 'м. Хмільник та Хмільницька',
                        "name_en": 'Khmilnyk and Khmilnytska Hromada',
                    },
                    {
                        "uid": 210,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 9,
        "name": 'Дніпропетровська область',
        "type": LocationType.OBLAST,
        "name_en": 'Dnipropetrovska Oblast',
        "districts": [
            {
                "uid": 44,
                "name": 'Дніпровський',
                "name_en": 'Dniprovskyi Raion',
                "hromadas": [
                    {
                        "uid": 332,
                        "name": 'м. Дніпро та Дніпровська',
                        "name_en": 'Dnipro and Dniprovska Hromada',
                    },
                    {
                        "uid": 333,
                        "name": 'Китайгородська',
                        "name_en": 'Kytaihorodska Hromada',
                    },
                    {
                        "uid": 334,
                        "name": 'Любимівська',
                        "name_en": 'Liubymivska Hromada',
                    },
                    {
                        "uid": 335,
                        "name": 'Ляшківська',
                        "name_en": 'Liashkivska Hromada',
                    },
                    {
                        "uid": 336,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 337,
                        "name": 'Могилівська',
                        "name_en": 'Mohylivska Hromada',
                    },
                    {
                        "uid": 338,
                        "name": 'Новоолександрівська',
                        "name_en": 'Novooleksandrivska Hromada',
                    },
                    {
                        "uid": 339,
                        "name": 'Новопокровська',
                        "name_en": 'Novopokrovska Hromada',
                    },
                    {
                        "uid": 340,
                        "name": 'Обухівська',
                        "name_en": 'Obukhivska Hromada',
                    },
                    {
                        "uid": 341,
                        "name": 'Петриківська',
                        "name_en": 'Petrykivska Hromada',
                    },
                    {
                        "uid": 342,
                        "name": 'Підгородненська',
                        "name_en": 'Pidhorodnenska Hromada',
                    },
                    {
                        "uid": 343,
                        "name": 'Святовасилівська',
                        "name_en": 'Sviatovasylivska Hromada',
                    },
                    {
                        "uid": 344,
                        "name": 'Слобожанська',
                        "name_en": 'Slobozhanska Hromada',
                    },
                    {
                        "uid": 345,
                        "name": 'Солонянська',
                        "name_en": 'Solonianska Hromada',
                    },
                    {
                        "uid": 346,
                        "name": 'Сурсько-Литовська',
                        "name_en": 'Sursko-Lytovska Hromada',
                    },
                    {
                        "uid": 347,
                        "name": 'Царичанська',
                        "name_en": 'Tsarychanska Hromada',
                    },
                    {
                        "uid": 348,
                        "name": 'Чумаківська',
                        "name_en": 'Chumakivska Hromada',
                    },
                ],
            },
            {
                "uid": 42,
                "name": "Кам'янський",
                "name_en": 'Kamianskyi Raion',
                "hromadas": [
                    {
                        "uid": 293,
                        "name": 'Божедарівська',
                        "name_en": 'Bozhedarivska Hromada',
                    },
                    {
                        "uid": 295,
                        "name": 'Верхньодніпровська',
                        "name_en": 'Verkhnodniprovska Hromada',
                    },
                    {
                        "uid": 294,
                        "name": 'Верхівцівська',
                        "name_en": 'Verkhivtsivska Hromada',
                    },
                    {
                        "uid": 296,
                        "name": 'Вишнівська',
                        "name_en": 'Vyshnivska Hromada',
                    },
                    {
                        "uid": 297,
                        "name": 'м. Вільногірськ та Вільногірська',
                        "name_en": 'Vilnohirsk and Vilnohirska Hromada',
                    },
                    {
                        "uid": 298,
                        "name": 'м. Жовті Води та Жовтоводська',
                        "name_en": 'Zhovti Vody and Zhovtovodska Hromada',
                    },
                    {
                        "uid": 299,
                        "name": 'Затишнянська',
                        "name_en": 'Zatyshnianska Hromada',
                    },
                    {
                        "uid": 300,
                        "name": 'м. Кам’янське та Кам’янська',
                        "name_en": 'Kamyanske and Kamyanska Hromada',
                    },
                    {
                        "uid": 301,
                        "name": 'Криничанська',
                        "name_en": 'Krynychanska Hromada',
                    },
                    {
                        "uid": 302,
                        "name": 'Лихівська',
                        "name_en": 'Lykhivska Hromada',
                    },
                    {
                        "uid": 303,
                        "name": "П'ятихатська",
                        "name_en": 'Piatykhatska Hromada',
                    },
                    {
                        "uid": 304,
                        "name": 'Саксаганська',
                        "name_en": 'Saksahanska Hromada',
                    },
                ],
            },
            {
                "uid": 46,
                "name": 'Криворізький',
                "name_en": 'Kryvorizkyi Raion',
                "hromadas": [
                    {
                        "uid": 271,
                        "name": 'Апостолівська',
                        "name_en": 'Apostolivska Hromada',
                    },
                    {
                        "uid": 272,
                        "name": 'Вакулівська',
                        "name_en": 'Vakulivska Hromada',
                    },
                    {
                        "uid": 273,
                        "name": 'Глеюватська',
                        "name_en": 'Hleiuvatska Hromada',
                    },
                    {
                        "uid": 274,
                        "name": 'Гречаноподівська',
                        "name_en": 'Hrechanopodivska Hromada',
                    },
                    {
                        "uid": 275,
                        "name": 'Грушівська',
                        "name_en": 'Hrushivska Hromada',
                    },
                    {
                        "uid": 276,
                        "name": 'Девладівська',
                        "name_en": 'Devladivska Hromada',
                    },
                    {
                        "uid": 277,
                        "name": 'Зеленодольська',
                        "name_en": 'Zelenodolska Hromada',
                    },
                    {
                        "uid": 278,
                        "name": 'Карпівська',
                        "name_en": 'Karpivska Hromada',
                    },
                    {
                        "uid": 279,
                        "name": 'м. Кривий Ріг та Криворізька',
                        "name_en": 'Kryvyi Rih and Kryvorizka Hromada',
                    },
                    {
                        "uid": 280,
                        "name": 'Лозуватська',
                        "name_en": 'Lozuvatska Hromada',
                    },
                    {
                        "uid": 281,
                        "name": 'Нивотрудівська',
                        "name_en": 'Nyvotrudivska Hromada',
                    },
                    {
                        "uid": 282,
                        "name": 'Новолатівська',
                        "name_en": 'Novolativska Hromada',
                    },
                    {
                        "uid": 283,
                        "name": 'Новопільська',
                        "name_en": 'Novopilska Hromada',
                    },
                    {
                        "uid": 284,
                        "name": 'Софіївська',
                        "name_en": 'Sofiivska Hromada',
                    },
                    {
                        "uid": 285,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska Hromada',
                    },
                ],
            },
            {
                "uid": 47,
                "name": 'Нікопольський',
                "name_en": 'Nikopolskyi Raion',
                "hromadas": [
                    {
                        "uid": 349,
                        "name": 'м. Марганець та Марганецька',
                        "name_en": 'Marhanets and Marhanetska Hromada',
                    },
                    {
                        "uid": 350,
                        "name": 'Мирівська',
                        "name_en": 'Myrivska Hromada',
                    },
                    {
                        "uid": 351,
                        "name": 'м. Нікополь та Нікопольська',
                        "name_en": 'Nikopol and Nikopolska Hromada',
                    },
                    {
                        "uid": 352,
                        "name": 'Першотравневська',
                        "name_en": 'Pershotravnevska Hromada',
                    },
                    {
                        "uid": 354,
                        "name": 'м. Покров та Покровська',
                        "name_en": 'Pokrov and Pokrovska Hromada',
                    },
                    {
                        "uid": 353,
                        "name": 'Покровська',
                        "name_en": 'Pokrovska Hromada',
                    },
                    {
                        "uid": 355,
                        "name": 'Томаківська',
                        "name_en": 'Tomakivska Hromada',
                    },
                    {
                        "uid": 356,
                        "name": 'Червоногригорівська',
                        "name_en": 'Chervonohryhorivska Hromada',
                    },
                ],
            },
            {
                "uid": 45,
                "name": 'Павлоградський',
                "name_en": 'Pavlohradskyi Raion',
                "hromadas": [
                    {
                        "uid": 286,
                        "name": 'Богданівська',
                        "name_en": 'Bohdanivska Hromada',
                    },
                    {
                        "uid": 287,
                        "name": 'Вербківська',
                        "name_en": 'Verbkivska Hromada',
                    },
                    {
                        "uid": 288,
                        "name": 'Межиріцька',
                        "name_en": 'Mezhyritska Hromada',
                    },
                    {
                        "uid": 289,
                        "name": 'м. Павлоград та Павлоградська',
                        "name_en": 'Pavlohrad and Pavlohradska Hromada',
                    },
                    {
                        "uid": 290,
                        "name": 'м. Тернівка та Тернівська',
                        "name_en": 'Ternivka and Ternivska Hromada',
                    },
                    {
                        "uid": 291,
                        "name": 'Троїцька',
                        "name_en": 'Troitska Hromada',
                    },
                    {
                        "uid": 292,
                        "name": 'Юр’ївська',
                        "name_en": 'Yuryivska Hromada',
                    },
                ],
            },
            {
                "uid": 43,
                "name": 'Самарівський',
                "name_en": 'Samarivskyi Raion',
                "hromadas": [
                    {
                        "uid": 324,
                        "name": 'Губиниська',
                        "name_en": 'Hubynyska Hromada',
                    },
                    {
                        "uid": 325,
                        "name": 'Личківська',
                        "name_en": 'Lychkivska Hromada',
                    },
                    {
                        "uid": 326,
                        "name": 'Магдалинівська',
                        "name_en": 'Mahdalynivska Hromada',
                    },
                    {
                        "uid": 328,
                        "name": 'Перещепинська',
                        "name_en": 'Pereshchepynska Hromada',
                    },
                    {
                        "uid": 329,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 327,
                        "name": 'м. Самар та Самарівська',
                        "name_en": 'Samar and Samarivska Hromada',
                    },
                    {
                        "uid": 330,
                        "name": 'Черкаська',
                        "name_en": 'Cherkaska Hromada',
                    },
                    {
                        "uid": 331,
                        "name": 'Чернеччинська',
                        "name_en": 'Chernechchynska Hromada',
                    },
                ],
            },
            {
                "uid": 48,
                "name": 'Синельниківський',
                "name_en": 'Synelnykivskyi Raion',
                "hromadas": [
                    {
                        "uid": 305,
                        "name": 'Брагинівська',
                        "name_en": 'Brahynivska Hromada',
                    },
                    {
                        "uid": 306,
                        "name": 'Васильківська',
                        "name_en": 'Vasylkivska Hromada',
                    },
                    {
                        "uid": 307,
                        "name": 'Великомихайлівська',
                        "name_en": 'Velykomykhailivska Hromada',
                    },
                    {
                        "uid": 308,
                        "name": 'Дубовиківська',
                        "name_en": 'Dubovykivska Hromada',
                    },
                    {
                        "uid": 309,
                        "name": 'Зайцівська',
                        "name_en": 'Zaitsivska Hromada',
                    },
                    {
                        "uid": 311,
                        "name": 'Маломихайлівська',
                        "name_en": 'Malomykhailivska Hromada',
                    },
                    {
                        "uid": 312,
                        "name": 'Межівська',
                        "name_en": 'Mezhivska Hromada',
                    },
                    {
                        "uid": 313,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 314,
                        "name": 'Новопавлівська',
                        "name_en": 'Novopavlivska Hromada',
                    },
                    {
                        "uid": 316,
                        "name": 'Петропавлівська',
                        "name_en": 'Petropavlivska Hromada',
                    },
                    {
                        "uid": 317,
                        "name": 'Покровська',
                        "name_en": 'Pokrovska Hromada',
                    },
                    {
                        "uid": 318,
                        "name": 'Раївська',
                        "name_en": 'Raivska Hromada',
                    },
                    {
                        "uid": 319,
                        "name": 'Роздорська',
                        "name_en": 'Rozdorska Hromada',
                    },
                    {
                        "uid": 320,
                        "name": 'м. Синельникове та Синельниківська',
                        "name_en": 'Synelnykove and Synelnykivska Hromada',
                    },
                    {
                        "uid": 321,
                        "name": 'Славгородська',
                        "name_en": 'Slavhorodska Hromada',
                    },
                    {
                        "uid": 322,
                        "name": "Слов'янська",
                        "name_en": 'Slovianska Hromada',
                    },
                    {
                        "uid": 323,
                        "name": 'Українська',
                        "name_en": 'Ukrainska Hromada',
                    },
                    {
                        "uid": 315,
                        "name": 'м. Шахтарськ та Шахтарська',
                        "name_en": 'Shakhtarsk and Shakhtarska Hromada',
                    },
                    {
                        "uid": 310,
                        "name": 'Іларіонівська',
                        "name_en": 'Ilarionivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 28,
        "name": 'Донецька область',
        "type": LocationType.OBLAST,
        "name_en": 'Donetska Oblast',
        "districts": [
            {
                "uid": 54,
                "name": 'Бахмутський',
                "name_en": 'Bakhmutskyi Raion',
                "hromadas": [
                    {
                        "uid": 383,
                        "name": 'Бахмутська',
                        "name_en": 'Bakhmutska Hromada',
                    },
                    {
                        "uid": 384,
                        "name": 'Званівська',
                        "name_en": 'Zvanivska Hromada',
                    },
                    {
                        "uid": 385,
                        "name": 'Світлодарська',
                        "name_en": 'Svitlodarska Hromada',
                    },
                    {
                        "uid": 387,
                        "name": 'Соледарська',
                        "name_en": 'Soledarska Hromada',
                    },
                    {
                        "uid": 386,
                        "name": 'Сіверська',
                        "name_en": 'Siverska Hromada',
                    },
                    {
                        "uid": 388,
                        "name": 'Торецька',
                        "name_en": 'Toretska Hromada',
                    },
                    {
                        "uid": 389,
                        "name": 'Часовоярська',
                        "name_en": 'Chasovoiarska Hromada',
                    },
                ],
            },
            {
                "uid": 55,
                "name": 'Волноваський',
                "name_en": 'Volnovaskyi Raion',
                "hromadas": [
                    {
                        "uid": 390,
                        "name": 'Великоновосілківська',
                        "name_en": 'Velykonovosilkivska Hromada',
                    },
                    {
                        "uid": 391,
                        "name": 'Волноваська',
                        "name_en": 'Volnovaska Hromada',
                    },
                    {
                        "uid": 392,
                        "name": 'Вугледарська',
                        "name_en": 'Vuhledarska Hromada',
                    },
                    {
                        "uid": 393,
                        "name": 'Комарська',
                        "name_en": 'Komarska Hromada',
                    },
                    {
                        "uid": 394,
                        "name": 'Мирненська',
                        "name_en": 'Myrnenska Hromada',
                    },
                    {
                        "uid": 395,
                        "name": 'Ольгинська',
                        "name_en": 'Olhynska Hromada',
                    },
                    {
                        "uid": 396,
                        "name": 'Старомлинівська',
                        "name_en": 'Staromlynivska Hromada',
                    },
                    {
                        "uid": 397,
                        "name": 'Хлібодарівська',
                        "name_en": 'Khlibodarivska Hromada',
                    },
                ],
            },
            {
                "uid": 51,
                "name": 'Горлівський',
                "name_en": 'Horlivskyi Raion',
                "hromadas": [
                    {
                        "uid": 414,
                        "name": 'Вуглегірська міська громада',
                        "name_en": 'Vuhlehirska miska hromada',
                    },
                    {
                        "uid": 415,
                        "name": 'м. Горлівка та Горлівська міська громада',
                        "name_en": 'Horlivka and Horlivska miska hromada',
                    },
                    {
                        "uid": 416,
                        "name": 'Дебальцівська міська громада',
                        "name_en": 'Debaltsivska miska hromada',
                    },
                    {
                        "uid": 418,
                        "name": 'Жданівська міська громада',
                        "name_en": 'Zhdanivska miska hromada',
                    },
                    {
                        "uid": 419,
                        "name": 'Сніжнянська міська громада',
                        "name_en": 'Snizhnianska miska hromada',
                    },
                    {
                        "uid": 420,
                        "name": 'Хрестівська міська громада',
                        "name_en": 'Khrestivska miska hromada',
                    },
                    {
                        "uid": 421,
                        "name": 'Чистяківська міська громада',
                        "name_en": 'Chystiakivska miska hromada',
                    },
                    {
                        "uid": 422,
                        "name": 'Шахтарська міська громада',
                        "name_en": 'Shakhtarska miska hromada',
                    },
                    {
                        "uid": 417,
                        "name": 'м. Єнакієве та Єнакієвська міська громада',
                        "name_en": 'Yenakiieve and Yenakiievska miska hromada',
                    },
                ],
            },
            {
                "uid": 53,
                "name": 'Донецький',
                "name_en": 'Donetskyi Raion',
                "hromadas": [
                    {
                        "uid": 403,
                        "name": 'Амвросіївська міська громада',
                        "name_en": 'Amvrosiivska miska hromada',
                    },
                    {
                        "uid": 404,
                        "name": 'Донецька міська громада',
                        "name_en": 'Donetska miska hromada',
                    },
                    {
                        "uid": 406,
                        "name": 'м. Макіївка та Макіївська міська громада',
                        "name_en": 'Makiivka and Makiivska miska hromada',
                    },
                    {
                        "uid": 407,
                        "name": 'Харцизьк міська громада',
                        "name_en": 'Khartsyzk miska hromada',
                    },
                    {
                        "uid": 408,
                        "name": 'Ясинуватська міська громада',
                        "name_en": 'Yasynuvatska miska hromada',
                    },
                    {
                        "uid": 405,
                        "name": 'Іловайська міська громада',
                        "name_en": 'Ilovaiska miska hromada',
                    },
                ],
            },
            {
                "uid": 49,
                "name": 'Кальміуський',
                "name_en": 'Kalmiuskyi Raion',
                "hromadas": [
                    {
                        "uid": 409,
                        "name": 'Бойківська селищна громада',
                        "name_en": 'Boikivska selyshchna hromada',
                    },
                    {
                        "uid": 410,
                        "name": 'Докучаєвська міська громада',
                        "name_en": 'Dokuchaievska miska hromada',
                    },
                    {
                        "uid": 411,
                        "name": 'Кальміуська міська громада',
                        "name_en": 'Kalmiuska miska hromada',
                    },
                    {
                        "uid": 412,
                        "name": 'Новоазовська міська громада',
                        "name_en": 'Novoazovska miska hromada',
                    },
                    {
                        "uid": 413,
                        "name": 'Старобешівська селищна громада',
                        "name_en": 'Starobeshivska selyshchna hromada',
                    },
                ],
            },
            {
                "uid": 50,
                "name": 'Краматорський',
                "name_en": 'Kramatorskyi Raion',
                "hromadas": [
                    {
                        "uid": 371,
                        "name": 'Андріївська',
                        "name_en": 'Andriivska Hromada',
                    },
                    {
                        "uid": 372,
                        "name": 'Дружківська',
                        "name_en": 'Druzhkivska Hromada',
                    },
                    {
                        "uid": 374,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 375,
                        "name": 'м. Краматорськ та Краматорська',
                        "name_en": 'Kramatorsk and Kramatorska Hromada',
                    },
                    {
                        "uid": 376,
                        "name": 'Лиманська',
                        "name_en": 'Lymanska Hromada',
                    },
                    {
                        "uid": 377,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 378,
                        "name": 'Новодонецька',
                        "name_en": 'Novodonetska Hromada',
                    },
                    {
                        "uid": 379,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 380,
                        "name": 'Святогірська',
                        "name_en": 'Sviatohirska Hromada',
                    },
                    {
                        "uid": 381,
                        "name": "м. Слов'янськ та Слов'янська",
                        "name_en": 'Sloviansk and Slovianska Hromada',
                    },
                    {
                        "uid": 382,
                        "name": 'Черкаська',
                        "name_en": 'Cherkaska Hromada',
                    },
                    {
                        "uid": 373,
                        "name": 'Іллінівська',
                        "name_en": 'Illinivska Hromada',
                    },
                ],
            },
            {
                "uid": 52,
                "name": 'Маріупольський',
                "name_en": 'Mariupolskyi Raion',
                "hromadas": [
                    {
                        "uid": 398,
                        "name": 'Кальчицька',
                        "name_en": 'Kalchytska Hromada',
                    },
                    {
                        "uid": 399,
                        "name": 'Мангушська',
                        "name_en": 'Manhushska Hromada',
                    },
                    {
                        "uid": 400,
                        "name": 'м. Маріуполь та Маріупольська',
                        "name_en": 'Mariupol and Mariupolska Hromada',
                    },
                    {
                        "uid": 401,
                        "name": 'Нікольська',
                        "name_en": 'Nikolska Hromada',
                    },
                    {
                        "uid": 402,
                        "name": 'Сартанська',
                        "name_en": 'Sartanska Hromada',
                    },
                ],
            },
            {
                "uid": 56,
                "name": 'Покровський',
                "name_en": 'Pokrovskyi Raion',
                "hromadas": [
                    {
                        "uid": 357,
                        "name": 'Авдіївська',
                        "name_en": 'Avdiivska Hromada',
                    },
                    {
                        "uid": 358,
                        "name": 'Білозерська',
                        "name_en": 'Bilozerska Hromada',
                    },
                    {
                        "uid": 359,
                        "name": 'Гродівська',
                        "name_en": 'Hrodivska Hromada',
                    },
                    {
                        "uid": 360,
                        "name": 'Добропільська',
                        "name_en": 'Dobropilska Hromada',
                    },
                    {
                        "uid": 361,
                        "name": 'Криворізька',
                        "name_en": 'Kryvorizka Hromada',
                    },
                    {
                        "uid": 362,
                        "name": 'Курахівська',
                        "name_en": 'Kurakhivska Hromada',
                    },
                    {
                        "uid": 363,
                        "name": "Мар'їнська",
                        "name_en": 'Marinska Hromada',
                    },
                    {
                        "uid": 364,
                        "name": 'Мирноградська',
                        "name_en": 'Myrnohradska Hromada',
                    },
                    {
                        "uid": 365,
                        "name": 'Новогродівська',
                        "name_en": 'Novohrodivska Hromada',
                    },
                    {
                        "uid": 366,
                        "name": 'Очеретинська',
                        "name_en": 'Ocheretynska Hromada',
                    },
                    {
                        "uid": 367,
                        "name": 'Покровська',
                        "name_en": 'Pokrovska Hromada',
                    },
                    {
                        "uid": 368,
                        "name": 'Селидівська',
                        "name_en": 'Selydivska Hromada',
                    },
                    {
                        "uid": 369,
                        "name": 'Удачненська',
                        "name_en": 'Udachnenska Hromada',
                    },
                    {
                        "uid": 370,
                        "name": 'Шахівська',
                        "name_en": 'Shakhivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 10,
        "name": 'Житомирська область',
        "type": LocationType.OBLAST,
        "name_en": 'Zhytomyrska Oblast',
        "districts": [
            {
                "uid": 57,
                "name": 'Бердичівський',
                "name_en": 'Berdychivskyi Raion',
                "hromadas": [
                    {
                        "uid": 423,
                        "name": 'Андрушівська',
                        "name_en": 'Andrushivska Hromada',
                    },
                    {
                        "uid": 424,
                        "name": 'м. Бердичів та Бердичівська',
                        "name_en": 'Berdychiv and Berdychivska Hromada',
                    },
                    {
                        "uid": 425,
                        "name": 'Вчорайшенська',
                        "name_en": 'Vchoraishenska Hromada',
                    },
                    {
                        "uid": 426,
                        "name": 'Гришковецька',
                        "name_en": 'Hryshkovetska Hromada',
                    },
                    {
                        "uid": 427,
                        "name": 'Краснопільська',
                        "name_en": 'Krasnopilska Hromada',
                    },
                    {
                        "uid": 428,
                        "name": 'Райгородська',
                        "name_en": 'Raihorodska Hromada',
                    },
                    {
                        "uid": 429,
                        "name": 'Ружинська',
                        "name_en": 'Ruzhynska Hromada',
                    },
                    {
                        "uid": 430,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska Hromada',
                    },
                    {
                        "uid": 431,
                        "name": 'Червоненська',
                        "name_en": 'Chervonenska Hromada',
                    },
                    {
                        "uid": 432,
                        "name": 'Швайківська',
                        "name_en": 'Shvaikivska Hromada',
                    },
                ],
            },
            {
                "uid": 59,
                "name": 'Житомирський',
                "name_en": 'Zhytomyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 433,
                        "name": 'Андрушківська',
                        "name_en": 'Andrushkivska Hromada',
                    },
                    {
                        "uid": 434,
                        "name": 'Березівська',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 435,
                        "name": 'Брусилівська',
                        "name_en": 'Brusylivska Hromada',
                    },
                    {
                        "uid": 436,
                        "name": 'Високівська',
                        "name_en": 'Vysokivska Hromada',
                    },
                    {
                        "uid": 437,
                        "name": 'Вишевицька',
                        "name_en": 'Vyshevytska Hromada',
                    },
                    {
                        "uid": 439,
                        "name": 'Волицька',
                        "name_en": 'Volytska Hromada',
                    },
                    {
                        "uid": 438,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 440,
                        "name": 'Глибочицька',
                        "name_en": 'Hlybochytska Hromada',
                    },
                    {
                        "uid": 441,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 442,
                        "name": 'м. Житомир та Житомирська',
                        "name_en": 'Zhytomyr and Zhytomyrska Hromada',
                    },
                    {
                        "uid": 443,
                        "name": 'Квітнева',
                        "name_en": 'Kvitneva Hromada',
                    },
                    {
                        "uid": 444,
                        "name": 'Корнинська',
                        "name_en": 'Kornynska Hromada',
                    },
                    {
                        "uid": 445,
                        "name": 'Коростишівська',
                        "name_en": 'Korostyshivska Hromada',
                    },
                    {
                        "uid": 446,
                        "name": 'Курненська',
                        "name_en": 'Kurnenska Hromada',
                    },
                    {
                        "uid": 447,
                        "name": 'Любарська',
                        "name_en": 'Liubarska Hromada',
                    },
                    {
                        "uid": 448,
                        "name": 'Миропільська',
                        "name_en": 'Myropilska Hromada',
                    },
                    {
                        "uid": 449,
                        "name": 'Новоборівська',
                        "name_en": 'Novoborivska Hromada',
                    },
                    {
                        "uid": 450,
                        "name": 'Новогуйвинська',
                        "name_en": 'Novohuivynska Hromada',
                    },
                    {
                        "uid": 451,
                        "name": 'Оліївська',
                        "name_en": 'Oliivska Hromada',
                    },
                    {
                        "uid": 452,
                        "name": 'Попільнянська',
                        "name_en": 'Popilnianska Hromada',
                    },
                    {
                        "uid": 453,
                        "name": 'Потіївська',
                        "name_en": 'Potiivska Hromada',
                    },
                    {
                        "uid": 454,
                        "name": 'Пулинська',
                        "name_en": 'Pulynska Hromada',
                    },
                    {
                        "uid": 455,
                        "name": 'Радомишльська',
                        "name_en": 'Radomyshlska Hromada',
                    },
                    {
                        "uid": 456,
                        "name": 'Романівська',
                        "name_en": 'Romanivska Hromada',
                    },
                    {
                        "uid": 457,
                        "name": 'Станишівська',
                        "name_en": 'Stanyshivska Hromada',
                    },
                    {
                        "uid": 458,
                        "name": 'Старосілецька',
                        "name_en": 'Starosiletska Hromada',
                    },
                    {
                        "uid": 459,
                        "name": 'Тетерівська',
                        "name_en": 'Teterivska Hromada',
                    },
                    {
                        "uid": 460,
                        "name": 'Харитонівська',
                        "name_en": 'Kharytonivska Hromada',
                    },
                    {
                        "uid": 461,
                        "name": 'Хорошівська',
                        "name_en": 'Khoroshivska Hromada',
                    },
                    {
                        "uid": 462,
                        "name": 'Черняхівська',
                        "name_en": 'Cherniakhivska Hromada',
                    },
                    {
                        "uid": 463,
                        "name": 'Чуднівська',
                        "name_en": 'Chudnivska Hromada',
                    },
                ],
            },
            {
                "uid": 60,
                "name": 'Звягельський',
                "name_en": 'Zviahelskyi Raion',
                "hromadas": [
                    {
                        "uid": 464,
                        "name": 'Баранівська',
                        "name_en": 'Baranivska Hromada',
                    },
                    {
                        "uid": 465,
                        "name": 'Барашівська',
                        "name_en": 'Barashivska Hromada',
                    },
                    {
                        "uid": 466,
                        "name": 'Брониківська',
                        "name_en": 'Bronykivska Hromada',
                    },
                    {
                        "uid": 467,
                        "name": 'Городницька',
                        "name_en": 'Horodnytska Hromada',
                    },
                    {
                        "uid": 468,
                        "name": 'Довбиська',
                        "name_en": 'Dovbyska Hromada',
                    },
                    {
                        "uid": 469,
                        "name": 'Дубрівська',
                        "name_en": 'Dubrivska Hromada',
                    },
                    {
                        "uid": 471,
                        "name": 'м. Звягель та Звягельська',
                        "name_en": 'Zviahel and Zviahelska Hromada',
                    },
                    {
                        "uid": 472,
                        "name": 'Піщівська',
                        "name_en": 'Pishchivska Hromada',
                    },
                    {
                        "uid": 473,
                        "name": 'Стриївська',
                        "name_en": 'Stryivska Hromada',
                    },
                    {
                        "uid": 474,
                        "name": 'Чижівська',
                        "name_en": 'Chyzhivska Hromada',
                    },
                    {
                        "uid": 475,
                        "name": 'Ярунська',
                        "name_en": 'Yarunska Hromada',
                    },
                    {
                        "uid": 470,
                        "name": 'Ємільчинська',
                        "name_en": 'Yemilchynska Hromada',
                    },
                ],
            },
            {
                "uid": 58,
                "name": 'Коростенський',
                "name_en": 'Korostenskyi Raion',
                "hromadas": [
                    {
                        "uid": 476,
                        "name": 'Білокоровицька',
                        "name_en": 'Bilokorovytska Hromada',
                    },
                    {
                        "uid": 477,
                        "name": 'Гладковицька',
                        "name_en": 'Hladkovytska Hromada',
                    },
                    {
                        "uid": 478,
                        "name": 'Горщиківська',
                        "name_en": 'Horshchykivska Hromada',
                    },
                    {
                        "uid": 480,
                        "name": 'м. Коростень та Коростенська',
                        "name_en": 'Korosten and Korostenska Hromada',
                    },
                    {
                        "uid": 481,
                        "name": 'Лугинська',
                        "name_en": 'Luhynska Hromada',
                    },
                    {
                        "uid": 482,
                        "name": 'м. Малин та Малинська',
                        "name_en": 'Malyn and Malynska Hromada',
                    },
                    {
                        "uid": 483,
                        "name": 'Народицька',
                        "name_en": 'Narodytska Hromada',
                    },
                    {
                        "uid": 484,
                        "name": 'Овруцька',
                        "name_en": 'Ovrutska Hromada',
                    },
                    {
                        "uid": 485,
                        "name": 'Олевська',
                        "name_en": 'Olevska Hromada',
                    },
                    {
                        "uid": 486,
                        "name": 'Словечанська',
                        "name_en": 'Slovechanska Hromada',
                    },
                    {
                        "uid": 487,
                        "name": 'Ушомирська',
                        "name_en": 'Ushomyrska Hromada',
                    },
                    {
                        "uid": 488,
                        "name": 'Чоповицька',
                        "name_en": 'Chopovytska Hromada',
                    },
                    {
                        "uid": 479,
                        "name": 'Іршанська',
                        "name_en": 'Irshanska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 11,
        "name": 'Закарпатська область',
        "type": LocationType.OBLAST,
        "name_en": 'Zakarpatska Oblast',
        "districts": [
            {
                "uid": 61,
                "name": 'Берегівський',
                "name_en": 'Berehivskyi Raion',
                "hromadas": [
                    {
                        "uid": 503,
                        "name": 'Батівська',
                        "name_en": 'Bativska Hromada',
                    },
                    {
                        "uid": 504,
                        "name": 'м. Берегове та Берегівська',
                        "name_en": 'Berehove and Berehivska Hromada',
                    },
                    {
                        "uid": 505,
                        "name": 'Великоберезька',
                        "name_en": 'Velykoberezka Hromada',
                    },
                    {
                        "uid": 506,
                        "name": 'Великобийганська',
                        "name_en": 'Velykobyihanska Hromada',
                    },
                    {
                        "uid": 507,
                        "name": 'Вилоцька',
                        "name_en": 'Vylotska Hromada',
                    },
                    {
                        "uid": 508,
                        "name": 'м. Виноградів та Виноградівська',
                        "name_en": 'Vynohradiv and Vynohradivska Hromada',
                    },
                    {
                        "uid": 509,
                        "name": "Кам'янська",
                        "name_en": 'Kamianska Hromada',
                    },
                    {
                        "uid": 510,
                        "name": 'Королівська',
                        "name_en": 'Korolivska Hromada',
                    },
                    {
                        "uid": 511,
                        "name": 'Косоньська',
                        "name_en": 'Kosonska Hromada',
                    },
                    {
                        "uid": 512,
                        "name": 'Пийтерфолвівська',
                        "name_en": 'Pyiterfolvivska Hromada',
                    },
                ],
            },
            {
                "uid": 65,
                "name": 'Мукачівський',
                "name_en": 'Mukachivskyi Raion',
                "hromadas": [
                    {
                        "uid": 540,
                        "name": 'Великолучківська',
                        "name_en": 'Velykoluchkivska Hromada',
                    },
                    {
                        "uid": 541,
                        "name": 'Верхньокоропецька',
                        "name_en": 'Verkhnokoropetska Hromada',
                    },
                    {
                        "uid": 542,
                        "name": 'Воловецька',
                        "name_en": 'Volovetska Hromada',
                    },
                    {
                        "uid": 543,
                        "name": 'Горондівська',
                        "name_en": 'Horondivska Hromada',
                    },
                    {
                        "uid": 544,
                        "name": 'Жденіївська',
                        "name_en": 'Zhdeniivska Hromada',
                    },
                    {
                        "uid": 546,
                        "name": 'Кольчинська',
                        "name_en": 'Kolchynska Hromada',
                    },
                    {
                        "uid": 547,
                        "name": 'м. Мукачево та Мукачівська',
                        "name_en": 'Mukachevo and Mukachivska Hromada',
                    },
                    {
                        "uid": 548,
                        "name": 'Неліпинська',
                        "name_en": 'Nelipynska Hromada',
                    },
                    {
                        "uid": 549,
                        "name": 'Нижньоворітська',
                        "name_en": 'Nyzhnovoritska Hromada',
                    },
                    {
                        "uid": 550,
                        "name": 'Полянська',
                        "name_en": 'Polianska Hromada',
                    },
                    {
                        "uid": 551,
                        "name": 'Свалявська',
                        "name_en": 'Svaliavska Hromada',
                    },
                    {
                        "uid": 552,
                        "name": 'Чинадіївська',
                        "name_en": 'Chynadiivska Hromada',
                    },
                    {
                        "uid": 545,
                        "name": 'Івановецька',
                        "name_en": 'Ivanovetska Hromada',
                    },
                ],
            },
            {
                "uid": 63,
                "name": 'Рахівський',
                "name_en": 'Rakhivskyi Raion',
                "hromadas": [
                    {
                        "uid": 536,
                        "name": 'Богданська',
                        "name_en": 'Bohdanska Hromada',
                    },
                    {
                        "uid": 537,
                        "name": 'Великобичківська',
                        "name_en": 'Velykobychkivska Hromada',
                    },
                    {
                        "uid": 538,
                        "name": 'м. Рахів та Рахівська',
                        "name_en": 'Rakhiv and Rakhivska Hromada',
                    },
                    {
                        "uid": 539,
                        "name": 'Ясінянська',
                        "name_en": 'Yasinianska Hromada',
                    },
                ],
            },
            {
                "uid": 64,
                "name": 'Тячівський',
                "name_en": 'Tiachivskyi Raion',
                "hromadas": [
                    {
                        "uid": 513,
                        "name": 'Бедевлянська',
                        "name_en": 'Bedevlianska Hromada',
                    },
                    {
                        "uid": 514,
                        "name": 'Буштинська',
                        "name_en": 'Bushtynska Hromada',
                    },
                    {
                        "uid": 515,
                        "name": 'Вільховецька',
                        "name_en": 'Vilkhovetska Hromada',
                    },
                    {
                        "uid": 516,
                        "name": 'Дубівська',
                        "name_en": 'Dubivska Hromada',
                    },
                    {
                        "uid": 517,
                        "name": 'Нересницька',
                        "name_en": 'Neresnytska Hromada',
                    },
                    {
                        "uid": 518,
                        "name": 'Солотвинська',
                        "name_en": 'Solotvynska Hromada',
                    },
                    {
                        "uid": 519,
                        "name": 'Тересвянська',
                        "name_en": 'Teresvianska Hromada',
                    },
                    {
                        "uid": 520,
                        "name": 'м. Тячів та Тячівська',
                        "name_en": 'Tiachiv and Tiachivska Hromada',
                    },
                    {
                        "uid": 521,
                        "name": 'Углянська',
                        "name_en": 'Uhlianska Hromada',
                    },
                    {
                        "uid": 522,
                        "name": 'Усть-Чорнянська',
                        "name_en": 'Ust-Chornianska Hromada',
                    },
                ],
            },
            {
                "uid": 66,
                "name": 'Ужгородський',
                "name_en": 'Uzhhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 489,
                        "name": 'Баранинська',
                        "name_en": 'Baranynska Hromada',
                    },
                    {
                        "uid": 490,
                        "name": 'Великоберезнянська',
                        "name_en": 'Velykobereznianska Hromada',
                    },
                    {
                        "uid": 491,
                        "name": 'Великодобронська',
                        "name_en": 'Velykodobronska Hromada',
                    },
                    {
                        "uid": 492,
                        "name": 'Дубриницько-Малоберезня',
                        "name_en": 'Dubrynytsko-Malobereznia Hromada',
                    },
                    {
                        "uid": 493,
                        "name": 'Костринська',
                        "name_en": 'Kostrynska Hromada',
                    },
                    {
                        "uid": 494,
                        "name": 'Оноківська',
                        "name_en": 'Onokivska Hromada',
                    },
                    {
                        "uid": 495,
                        "name": 'Перечинська',
                        "name_en": 'Perechynska Hromada',
                    },
                    {
                        "uid": 496,
                        "name": 'Середнянська',
                        "name_en": 'Serednianska Hromada',
                    },
                    {
                        "uid": 497,
                        "name": 'Ставненська',
                        "name_en": 'Stavnenska Hromada',
                    },
                    {
                        "uid": 498,
                        "name": 'Сюртівська',
                        "name_en": 'Siurtivska Hromada',
                    },
                    {
                        "uid": 499,
                        "name": "Тур'є-Реметівська",
                        "name_en": 'Turie-Remetivska Hromada',
                    },
                    {
                        "uid": 500,
                        "name": 'м. Ужгород та Ужгородська',
                        "name_en": 'Uzhhorod and Uzhhorodska Hromada',
                    },
                    {
                        "uid": 501,
                        "name": 'Холмківська',
                        "name_en": 'Kholmkivska Hromada',
                    },
                    {
                        "uid": 502,
                        "name": 'м. Чоп та Чопська',
                        "name_en": 'Chop and Chopska Hromada',
                    },
                ],
            },
            {
                "uid": 62,
                "name": 'Хустський',
                "name_en": 'Khustskyi Raion',
                "hromadas": [
                    {
                        "uid": 523,
                        "name": 'Білківська',
                        "name_en": 'Bilkivska Hromada',
                    },
                    {
                        "uid": 524,
                        "name": 'Вишківська',
                        "name_en": 'Vyshkivska Hromada',
                    },
                    {
                        "uid": 525,
                        "name": 'Горінчівська',
                        "name_en": 'Horinchivska Hromada',
                    },
                    {
                        "uid": 526,
                        "name": 'Довжанська',
                        "name_en": 'Dovzhanska Hromada',
                    },
                    {
                        "uid": 527,
                        "name": 'Драгівська',
                        "name_en": 'Drahivska Hromada',
                    },
                    {
                        "uid": 528,
                        "name": 'Зарічанська',
                        "name_en": 'Zarichanska Hromada',
                    },
                    {
                        "uid": 530,
                        "name": 'Керецьківська',
                        "name_en": 'Keretskivska Hromada',
                    },
                    {
                        "uid": 531,
                        "name": 'Колочавська',
                        "name_en": 'Kolochavska Hromada',
                    },
                    {
                        "uid": 532,
                        "name": "м. Міжгір'я та Міжгірська",
                        "name_en": 'Mizhhiria and Mizhhirska Hromada',
                    },
                    {
                        "uid": 533,
                        "name": 'Пилипецька',
                        "name_en": 'Pylypetska Hromada',
                    },
                    {
                        "uid": 534,
                        "name": 'Синевирська',
                        "name_en": 'Synevyrska Hromada',
                    },
                    {
                        "uid": 535,
                        "name": 'м. Хуст та Хустська',
                        "name_en": 'Khust and Khustska Hromada',
                    },
                    {
                        "uid": 529,
                        "name": 'м. Іршава та Іршавська',
                        "name_en": 'Irshava and Irshavska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 12,
        "name": 'Запорізька область',
        "type": LocationType.OBLAST,
        "name_en": 'Zaporizka Oblast',
        "districts": [
            {
                "uid": 147,
                "name": 'Бердянський',
                "name_en": 'Berdianskyi Raion',
                "hromadas": [
                    {
                        "uid": 553,
                        "name": 'Андрівська',
                        "name_en": 'Andrivska Hromada',
                    },
                    {
                        "uid": 554,
                        "name": 'Андріївська',
                        "name_en": 'Andriivska Hromada',
                    },
                    {
                        "uid": 555,
                        "name": 'м. Бердянськ та Бердянська',
                        "name_en": 'Berdiansk and Berdianska Hromada',
                    },
                    {
                        "uid": 556,
                        "name": 'Берестівська',
                        "name_en": 'Berestivska Hromada',
                    },
                    {
                        "uid": 557,
                        "name": 'Коларівська',
                        "name_en": 'Kolarivska Hromada',
                    },
                    {
                        "uid": 558,
                        "name": 'Осипенківська',
                        "name_en": 'Osypenkivska Hromada',
                    },
                    {
                        "uid": 559,
                        "name": 'Приморська',
                        "name_en": 'Prymorska Hromada',
                    },
                    {
                        "uid": 560,
                        "name": 'Чернігівська',
                        "name_en": 'Chernihivska Hromada',
                    },
                ],
            },
            {
                "uid": 146,
                "name": 'Василівський',
                "name_en": 'Vasylivskyi Raion',
                "hromadas": [
                    {
                        "uid": 593,
                        "name": 'Благовіщенська',
                        "name_en": 'Blahovishchenska Hromada',
                    },
                    {
                        "uid": 594,
                        "name": 'Василівська',
                        "name_en": 'Vasylivska Hromada',
                    },
                    {
                        "uid": 595,
                        "name": 'Великобілозерська',
                        "name_en": 'Velykobilozerska Hromada',
                    },
                    {
                        "uid": 596,
                        "name": 'Водянська',
                        "name_en": 'Vodianska Hromada',
                    },
                    {
                        "uid": 597,
                        "name": 'Дніпрорудненська',
                        "name_en": 'Dniprorudnenska Hromada',
                    },
                    {
                        "uid": 598,
                        "name": 'м. Енергодар та Енергодарська',
                        "name_en": 'Enerhodar and Enerhodarska Hromada',
                    },
                    {
                        "uid": 599,
                        "name": "Кам'янсько-Дніпровська",
                        "name_en": 'Kamiansko-Dniprovska Hromada',
                    },
                    {
                        "uid": 600,
                        "name": 'Малобілозерська',
                        "name_en": 'Malobilozerska Hromada',
                    },
                    {
                        "uid": 601,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 602,
                        "name": 'Роздольська',
                        "name_en": 'Rozdolska Hromada',
                    },
                    {
                        "uid": 603,
                        "name": 'Степногірська',
                        "name_en": 'Stepnohirska Hromada',
                    },
                ],
            },
            {
                "uid": 149,
                "name": 'Запорізький',
                "name_en": 'Zaporizkyi Raion',
                "hromadas": [
                    {
                        "uid": 561,
                        "name": 'Біленьківська',
                        "name_en": 'Bilenkivska Hromada',
                    },
                    {
                        "uid": 562,
                        "name": 'Вільнянська',
                        "name_en": 'Vilnianska Hromada',
                    },
                    {
                        "uid": 563,
                        "name": 'Долинська',
                        "name_en": 'Dolynska Hromada',
                    },
                    {
                        "uid": 564,
                        "name": 'м. Запоріжжя та Запорізька',
                        "name_en": 'Zaporizhzhia and Zaporizka Hromada',
                    },
                    {
                        "uid": 565,
                        "name": 'Комишуваська',
                        "name_en": 'Komyshuvaska Hromada',
                    },
                    {
                        "uid": 566,
                        "name": 'Кушугумська',
                        "name_en": 'Kushuhumska Hromada',
                    },
                    {
                        "uid": 567,
                        "name": 'Матвіївська',
                        "name_en": 'Matviivska Hromada',
                    },
                    {
                        "uid": 569,
                        "name": 'Михайло-Лукашівська',
                        "name_en": 'Mykhailo-Lukashivska Hromada',
                    },
                    {
                        "uid": 568,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 570,
                        "name": 'Новомиколаївська',
                        "name_en": 'Novomykolaivska Hromada',
                    },
                    {
                        "uid": 571,
                        "name": 'Новоолександрівська',
                        "name_en": 'Novooleksandrivska Hromada',
                    },
                    {
                        "uid": 572,
                        "name": 'Павлівська',
                        "name_en": 'Pavlivska Hromada',
                    },
                    {
                        "uid": 573,
                        "name": 'Петро-Михайлівська',
                        "name_en": 'Petro-Mykhailivska Hromada',
                    },
                    {
                        "uid": 574,
                        "name": 'Степненська',
                        "name_en": 'Stepnenska Hromada',
                    },
                    {
                        "uid": 575,
                        "name": 'Таврійська',
                        "name_en": 'Tavriiska Hromada',
                    },
                    {
                        "uid": 576,
                        "name": 'Тернуватська',
                        "name_en": 'Ternuvatska Hromada',
                    },
                    {
                        "uid": 577,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska Hromada',
                    },
                ],
            },
            {
                "uid": 148,
                "name": 'Мелітопольський',
                "name_en": 'Melitopolskyi Raion',
                "hromadas": [
                    {
                        "uid": 604,
                        "name": 'Веселівська',
                        "name_en": 'Veselivska Hromada',
                    },
                    {
                        "uid": 605,
                        "name": 'Кирилівська',
                        "name_en": 'Kyrylivska Hromada',
                    },
                    {
                        "uid": 606,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 607,
                        "name": 'м. Мелітополь та Мелітопольська',
                        "name_en": 'Melitopol and Melitopolska Hromada',
                    },
                    {
                        "uid": 608,
                        "name": 'Мирненська',
                        "name_en": 'Myrnenska Hromada',
                    },
                    {
                        "uid": 609,
                        "name": 'Новенська',
                        "name_en": 'Novenska Hromada',
                    },
                    {
                        "uid": 610,
                        "name": 'Новобогданівська',
                        "name_en": 'Novobohdanivska Hromada',
                    },
                    {
                        "uid": 611,
                        "name": 'Нововасилівська',
                        "name_en": 'Novovasylivska Hromada',
                    },
                    {
                        "uid": 612,
                        "name": 'Новоуспенівська',
                        "name_en": 'Novouspenivska Hromada',
                    },
                    {
                        "uid": 613,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 614,
                        "name": 'Плодородненська',
                        "name_en": 'Plodorodnenska Hromada',
                    },
                    {
                        "uid": 615,
                        "name": 'Приазовська',
                        "name_en": 'Pryazovska Hromada',
                    },
                    {
                        "uid": 616,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska Hromada',
                    },
                    {
                        "uid": 617,
                        "name": 'Терпіннівська',
                        "name_en": 'Terpinnivska Hromada',
                    },
                    {
                        "uid": 618,
                        "name": 'Чкаловська',
                        "name_en": 'Chkalovska Hromada',
                    },
                    {
                        "uid": 619,
                        "name": 'Якимівська',
                        "name_en": 'Yakymivska Hromada',
                    },
                ],
            },
            {
                "uid": 145,
                "name": 'Пологівський',
                "name_en": 'Polohivskyi Raion',
                "hromadas": [
                    {
                        "uid": 578,
                        "name": 'Більмацька',
                        "name_en": 'Bilmatska Hromada',
                    },
                    {
                        "uid": 579,
                        "name": 'Воздвижівська',
                        "name_en": 'Vozdvyzhivska Hromada',
                    },
                    {
                        "uid": 580,
                        "name": 'Воскресенська',
                        "name_en": 'Voskresenska Hromada',
                    },
                    {
                        "uid": 581,
                        "name": 'Гуляйпільська',
                        "name_en": 'Huliaipilska Hromada',
                    },
                    {
                        "uid": 582,
                        "name": 'Комиш-Зорянська',
                        "name_en": 'Komysh-Zorianska Hromada',
                    },
                    {
                        "uid": 583,
                        "name": 'Малинівська',
                        "name_en": 'Malynivska Hromada',
                    },
                    {
                        "uid": 584,
                        "name": 'Малотокмачанська',
                        "name_en": 'Malotokmachanska Hromada',
                    },
                    {
                        "uid": 585,
                        "name": 'Молочанська',
                        "name_en": 'Molochanska Hromada',
                    },
                    {
                        "uid": 586,
                        "name": 'Оріхівська',
                        "name_en": 'Orikhivska Hromada',
                    },
                    {
                        "uid": 587,
                        "name": 'Пологівська',
                        "name_en": 'Polohivska Hromada',
                    },
                    {
                        "uid": 588,
                        "name": 'Преображенська',
                        "name_en": 'Preobrazhenska Hromada',
                    },
                    {
                        "uid": 589,
                        "name": 'Розівська',
                        "name_en": 'Rozivska Hromada',
                    },
                    {
                        "uid": 590,
                        "name": 'Смирновська',
                        "name_en": 'Smyrnovska Hromada',
                    },
                    {
                        "uid": 591,
                        "name": 'м. Токмак та Токмацька',
                        "name_en": 'Tokmak and Tokmatska Hromada',
                    },
                    {
                        "uid": 592,
                        "name": 'Федорівська',
                        "name_en": 'Fedorivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 14,
        "name": 'Київська область',
        "type": LocationType.OBLAST,
        "name_en": 'Kyivska Oblast',
        "districts": [
            {
                "uid": 78,
                "name": 'Бориспільський',
                "name_en": 'Boryspilskyi Raion',
                "hromadas": [
                    {
                        "uid": 733,
                        "name": 'м. Бориспіль та Бориспільська',
                        "name_en": 'Boryspil and Boryspilska Hromada',
                    },
                    {
                        "uid": 734,
                        "name": 'Вороньківська',
                        "name_en": 'Voronkivska Hromada',
                    },
                    {
                        "uid": 735,
                        "name": 'Гірська',
                        "name_en": 'Hirska Hromada',
                    },
                    {
                        "uid": 736,
                        "name": 'Дівичківська',
                        "name_en": 'Divychkivska Hromada',
                    },
                    {
                        "uid": 737,
                        "name": 'Золочівська',
                        "name_en": 'Zolochivska Hromada',
                    },
                    {
                        "uid": 738,
                        "name": 'м. Переяслав та Переяславська',
                        "name_en": 'Pereiaslav and Pereiaslavska Hromada',
                    },
                    {
                        "uid": 739,
                        "name": 'Пристолична',
                        "name_en": 'Prystolychna Hromada',
                    },
                    {
                        "uid": 740,
                        "name": 'Студениківська',
                        "name_en": 'Studenykivska Hromada',
                    },
                    {
                        "uid": 741,
                        "name": 'Ташанська',
                        "name_en": 'Tashanska Hromada',
                    },
                    {
                        "uid": 742,
                        "name": 'Циблівська',
                        "name_en": 'Tsyblivska Hromada',
                    },
                    {
                        "uid": 743,
                        "name": 'Яготинська',
                        "name_en": 'Yahotynska Hromada',
                    },
                ],
            },
            {
                "uid": 79,
                "name": 'Броварський',
                "name_en": 'Brovarskyi Raion',
                "hromadas": [
                    {
                        "uid": 682,
                        "name": 'Баришівська',
                        "name_en": 'Baryshivska Hromada',
                    },
                    {
                        "uid": 683,
                        "name": 'м. Березань та Березанська',
                        "name_en": 'Berezan and Berezanska Hromada',
                    },
                    {
                        "uid": 684,
                        "name": 'м. Бровари та Броварська',
                        "name_en": 'Brovary and Brovarska Hromada',
                    },
                    {
                        "uid": 685,
                        "name": 'Великодимерська',
                        "name_en": 'Velykodymerska Hromada',
                    },
                    {
                        "uid": 686,
                        "name": 'Зазимська',
                        "name_en": 'Zazymska Hromada',
                    },
                    {
                        "uid": 687,
                        "name": 'Згурівська',
                        "name_en": 'Zghurivska Hromada',
                    },
                    {
                        "uid": 688,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 689,
                        "name": 'Калитянська',
                        "name_en": 'Kalytianska Hromada',
                    },
                ],
            },
            {
                "uid": 75,
                "name": 'Бучанський',
                "name_en": 'Buchanskyi Raion',
                "hromadas": [
                    {
                        "uid": 700,
                        "name": 'Бородянська',
                        "name_en": 'Borodianska Hromada',
                    },
                    {
                        "uid": 701,
                        "name": 'Борщагівська',
                        "name_en": 'Borshchahivska Hromada',
                    },
                    {
                        "uid": 702,
                        "name": 'м. Буча та Бучанська',
                        "name_en": 'Bucha and Buchanska Hromada',
                    },
                    {
                        "uid": 699,
                        "name": 'Білогородська',
                        "name_en": 'Bilohorodska Hromada',
                    },
                    {
                        "uid": 703,
                        "name": 'Вишнева',
                        "name_en": 'Vyshneva Hromada',
                    },
                    {
                        "uid": 704,
                        "name": 'Гостомелська',
                        "name_en": 'Hostomelska Hromada',
                    },
                    {
                        "uid": 705,
                        "name": 'Дмитрівська',
                        "name_en": 'Dmytrivska Hromada',
                    },
                    {
                        "uid": 707,
                        "name": 'Коцюбинська',
                        "name_en": 'Kotsiubynska Hromada',
                    },
                    {
                        "uid": 708,
                        "name": 'Макарівська',
                        "name_en": 'Makarivska Hromada',
                    },
                    {
                        "uid": 709,
                        "name": 'Немішаївська',
                        "name_en": 'Nemishaivska Hromada',
                    },
                    {
                        "uid": 710,
                        "name": 'Пісківська',
                        "name_en": 'Piskivska Hromada',
                    },
                    {
                        "uid": 706,
                        "name": 'м. Ірпінь та Ірпінська',
                        "name_en": 'Irpin and Irpinska Hromada',
                    },
                ],
            },
            {
                "uid": 73,
                "name": 'Білоцерківський',
                "name_en": 'Bilotserkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 711,
                        "name": 'м. Біла Церква та Білоцерківська',
                        "name_en": 'Bila Tserkva and Bilotserkivska Hromada',
                    },
                    {
                        "uid": 712,
                        "name": 'Володарська',
                        "name_en": 'Volodarska Hromada',
                    },
                    {
                        "uid": 713,
                        "name": 'Гребінківська',
                        "name_en": 'Hrebinkivska Hromada',
                    },
                    {
                        "uid": 714,
                        "name": 'Ковалівська',
                        "name_en": 'Kovalivska Hromada',
                    },
                    {
                        "uid": 715,
                        "name": 'Маловільшанська',
                        "name_en": 'Malovilshanska Hromada',
                    },
                    {
                        "uid": 716,
                        "name": 'Медвинська',
                        "name_en": 'Medvynska Hromada',
                    },
                    {
                        "uid": 717,
                        "name": 'Рокитнянська',
                        "name_en": 'Rokytnianska Hromada',
                    },
                    {
                        "uid": 718,
                        "name": 'Сквирська',
                        "name_en": 'Skvyrska Hromada',
                    },
                    {
                        "uid": 719,
                        "name": 'Ставищенська',
                        "name_en": 'Stavyshchenska Hromada',
                    },
                    {
                        "uid": 720,
                        "name": 'Таращанська',
                        "name_en": 'Tarashchanska Hromada',
                    },
                    {
                        "uid": 721,
                        "name": 'Тетіївська',
                        "name_en": 'Tetiivska Hromada',
                    },
                    {
                        "uid": 722,
                        "name": 'Узинська',
                        "name_en": 'Uzynska Hromada',
                    },
                    {
                        "uid": 723,
                        "name": 'Фурсівська',
                        "name_en": 'Fursivska Hromada',
                    },
                ],
            },
            {
                "uid": 74,
                "name": 'Вишгородський',
                "name_en": 'Vyshhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 744,
                        "name": 'Вишгородська',
                        "name_en": 'Vyshhorodska Hromada',
                    },
                    {
                        "uid": 745,
                        "name": 'Димерська',
                        "name_en": 'Dymerska Hromada',
                    },
                    {
                        "uid": 747,
                        "name": 'Петрівська',
                        "name_en": 'Petrivska Hromada',
                    },
                    {
                        "uid": 749,
                        "name": 'Поліська',
                        "name_en": 'Poliska Hromada',
                    },
                    {
                        "uid": 748,
                        "name": 'Пірнівська',
                        "name_en": 'Pirnivska Hromada',
                    },
                    {
                        "uid": 750,
                        "name": 'м. Славутич та Славутицька',
                        "name_en": 'Slavutych and Slavutytska Hromada',
                    },
                    {
                        "uid": 746,
                        "name": 'Іванківська',
                        "name_en": 'Ivankivska Hromada',
                    },
                ],
            },
            {
                "uid": 76,
                "name": 'Обухівський',
                "name_en": 'Obukhivskyi Raion',
                "hromadas": [
                    {
                        "uid": 724,
                        "name": 'Богуславська',
                        "name_en": 'Bohuslavska Hromada',
                    },
                    {
                        "uid": 725,
                        "name": 'м. Васильків та Васильківська',
                        "name_en": 'Vasylkiv and Vasylkivska Hromada',
                    },
                    {
                        "uid": 726,
                        "name": 'Кагарлицька',
                        "name_en": 'Kaharlytska Hromada',
                    },
                    {
                        "uid": 727,
                        "name": 'Козинська',
                        "name_en": 'Kozynska Hromada',
                    },
                    {
                        "uid": 728,
                        "name": 'Миронівська',
                        "name_en": 'Myronivska Hromada',
                    },
                    {
                        "uid": 729,
                        "name": 'м. Обухів та Обухівська',
                        "name_en": 'Obukhiv and Obukhivska Hromada',
                    },
                    {
                        "uid": 730,
                        "name": 'м. Ржищів та Ржищівська',
                        "name_en": 'Rzhyshchiv and Rzhyshchivska Hromada',
                    },
                    {
                        "uid": 731,
                        "name": 'Українська',
                        "name_en": 'Ukrainska Hromada',
                    },
                    {
                        "uid": 732,
                        "name": 'Феодосіївська',
                        "name_en": 'Feodosiivska Hromada',
                    },
                ],
            },
            {
                "uid": 77,
                "name": 'Фастівський',
                "name_en": 'Fastivskyi Raion',
                "hromadas": [
                    {
                        "uid": 690,
                        "name": 'Бишівська',
                        "name_en": 'Byshivska Hromada',
                    },
                    {
                        "uid": 691,
                        "name": 'Боярська',
                        "name_en": 'Boiarska Hromada',
                    },
                    {
                        "uid": 692,
                        "name": 'Гатненська',
                        "name_en": 'Hatnenska Hromada',
                    },
                    {
                        "uid": 693,
                        "name": 'Глевахівська',
                        "name_en": 'Hlevakhivska Hromada',
                    },
                    {
                        "uid": 694,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 695,
                        "name": 'Кожанська',
                        "name_en": 'Kozhanska Hromada',
                    },
                    {
                        "uid": 696,
                        "name": 'Томашівська',
                        "name_en": 'Tomashivska Hromada',
                    },
                    {
                        "uid": 697,
                        "name": 'м. Фастів та Фастівська',
                        "name_en": 'Fastiv and Fastivska Hromada',
                    },
                    {
                        "uid": 698,
                        "name": 'Чабанівська',
                        "name_en": 'Chabanivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 15,
        "name": 'Кіровоградська область',
        "type": LocationType.OBLAST,
        "name_en": 'Kirovohradska Oblast',
        "districts": [
            {
                "uid": 82,
                "name": 'Голованівський',
                "name_en": 'Holovanivskyi Raion',
                "hromadas": [
                    {
                        "uid": 768,
                        "name": 'Благовіщенська',
                        "name_en": 'Blahovishchenska Hromada',
                    },
                    {
                        "uid": 769,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 770,
                        "name": 'Гайворонська',
                        "name_en": 'Haivoronska Hromada',
                    },
                    {
                        "uid": 771,
                        "name": 'Голованівська',
                        "name_en": 'Holovanivska Hromada',
                    },
                    {
                        "uid": 772,
                        "name": 'Заваллівська',
                        "name_en": 'Zavallivska Hromada',
                    },
                    {
                        "uid": 773,
                        "name": 'Надлацька',
                        "name_en": 'Nadlatska Hromada',
                    },
                    {
                        "uid": 774,
                        "name": 'Новоархангельська',
                        "name_en": 'Novoarkhanhelska Hromada',
                    },
                    {
                        "uid": 775,
                        "name": 'Перегонівська',
                        "name_en": 'Perehonivska Hromada',
                    },
                    {
                        "uid": 777,
                        "name": 'Побузька',
                        "name_en": 'Pobuzka Hromada',
                    },
                    {
                        "uid": 776,
                        "name": 'Підвисоцька',
                        "name_en": 'Pidvysotska Hromada',
                    },
                ],
            },
            {
                "uid": 81,
                "name": 'Кропивницький',
                "name_en": 'Kropyvnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 751,
                        "name": 'Аджамська',
                        "name_en": 'Adzhamska Hromada',
                    },
                    {
                        "uid": 752,
                        "name": 'Бобринецька',
                        "name_en": 'Bobrynetska Hromada',
                    },
                    {
                        "uid": 753,
                        "name": 'Великосеверинівська',
                        "name_en": 'Velykoseverynivska Hromada',
                    },
                    {
                        "uid": 754,
                        "name": 'Гурівська',
                        "name_en": 'Hurivska Hromada',
                    },
                    {
                        "uid": 755,
                        "name": 'Дмитрівська',
                        "name_en": 'Dmytrivska Hromada',
                    },
                    {
                        "uid": 756,
                        "name": 'Долинська',
                        "name_en": 'Dolynska Hromada',
                    },
                    {
                        "uid": 757,
                        "name": "м. Знам'янка та Знам’янська",
                        "name_en": 'Znamianka and Znamyanska Hromada',
                    },
                    {
                        "uid": 758,
                        "name": 'Катеринівська',
                        "name_en": 'Katerynivska Hromada',
                    },
                    {
                        "uid": 759,
                        "name": 'Кетрисанівська',
                        "name_en": 'Ketrysanivska Hromada',
                    },
                    {
                        "uid": 760,
                        "name": 'Компаніївська',
                        "name_en": 'Kompaniivska Hromada',
                    },
                    {
                        "uid": 761,
                        "name": 'м. Кропивницький та Кропивницька',
                        "name_en": 'Kropyvnytskyi and Kropyvnytska Hromada',
                    },
                    {
                        "uid": 762,
                        "name": 'Новгородківська',
                        "name_en": 'Novhorodkivska Hromada',
                    },
                    {
                        "uid": 763,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 764,
                        "name": 'Первозванівська',
                        "name_en": 'Pervozvanivska Hromada',
                    },
                    {
                        "uid": 765,
                        "name": 'Соколівська',
                        "name_en": 'Sokolivska Hromada',
                    },
                    {
                        "uid": 766,
                        "name": 'Суботцівська',
                        "name_en": 'Subottsivska Hromada',
                    },
                    {
                        "uid": 767,
                        "name": 'Устинівська',
                        "name_en": 'Ustynivska Hromada',
                    },
                ],
            },
            {
                "uid": 83,
                "name": 'Новоукраїнський',
                "name_en": 'Novoukrainskyi Raion',
                "hromadas": [
                    {
                        "uid": 787,
                        "name": 'Ганнівська',
                        "name_en": 'Hannivska Hromada',
                    },
                    {
                        "uid": 788,
                        "name": 'Глодоська',
                        "name_en": 'Hlodoska Hromada',
                    },
                    {
                        "uid": 789,
                        "name": 'Добровеличківська',
                        "name_en": 'Dobrovelychkivska Hromada',
                    },
                    {
                        "uid": 790,
                        "name": 'Злинська',
                        "name_en": 'Zlynska Hromada',
                    },
                    {
                        "uid": 791,
                        "name": 'Маловисківська',
                        "name_en": 'Malovyskivska Hromada',
                    },
                    {
                        "uid": 792,
                        "name": 'Мар’янівська',
                        "name_en": 'Maryanivska Hromada',
                    },
                    {
                        "uid": 793,
                        "name": 'Новомиргородська',
                        "name_en": 'Novomyrhorodska Hromada',
                    },
                    {
                        "uid": 794,
                        "name": 'Новоукраїнська',
                        "name_en": 'Novoukrainska Hromada',
                    },
                    {
                        "uid": 796,
                        "name": 'Помічнянська',
                        "name_en": 'Pomichnianska Hromada',
                    },
                    {
                        "uid": 795,
                        "name": 'Піщанобрідська',
                        "name_en": 'Pishchanobridska Hromada',
                    },
                    {
                        "uid": 797,
                        "name": 'Рівнянська',
                        "name_en": 'Rivnianska Hromada',
                    },
                    {
                        "uid": 798,
                        "name": 'Смолінська',
                        "name_en": 'Smolinska Hromada',
                    },
                    {
                        "uid": 799,
                        "name": 'Тишківська',
                        "name_en": 'Tyshkivska Hromada',
                    },
                ],
            },
            {
                "uid": 80,
                "name": 'Олександрійський',
                "name_en": 'Oleksandriiskyi Raion',
                "hromadas": [
                    {
                        "uid": 778,
                        "name": 'Великоандрусівська',
                        "name_en": 'Velykoandrusivska Hromada',
                    },
                    {
                        "uid": 779,
                        "name": 'Новопразька',
                        "name_en": 'Novoprazka Hromada',
                    },
                    {
                        "uid": 780,
                        "name": 'м. Олександрія та Олександрійська',
                        "name_en": 'Oleksandriia and Oleksandriiska Hromada',
                    },
                    {
                        "uid": 781,
                        "name": 'Онуфріївська',
                        "name_en": 'Onufriivska Hromada',
                    },
                    {
                        "uid": 782,
                        "name": 'Пантаївська',
                        "name_en": 'Pantaivska Hromada',
                    },
                    {
                        "uid": 783,
                        "name": 'Петрівська',
                        "name_en": 'Petrivska Hromada',
                    },
                    {
                        "uid": 784,
                        "name": 'Попельнастівська',
                        "name_en": 'Popelnastivska Hromada',
                    },
                    {
                        "uid": 785,
                        "name": 'Приютівська',
                        "name_en": 'Pryiutivska Hromada',
                    },
                    {
                        "uid": 786,
                        "name": 'м. Світловодськ та Світловодська',
                        "name_en": 'Svitlovodsk and Svitlovodska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 16,
        "name": 'Луганська область',
        "type": LocationType.OBLAST,
        "name_en": 'Luhanska Oblast',
        "districts": [
            {
                "uid": 1803,
                "name": 'Алчевський',
                "name_en": 'Alchevskyi Raion',
                "hromadas": [
                    {
                        "uid": 1903,
                        "name": 'м. Алчевськ та Алчевська',
                        "name_en": 'Alchevsk and Alchevska Hromada',
                    },
                    {
                        "uid": 1911,
                        "name": "м. Зимогір'я та Зимогір'ївська",
                        "name_en": 'Zymohiria and Zymohirivska Hromada',
                    },
                    {
                        "uid": 1909,
                        "name": 'м. Кадіївка та Кадіївська',
                        "name_en": 'Kadiivka and Kadiivska Hromada',
                    },
                ],
            },
            {
                "uid": 1804,
                "name": 'Довжанський',
                "name_en": 'Dovzhanskyi Raion',
                "hromadas": [
                    {
                        "uid": 1908,
                        "name": 'м. Довжанськ та Довжанська',
                        "name_en": 'Dovzhansk and Dovzhanska Hromada',
                    },
                    {
                        "uid": 1905,
                        "name": 'м. Сорокине та Сорокинська',
                        "name_en": 'Sorokyne and Sorokynska Hromada',
                    },
                ],
            },
            {
                "uid": 1801,
                "name": 'Луганський',
                "name_en": 'Luhanskyi Raion',
                "hromadas": [
                    {
                        "uid": 1901,
                        "name": 'м. Луганськ та Луганська',
                        "name_en": 'Luhansk and Luhanska Hromada',
                    },
                    {
                        "uid": 1910,
                        "name": 'м. Лутугине та Лутугинська',
                        "name_en": 'Lutuhyne and Lutuhynska Hromada',
                    },
                    {
                        "uid": 1904,
                        "name": 'м. Молодогвардійськ та Молодогвардійська',
                        "name_en": 'Molodohvardiisk and Molodohvardiiska Hromada',
                    },
                ],
            },
            {
                "uid": 1802,
                "name": 'Ровеньківський',
                "name_en": 'Rovenkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1902,
                        "name": 'м. Антрацит та Антрацитівська',
                        "name_en": 'Antratsyt and Antratsytivska Hromada',
                    },
                    {
                        "uid": 1907,
                        "name": 'м. Ровеньки та Ровеньківська',
                        "name_en": 'Rovenky and Rovenkivska Hromada',
                    },
                    {
                        "uid": 1906,
                        "name": 'м. Хрустальний та Хрустальненська',
                        "name_en": 'Khrustalnyi and Khrustalnenska Hromada',
                    },
                ],
            },
            {
                "uid": 85,
                "name": 'Сватівський',
                "name_en": 'Svativskyi Raion',
                "hromadas": [
                    {
                        "uid": 808,
                        "name": 'Білокуракинська',
                        "name_en": 'Bilokurakynska Hromada',
                    },
                    {
                        "uid": 809,
                        "name": 'Коломийчиська',
                        "name_en": 'Kolomyichyska Hromada',
                    },
                    {
                        "uid": 810,
                        "name": 'Красноріченська',
                        "name_en": 'Krasnorichenska Hromada',
                    },
                    {
                        "uid": 811,
                        "name": 'Лозно-Олександрівська',
                        "name_en": 'Lozno-Oleksandrivska Hromada',
                    },
                    {
                        "uid": 812,
                        "name": 'Нижньодуванська',
                        "name_en": 'Nyzhnoduvanska Hromada',
                    },
                    {
                        "uid": 813,
                        "name": 'Сватівська',
                        "name_en": 'Svativska Hromada',
                    },
                    {
                        "uid": 814,
                        "name": 'Троїцька',
                        "name_en": 'Troitska Hromada',
                    },
                ],
            },
            {
                "uid": 86,
                "name": 'Старобільський',
                "name_en": 'Starobilskyi Raion',
                "hromadas": [
                    {
                        "uid": 800,
                        "name": 'Біловодська',
                        "name_en": 'Bilovodska Hromada',
                    },
                    {
                        "uid": 801,
                        "name": 'Білолуцька',
                        "name_en": 'Bilolutska Hromada',
                    },
                    {
                        "uid": 802,
                        "name": 'Марківська',
                        "name_en": 'Markivska Hromada',
                    },
                    {
                        "uid": 803,
                        "name": 'Міловська',
                        "name_en": 'Milovska Hromada',
                    },
                    {
                        "uid": 804,
                        "name": 'Новопсковська',
                        "name_en": 'Novopskovska Hromada',
                    },
                    {
                        "uid": 805,
                        "name": 'Старобільська',
                        "name_en": 'Starobilska Hromada',
                    },
                    {
                        "uid": 806,
                        "name": 'Чмирівська',
                        "name_en": 'Chmyrivska Hromada',
                    },
                    {
                        "uid": 807,
                        "name": 'Шульгинська',
                        "name_en": 'Shulhynska Hromada',
                    },
                ],
            },
            {
                "uid": 84,
                "name": 'Сіверськодонецький',
                "name_en": 'Siverskodonetskyi Raion',
                "hromadas": [
                    {
                        "uid": 815,
                        "name": 'Гірська',
                        "name_en": 'Hirska Hromada',
                    },
                    {
                        "uid": 816,
                        "name": 'м. Кремінна та Кремінська',
                        "name_en": 'Kreminna and Kreminska Hromada',
                    },
                    {
                        "uid": 817,
                        "name": 'м. Лисичанськ та Лисичанська',
                        "name_en": 'Lysychansk and Lysychanska Hromada',
                    },
                    {
                        "uid": 818,
                        "name": 'Попаснянська',
                        "name_en": 'Popasnianska Hromada',
                    },
                    {
                        "uid": 819,
                        "name": 'м. Рубіжне та Рубіжанська',
                        "name_en": 'Rubizhne and Rubizhanska Hromada',
                    },
                    {
                        "uid": 820,
                        "name": 'м. Сіверськодонецьк та Сіверськодонецька',
                        "name_en": 'Siverskodonetsk and Siverskodonetska Hromada',
                    },
                ],
            },
            {
                "uid": 87,
                "name": 'Щастинський',
                "name_en": 'Shchastynskyi Raion',
                "hromadas": [
                    {
                        "uid": 821,
                        "name": 'Нижньотеплівська',
                        "name_en": 'Nyzhnoteplivska Hromada',
                    },
                    {
                        "uid": 822,
                        "name": 'Новоайдарська',
                        "name_en": 'Novoaidarska Hromada',
                    },
                    {
                        "uid": 823,
                        "name": 'Станично-Луганська',
                        "name_en": 'Stanychno-Luhanska Hromada',
                    },
                    {
                        "uid": 824,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska Hromada',
                    },
                    {
                        "uid": 825,
                        "name": 'Щастинська',
                        "name_en": 'Shchastynska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 27,
        "name": 'Львівська область',
        "type": LocationType.OBLAST,
        "name_en": 'Lvivska Oblast',
        "districts": [
            {
                "uid": 91,
                "name": 'Дрогобицький',
                "name_en": 'Drohobytskyi Raion',
                "hromadas": [
                    {
                        "uid": 867,
                        "name": 'м. Борислав та Бориславська',
                        "name_en": 'Boryslav and Boryslavska Hromada',
                    },
                    {
                        "uid": 868,
                        "name": 'м. Дрогобич та Дрогобицька',
                        "name_en": 'Drohobych and Drohobytska Hromada',
                    },
                    {
                        "uid": 869,
                        "name": 'Меденицька',
                        "name_en": 'Medenytska Hromada',
                    },
                    {
                        "uid": 870,
                        "name": 'Східницька',
                        "name_en": 'Skhidnytska Hromada',
                    },
                    {
                        "uid": 871,
                        "name": 'м. Трускавець та Трускавецька',
                        "name_en": 'Truskavets and Truskavetska Hromada',
                    },
                ],
            },
            {
                "uid": 94,
                "name": 'Золочівський',
                "name_en": 'Zolochivskyi Raion',
                "hromadas": [
                    {
                        "uid": 872,
                        "name": 'Бродівська',
                        "name_en": 'Brodivska Hromada',
                    },
                    {
                        "uid": 873,
                        "name": 'Буська',
                        "name_en": 'Buska Hromada',
                    },
                    {
                        "uid": 874,
                        "name": 'Заболотцівська',
                        "name_en": 'Zabolottsivska Hromada',
                    },
                    {
                        "uid": 875,
                        "name": 'Золочівська',
                        "name_en": 'Zolochivska Hromada',
                    },
                    {
                        "uid": 876,
                        "name": 'Красненська',
                        "name_en": 'Krasnenska Hromada',
                    },
                    {
                        "uid": 878,
                        "name": 'Поморянська',
                        "name_en": 'Pomorianska Hromada',
                    },
                    {
                        "uid": 877,
                        "name": 'Підкамінська',
                        "name_en": 'Pidkaminska Hromada',
                    },
                ],
            },
            {
                "uid": 90,
                "name": 'Львівський',
                "name_en": 'Lvivskyi Raion',
                "hromadas": [
                    {
                        "uid": 833,
                        "name": 'Бібрська',
                        "name_en": 'Bibrska Hromada',
                    },
                    {
                        "uid": 834,
                        "name": 'Великолюбінська',
                        "name_en": 'Velykoliubinska Hromada',
                    },
                    {
                        "uid": 835,
                        "name": 'Глинянська',
                        "name_en": 'Hlynianska Hromada',
                    },
                    {
                        "uid": 836,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 837,
                        "name": 'Давидівська',
                        "name_en": 'Davydivska Hromada',
                    },
                    {
                        "uid": 838,
                        "name": 'Добросинсько-Магерівська',
                        "name_en": 'Dobrosynsko-Maherivska Hromada',
                    },
                    {
                        "uid": 839,
                        "name": 'Жовківська',
                        "name_en": 'Zhovkivska Hromada',
                    },
                    {
                        "uid": 840,
                        "name": 'Жовтанецька',
                        "name_en": 'Zhovtanetska Hromada',
                    },
                    {
                        "uid": 841,
                        "name": 'Зимноводівська',
                        "name_en": 'Zymnovodivska Hromada',
                    },
                    {
                        "uid": 842,
                        "name": 'Кам’янка-Бузька',
                        "name_en": 'Kamyanka-Buzka Hromada',
                    },
                    {
                        "uid": 843,
                        "name": 'Комарнівська',
                        "name_en": 'Komarnivska Hromada',
                    },
                    {
                        "uid": 844,
                        "name": 'Куликівська',
                        "name_en": 'Kulykivska Hromada',
                    },
                    {
                        "uid": 845,
                        "name": 'м. Львів та Львівська',
                        "name_en": 'Lviv and Lvivska Hromada',
                    },
                    {
                        "uid": 846,
                        "name": 'Мурованська',
                        "name_en": 'Murovanska Hromada',
                    },
                    {
                        "uid": 847,
                        "name": 'Новояричівська',
                        "name_en": 'Novoiarychivska Hromada',
                    },
                    {
                        "uid": 848,
                        "name": 'Оброшинська',
                        "name_en": 'Obroshynska Hromada',
                    },
                    {
                        "uid": 849,
                        "name": 'Перемишлянська',
                        "name_en": 'Peremyshlianska Hromada',
                    },
                    {
                        "uid": 851,
                        "name": 'Пустомитівська',
                        "name_en": 'Pustomytivska Hromada',
                    },
                    {
                        "uid": 850,
                        "name": 'Підберізцівська',
                        "name_en": 'Pidberiztsivska Hromada',
                    },
                    {
                        "uid": 852,
                        "name": 'Рава-Руська',
                        "name_en": 'Rava-Ruska Hromada',
                    },
                    {
                        "uid": 853,
                        "name": 'Сокільницька',
                        "name_en": 'Sokilnytska Hromada',
                    },
                    {
                        "uid": 854,
                        "name": 'Солонківська',
                        "name_en": 'Solonkivska Hromada',
                    },
                    {
                        "uid": 855,
                        "name": 'Щирецька',
                        "name_en": 'Shchyretska Hromada',
                    },
                ],
            },
            {
                "uid": 88,
                "name": 'Самбірський',
                "name_en": 'Sambirskyi Raion',
                "hromadas": [
                    {
                        "uid": 857,
                        "name": 'Боринська',
                        "name_en": 'Borynska Hromada',
                    },
                    {
                        "uid": 856,
                        "name": 'Бісковицька',
                        "name_en": 'Biskovytska Hromada',
                    },
                    {
                        "uid": 858,
                        "name": 'Добромильська',
                        "name_en": 'Dobromylska Hromada',
                    },
                    {
                        "uid": 859,
                        "name": 'Новокалинівська',
                        "name_en": 'Novokalynivska Hromada',
                    },
                    {
                        "uid": 860,
                        "name": 'Ралівська',
                        "name_en": 'Ralivska Hromada',
                    },
                    {
                        "uid": 861,
                        "name": 'Рудківська',
                        "name_en": 'Rudkivska Hromada',
                    },
                    {
                        "uid": 862,
                        "name": 'м. Самбір та Самбірська',
                        "name_en": 'Sambir and Sambirska Hromada',
                    },
                    {
                        "uid": 863,
                        "name": 'Старосамбірська',
                        "name_en": 'Starosambirska Hromada',
                    },
                    {
                        "uid": 864,
                        "name": 'Стрілківська',
                        "name_en": 'Strilkivska Hromada',
                    },
                    {
                        "uid": 865,
                        "name": 'Турківська',
                        "name_en": 'Turkivska Hromada',
                    },
                    {
                        "uid": 866,
                        "name": 'Хирівська',
                        "name_en": 'Khyrivska Hromada',
                    },
                ],
            },
            {
                "uid": 89,
                "name": 'Стрийський',
                "name_en": 'Stryiskyi Raion',
                "hromadas": [
                    {
                        "uid": 879,
                        "name": 'Гніздичівська',
                        "name_en": 'Hnizdychivska Hromada',
                    },
                    {
                        "uid": 880,
                        "name": 'Грабовецько-Дулібівська',
                        "name_en": 'Hrabovetsko-Dulibivska Hromada',
                    },
                    {
                        "uid": 881,
                        "name": 'Жидачівська',
                        "name_en": 'Zhydachivska Hromada',
                    },
                    {
                        "uid": 882,
                        "name": 'Журавненська',
                        "name_en": 'Zhuravnenska Hromada',
                    },
                    {
                        "uid": 883,
                        "name": 'Козівська',
                        "name_en": 'Kozivska Hromada',
                    },
                    {
                        "uid": 884,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 885,
                        "name": 'м. Моршин та Моршинська',
                        "name_en": 'Morshyn and Morshynska Hromada',
                    },
                    {
                        "uid": 886,
                        "name": 'м. Новий Розділ та Новороздільська',
                        "name_en": 'Novyi Rozdil and Novorozdilska Hromada',
                    },
                    {
                        "uid": 887,
                        "name": 'Розвадівська',
                        "name_en": 'Rozvadivska Hromada',
                    },
                    {
                        "uid": 888,
                        "name": 'Сколівська',
                        "name_en": 'Skolivska Hromada',
                    },
                    {
                        "uid": 889,
                        "name": 'Славська',
                        "name_en": 'Slavska Hromada',
                    },
                    {
                        "uid": 890,
                        "name": 'м. Стрий та Стрийська',
                        "name_en": 'Stryi and Stryiska Hromada',
                    },
                    {
                        "uid": 891,
                        "name": 'Тростянецька',
                        "name_en": 'Trostianetska Hromada',
                    },
                    {
                        "uid": 892,
                        "name": 'Ходорівська',
                        "name_en": 'Khodorivska Hromada',
                    },
                ],
            },
            {
                "uid": 92,
                "name": 'Шептицький',
                "name_en": 'Sheptytskyi Raion',
                "hromadas": [
                    {
                        "uid": 826,
                        "name": 'Белзька',
                        "name_en": 'Belzka Hromada',
                    },
                    {
                        "uid": 827,
                        "name": 'Великомостівська',
                        "name_en": 'Velykomostivska Hromada',
                    },
                    {
                        "uid": 828,
                        "name": 'Добротвірська',
                        "name_en": 'Dobrotvirska Hromada',
                    },
                    {
                        "uid": 829,
                        "name": 'Лопатинська',
                        "name_en": 'Lopatynska Hromada',
                    },
                    {
                        "uid": 830,
                        "name": 'Радехівська',
                        "name_en": 'Radekhivska Hromada',
                    },
                    {
                        "uid": 831,
                        "name": 'Сокальська',
                        "name_en": 'Sokalska Hromada',
                    },
                    {
                        "uid": 832,
                        "name": 'м. Шептицький та Шептицька',
                        "name_en": 'Sheptytskyi and Sheptytska Hromada',
                    },
                ],
            },
            {
                "uid": 93,
                "name": 'Яворівський',
                "name_en": 'Yavorivskyi Raion',
                "hromadas": [
                    {
                        "uid": 894,
                        "name": 'Мостиська',
                        "name_en": 'Mostyska Hromada',
                    },
                    {
                        "uid": 895,
                        "name": 'Новояворівськ',
                        "name_en": 'Novoiavorivsk Hromada',
                    },
                    {
                        "uid": 896,
                        "name": 'Судововишнянська',
                        "name_en": 'Sudovovyshnianska Hromada',
                    },
                    {
                        "uid": 897,
                        "name": 'Шегинівська',
                        "name_en": 'Shehynivska Hromada',
                    },
                    {
                        "uid": 898,
                        "name": 'Яворівська',
                        "name_en": 'Yavorivska Hromada',
                    },
                    {
                        "uid": 893,
                        "name": 'Івано-Франківська',
                        "name_en": 'Ivano-Frankivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 17,
        "name": 'Миколаївська область',
        "type": LocationType.OBLAST,
        "name_en": 'Mykolaivska Oblast',
        "districts": [
            {
                "uid": 96,
                "name": 'Баштанський',
                "name_en": 'Bashtanskyi Raion',
                "hromadas": [
                    {
                        "uid": 907,
                        "name": 'м. Баштанка та Баштанська',
                        "name_en": 'Bashtanka and Bashtanska Hromada',
                    },
                    {
                        "uid": 908,
                        "name": 'Березнегуватська',
                        "name_en": 'Bereznehuvatska Hromada',
                    },
                    {
                        "uid": 910,
                        "name": 'Володимирівська',
                        "name_en": 'Volodymyrivska Hromada',
                    },
                    {
                        "uid": 909,
                        "name": 'Вільнозапорізька',
                        "name_en": 'Vilnozaporizka Hromada',
                    },
                    {
                        "uid": 911,
                        "name": 'Горохівська',
                        "name_en": 'Horokhivska Hromada',
                    },
                    {
                        "uid": 913,
                        "name": 'Казанківська',
                        "name_en": 'Kazankivska Hromada',
                    },
                    {
                        "uid": 914,
                        "name": 'Новобузька',
                        "name_en": 'Novobuzka Hromada',
                    },
                    {
                        "uid": 915,
                        "name": 'Привільненська',
                        "name_en": 'Pryvilnenska Hromada',
                    },
                    {
                        "uid": 916,
                        "name": 'м. Снігурівка та Снігурівська',
                        "name_en": 'Snihurivka and Snihurivska Hromada',
                    },
                    {
                        "uid": 917,
                        "name": 'Софіївська',
                        "name_en": 'Sofiivska Hromada',
                    },
                    {
                        "uid": 918,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska Hromada',
                    },
                    {
                        "uid": 912,
                        "name": 'Інгульська',
                        "name_en": 'Inhulska Hromada',
                    },
                ],
            },
            {
                "uid": 95,
                "name": 'Вознесенський',
                "name_en": 'Voznesenskyi Raion',
                "hromadas": [
                    {
                        "uid": 938,
                        "name": 'Братська',
                        "name_en": 'Bratska Hromada',
                    },
                    {
                        "uid": 939,
                        "name": 'Бузька',
                        "name_en": 'Buzka Hromada',
                    },
                    {
                        "uid": 940,
                        "name": 'Веселинівська',
                        "name_en": 'Veselynivska Hromada',
                    },
                    {
                        "uid": 941,
                        "name": 'м. Вознесенськ та Вознесенська',
                        "name_en": 'Voznesensk and Voznesenska Hromada',
                    },
                    {
                        "uid": 942,
                        "name": 'Доманівська',
                        "name_en": 'Domanivska Hromada',
                    },
                    {
                        "uid": 943,
                        "name": 'Дорошівська',
                        "name_en": 'Doroshivska Hromada',
                    },
                    {
                        "uid": 945,
                        "name": 'Мостівська',
                        "name_en": 'Mostivska Hromada',
                    },
                    {
                        "uid": 946,
                        "name": "Новомар'ївська",
                        "name_en": 'Novomarivska Hromada',
                    },
                    {
                        "uid": 947,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 948,
                        "name": 'Прибужанівська',
                        "name_en": 'Prybuzhanivska Hromada',
                    },
                    {
                        "uid": 949,
                        "name": 'Прибузька',
                        "name_en": 'Prybuzka Hromada',
                    },
                    {
                        "uid": 950,
                        "name": 'м. Южноукраїнськ та Южноукраїнська',
                        "name_en": 'Yuzhnoukrainsk and Yuzhnoukrainska Hromada',
                    },
                    {
                        "uid": 944,
                        "name": 'Єланецька',
                        "name_en": 'Yelanetska Hromada',
                    },
                ],
            },
            {
                "uid": 98,
                "name": 'Миколаївський',
                "name_en": 'Mykolaivskyi Raion',
                "hromadas": [
                    {
                        "uid": 919,
                        "name": 'Березанська',
                        "name_en": 'Berezanska Hromada',
                    },
                    {
                        "uid": 920,
                        "name": 'Веснянська',
                        "name_en": 'Vesnianska Hromada',
                    },
                    {
                        "uid": 921,
                        "name": 'Воскресенська',
                        "name_en": 'Voskresenska Hromada',
                    },
                    {
                        "uid": 922,
                        "name": 'Галицинівська',
                        "name_en": 'Halytsynivska Hromada',
                    },
                    {
                        "uid": 923,
                        "name": 'Коблівська',
                        "name_en": 'Koblivska Hromada',
                    },
                    {
                        "uid": 924,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 925,
                        "name": 'Куцурубська',
                        "name_en": 'Kutsurubska Hromada',
                    },
                    {
                        "uid": 926,
                        "name": 'м. Миколаїв та Миколаївська',
                        "name_en": 'Mykolaiv and Mykolaivska Hromada',
                    },
                    {
                        "uid": 927,
                        "name": 'Мішково-Погорілівська',
                        "name_en": 'Mishkovo-Pohorilivska Hromada',
                    },
                    {
                        "uid": 928,
                        "name": 'Нечаянська',
                        "name_en": 'Nechaianska Hromada',
                    },
                    {
                        "uid": 929,
                        "name": 'м. Нова-Одеса та Новоодеська',
                        "name_en": 'Nova-Odesa and Novoodeska Hromada',
                    },
                    {
                        "uid": 930,
                        "name": 'Ольшанська',
                        "name_en": 'Olshanska Hromada',
                    },
                    {
                        "uid": 931,
                        "name": 'м. Очаків та Очаківська',
                        "name_en": 'Ochakiv and Ochakivska Hromada',
                    },
                    {
                        "uid": 932,
                        "name": 'Первомайська',
                        "name_en": 'Pervomaiska Hromada',
                    },
                    {
                        "uid": 933,
                        "name": 'Радсадівська',
                        "name_en": 'Radsadivska Hromada',
                    },
                    {
                        "uid": 934,
                        "name": 'Степівська',
                        "name_en": 'Stepivska Hromada',
                    },
                    {
                        "uid": 935,
                        "name": 'Сухоєланецька',
                        "name_en": 'Sukhoielanetska Hromada',
                    },
                    {
                        "uid": 936,
                        "name": 'Чорноморська',
                        "name_en": 'Chornomorska Hromada',
                    },
                    {
                        "uid": 937,
                        "name": 'Шевченківська',
                        "name_en": 'Shevchenkivska Hromada',
                    },
                ],
            },
            {
                "uid": 97,
                "name": 'Первомайський',
                "name_en": 'Pervomaiskyi Raion',
                "hromadas": [
                    {
                        "uid": 899,
                        "name": 'Арбузинська',
                        "name_en": 'Arbuzynska Hromada',
                    },
                    {
                        "uid": 900,
                        "name": 'Благодатненська',
                        "name_en": 'Blahodatnenska Hromada',
                    },
                    {
                        "uid": 901,
                        "name": 'Врадіївська',
                        "name_en": 'Vradiivska Hromada',
                    },
                    {
                        "uid": 902,
                        "name": "Кам'яномостівська",
                        "name_en": 'Kamianomostivska Hromada',
                    },
                    {
                        "uid": 903,
                        "name": 'Кривоозерська',
                        "name_en": 'Kryvoozerska Hromada',
                    },
                    {
                        "uid": 904,
                        "name": 'Мигіївська',
                        "name_en": 'Myhiivska Hromada',
                    },
                    {
                        "uid": 905,
                        "name": 'м. Первомайськ та Первомайська',
                        "name_en": 'Pervomaisk and Pervomaiska Hromada',
                    },
                    {
                        "uid": 906,
                        "name": 'Синюхинобрідська',
                        "name_en": 'Syniukhynobridska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 18,
        "name": 'Одеська область',
        "type": LocationType.OBLAST,
        "name_en": 'Odeska Oblast',
        "districts": [
            {
                "uid": 100,
                "name": 'Березівський',
                "name_en": 'Berezivskyi Raion',
                "hromadas": [
                    {
                        "uid": 985,
                        "name": 'Андрієво-Іванівська',
                        "name_en": 'Andriievo-Ivanivska Hromada',
                    },
                    {
                        "uid": 986,
                        "name": 'Березівська',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 987,
                        "name": 'Великобуялицька',
                        "name_en": 'Velykobuialytska Hromada',
                    },
                    {
                        "uid": 988,
                        "name": 'Знам’янська',
                        "name_en": 'Znamyanska Hromada',
                    },
                    {
                        "uid": 990,
                        "name": 'Коноплянська',
                        "name_en": 'Konoplianska Hromada',
                    },
                    {
                        "uid": 991,
                        "name": 'Курісовська',
                        "name_en": 'Kurisovska Hromada',
                    },
                    {
                        "uid": 992,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 993,
                        "name": 'Новокальчевська',
                        "name_en": 'Novokalchevska Hromada',
                    },
                    {
                        "uid": 994,
                        "name": 'Петровірівська',
                        "name_en": 'Petrovirivska Hromada',
                    },
                    {
                        "uid": 995,
                        "name": 'Раухівська',
                        "name_en": 'Raukhivska Hromada',
                    },
                    {
                        "uid": 996,
                        "name": 'Розквітівська',
                        "name_en": 'Rozkvitivska Hromada',
                    },
                    {
                        "uid": 997,
                        "name": 'Старомаяківська',
                        "name_en": 'Staromaiakivska Hromada',
                    },
                    {
                        "uid": 998,
                        "name": 'Стрюківська',
                        "name_en": 'Striukivska Hromada',
                    },
                    {
                        "uid": 999,
                        "name": 'Чогодарівська',
                        "name_en": 'Chohodarivska Hromada',
                    },
                    {
                        "uid": 1000,
                        "name": 'Ширяївська',
                        "name_en": 'Shyriaivska Hromada',
                    },
                    {
                        "uid": 989,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
            {
                "uid": 105,
                "name": 'Болградський',
                "name_en": 'Bolhradskyi Raion',
                "hromadas": [
                    {
                        "uid": 1001,
                        "name": 'Арцизька',
                        "name_en": 'Artsyzka Hromada',
                    },
                    {
                        "uid": 1002,
                        "name": 'Болградська',
                        "name_en": 'Bolhradska Hromada',
                    },
                    {
                        "uid": 1003,
                        "name": 'Бородінська',
                        "name_en": 'Borodinska Hromada',
                    },
                    {
                        "uid": 1004,
                        "name": 'Василівська',
                        "name_en": 'Vasylivska Hromada',
                    },
                    {
                        "uid": 1005,
                        "name": 'Городненська',
                        "name_en": 'Horodnenska Hromada',
                    },
                    {
                        "uid": 1006,
                        "name": 'Криниченська',
                        "name_en": 'Krynychenska Hromada',
                    },
                    {
                        "uid": 1007,
                        "name": 'Кубейська',
                        "name_en": 'Kubeiska Hromada',
                    },
                    {
                        "uid": 1008,
                        "name": 'Павлівська',
                        "name_en": 'Pavlivska Hromada',
                    },
                    {
                        "uid": 1009,
                        "name": 'Тарутинська',
                        "name_en": 'Tarutynska Hromada',
                    },
                    {
                        "uid": 1010,
                        "name": 'Теплицька',
                        "name_en": 'Teplytska Hromada',
                    },
                ],
            },
            {
                "uid": 102,
                "name": 'Білгород-Дністровський',
                "name_en": 'Bilhorod-Dnistrovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1011,
                        "name": 'м. Білгород-Дністровський та Білгород-Дністровська',
                        "name_en": 'Bilhorod-Dnistrovskyi and Bilhorod-Dnistrovska Hromada',
                    },
                    {
                        "uid": 1012,
                        "name": 'Дивізійська',
                        "name_en": 'Dyviziiska Hromada',
                    },
                    {
                        "uid": 1013,
                        "name": 'Кароліно-Бугазька',
                        "name_en": 'Karolino-Buhazka Hromada',
                    },
                    {
                        "uid": 1014,
                        "name": 'Кулевчанська',
                        "name_en": 'Kulevchanska Hromada',
                    },
                    {
                        "uid": 1015,
                        "name": 'Лиманська',
                        "name_en": 'Lymanska Hromada',
                    },
                    {
                        "uid": 1016,
                        "name": 'Маразліївська',
                        "name_en": 'Marazliivska Hromada',
                    },
                    {
                        "uid": 1017,
                        "name": 'Мологівська',
                        "name_en": 'Molohivska Hromada',
                    },
                    {
                        "uid": 1018,
                        "name": 'Петропавлівська',
                        "name_en": 'Petropavlivska Hromada',
                    },
                    {
                        "uid": 1019,
                        "name": 'Плахтіївська',
                        "name_en": 'Plakhtiivska Hromada',
                    },
                    {
                        "uid": 1020,
                        "name": 'Саратська',
                        "name_en": 'Saratska Hromada',
                    },
                    {
                        "uid": 1021,
                        "name": 'Сергіївська',
                        "name_en": 'Serhiivska Hromada',
                    },
                    {
                        "uid": 1022,
                        "name": 'Старокозацька',
                        "name_en": 'Starokozatska Hromada',
                    },
                    {
                        "uid": 1023,
                        "name": 'Татарбунарська',
                        "name_en": 'Tatarbunarska Hromada',
                    },
                    {
                        "uid": 1024,
                        "name": 'Тузлівська',
                        "name_en": 'Tuzlivska Hromada',
                    },
                    {
                        "uid": 1025,
                        "name": 'Успенівська',
                        "name_en": 'Uspenivska Hromada',
                    },
                    {
                        "uid": 1026,
                        "name": 'Шабівська',
                        "name_en": 'Shabivska Hromada',
                    },
                ],
            },
            {
                "uid": 104,
                "name": 'Одеський',
                "name_en": 'Odeskyi Raion',
                "hromadas": [
                    {
                        "uid": 951,
                        "name": 'Авангардівська',
                        "name_en": 'Avanhardivska Hromada',
                    },
                    {
                        "uid": 952,
                        "name": 'Біляївська',
                        "name_en": 'Biliaivska Hromada',
                    },
                    {
                        "uid": 953,
                        "name": 'Великодальницька',
                        "name_en": 'Velykodalnytska Hromada',
                    },
                    {
                        "uid": 954,
                        "name": 'Великодолинська',
                        "name_en": 'Velykodolynska Hromada',
                    },
                    {
                        "uid": 955,
                        "name": 'Вигодянська',
                        "name_en": 'Vyhodianska Hromada',
                    },
                    {
                        "uid": 956,
                        "name": 'Визирська',
                        "name_en": 'Vyzyrska Hromada',
                    },
                    {
                        "uid": 957,
                        "name": 'Дальницька',
                        "name_en": 'Dalnytska Hromada',
                    },
                    {
                        "uid": 958,
                        "name": 'Дачненська',
                        "name_en": 'Dachnenska Hromada',
                    },
                    {
                        "uid": 959,
                        "name": 'Доброславська',
                        "name_en": 'Dobroslavska Hromada',
                    },
                    {
                        "uid": 960,
                        "name": 'Красносільська',
                        "name_en": 'Krasnosilska Hromada',
                    },
                    {
                        "uid": 961,
                        "name": 'Маяківська',
                        "name_en": 'Maiakivska Hromada',
                    },
                    {
                        "uid": 962,
                        "name": 'Нерубайська',
                        "name_en": 'Nerubaiska Hromada',
                    },
                    {
                        "uid": 963,
                        "name": 'Овідіопольська',
                        "name_en": 'Ovidiopolska Hromada',
                    },
                    {
                        "uid": 964,
                        "name": 'м. Одеса та Одеська',
                        "name_en": 'Odesa and Odeska Hromada',
                    },
                    {
                        "uid": 971,
                        "name": 'м. Південне та Південна',
                        "name_en": 'Pivdenne and Pivdenna Hromada',
                    },
                    {
                        "uid": 965,
                        "name": 'Таїровська',
                        "name_en": 'Tairovska Hromada',
                    },
                    {
                        "uid": 966,
                        "name": 'Теплодарська',
                        "name_en": 'Teplodarska Hromada',
                    },
                    {
                        "uid": 967,
                        "name": 'Усатівська',
                        "name_en": 'Usativska Hromada',
                    },
                    {
                        "uid": 968,
                        "name": 'Фонтанська',
                        "name_en": 'Fontanska Hromada',
                    },
                    {
                        "uid": 969,
                        "name": 'м. Чорноморськ та Чорноморська',
                        "name_en": 'Chornomorsk and Chornomorska Hromada',
                    },
                    {
                        "uid": 970,
                        "name": 'Чорноморська',
                        "name_en": 'Chornomorska Hromada',
                    },
                    {
                        "uid": 972,
                        "name": 'Яськівська',
                        "name_en": 'Yaskivska Hromada',
                    },
                ],
            },
            {
                "uid": 99,
                "name": 'Подільський',
                "name_en": 'Podilskyi Raion',
                "hromadas": [
                    {
                        "uid": 973,
                        "name": 'Ананьївська',
                        "name_en": 'Ananivska Hromada',
                    },
                    {
                        "uid": 974,
                        "name": 'Балтська',
                        "name_en": 'Baltska Hromada',
                    },
                    {
                        "uid": 975,
                        "name": 'Долинська',
                        "name_en": 'Dolynska Hromada',
                    },
                    {
                        "uid": 976,
                        "name": 'Зеленогірська',
                        "name_en": 'Zelenohirska Hromada',
                    },
                    {
                        "uid": 977,
                        "name": 'Кодимська',
                        "name_en": 'Kodymska Hromada',
                    },
                    {
                        "uid": 978,
                        "name": 'Куяльницька',
                        "name_en": 'Kuialnytska Hromada',
                    },
                    {
                        "uid": 979,
                        "name": 'Любашівська',
                        "name_en": 'Liubashivska Hromada',
                    },
                    {
                        "uid": 980,
                        "name": 'Окнянська',
                        "name_en": 'Oknianska Hromada',
                    },
                    {
                        "uid": 982,
                        "name": 'Подільська',
                        "name_en": 'Podilska Hromada',
                    },
                    {
                        "uid": 981,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 983,
                        "name": 'Савранська',
                        "name_en": 'Savranska Hromada',
                    },
                    {
                        "uid": 984,
                        "name": 'Слобідська',
                        "name_en": 'Slobidska Hromada',
                    },
                ],
            },
            {
                "uid": 103,
                "name": 'Роздільнянський',
                "name_en": 'Rozdilnianskyi Raion',
                "hromadas": [
                    {
                        "uid": 1027,
                        "name": 'Великомихайлівська',
                        "name_en": 'Velykomykhailivska Hromada',
                    },
                    {
                        "uid": 1028,
                        "name": 'Великоплосківська',
                        "name_en": 'Velykoploskivska Hromada',
                    },
                    {
                        "uid": 1029,
                        "name": 'Затишанська',
                        "name_en": 'Zatyshanska Hromada',
                    },
                    {
                        "uid": 1030,
                        "name": 'Захарівська',
                        "name_en": 'Zakharivska Hromada',
                    },
                    {
                        "uid": 1031,
                        "name": 'Лиманська',
                        "name_en": 'Lymanska Hromada',
                    },
                    {
                        "uid": 1032,
                        "name": 'Новоборисівська',
                        "name_en": 'Novoborysivska Hromada',
                    },
                    {
                        "uid": 1033,
                        "name": 'Роздільнянська',
                        "name_en": 'Rozdilnianska Hromada',
                    },
                    {
                        "uid": 1034,
                        "name": 'Степанівська',
                        "name_en": 'Stepanivska Hromada',
                    },
                    {
                        "uid": 1035,
                        "name": 'Цебриківська',
                        "name_en": 'Tsebrykivska Hromada',
                    },
                ],
            },
            {
                "uid": 101,
                "name": 'Ізмаїльський',
                "name_en": 'Izmailskyi Raion',
                "hromadas": [
                    {
                        "uid": 1036,
                        "name": 'Вилківська',
                        "name_en": 'Vylkivska Hromada',
                    },
                    {
                        "uid": 1038,
                        "name": 'Кілійська',
                        "name_en": 'Kiliiska Hromada',
                    },
                    {
                        "uid": 1039,
                        "name": 'Ренійська',
                        "name_en": 'Reniiska Hromada',
                    },
                    {
                        "uid": 1040,
                        "name": "Саф'янівська",
                        "name_en": 'Safianivska Hromada',
                    },
                    {
                        "uid": 1041,
                        "name": 'Суворовська',
                        "name_en": 'Suvorovska Hromada',
                    },
                    {
                        "uid": 1037,
                        "name": 'м. Ізмаїл та Ізмаїльська',
                        "name_en": 'Izmail and Izmailska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 19,
        "name": 'Полтавська область',
        "type": LocationType.OBLAST,
        "name_en": 'Poltavska Oblast',
        "districts": [
            {
                "uid": 107,
                "name": 'Кременчуцький',
                "name_en": 'Kremenchutskyi Raion',
                "hromadas": [
                    {
                        "uid": 1083,
                        "name": 'Глобинська',
                        "name_en": 'Hlobynska Hromada',
                    },
                    {
                        "uid": 1084,
                        "name": 'м. Горішні плавні та Горішньоплавнівська',
                        "name_en": 'Horishni plavni and Horishnoplavnivska Hromada',
                    },
                    {
                        "uid": 1085,
                        "name": 'Градизька',
                        "name_en": 'Hradyzka Hromada',
                    },
                    {
                        "uid": 1086,
                        "name": "Кам'янопотоківська",
                        "name_en": 'Kamianopotokivska Hromada',
                    },
                    {
                        "uid": 1087,
                        "name": 'Козельщинська',
                        "name_en": 'Kozelshchynska Hromada',
                    },
                    {
                        "uid": 1088,
                        "name": 'м. Кременчук та Кременчуцька',
                        "name_en": 'Kremenchuk and Kremenchutska Hromada',
                    },
                    {
                        "uid": 1089,
                        "name": 'Новогалещинська',
                        "name_en": 'Novohaleshchynska Hromada',
                    },
                    {
                        "uid": 1090,
                        "name": 'Оболонська',
                        "name_en": 'Obolonska Hromada',
                    },
                    {
                        "uid": 1091,
                        "name": 'Омельницька',
                        "name_en": 'Omelnytska Hromada',
                    },
                    {
                        "uid": 1093,
                        "name": 'Пришибська',
                        "name_en": 'Pryshybska Hromada',
                    },
                    {
                        "uid": 1092,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 1094,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska Hromada',
                    },
                ],
            },
            {
                "uid": 106,
                "name": 'Лубенський',
                "name_en": 'Lubenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1095,
                        "name": 'Гребінківська',
                        "name_en": 'Hrebinkivska Hromada',
                    },
                    {
                        "uid": 1096,
                        "name": 'м. Лубни та Лубенська',
                        "name_en": 'Lubny and Lubenska Hromada',
                    },
                    {
                        "uid": 1097,
                        "name": 'Новооржицька',
                        "name_en": 'Novoorzhytska Hromada',
                    },
                    {
                        "uid": 1098,
                        "name": 'Оржицька',
                        "name_en": 'Orzhytska Hromada',
                    },
                    {
                        "uid": 1099,
                        "name": 'м. Пирятин та Пирятинська',
                        "name_en": 'Pyriatyn and Pyriatynska Hromada',
                    },
                    {
                        "uid": 1100,
                        "name": 'Хорольська',
                        "name_en": 'Khorolska Hromada',
                    },
                    {
                        "uid": 1101,
                        "name": 'Чорнухинська',
                        "name_en": 'Chornukhynska Hromada',
                    },
                ],
            },
            {
                "uid": 108,
                "name": 'Миргородський',
                "name_en": 'Myrhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 1066,
                        "name": 'Білоцерківська',
                        "name_en": 'Bilotserkivska Hromada',
                    },
                    {
                        "uid": 1067,
                        "name": 'Великобагачанська',
                        "name_en": 'Velykobahachanska Hromada',
                    },
                    {
                        "uid": 1068,
                        "name": 'Великобудищанська',
                        "name_en": 'Velykobudyshchanska Hromada',
                    },
                    {
                        "uid": 1069,
                        "name": 'Великосорочинська',
                        "name_en": 'Velykosorochynska Hromada',
                    },
                    {
                        "uid": 1070,
                        "name": 'Гадяцька',
                        "name_en": 'Hadiatska Hromada',
                    },
                    {
                        "uid": 1071,
                        "name": 'Гоголівська',
                        "name_en": 'Hoholivska Hromada',
                    },
                    {
                        "uid": 1072,
                        "name": 'Заводська',
                        "name_en": 'Zavodska Hromada',
                    },
                    {
                        "uid": 1073,
                        "name": 'Комишнянська',
                        "name_en": 'Komyshnianska Hromada',
                    },
                    {
                        "uid": 1074,
                        "name": 'Краснолуцька',
                        "name_en": 'Krasnolutska Hromada',
                    },
                    {
                        "uid": 1075,
                        "name": 'м. Лохвиця та Лохвицька',
                        "name_en": 'Lokhvytsia and Lokhvytska Hromada',
                    },
                    {
                        "uid": 1076,
                        "name": 'Лютенська',
                        "name_en": 'Liutenska Hromada',
                    },
                    {
                        "uid": 1077,
                        "name": 'м. Миргород та Миргородська',
                        "name_en": 'Myrhorod and Myrhorodska Hromada',
                    },
                    {
                        "uid": 1078,
                        "name": 'Петрівсько-Роменська',
                        "name_en": 'Petrivsko-Romenska Hromada',
                    },
                    {
                        "uid": 1079,
                        "name": 'Ромоданівська',
                        "name_en": 'Romodanivska Hromada',
                    },
                    {
                        "uid": 1080,
                        "name": 'Сенчанська',
                        "name_en": 'Senchanska Hromada',
                    },
                    {
                        "uid": 1081,
                        "name": 'Сергіївська',
                        "name_en": 'Serhiivska Hromada',
                    },
                    {
                        "uid": 1082,
                        "name": 'Шишацька',
                        "name_en": 'Shyshatska Hromada',
                    },
                ],
            },
            {
                "uid": 109,
                "name": 'Полтавський',
                "name_en": 'Poltavskyi Raion',
                "hromadas": [
                    {
                        "uid": 1042,
                        "name": 'Білицька',
                        "name_en": 'Bilytska Hromada',
                    },
                    {
                        "uid": 1043,
                        "name": 'Великорублівська',
                        "name_en": 'Velykorublivska Hromada',
                    },
                    {
                        "uid": 1044,
                        "name": 'Диканьська',
                        "name_en": 'Dykanska Hromada',
                    },
                    {
                        "uid": 1045,
                        "name": 'Драбинівська',
                        "name_en": 'Drabynivska Hromada',
                    },
                    {
                        "uid": 1046,
                        "name": 'Зіньківська',
                        "name_en": 'Zinkivska Hromada',
                    },
                    {
                        "uid": 1047,
                        "name": 'Карлівська',
                        "name_en": 'Karlivska Hromada',
                    },
                    {
                        "uid": 1048,
                        "name": 'Кобеляцька',
                        "name_en": 'Kobeliatska Hromada',
                    },
                    {
                        "uid": 1049,
                        "name": 'Коломацька',
                        "name_en": 'Kolomatska Hromada',
                    },
                    {
                        "uid": 1050,
                        "name": 'Котелевська',
                        "name_en": 'Kotelevska Hromada',
                    },
                    {
                        "uid": 1051,
                        "name": 'Ланнівська',
                        "name_en": 'Lannivska Hromada',
                    },
                    {
                        "uid": 1052,
                        "name": 'Мартинівська',
                        "name_en": 'Martynivska Hromada',
                    },
                    {
                        "uid": 1053,
                        "name": 'Мачухівська',
                        "name_en": 'Machukhivska Hromada',
                    },
                    {
                        "uid": 1054,
                        "name": 'Машівська',
                        "name_en": 'Mashivska Hromada',
                    },
                    {
                        "uid": 1055,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 1056,
                        "name": 'Нехворощанська',
                        "name_en": 'Nekhvoroshchanska Hromada',
                    },
                    {
                        "uid": 1057,
                        "name": 'Новосанжарська',
                        "name_en": 'Novosanzharska Hromada',
                    },
                    {
                        "uid": 1058,
                        "name": 'Новоселівська',
                        "name_en": 'Novoselivska Hromada',
                    },
                    {
                        "uid": 1059,
                        "name": 'Опішнянська',
                        "name_en": 'Opishnianska Hromada',
                    },
                    {
                        "uid": 1060,
                        "name": 'м. Полтава та Полтавська',
                        "name_en": 'Poltava and Poltavska Hromada',
                    },
                    {
                        "uid": 1061,
                        "name": 'Решетилівська',
                        "name_en": 'Reshetylivska Hromada',
                    },
                    {
                        "uid": 1062,
                        "name": 'Скороходівська',
                        "name_en": 'Skorokhodivska Hromada',
                    },
                    {
                        "uid": 1063,
                        "name": 'Терешківська',
                        "name_en": 'Tereshkivska Hromada',
                    },
                    {
                        "uid": 1064,
                        "name": 'Чутівська',
                        "name_en": 'Chutivska Hromada',
                    },
                    {
                        "uid": 1065,
                        "name": 'Щербанівська',
                        "name_en": 'Shcherbanivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 5,
        "name": 'Рівненська область',
        "type": LocationType.OBLAST,
        "name_en": 'Rivnenska Oblast',
        "districts": [
            {
                "uid": 110,
                "name": 'Вараський',
                "name_en": 'Varaskyi Raion',
                "hromadas": [
                    {
                        "uid": 1102,
                        "name": 'Антонівська',
                        "name_en": 'Antonivska Hromada',
                    },
                    {
                        "uid": 1103,
                        "name": 'м. Вараш та Вараська',
                        "name_en": 'Varash and Varaska Hromada',
                    },
                    {
                        "uid": 1104,
                        "name": 'Володимирецька',
                        "name_en": 'Volodymyretska Hromada',
                    },
                    {
                        "uid": 1105,
                        "name": 'Зарічненська',
                        "name_en": 'Zarichnenska Hromada',
                    },
                    {
                        "uid": 1106,
                        "name": 'Каноницька',
                        "name_en": 'Kanonytska Hromada',
                    },
                    {
                        "uid": 1107,
                        "name": 'Локницька',
                        "name_en": 'Loknytska Hromada',
                    },
                    {
                        "uid": 1108,
                        "name": 'Полицька',
                        "name_en": 'Polytska Hromada',
                    },
                    {
                        "uid": 1109,
                        "name": 'Рафалівська',
                        "name_en": 'Rafalivska Hromada',
                    },
                ],
            },
            {
                "uid": 111,
                "name": 'Дубенський',
                "name_en": 'Dubenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1147,
                        "name": 'Бокіймівська',
                        "name_en": 'Bokiimivska Hromada',
                    },
                    {
                        "uid": 1148,
                        "name": 'Боремельська',
                        "name_en": 'Boremelska Hromada',
                    },
                    {
                        "uid": 1149,
                        "name": 'Варковицька',
                        "name_en": 'Varkovytska Hromada',
                    },
                    {
                        "uid": 1150,
                        "name": 'Вербська',
                        "name_en": 'Verbska Hromada',
                    },
                    {
                        "uid": 1151,
                        "name": 'Демидівська',
                        "name_en": 'Demydivska Hromada',
                    },
                    {
                        "uid": 1152,
                        "name": 'м. Дубно та Дубенська',
                        "name_en": 'Dubno and Dubenska Hromada',
                    },
                    {
                        "uid": 1153,
                        "name": 'Козинська',
                        "name_en": 'Kozynska Hromada',
                    },
                    {
                        "uid": 1154,
                        "name": 'Крупецька',
                        "name_en": 'Krupetska Hromada',
                    },
                    {
                        "uid": 1155,
                        "name": 'Мирогощанська',
                        "name_en": 'Myrohoshchanska Hromada',
                    },
                    {
                        "uid": 1156,
                        "name": 'Млинівська',
                        "name_en": 'Mlynivska Hromada',
                    },
                    {
                        "uid": 1157,
                        "name": 'Острожецька',
                        "name_en": 'Ostrozhetska Hromada',
                    },
                    {
                        "uid": 1159,
                        "name": 'Повчанська',
                        "name_en": 'Povchanska Hromada',
                    },
                    {
                        "uid": 1160,
                        "name": 'Привільненська',
                        "name_en": 'Pryvilnenska Hromada',
                    },
                    {
                        "uid": 1158,
                        "name": 'Підлозцівська',
                        "name_en": 'Pidloztsivska Hromada',
                    },
                    {
                        "uid": 1161,
                        "name": 'Радивилівська',
                        "name_en": 'Radyvylivska Hromada',
                    },
                    {
                        "uid": 1162,
                        "name": 'Семидубська',
                        "name_en": 'Semydubska Hromada',
                    },
                    {
                        "uid": 1163,
                        "name": 'Смизька',
                        "name_en": 'Smyzka Hromada',
                    },
                    {
                        "uid": 1164,
                        "name": 'Тараканівська',
                        "name_en": 'Tarakanivska Hromada',
                    },
                    {
                        "uid": 1165,
                        "name": 'Ярославицька',
                        "name_en": 'Yaroslavytska Hromada',
                    },
                ],
            },
            {
                "uid": 112,
                "name": 'Рівненський',
                "name_en": 'Rivnenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1110,
                        "name": 'Бабинська',
                        "name_en": 'Babynska Hromada',
                    },
                    {
                        "uid": 1111,
                        "name": 'Березнівська',
                        "name_en": 'Bereznivska Hromada',
                    },
                    {
                        "uid": 1113,
                        "name": 'Бугринська',
                        "name_en": 'Buhrynska Hromada',
                    },
                    {
                        "uid": 1112,
                        "name": 'Білокриницька',
                        "name_en": 'Bilokrynytska Hromada',
                    },
                    {
                        "uid": 1114,
                        "name": 'Великомежиріцька',
                        "name_en": 'Velykomezhyritska Hromada',
                    },
                    {
                        "uid": 1115,
                        "name": 'Великоомелянська',
                        "name_en": 'Velykoomelianska Hromada',
                    },
                    {
                        "uid": 1116,
                        "name": 'Головинська',
                        "name_en": 'Holovynska Hromada',
                    },
                    {
                        "uid": 1117,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 1118,
                        "name": 'Гощанська',
                        "name_en": 'Hoshchanska Hromada',
                    },
                    {
                        "uid": 1119,
                        "name": 'Деражненська',
                        "name_en": 'Derazhnenska Hromada',
                    },
                    {
                        "uid": 1120,
                        "name": 'Дядьковицька',
                        "name_en": 'Diadkovytska Hromada',
                    },
                    {
                        "uid": 1121,
                        "name": 'Здовбицька',
                        "name_en": 'Zdovbytska Hromada',
                    },
                    {
                        "uid": 1122,
                        "name": 'Здолбунівська',
                        "name_en": 'Zdolbunivska Hromada',
                    },
                    {
                        "uid": 1123,
                        "name": 'Зорянська',
                        "name_en": 'Zorianska Hromada',
                    },
                    {
                        "uid": 1124,
                        "name": 'Клеванська',
                        "name_en": 'Klevanska Hromada',
                    },
                    {
                        "uid": 1125,
                        "name": 'Корецька',
                        "name_en": 'Koretska Hromada',
                    },
                    {
                        "uid": 1126,
                        "name": 'Корнинська',
                        "name_en": 'Kornynska Hromada',
                    },
                    {
                        "uid": 1127,
                        "name": 'Костопільська',
                        "name_en": 'Kostopilska Hromada',
                    },
                    {
                        "uid": 1128,
                        "name": 'Малинська',
                        "name_en": 'Malynska Hromada',
                    },
                    {
                        "uid": 1129,
                        "name": 'Малолюбашанська',
                        "name_en": 'Maloliubashanska Hromada',
                    },
                    {
                        "uid": 1130,
                        "name": 'Мізоцька',
                        "name_en": 'Mizotska Hromada',
                    },
                    {
                        "uid": 1131,
                        "name": 'Олександрійська',
                        "name_en": 'Oleksandriiska Hromada',
                    },
                    {
                        "uid": 1132,
                        "name": 'м. Острог та Острозька',
                        "name_en": 'Ostroh and Ostrozka Hromada',
                    },
                    {
                        "uid": 1133,
                        "name": 'м. Рівне та Рівненська',
                        "name_en": 'Rivne and Rivnenska Hromada',
                    },
                    {
                        "uid": 1134,
                        "name": 'Соснівська',
                        "name_en": 'Sosnivska Hromada',
                    },
                    {
                        "uid": 1135,
                        "name": 'Шпанівська',
                        "name_en": 'Shpanivska Hromada',
                    },
                ],
            },
            {
                "uid": 113,
                "name": 'Сарненський',
                "name_en": 'Sarnenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1136,
                        "name": 'Березівська',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 1137,
                        "name": 'Вирівська',
                        "name_en": 'Vyrivska Hromada',
                    },
                    {
                        "uid": 1138,
                        "name": 'Висоцька',
                        "name_en": 'Vysotska Hromada',
                    },
                    {
                        "uid": 1139,
                        "name": 'Дубровицька',
                        "name_en": 'Dubrovytska Hromada',
                    },
                    {
                        "uid": 1140,
                        "name": 'Клесівська',
                        "name_en": 'Klesivska Hromada',
                    },
                    {
                        "uid": 1141,
                        "name": 'Миляцька',
                        "name_en": 'Myliatska Hromada',
                    },
                    {
                        "uid": 1142,
                        "name": 'Немовицька',
                        "name_en": 'Nemovytska Hromada',
                    },
                    {
                        "uid": 1143,
                        "name": 'Рокитнівська',
                        "name_en": 'Rokytnivska Hromada',
                    },
                    {
                        "uid": 1144,
                        "name": 'м. Сарни та Сарненська',
                        "name_en": 'Sarny and Sarnenska Hromada',
                    },
                    {
                        "uid": 1145,
                        "name": 'Старосільська',
                        "name_en": 'Starosilska Hromada',
                    },
                    {
                        "uid": 1146,
                        "name": 'Степанська',
                        "name_en": 'Stepanska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 20,
        "name": 'Сумська область',
        "type": LocationType.OBLAST,
        "name_en": 'Sumska Oblast',
        "districts": [
            {
                "uid": 117,
                "name": 'Конотопський',
                "name_en": 'Konotopskyi Raion',
                "hromadas": [
                    {
                        "uid": 1209,
                        "name": 'Бочечківська',
                        "name_en": 'Bochechkivska Hromada',
                    },
                    {
                        "uid": 1210,
                        "name": 'м. Буринь та Буринська',
                        "name_en": 'Buryn and Burynska Hromada',
                    },
                    {
                        "uid": 1211,
                        "name": 'Дубов’язівська',
                        "name_en": 'Dubovyazivska Hromada',
                    },
                    {
                        "uid": 1212,
                        "name": 'м. Конотоп та Конотопська',
                        "name_en": 'Konotop and Konotopska Hromada',
                    },
                    {
                        "uid": 1213,
                        "name": 'м. Кролевець та Кролевецька',
                        "name_en": 'Krolevets and Krolevetska Hromada',
                    },
                    {
                        "uid": 1214,
                        "name": 'Новослобідська',
                        "name_en": 'Novoslobidska Hromada',
                    },
                    {
                        "uid": 1215,
                        "name": 'Попівська',
                        "name_en": 'Popivska Hromada',
                    },
                    {
                        "uid": 1216,
                        "name": 'м. Путивль та Путивльська',
                        "name_en": 'Putyvl and Putyvlska Hromada',
                    },
                ],
            },
            {
                "uid": 118,
                "name": 'Охтирський',
                "name_en": 'Okhtyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 1200,
                        "name": 'Боромлянська',
                        "name_en": 'Boromlianska Hromada',
                    },
                    {
                        "uid": 1201,
                        "name": 'м. Велика Писарівка та Великописарівська',
                        "name_en": 'Velyka Pysarivka and Velykopysarivska Hromada',
                    },
                    {
                        "uid": 1202,
                        "name": 'Грунська',
                        "name_en": 'Hrunska Hromada',
                    },
                    {
                        "uid": 1203,
                        "name": 'Кириківська',
                        "name_en": 'Kyrykivska Hromada',
                    },
                    {
                        "uid": 1204,
                        "name": 'Комишанська',
                        "name_en": 'Komyshanska Hromada',
                    },
                    {
                        "uid": 1205,
                        "name": 'м. Охтирка та Охтирська',
                        "name_en": 'Okhtyrka and Okhtyrska Hromada',
                    },
                    {
                        "uid": 1206,
                        "name": 'м. Тростянець та Тростянецька',
                        "name_en": 'Trostianets and Trostianetska Hromada',
                    },
                    {
                        "uid": 1207,
                        "name": 'Чернеччинська',
                        "name_en": 'Chernechchynska Hromada',
                    },
                    {
                        "uid": 1208,
                        "name": 'Чупахівська',
                        "name_en": 'Chupakhivska Hromada',
                    },
                ],
            },
            {
                "uid": 116,
                "name": 'Роменський',
                "name_en": 'Romenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1166,
                        "name": 'Андріяшівська',
                        "name_en": 'Andriiashivska Hromada',
                    },
                    {
                        "uid": 1167,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 1168,
                        "name": 'Коровинська',
                        "name_en": 'Korovynska Hromada',
                    },
                    {
                        "uid": 1169,
                        "name": 'м. Липова Долина та Липоводолинська',
                        "name_en": 'Lypova Dolyna and Lypovodolynska Hromada',
                    },
                    {
                        "uid": 1170,
                        "name": 'м. Недригайлів та Недригайлівська',
                        "name_en": 'Nedryhailiv and Nedryhailivska Hromada',
                    },
                    {
                        "uid": 1171,
                        "name": 'м. Ромни та Роменська',
                        "name_en": 'Romny and Romenska Hromada',
                    },
                    {
                        "uid": 1172,
                        "name": 'Синівська',
                        "name_en": 'Synivska Hromada',
                    },
                    {
                        "uid": 1173,
                        "name": 'Хмелівська',
                        "name_en": 'Khmelivska Hromada',
                    },
                ],
            },
            {
                "uid": 114,
                "name": 'Сумський',
                "name_en": 'Sumskyi Raion',
                "hromadas": [
                    {
                        "uid": 1174,
                        "name": 'Бездрицька',
                        "name_en": 'Bezdrytska Hromada',
                    },
                    {
                        "uid": 1175,
                        "name": 'м. Білопілля та Білопільська',
                        "name_en": 'Bilopillia and Bilopilska Hromada',
                    },
                    {
                        "uid": 1176,
                        "name": 'Верхньосироватська',
                        "name_en": 'Verkhnosyrovatska Hromada',
                    },
                    {
                        "uid": 1177,
                        "name": 'Ворожбянська',
                        "name_en": 'Vorozhbianska Hromada',
                    },
                    {
                        "uid": 1178,
                        "name": 'м. Краснопілля та Краснопільська',
                        "name_en": 'Krasnopillia and Krasnopilska Hromada',
                    },
                    {
                        "uid": 1179,
                        "name": 'м. Лебедин та Лебединська',
                        "name_en": 'Lebedyn and Lebedynska Hromada',
                    },
                    {
                        "uid": 1181,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 1180,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 1182,
                        "name": 'Миропільська',
                        "name_en": 'Myropilska Hromada',
                    },
                    {
                        "uid": 1183,
                        "name": 'Нижньосироватська',
                        "name_en": 'Nyzhnosyrovatska Hromada',
                    },
                    {
                        "uid": 1184,
                        "name": 'Річківська',
                        "name_en": 'Richkivska Hromada',
                    },
                    {
                        "uid": 1185,
                        "name": 'Садівська',
                        "name_en": 'Sadivska Hromada',
                    },
                    {
                        "uid": 1186,
                        "name": 'Степанівська',
                        "name_en": 'Stepanivska Hromada',
                    },
                    {
                        "uid": 1187,
                        "name": 'м. Суми та Сумська',
                        "name_en": 'Sumy and Sumska Hromada',
                    },
                    {
                        "uid": 1188,
                        "name": 'Хотінська',
                        "name_en": 'Khotinska Hromada',
                    },
                    {
                        "uid": 1189,
                        "name": 'Юнаківська',
                        "name_en": 'Yunakivska Hromada',
                    },
                ],
            },
            {
                "uid": 115,
                "name": 'Шосткинський',
                "name_en": 'Shostkynskyi Raion',
                "hromadas": [
                    {
                        "uid": 1190,
                        "name": 'Березівська',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 1191,
                        "name": 'м. Глухів та Глухівська',
                        "name_en": 'Hlukhiv and Hlukhivska Hromada',
                    },
                    {
                        "uid": 1192,
                        "name": 'Дружбівська',
                        "name_en": 'Druzhbivska Hromada',
                    },
                    {
                        "uid": 1193,
                        "name": 'Есманьська',
                        "name_en": 'Esmanska Hromada',
                    },
                    {
                        "uid": 1194,
                        "name": 'Зноб-Новгородська',
                        "name_en": 'Znob-Novhorodska Hromada',
                    },
                    {
                        "uid": 1195,
                        "name": 'Свеська',
                        "name_en": 'Sveska Hromada',
                    },
                    {
                        "uid": 1196,
                        "name": 'м. Середина-Буда та Середино-Будська',
                        "name_en": 'Seredyna-Buda and Seredyno-Budska Hromada',
                    },
                    {
                        "uid": 1197,
                        "name": 'Шалигинська',
                        "name_en": 'Shalyhynska Hromada',
                    },
                    {
                        "uid": 1198,
                        "name": 'м. Шостка та Шосткинська',
                        "name_en": 'Shostka and Shostkynska Hromada',
                    },
                    {
                        "uid": 1199,
                        "name": 'м. Ямпіль та Ямпільська',
                        "name_en": 'Yampil and Yampilska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 21,
        "name": 'Тернопільська область',
        "type": LocationType.OBLAST,
        "name_en": 'Ternopilska Oblast',
        "districts": [
            {
                "uid": 120,
                "name": 'Кременецький',
                "name_en": 'Kremenetskyi Raion',
                "hromadas": [
                    {
                        "uid": 1264,
                        "name": 'Борсуківська',
                        "name_en": 'Borsukivska Hromada',
                    },
                    {
                        "uid": 1265,
                        "name": 'Великодедеркальська',
                        "name_en": 'Velykodederkalska Hromada',
                    },
                    {
                        "uid": 1266,
                        "name": 'Вишнівецька',
                        "name_en": 'Vyshnivetska Hromada',
                    },
                    {
                        "uid": 1267,
                        "name": 'м. Кременець та Кременецька',
                        "name_en": 'Kremenets and Kremenetska Hromada',
                    },
                    {
                        "uid": 1268,
                        "name": 'Лановецька',
                        "name_en": 'Lanovetska Hromada',
                    },
                    {
                        "uid": 1269,
                        "name": 'Лопушненська',
                        "name_en": 'Lopushnenska Hromada',
                    },
                    {
                        "uid": 1270,
                        "name": 'Почаївська',
                        "name_en": 'Pochaivska Hromada',
                    },
                    {
                        "uid": 1271,
                        "name": 'Шумська',
                        "name_en": 'Shumska Hromada',
                    },
                ],
            },
            {
                "uid": 119,
                "name": 'Тернопільський',
                "name_en": 'Ternopilskyi Raion',
                "hromadas": [
                    {
                        "uid": 1217,
                        "name": 'Байковецька',
                        "name_en": 'Baikovetska Hromada',
                    },
                    {
                        "uid": 1218,
                        "name": 'м. Бережани та Бережанська',
                        "name_en": 'Berezhany and Berezhanska Hromada',
                    },
                    {
                        "uid": 1219,
                        "name": 'Білецька',
                        "name_en": 'Biletska Hromada',
                    },
                    {
                        "uid": 1220,
                        "name": 'Великоберезовицька',
                        "name_en": 'Velykoberezovytska Hromada',
                    },
                    {
                        "uid": 1221,
                        "name": 'Великобірківська',
                        "name_en": 'Velykobirkivska Hromada',
                    },
                    {
                        "uid": 1222,
                        "name": 'Великогаївська',
                        "name_en": 'Velykohaivska Hromada',
                    },
                    {
                        "uid": 1223,
                        "name": 'Залозецька',
                        "name_en": 'Zalozetska Hromada',
                    },
                    {
                        "uid": 1224,
                        "name": 'Збаразька',
                        "name_en": 'Zbarazka Hromada',
                    },
                    {
                        "uid": 1225,
                        "name": 'Зборівська',
                        "name_en": 'Zborivska Hromada',
                    },
                    {
                        "uid": 1226,
                        "name": 'Золотниківська',
                        "name_en": 'Zolotnykivska Hromada',
                    },
                    {
                        "uid": 1229,
                        "name": 'Козлівська',
                        "name_en": 'Kozlivska Hromada',
                    },
                    {
                        "uid": 1228,
                        "name": 'Козівська',
                        "name_en": 'Kozivska Hromada',
                    },
                    {
                        "uid": 1230,
                        "name": 'Купчинецька',
                        "name_en": 'Kupchynetska Hromada',
                    },
                    {
                        "uid": 1231,
                        "name": 'Микулинецька',
                        "name_en": 'Mykulynetska Hromada',
                    },
                    {
                        "uid": 1232,
                        "name": 'Нараївська',
                        "name_en": 'Naraivska Hromada',
                    },
                    {
                        "uid": 1233,
                        "name": 'Озернянська',
                        "name_en": 'Ozernianska Hromada',
                    },
                    {
                        "uid": 1234,
                        "name": 'Підволочиська',
                        "name_en": 'Pidvolochyska Hromada',
                    },
                    {
                        "uid": 1235,
                        "name": 'Підгаєцька',
                        "name_en": 'Pidhaietska Hromada',
                    },
                    {
                        "uid": 1236,
                        "name": 'Підгороднянська',
                        "name_en": 'Pidhorodnianska Hromada',
                    },
                    {
                        "uid": 1237,
                        "name": 'Саранчуківська',
                        "name_en": 'Saranchukivska Hromada',
                    },
                    {
                        "uid": 1238,
                        "name": 'Скалатська',
                        "name_en": 'Skalatska Hromada',
                    },
                    {
                        "uid": 1239,
                        "name": 'Скориківська',
                        "name_en": 'Skorykivska Hromada',
                    },
                    {
                        "uid": 1240,
                        "name": 'Теребовлянська',
                        "name_en": 'Terebovlianska Hromada',
                    },
                    {
                        "uid": 1241,
                        "name": 'м. Тернопіль та Тернопільська',
                        "name_en": 'Ternopil and Ternopilska Hromada',
                    },
                    {
                        "uid": 1227,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
            {
                "uid": 121,
                "name": 'Чортківський',
                "name_en": 'Chortkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1244,
                        "name": 'Борщівська',
                        "name_en": 'Borshchivska Hromada',
                    },
                    {
                        "uid": 1245,
                        "name": 'Бучацька',
                        "name_en": 'Buchatska Hromada',
                    },
                    {
                        "uid": 1242,
                        "name": 'Білобожницька',
                        "name_en": 'Bilobozhnytska Hromada',
                    },
                    {
                        "uid": 1243,
                        "name": 'Більче-Золотецька',
                        "name_en": 'Bilche-Zolotetska Hromada',
                    },
                    {
                        "uid": 1246,
                        "name": 'Васильковецька',
                        "name_en": 'Vasylkovetska Hromada',
                    },
                    {
                        "uid": 1247,
                        "name": 'Гримайлівська',
                        "name_en": 'Hrymailivska Hromada',
                    },
                    {
                        "uid": 1248,
                        "name": 'Гусятинська',
                        "name_en": 'Husiatynska Hromada',
                    },
                    {
                        "uid": 1249,
                        "name": 'Заводська',
                        "name_en": 'Zavodska Hromada',
                    },
                    {
                        "uid": 1250,
                        "name": 'Заліщицька',
                        "name_en": 'Zalishchytska Hromada',
                    },
                    {
                        "uid": 1251,
                        "name": 'Золотопотіцька',
                        "name_en": 'Zolotopotitska Hromada',
                    },
                    {
                        "uid": 1253,
                        "name": 'Колиндянська',
                        "name_en": 'Kolyndianska Hromada',
                    },
                    {
                        "uid": 1254,
                        "name": 'Копичинецька',
                        "name_en": 'Kopychynetska Hromada',
                    },
                    {
                        "uid": 1255,
                        "name": 'Коропецька',
                        "name_en": 'Koropetska Hromada',
                    },
                    {
                        "uid": 1256,
                        "name": 'Мельнице-Подільська',
                        "name_en": 'Melnytse-Podilska Hromada',
                    },
                    {
                        "uid": 1257,
                        "name": 'Монастириська',
                        "name_en": 'Monastyryska Hromada',
                    },
                    {
                        "uid": 1258,
                        "name": 'Нагірянська',
                        "name_en": 'Nahirianska Hromada',
                    },
                    {
                        "uid": 1259,
                        "name": 'Скала-Подільська',
                        "name_en": 'Skala-Podilska Hromada',
                    },
                    {
                        "uid": 1260,
                        "name": 'Товстенська',
                        "name_en": 'Tovstenska Hromada',
                    },
                    {
                        "uid": 1261,
                        "name": 'Трибухівська',
                        "name_en": 'Trybukhivska Hromada',
                    },
                    {
                        "uid": 1262,
                        "name": 'Хоростківська',
                        "name_en": 'Khorostkivska Hromada',
                    },
                    {
                        "uid": 1263,
                        "name": 'м. Чортків та Чортківська',
                        "name_en": 'Chortkiv and Chortkivska Hromada',
                    },
                    {
                        "uid": 1252,
                        "name": 'Іване-Пустенська',
                        "name_en": 'Ivane-Pustenska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 22,
        "name": 'Харківська область',
        "type": LocationType.OBLAST,
        "name_en": 'Kharkivska Oblast',
        "districts": [
            {
                "uid": 127,
                "name": 'Берестинський',
                "name_en": 'Berestynskyi Raion',
                "hromadas": [
                    {
                        "uid": 1324,
                        "name": 'Берестинська',
                        "name_en": 'Berestynska Hromada',
                    },
                    {
                        "uid": 1322,
                        "name": 'Зачепилівська',
                        "name_en": 'Zachepylivska Hromada',
                    },
                    {
                        "uid": 1323,
                        "name": 'Кегичівська',
                        "name_en": 'Kehychivska Hromada',
                    },
                    {
                        "uid": 1325,
                        "name": 'Наталинська',
                        "name_en": 'Natalynska Hromada',
                    },
                    {
                        "uid": 1326,
                        "name": 'Сахновщинська',
                        "name_en": 'Sakhnovshchynska Hromada',
                    },
                    {
                        "uid": 1327,
                        "name": 'Старовірівська',
                        "name_en": 'Starovirivska Hromada',
                    },
                ],
            },
            {
                "uid": 126,
                "name": 'Богодухівський',
                "name_en": 'Bohodukhivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1300,
                        "name": 'м. Богодухів та Богодухівська',
                        "name_en": 'Bohodukhiv and Bohodukhivska Hromada',
                    },
                    {
                        "uid": 1301,
                        "name": 'Валківська',
                        "name_en": 'Valkivska Hromada',
                    },
                    {
                        "uid": 1302,
                        "name": 'Золочівська',
                        "name_en": 'Zolochivska Hromada',
                    },
                    {
                        "uid": 1303,
                        "name": 'Коломацька',
                        "name_en": 'Kolomatska Hromada',
                    },
                    {
                        "uid": 1304,
                        "name": 'Краснокутська',
                        "name_en": 'Krasnokutska Hromada',
                    },
                ],
            },
            {
                "uid": 123,
                "name": "Куп'янський",
                "name_en": 'Kupianskyi Raion',
                "hromadas": [
                    {
                        "uid": 1305,
                        "name": 'Великобурлуцька',
                        "name_en": 'Velykoburlutska Hromada',
                    },
                    {
                        "uid": 1306,
                        "name": 'Вільхуватська',
                        "name_en": 'Vilkhuvatska Hromada',
                    },
                    {
                        "uid": 1307,
                        "name": 'Дворічанська',
                        "name_en": 'Dvorichanska Hromada',
                    },
                    {
                        "uid": 1309,
                        "name": "м. Куп'янськ та Куп'янська",
                        "name_en": 'Kupiansk and Kupianska Hromada',
                    },
                    {
                        "uid": 1310,
                        "name": 'Курилівська',
                        "name_en": 'Kurylivska Hromada',
                    },
                    {
                        "uid": 1308,
                        "name": 'Кіндрашівська',
                        "name_en": 'Kindrashivska Hromada',
                    },
                    {
                        "uid": 1311,
                        "name": 'Петропавлівська',
                        "name_en": 'Petropavlivska Hromada',
                    },
                    {
                        "uid": 1312,
                        "name": 'Шевченківська',
                        "name_en": 'Shevchenkivska Hromada',
                    },
                ],
            },
            {
                "uid": 128,
                "name": 'Лозівський',
                "name_en": 'Lozivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1296,
                        "name": 'Близнюківська',
                        "name_en": 'Blyzniukivska Hromada',
                    },
                    {
                        "uid": 1295,
                        "name": 'Біляївська',
                        "name_en": 'Biliaivska Hromada',
                    },
                    {
                        "uid": 1299,
                        "name": 'м. Златопіль та Златопільська',
                        "name_en": 'Zlatopil and Zlatopilska Hromada',
                    },
                    {
                        "uid": 1297,
                        "name": 'м. Лозова та Лозівська',
                        "name_en": 'Lozova and Lozivska Hromada',
                    },
                    {
                        "uid": 1298,
                        "name": 'Олексіївська',
                        "name_en": 'Oleksiivska Hromada',
                    },
                ],
            },
            {
                "uid": 124,
                "name": 'Харківський',
                "name_en": 'Kharkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1280,
                        "name": 'Безлюдівська',
                        "name_en": 'Bezliudivska Hromada',
                    },
                    {
                        "uid": 1281,
                        "name": 'Височанська',
                        "name_en": 'Vysochanska Hromada',
                    },
                    {
                        "uid": 1282,
                        "name": 'Вільхівська',
                        "name_en": 'Vilkhivska Hromada',
                    },
                    {
                        "uid": 1283,
                        "name": 'Дергачівська',
                        "name_en": 'Derhachivska Hromada',
                    },
                    {
                        "uid": 1284,
                        "name": 'Липецька',
                        "name_en": 'Lypetska Hromada',
                    },
                    {
                        "uid": 1285,
                        "name": 'м. Люботин та Люботинська',
                        "name_en": 'Liubotyn and Liubotynska Hromada',
                    },
                    {
                        "uid": 1286,
                        "name": 'Малоданилівська',
                        "name_en": 'Malodanylivska Hromada',
                    },
                    {
                        "uid": 1287,
                        "name": "Мереф'янська",
                        "name_en": 'Merefianska Hromada',
                    },
                    {
                        "uid": 1288,
                        "name": 'Нововодолазька',
                        "name_en": 'Novovodolazka Hromada',
                    },
                    {
                        "uid": 1289,
                        "name": 'Південноміська',
                        "name_en": 'Pivdennomiska Hromada',
                    },
                    {
                        "uid": 1290,
                        "name": 'Пісочинська',
                        "name_en": 'Pisochynska Hromada',
                    },
                    {
                        "uid": 1291,
                        "name": 'Роганська',
                        "name_en": 'Rohanska Hromada',
                    },
                    {
                        "uid": 1292,
                        "name": 'Солоницівська',
                        "name_en": 'Solonytsivska Hromada',
                    },
                    {
                        "uid": 1293,
                        "name": 'м. Харків та Харківська',
                        "name_en": 'Kharkiv and Kharkivska Hromada',
                    },
                    {
                        "uid": 1294,
                        "name": 'Циркунівська',
                        "name_en": 'Tsyrkunivska Hromada',
                    },
                ],
            },
            {
                "uid": 122,
                "name": 'Чугуївський',
                "name_en": 'Chuhuivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1313,
                        "name": 'Вовчанська',
                        "name_en": 'Vovchanska Hromada',
                    },
                    {
                        "uid": 1314,
                        "name": 'Зміївська',
                        "name_en": 'Zmiivska Hromada',
                    },
                    {
                        "uid": 1315,
                        "name": 'Малинівська',
                        "name_en": 'Malynivska Hromada',
                    },
                    {
                        "uid": 1316,
                        "name": 'Новопокровська',
                        "name_en": 'Novopokrovska Hromada',
                    },
                    {
                        "uid": 1317,
                        "name": 'Печенізька',
                        "name_en": 'Pechenizka Hromada',
                    },
                    {
                        "uid": 1318,
                        "name": 'Слобожанська',
                        "name_en": 'Slobozhanska Hromada',
                    },
                    {
                        "uid": 1319,
                        "name": 'Старосалтівська',
                        "name_en": 'Starosaltivska Hromada',
                    },
                    {
                        "uid": 1320,
                        "name": 'Чкаловська',
                        "name_en": 'Chkalovska Hromada',
                    },
                    {
                        "uid": 1321,
                        "name": 'м. Чугуїв та Чугуївська',
                        "name_en": 'Chuhuiv and Chuhuivska Hromada',
                    },
                ],
            },
            {
                "uid": 125,
                "name": 'Ізюмський',
                "name_en": 'Iziumskyi Raion',
                "hromadas": [
                    {
                        "uid": 1272,
                        "name": 'Балаклійська',
                        "name_en": 'Balakliiska Hromada',
                    },
                    {
                        "uid": 1273,
                        "name": 'Барвінківська',
                        "name_en": 'Barvinkivska Hromada',
                    },
                    {
                        "uid": 1274,
                        "name": 'Борівська',
                        "name_en": 'Borivska Hromada',
                    },
                    {
                        "uid": 1275,
                        "name": 'Донецька',
                        "name_en": 'Donetska Hromada',
                    },
                    {
                        "uid": 1277,
                        "name": 'Куньєвська',
                        "name_en": 'Kunievska Hromada',
                    },
                    {
                        "uid": 1278,
                        "name": 'Оскільська',
                        "name_en": 'Oskilska Hromada',
                    },
                    {
                        "uid": 1279,
                        "name": 'Савинська',
                        "name_en": 'Savynska Hromada',
                    },
                    {
                        "uid": 1276,
                        "name": 'м. Ізюм та Ізюмська',
                        "name_en": 'Izium and Iziumska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 23,
        "name": 'Херсонська область',
        "type": LocationType.OBLAST,
        "name_en": 'Khersonska Oblast',
        "districts": [
            {
                "uid": 129,
                "name": 'Бериславський',
                "name_en": 'Beryslavskyi Raion',
                "hromadas": [
                    {
                        "uid": 1343,
                        "name": 'Бериславська',
                        "name_en": 'Beryslavska Hromada',
                    },
                    {
                        "uid": 1344,
                        "name": 'Борозенська',
                        "name_en": 'Borozenska Hromada',
                    },
                    {
                        "uid": 1345,
                        "name": 'Великоолександрівська',
                        "name_en": 'Velykooleksandrivska Hromada',
                    },
                    {
                        "uid": 1346,
                        "name": 'Високопільська',
                        "name_en": 'Vysokopilska Hromada',
                    },
                    {
                        "uid": 1347,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 1348,
                        "name": 'Кочубеївська',
                        "name_en": 'Kochubeivska Hromada',
                    },
                    {
                        "uid": 1349,
                        "name": 'Милівська',
                        "name_en": 'Mylivska Hromada',
                    },
                    {
                        "uid": 1350,
                        "name": 'Нововоронцовська',
                        "name_en": 'Novovorontsovska Hromada',
                    },
                    {
                        "uid": 1351,
                        "name": 'Новоолександрівська',
                        "name_en": 'Novooleksandrivska Hromada',
                    },
                    {
                        "uid": 1352,
                        "name": 'Новорайська',
                        "name_en": 'Novoraiska Hromada',
                    },
                    {
                        "uid": 1353,
                        "name": 'Тягинська',
                        "name_en": 'Tiahynska Hromada',
                    },
                ],
            },
            {
                "uid": 133,
                "name": 'Генічеський',
                "name_en": 'Henicheskyi Raion',
                "hromadas": [
                    {
                        "uid": 1373,
                        "name": 'Генічеська',
                        "name_en": 'Henicheska Hromada',
                    },
                    {
                        "uid": 1375,
                        "name": 'Нижньосірогозька',
                        "name_en": 'Nyzhnosirohozka Hromada',
                    },
                    {
                        "uid": 1376,
                        "name": 'Новотроїцька',
                        "name_en": 'Novotroitska Hromada',
                    },
                    {
                        "uid": 1374,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
            {
                "uid": 131,
                "name": 'Каховський',
                "name_en": 'Kakhovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1328,
                        "name": 'Асканія-Нова',
                        "name_en": 'Askaniia-Nova Hromada',
                    },
                    {
                        "uid": 1329,
                        "name": 'Великолепетиська',
                        "name_en": 'Velykolepetyska Hromada',
                    },
                    {
                        "uid": 1330,
                        "name": 'Верхньорогачицька',
                        "name_en": 'Verkhnorohachytska Hromada',
                    },
                    {
                        "uid": 1331,
                        "name": 'Горностаївська',
                        "name_en": 'Hornostaivska Hromada',
                    },
                    {
                        "uid": 1332,
                        "name": 'Зеленопідська',
                        "name_en": 'Zelenopidska Hromada',
                    },
                    {
                        "uid": 1333,
                        "name": 'м. Каховка та Каховська',
                        "name_en": 'Kakhovka and Kakhovska Hromada',
                    },
                    {
                        "uid": 1334,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 1335,
                        "name": 'Любимівська',
                        "name_en": 'Liubymivska Hromada',
                    },
                    {
                        "uid": 1336,
                        "name": 'м. Нова Каховка та Новокаховська',
                        "name_en": 'Nova Kakhovka and Novokakhovska Hromada',
                    },
                    {
                        "uid": 1337,
                        "name": 'Присиваська',
                        "name_en": 'Prysyvaska Hromada',
                    },
                    {
                        "uid": 1338,
                        "name": 'Рубанівська',
                        "name_en": 'Rubanivska Hromada',
                    },
                    {
                        "uid": 1339,
                        "name": 'Тавричанська',
                        "name_en": 'Tavrychanska Hromada',
                    },
                    {
                        "uid": 1340,
                        "name": 'Таврійська',
                        "name_en": 'Tavriiska Hromada',
                    },
                    {
                        "uid": 1341,
                        "name": 'Хрестівська',
                        "name_en": 'Khrestivska Hromada',
                    },
                    {
                        "uid": 1342,
                        "name": 'Чаплинська',
                        "name_en": 'Chaplynska Hromada',
                    },
                ],
            },
            {
                "uid": 130,
                "name": 'Скадовський',
                "name_en": 'Skadovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1354,
                        "name": 'Бехтерська',
                        "name_en": 'Bekhterska Hromada',
                    },
                    {
                        "uid": 1355,
                        "name": 'м. Гола Пристань та Голопристанська',
                        "name_en": 'Hola Prystan and Holoprystanska Hromada',
                    },
                    {
                        "uid": 1356,
                        "name": 'Долматівська',
                        "name_en": 'Dolmativska Hromada',
                    },
                    {
                        "uid": 1357,
                        "name": 'Каланчацька',
                        "name_en": 'Kalanchatska Hromada',
                    },
                    {
                        "uid": 1358,
                        "name": 'Лазурненська',
                        "name_en": 'Lazurnenska Hromada',
                    },
                    {
                        "uid": 1359,
                        "name": 'Мирненська',
                        "name_en": 'Myrnenska Hromada',
                    },
                    {
                        "uid": 1360,
                        "name": 'Новомиколаївська',
                        "name_en": 'Novomykolaivska Hromada',
                    },
                    {
                        "uid": 1361,
                        "name": 'Скадовська',
                        "name_en": 'Skadovska Hromada',
                    },
                    {
                        "uid": 1362,
                        "name": 'Чулаківська',
                        "name_en": 'Chulakivska Hromada',
                    },
                ],
            },
            {
                "uid": 132,
                "name": 'Херсонський',
                "name_en": 'Khersonskyi Raion',
                "hromadas": [
                    {
                        "uid": 1363,
                        "name": 'Білозерська',
                        "name_en": 'Bilozerska Hromada',
                    },
                    {
                        "uid": 1364,
                        "name": 'Великокопанівська',
                        "name_en": 'Velykokopanivska Hromada',
                    },
                    {
                        "uid": 1365,
                        "name": 'Виноградівська',
                        "name_en": 'Vynohradivska Hromada',
                    },
                    {
                        "uid": 1366,
                        "name": 'Дар’ївська',
                        "name_en": 'Daryivska Hromada',
                    },
                    {
                        "uid": 1367,
                        "name": 'Музиківська',
                        "name_en": 'Muzykivska Hromada',
                    },
                    {
                        "uid": 1368,
                        "name": 'Олешківська',
                        "name_en": 'Oleshkivska Hromada',
                    },
                    {
                        "uid": 1369,
                        "name": 'Станіславська',
                        "name_en": 'Stanislavska Hromada',
                    },
                    {
                        "uid": 1370,
                        "name": 'м. Херсон та Херсонська',
                        "name_en": 'Kherson and Khersonska Hromada',
                    },
                    {
                        "uid": 1371,
                        "name": 'Чорнобаївська',
                        "name_en": 'Chornobaivska Hromada',
                    },
                    {
                        "uid": 1372,
                        "name": 'Ювілейна',
                        "name_en": 'Yuvileina Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 3,
        "name": 'Хмельницька область',
        "type": LocationType.OBLAST,
        "name_en": 'Khmelnytska Oblast',
        "districts": [
            {
                "uid": 135,
                "name": "Кам'янець-Подільський",
                "name_en": 'Kamianets-Podilskyi Raion',
                "hromadas": [
                    {
                        "uid": 1422,
                        "name": 'Гуківська',
                        "name_en": 'Hukivska Hromada',
                    },
                    {
                        "uid": 1423,
                        "name": 'Гуменецька',
                        "name_en": 'Humenetska Hromada',
                    },
                    {
                        "uid": 1424,
                        "name": 'Дунаєвецька',
                        "name_en": 'Dunaievetska Hromada',
                    },
                    {
                        "uid": 1425,
                        "name": 'Жванецька',
                        "name_en": 'Zhvanetska Hromada',
                    },
                    {
                        "uid": 1426,
                        "name": 'Закупненська',
                        "name_en": 'Zakupnenska Hromada',
                    },
                    {
                        "uid": 1427,
                        "name": "м. Кам'янець-Подільський та Кам'янець-Подільська",
                        "name_en": 'Kamianets-Podilskyi and Kamianets-Podilska Hromada',
                    },
                    {
                        "uid": 1428,
                        "name": 'Китайгородська',
                        "name_en": 'Kytaihorodska Hromada',
                    },
                    {
                        "uid": 1429,
                        "name": 'Маківська',
                        "name_en": 'Makivska Hromada',
                    },
                    {
                        "uid": 1430,
                        "name": 'Новодунаєвецька',
                        "name_en": 'Novodunaievetska Hromada',
                    },
                    {
                        "uid": 1431,
                        "name": 'Новоушицька',
                        "name_en": 'Novoushytska Hromada',
                    },
                    {
                        "uid": 1432,
                        "name": 'Орининська',
                        "name_en": 'Orynynska Hromada',
                    },
                    {
                        "uid": 1433,
                        "name": 'Слобідсько-Кульчієвецьк',
                        "name_en": 'Slobidsko-Kulchiievetsk Hromada',
                    },
                    {
                        "uid": 1434,
                        "name": 'Смотрицька',
                        "name_en": 'Smotrytska Hromada',
                    },
                    {
                        "uid": 1435,
                        "name": 'Староушицька',
                        "name_en": 'Staroushytska Hromada',
                    },
                    {
                        "uid": 1436,
                        "name": 'Чемеровецька',
                        "name_en": 'Chemerovetska Hromada',
                    },
                ],
            },
            {
                "uid": 134,
                "name": 'Хмельницький',
                "name_en": 'Khmelnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 1377,
                        "name": 'Антонінська',
                        "name_en": 'Antoninska Hromada',
                    },
                    {
                        "uid": 1380,
                        "name": 'Вовковинецька',
                        "name_en": 'Vovkovynetska Hromada',
                    },
                    {
                        "uid": 1381,
                        "name": 'Волочиська',
                        "name_en": 'Volochyska Hromada',
                    },
                    {
                        "uid": 1378,
                        "name": 'Війтовецька',
                        "name_en": 'Viitovetska Hromada',
                    },
                    {
                        "uid": 1379,
                        "name": 'Віньковецька',
                        "name_en": 'Vinkovetska Hromada',
                    },
                    {
                        "uid": 1382,
                        "name": 'Гвардійська',
                        "name_en": 'Hvardiiska Hromada',
                    },
                    {
                        "uid": 1383,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 1384,
                        "name": 'Деражнянська',
                        "name_en": 'Derazhnianska Hromada',
                    },
                    {
                        "uid": 1385,
                        "name": 'Заслучненська',
                        "name_en": 'Zasluchnenska Hromada',
                    },
                    {
                        "uid": 1386,
                        "name": 'Зіньківська',
                        "name_en": 'Zinkivska Hromada',
                    },
                    {
                        "uid": 1387,
                        "name": 'Красилівська',
                        "name_en": 'Krasylivska Hromada',
                    },
                    {
                        "uid": 1388,
                        "name": 'Летичівська',
                        "name_en": 'Letychivska Hromada',
                    },
                    {
                        "uid": 1389,
                        "name": 'Лісовогринівецька',
                        "name_en": 'Lisovohrynivetska Hromada',
                    },
                    {
                        "uid": 1390,
                        "name": 'Меджибізька',
                        "name_en": 'Medzhybizka Hromada',
                    },
                    {
                        "uid": 1391,
                        "name": 'Миролюбненська',
                        "name_en": 'Myroliubnenska Hromada',
                    },
                    {
                        "uid": 1392,
                        "name": 'Наркевицька',
                        "name_en": 'Narkevytska Hromada',
                    },
                    {
                        "uid": 1393,
                        "name": 'Розсошанська',
                        "name_en": 'Rozsoshanska Hromada',
                    },
                    {
                        "uid": 1394,
                        "name": 'Сатанівська',
                        "name_en": 'Satanivska Hromada',
                    },
                    {
                        "uid": 1395,
                        "name": 'Солобковецька',
                        "name_en": 'Solobkovetska Hromada',
                    },
                    {
                        "uid": 1396,
                        "name": 'м. Старокостянтинів та Старокостянтинівська',
                        "name_en": 'Starokostiantyniv and Starokostiantynivska Hromada',
                    },
                    {
                        "uid": 1397,
                        "name": 'Староостропільська',
                        "name_en": 'Staroostropilska Hromada',
                    },
                    {
                        "uid": 1398,
                        "name": 'Старосинявська',
                        "name_en": 'Starosyniavska Hromada',
                    },
                    {
                        "uid": 1399,
                        "name": 'Теофіпольська',
                        "name_en": 'Teofipolska Hromada',
                    },
                    {
                        "uid": 1400,
                        "name": 'м. Хмельницький та Хмельницька',
                        "name_en": 'Khmelnytskyi and Khmelnytska Hromada',
                    },
                    {
                        "uid": 1401,
                        "name": 'Чорноострівська',
                        "name_en": 'Chornoostrivska Hromada',
                    },
                    {
                        "uid": 1402,
                        "name": 'Щиборівська',
                        "name_en": 'Shchyborivska Hromada',
                    },
                    {
                        "uid": 1403,
                        "name": 'Ярмолинецька',
                        "name_en": 'Yarmolynetska Hromada',
                    },
                ],
            },
            {
                "uid": 136,
                "name": 'Шепетівський',
                "name_en": 'Shepetivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1404,
                        "name": 'Берездівська',
                        "name_en": 'Berezdivska Hromada',
                    },
                    {
                        "uid": 1405,
                        "name": 'Білогірська',
                        "name_en": 'Bilohirska Hromada',
                    },
                    {
                        "uid": 1406,
                        "name": 'Ганнопільська',
                        "name_en": 'Hannopilska Hromada',
                    },
                    {
                        "uid": 1407,
                        "name": 'Грицівська',
                        "name_en": 'Hrytsivska Hromada',
                    },
                    {
                        "uid": 1409,
                        "name": 'Крупецька',
                        "name_en": 'Krupetska Hromada',
                    },
                    {
                        "uid": 1410,
                        "name": 'Ленковецька',
                        "name_en": 'Lenkovetska Hromada',
                    },
                    {
                        "uid": 1411,
                        "name": 'Михайлюцька',
                        "name_en": 'Mykhailiutska Hromada',
                    },
                    {
                        "uid": 1412,
                        "name": 'м. Нетішин та Нетішинська',
                        "name_en": 'Netishyn and Netishynska Hromada',
                    },
                    {
                        "uid": 1413,
                        "name": 'Плужненська',
                        "name_en": 'Pluzhnenska Hromada',
                    },
                    {
                        "uid": 1414,
                        "name": 'Полонська',
                        "name_en": 'Polonska Hromada',
                    },
                    {
                        "uid": 1415,
                        "name": 'Понінківська',
                        "name_en": 'Poninkivska Hromada',
                    },
                    {
                        "uid": 1416,
                        "name": 'Сахновецька',
                        "name_en": 'Sakhnovetska Hromada',
                    },
                    {
                        "uid": 1417,
                        "name": 'м. Славута та Славутська',
                        "name_en": 'Slavuta and Slavutska Hromada',
                    },
                    {
                        "uid": 1418,
                        "name": 'Судилківська',
                        "name_en": 'Sudylkivska Hromada',
                    },
                    {
                        "uid": 1419,
                        "name": 'Улашанівська',
                        "name_en": 'Ulashanivska Hromada',
                    },
                    {
                        "uid": 1420,
                        "name": 'м. Шепетівка та Шепетівська',
                        "name_en": 'Shepetivka and Shepetivska Hromada',
                    },
                    {
                        "uid": 1421,
                        "name": 'Ямпільська',
                        "name_en": 'Yampilska Hromada',
                    },
                    {
                        "uid": 1408,
                        "name": 'Ізяславська',
                        "name_en": 'Iziaslavska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 24,
        "name": 'Черкаська область',
        "type": LocationType.OBLAST,
        "name_en": 'Cherkaska Oblast',
        "districts": [
            {
                "uid": 150,
                "name": 'Звенигородський',
                "name_en": 'Zvenyhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 1475,
                        "name": 'Бужанська',
                        "name_en": 'Buzhanska Hromada',
                    },
                    {
                        "uid": 1476,
                        "name": 'м. Ватутіне та Ватутінська',
                        "name_en": 'Vatutine and Vatutinska Hromada',
                    },
                    {
                        "uid": 1477,
                        "name": 'Виноградська',
                        "name_en": 'Vynohradska Hromada',
                    },
                    {
                        "uid": 1479,
                        "name": 'Водяницька',
                        "name_en": 'Vodianytska Hromada',
                    },
                    {
                        "uid": 1478,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 1481,
                        "name": 'Звенигородська',
                        "name_en": 'Zvenyhorodska Hromada',
                    },
                    {
                        "uid": 1482,
                        "name": 'Катеринопільська',
                        "name_en": 'Katerynopilska Hromada',
                    },
                    {
                        "uid": 1483,
                        "name": "Лип'янська",
                        "name_en": 'Lypianska Hromada',
                    },
                    {
                        "uid": 1484,
                        "name": 'Лисянська',
                        "name_en": 'Lysianska Hromada',
                    },
                    {
                        "uid": 1485,
                        "name": 'Матусівська',
                        "name_en": 'Matusivska Hromada',
                    },
                    {
                        "uid": 1486,
                        "name": 'Мокрокалигірська',
                        "name_en": 'Mokrokalyhirska Hromada',
                    },
                    {
                        "uid": 1487,
                        "name": 'Селищенська',
                        "name_en": 'Selyshchenska Hromada',
                    },
                    {
                        "uid": 1488,
                        "name": 'Стеблівська',
                        "name_en": 'Steblivska Hromada',
                    },
                    {
                        "uid": 1489,
                        "name": 'м. Тальне та Тальнівська',
                        "name_en": 'Talne and Talnivska Hromada',
                    },
                    {
                        "uid": 1490,
                        "name": 'Шевченківська',
                        "name_en": 'Shevchenkivska Hromada',
                    },
                    {
                        "uid": 1491,
                        "name": 'м. Шпола та Шполянська',
                        "name_en": 'Shpola and Shpolianska Hromada',
                    },
                    {
                        "uid": 1480,
                        "name": 'Єрківська',
                        "name_en": 'Yerkivska Hromada',
                    },
                ],
            },
            {
                "uid": 153,
                "name": 'Золотоніський',
                "name_en": 'Zolotoniskyi Raion',
                "hromadas": [
                    {
                        "uid": 1492,
                        "name": 'Великохутірська',
                        "name_en": 'Velykokhutirska Hromada',
                    },
                    {
                        "uid": 1493,
                        "name": 'Вознесенська',
                        "name_en": 'Voznesenska Hromada',
                    },
                    {
                        "uid": 1494,
                        "name": 'Гельмязівська',
                        "name_en": 'Helmiazivska Hromada',
                    },
                    {
                        "uid": 1495,
                        "name": 'Драбівська',
                        "name_en": 'Drabivska Hromada',
                    },
                    {
                        "uid": 1496,
                        "name": 'Золотоніська',
                        "name_en": 'Zolotoniska Hromada',
                    },
                    {
                        "uid": 1497,
                        "name": 'Зорівська',
                        "name_en": 'Zorivska Hromada',
                    },
                    {
                        "uid": 1499,
                        "name": 'Новодмитрівська',
                        "name_en": 'Novodmytrivska Hromada',
                    },
                    {
                        "uid": 1500,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 1501,
                        "name": 'Чорнобаївська',
                        "name_en": 'Chornobaivska Hromada',
                    },
                    {
                        "uid": 1502,
                        "name": 'Шрамківська',
                        "name_en": 'Shramkivska Hromada',
                    },
                    {
                        "uid": 1498,
                        "name": 'Іркліївська',
                        "name_en": 'Irkliivska Hromada',
                    },
                ],
            },
            {
                "uid": 151,
                "name": 'Уманський',
                "name_en": 'Umanskyi Raion',
                "hromadas": [
                    {
                        "uid": 1437,
                        "name": 'Бабанська',
                        "name_en": 'Babanska Hromada',
                    },
                    {
                        "uid": 1438,
                        "name": 'Баштечківська',
                        "name_en": 'Bashtechkivska Hromada',
                    },
                    {
                        "uid": 1439,
                        "name": 'Буцька',
                        "name_en": 'Butska Hromada',
                    },
                    {
                        "uid": 1440,
                        "name": 'Дмитрушківська',
                        "name_en": 'Dmytrushkivska Hromada',
                    },
                    {
                        "uid": 1441,
                        "name": 'Жашківська',
                        "name_en": 'Zhashkivska Hromada',
                    },
                    {
                        "uid": 1443,
                        "name": 'Ладижинська',
                        "name_en": 'Ladyzhynska Hromada',
                    },
                    {
                        "uid": 1444,
                        "name": 'Маньківська',
                        "name_en": 'Mankivska Hromada',
                    },
                    {
                        "uid": 1445,
                        "name": 'м. Монастирище та Монастрищенська',
                        "name_en": 'Monastyryshche and Monastryshchenska Hromada',
                    },
                    {
                        "uid": 1446,
                        "name": 'Паланська',
                        "name_en": 'Palanska Hromada',
                    },
                    {
                        "uid": 1447,
                        "name": 'Уманська',
                        "name_en": 'Umanska Hromada',
                    },
                    {
                        "uid": 1448,
                        "name": 'м. Христинівка та Христинівська',
                        "name_en": 'Khrystynivka and Khrystynivska Hromada',
                    },
                    {
                        "uid": 1442,
                        "name": 'Іваньківська',
                        "name_en": 'Ivankivska Hromada',
                    },
                ],
            },
            {
                "uid": 152,
                "name": 'Черкаський',
                "name_en": 'Cherkaskyi Raion',
                "hromadas": [
                    {
                        "uid": 1449,
                        "name": 'Балаклеївська',
                        "name_en": 'Balakleivska Hromada',
                    },
                    {
                        "uid": 1450,
                        "name": 'Березняківська',
                        "name_en": 'Berezniakivska Hromada',
                    },
                    {
                        "uid": 1452,
                        "name": 'Бобрицька',
                        "name_en": 'Bobrytska Hromada',
                    },
                    {
                        "uid": 1453,
                        "name": 'Будищенська',
                        "name_en": 'Budyshchenska Hromada',
                    },
                    {
                        "uid": 1451,
                        "name": 'Білозірська',
                        "name_en": 'Bilozirska Hromada',
                    },
                    {
                        "uid": 1454,
                        "name": 'Городищенська',
                        "name_en": 'Horodyshchenska Hromada',
                    },
                    {
                        "uid": 1455,
                        "name": 'Кам’янська',
                        "name_en": 'Kamyanska Hromada',
                    },
                    {
                        "uid": 1456,
                        "name": 'Канівська',
                        "name_en": 'Kanivska Hromada',
                    },
                    {
                        "uid": 1457,
                        "name": 'м. Корсунь-Шевченківський та Корсунь-Шевченківська',
                        "name_en": 'Korsun-Shevchenkivskyi and Korsun-Shevchenkivska Hromada',
                    },
                    {
                        "uid": 1458,
                        "name": 'Леськівська',
                        "name_en": 'Leskivska Hromada',
                    },
                    {
                        "uid": 1459,
                        "name": 'Ліплявська',
                        "name_en": 'Lipliavska Hromada',
                    },
                    {
                        "uid": 1460,
                        "name": 'Медведівська',
                        "name_en": 'Medvedivska Hromada',
                    },
                    {
                        "uid": 1461,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 1462,
                        "name": 'Мліївська',
                        "name_en": 'Mliivska Hromada',
                    },
                    {
                        "uid": 1463,
                        "name": 'Мошнівська',
                        "name_en": 'Moshnivska Hromada',
                    },
                    {
                        "uid": 1464,
                        "name": 'Набутівська',
                        "name_en": 'Nabutivska Hromada',
                    },
                    {
                        "uid": 1465,
                        "name": 'Ротмістрівська',
                        "name_en": 'Rotmistrivska Hromada',
                    },
                    {
                        "uid": 1466,
                        "name": 'Русько-Полянська',
                        "name_en": 'Rusko-Polianska Hromada',
                    },
                    {
                        "uid": 1467,
                        "name": 'Сагунівська',
                        "name_en": 'Sahunivska Hromada',
                    },
                    {
                        "uid": 1468,
                        "name": 'Смілянська',
                        "name_en": 'Smilianska Hromada',
                    },
                    {
                        "uid": 1469,
                        "name": 'Степанецька',
                        "name_en": 'Stepanetska Hromada',
                    },
                    {
                        "uid": 1470,
                        "name": 'Степанківська',
                        "name_en": 'Stepankivska Hromada',
                    },
                    {
                        "uid": 1471,
                        "name": 'Тернівська',
                        "name_en": 'Ternivska Hromada',
                    },
                    {
                        "uid": 1472,
                        "name": 'Червонослобідська',
                        "name_en": 'Chervonoslobidska Hromada',
                    },
                    {
                        "uid": 1473,
                        "name": 'м. Черкаси та Черкаська',
                        "name_en": 'Cherkasy and Cherkaska Hromada',
                    },
                    {
                        "uid": 1474,
                        "name": 'м. Чигирин та Чигиринська',
                        "name_en": 'Chyhyryn and Chyhyrynska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 26,
        "name": 'Чернівецька область',
        "type": LocationType.OBLAST,
        "name_en": 'Chernivetska Oblast',
        "districts": [
            {
                "uid": 138,
                "name": 'Вижницький',
                "name_en": 'Vyzhnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 1503,
                        "name": 'Банилівська',
                        "name_en": 'Banylivska Hromada',
                    },
                    {
                        "uid": 1504,
                        "name": 'Берегометська',
                        "name_en": 'Berehometska Hromada',
                    },
                    {
                        "uid": 1505,
                        "name": 'Брусницька',
                        "name_en": 'Brusnytska Hromada',
                    },
                    {
                        "uid": 1506,
                        "name": 'Вашківецька',
                        "name_en": 'Vashkivetska Hromada',
                    },
                    {
                        "uid": 1507,
                        "name": 'Вижницька',
                        "name_en": 'Vyzhnytska Hromada',
                    },
                    {
                        "uid": 1508,
                        "name": 'Конятинська',
                        "name_en": 'Koniatynska Hromada',
                    },
                    {
                        "uid": 1509,
                        "name": 'Путильська',
                        "name_en": 'Putylska Hromada',
                    },
                    {
                        "uid": 1510,
                        "name": 'Селятинська',
                        "name_en": 'Seliatynska Hromada',
                    },
                    {
                        "uid": 1511,
                        "name": 'Усть-Путильська',
                        "name_en": 'Ust-Putylska Hromada',
                    },
                ],
            },
            {
                "uid": 139,
                "name": 'Дністровський',
                "name_en": 'Dnistrovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1545,
                        "name": 'Вашковецька',
                        "name_en": 'Vashkovetska Hromada',
                    },
                    {
                        "uid": 1546,
                        "name": 'Кельменецька',
                        "name_en": 'Kelmenetska Hromada',
                    },
                    {
                        "uid": 1547,
                        "name": 'Клішковецька',
                        "name_en": 'Klishkovetska Hromada',
                    },
                    {
                        "uid": 1548,
                        "name": 'Лівинецька',
                        "name_en": 'Livynetska Hromada',
                    },
                    {
                        "uid": 1549,
                        "name": 'Мамалигівська',
                        "name_en": 'Mamalyhivska Hromada',
                    },
                    {
                        "uid": 1550,
                        "name": 'Недобоївська',
                        "name_en": 'Nedoboivska Hromada',
                    },
                    {
                        "uid": 1551,
                        "name": 'м. Новодністровськ та Новодністровська',
                        "name_en": 'Novodnistrovsk and Novodnistrovska Hromada',
                    },
                    {
                        "uid": 1552,
                        "name": 'Рукшинська',
                        "name_en": 'Rukshynska Hromada',
                    },
                    {
                        "uid": 1553,
                        "name": 'Сокирянська',
                        "name_en": 'Sokyrianska Hromada',
                    },
                    {
                        "uid": 1554,
                        "name": 'Хотинська',
                        "name_en": 'Khotynska Hromada',
                    },
                ],
            },
            {
                "uid": 137,
                "name": 'Чернівецький',
                "name_en": 'Chernivetskyi Raion',
                "hromadas": [
                    {
                        "uid": 1512,
                        "name": 'Боянська',
                        "name_en": 'Boianska Hromada',
                    },
                    {
                        "uid": 1513,
                        "name": 'Ванчиковецька',
                        "name_en": 'Vanchykovetska Hromada',
                    },
                    {
                        "uid": 1514,
                        "name": 'Великокучурівська',
                        "name_en": 'Velykokuchurivska Hromada',
                    },
                    {
                        "uid": 1515,
                        "name": 'Веренчацька',
                        "name_en": 'Verenchatska Hromada',
                    },
                    {
                        "uid": 1517,
                        "name": 'Волоківська',
                        "name_en": 'Volokivska Hromada',
                    },
                    {
                        "uid": 1516,
                        "name": 'Вікнянська',
                        "name_en": 'Viknianska Hromada',
                    },
                    {
                        "uid": 1518,
                        "name": 'Герцаївська',
                        "name_en": 'Hertsaivska Hromada',
                    },
                    {
                        "uid": 1519,
                        "name": 'Глибоцька',
                        "name_en": 'Hlybotska Hromada',
                    },
                    {
                        "uid": 1520,
                        "name": 'Горішньошеровецька',
                        "name_en": 'Horishnosherovetska Hromada',
                    },
                    {
                        "uid": 1521,
                        "name": 'Заставнівська',
                        "name_en": 'Zastavnivska Hromada',
                    },
                    {
                        "uid": 1522,
                        "name": 'Кадубовецька',
                        "name_en": 'Kadubovetska Hromada',
                    },
                    {
                        "uid": 1523,
                        "name": "Кам'янецька",
                        "name_en": 'Kamianetska Hromada',
                    },
                    {
                        "uid": 1524,
                        "name": "Кам'янська",
                        "name_en": 'Kamianska Hromada',
                    },
                    {
                        "uid": 1525,
                        "name": 'Карапачівська',
                        "name_en": 'Karapachivska Hromada',
                    },
                    {
                        "uid": 1527,
                        "name": 'Кострижівська',
                        "name_en": 'Kostryzhivska Hromada',
                    },
                    {
                        "uid": 1528,
                        "name": 'Красноїльська',
                        "name_en": 'Krasnoilska Hromada',
                    },
                    {
                        "uid": 1526,
                        "name": 'Кіцманська',
                        "name_en": 'Kitsmanska Hromada',
                    },
                    {
                        "uid": 1529,
                        "name": 'Магальська',
                        "name_en": 'Mahalska Hromada',
                    },
                    {
                        "uid": 1530,
                        "name": 'Мамаївська',
                        "name_en": 'Mamaivska Hromada',
                    },
                    {
                        "uid": 1531,
                        "name": 'Неполоковецька',
                        "name_en": 'Nepolokovetska Hromada',
                    },
                    {
                        "uid": 1532,
                        "name": 'Новоселицька',
                        "name_en": 'Novoselytska Hromada',
                    },
                    {
                        "uid": 1533,
                        "name": 'Острицька',
                        "name_en": 'Ostrytska Hromada',
                    },
                    {
                        "uid": 1534,
                        "name": 'Петровецька',
                        "name_en": 'Petrovetska Hromada',
                    },
                    {
                        "uid": 1535,
                        "name": 'Ставчанська',
                        "name_en": 'Stavchanska Hromada',
                    },
                    {
                        "uid": 1536,
                        "name": 'Сторожинецька',
                        "name_en": 'Storozhynetska Hromada',
                    },
                    {
                        "uid": 1537,
                        "name": 'Сучевенська',
                        "name_en": 'Suchevenska Hromada',
                    },
                    {
                        "uid": 1538,
                        "name": 'Тарашанська',
                        "name_en": 'Tarashanska Hromada',
                    },
                    {
                        "uid": 1539,
                        "name": 'Тереблеченська',
                        "name_en": 'Tereblechenska Hromada',
                    },
                    {
                        "uid": 1540,
                        "name": 'Топорівська',
                        "name_en": 'Toporivska Hromada',
                    },
                    {
                        "uid": 1541,
                        "name": 'Чагорська',
                        "name_en": 'Chahorska Hromada',
                    },
                    {
                        "uid": 1542,
                        "name": 'м. Чернівці та Чернівецька',
                        "name_en": 'Chernivtsi and Chernivetska Hromada',
                    },
                    {
                        "uid": 1543,
                        "name": 'Чудейська',
                        "name_en": 'Chudeiska Hromada',
                    },
                    {
                        "uid": 1544,
                        "name": 'Юрковецька',
                        "name_en": 'Yurkovetska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 25,
        "name": 'Чернігівська область',
        "type": LocationType.OBLAST,
        "name_en": 'Chernihivska Oblast',
        "districts": [
            {
                "uid": 144,
                "name": 'Корюківський',
                "name_en": 'Koriukivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1607,
                        "name": 'Корюківська',
                        "name_en": 'Koriukivska Hromada',
                    },
                    {
                        "uid": 1608,
                        "name": 'Менська',
                        "name_en": 'Menska Hromada',
                    },
                    {
                        "uid": 1609,
                        "name": 'Сновська',
                        "name_en": 'Snovska Hromada',
                    },
                    {
                        "uid": 1610,
                        "name": 'Сосницька',
                        "name_en": 'Sosnytska Hromada',
                    },
                    {
                        "uid": 1611,
                        "name": 'Холминська',
                        "name_en": 'Kholmynska Hromada',
                    },
                ],
            },
            {
                "uid": 141,
                "name": 'Новгород-Сіверський',
                "name_en": 'Novhorod-Siverskyi Raion',
                "hromadas": [
                    {
                        "uid": 1603,
                        "name": 'Коропська',
                        "name_en": 'Koropska Hromada',
                    },
                    {
                        "uid": 1604,
                        "name": 'м. Новгород-Сіверський та Новгород-Сіверська',
                        "name_en": 'Novhorod-Siverskyi and Novhorod-Siverska Hromada',
                    },
                    {
                        "uid": 1605,
                        "name": 'Понорницька',
                        "name_en": 'Ponornytska Hromada',
                    },
                    {
                        "uid": 1606,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska Hromada',
                    },
                ],
            },
            {
                "uid": 142,
                "name": 'Ніжинський',
                "name_en": 'Nizhynskyi Raion',
                "hromadas": [
                    {
                        "uid": 1555,
                        "name": 'Батуринська',
                        "name_en": 'Baturynska Hromada',
                    },
                    {
                        "uid": 1556,
                        "name": 'Бахмацька',
                        "name_en": 'Bakhmatska Hromada',
                    },
                    {
                        "uid": 1557,
                        "name": 'Бобровицька',
                        "name_en": 'Bobrovytska Hromada',
                    },
                    {
                        "uid": 1558,
                        "name": 'Борзнянська',
                        "name_en": 'Borznianska Hromada',
                    },
                    {
                        "uid": 1559,
                        "name": 'Вертіївська',
                        "name_en": 'Vertiivska Hromada',
                    },
                    {
                        "uid": 1560,
                        "name": 'Височанська',
                        "name_en": 'Vysochanska Hromada',
                    },
                    {
                        "uid": 1561,
                        "name": 'Дмитрівська',
                        "name_en": 'Dmytrivska Hromada',
                    },
                    {
                        "uid": 1562,
                        "name": 'Комарівська',
                        "name_en": 'Komarivska Hromada',
                    },
                    {
                        "uid": 1563,
                        "name": 'Крутівська',
                        "name_en": 'Krutivska Hromada',
                    },
                    {
                        "uid": 1564,
                        "name": 'Лосинівська',
                        "name_en": 'Losynivska Hromada',
                    },
                    {
                        "uid": 1565,
                        "name": 'Макіївська',
                        "name_en": 'Makiivska Hromada',
                    },
                    {
                        "uid": 1566,
                        "name": 'Мринська',
                        "name_en": 'Mrynska Hromada',
                    },
                    {
                        "uid": 1568,
                        "name": 'Новобасанська',
                        "name_en": 'Novobasanska Hromada',
                    },
                    {
                        "uid": 1569,
                        "name": 'Носівська',
                        "name_en": 'Nosivska Hromada',
                    },
                    {
                        "uid": 1567,
                        "name": 'м. Ніжин та Ніжинська',
                        "name_en": 'Nizhyn and Nizhynska Hromada',
                    },
                    {
                        "uid": 1570,
                        "name": 'Плисківська',
                        "name_en": 'Plyskivska Hromada',
                    },
                    {
                        "uid": 1571,
                        "name": 'Талалаївська',
                        "name_en": 'Talalaivska Hromada',
                    },
                ],
            },
            {
                "uid": 143,
                "name": 'Прилуцький',
                "name_en": 'Prylutskyi Raion',
                "hromadas": [
                    {
                        "uid": 1592,
                        "name": 'Варвинська',
                        "name_en": 'Varvynska Hromada',
                    },
                    {
                        "uid": 1594,
                        "name": 'Ладанська',
                        "name_en": 'Ladanska Hromada',
                    },
                    {
                        "uid": 1595,
                        "name": 'Линовицька',
                        "name_en": 'Lynovytska Hromada',
                    },
                    {
                        "uid": 1596,
                        "name": 'Малодівицька',
                        "name_en": 'Malodivytska Hromada',
                    },
                    {
                        "uid": 1597,
                        "name": 'Парафіївська',
                        "name_en": 'Parafiivska Hromada',
                    },
                    {
                        "uid": 1598,
                        "name": 'м. Прилуки та Прилуцька',
                        "name_en": 'Pryluky and Prylutska Hromada',
                    },
                    {
                        "uid": 1599,
                        "name": 'Срібнянська',
                        "name_en": 'Sribnianska Hromada',
                    },
                    {
                        "uid": 1600,
                        "name": "Сухополов'янська",
                        "name_en": 'Sukhopolovianska Hromada',
                    },
                    {
                        "uid": 1601,
                        "name": 'Талалаївська',
                        "name_en": 'Talalaivska Hromada',
                    },
                    {
                        "uid": 1602,
                        "name": 'Яблунівська',
                        "name_en": 'Yablunivska Hromada',
                    },
                    {
                        "uid": 1593,
                        "name": 'Ічнянська',
                        "name_en": 'Ichnianska Hromada',
                    },
                ],
            },
            {
                "uid": 140,
                "name": 'Чернігівський',
                "name_en": 'Chernihivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1572,
                        "name": 'Березнянська',
                        "name_en": 'Bereznianska Hromada',
                    },
                    {
                        "uid": 1573,
                        "name": 'Гончарівська',
                        "name_en": 'Honcharivska Hromada',
                    },
                    {
                        "uid": 1574,
                        "name": 'Городнянська',
                        "name_en": 'Horodnianska Hromada',
                    },
                    {
                        "uid": 1575,
                        "name": 'Деснянська',
                        "name_en": 'Desnianska Hromada',
                    },
                    {
                        "uid": 1576,
                        "name": 'Добрянська',
                        "name_en": 'Dobrianska Hromada',
                    },
                    {
                        "uid": 1579,
                        "name": 'Киселівська',
                        "name_en": 'Kyselivska Hromada',
                    },
                    {
                        "uid": 1578,
                        "name": 'Киїнська',
                        "name_en": 'Kyinska Hromada',
                    },
                    {
                        "uid": 1581,
                        "name": 'Козелецька',
                        "name_en": 'Kozeletska Hromada',
                    },
                    {
                        "uid": 1582,
                        "name": 'Куликівська',
                        "name_en": 'Kulykivska Hromada',
                    },
                    {
                        "uid": 1580,
                        "name": 'Кіптівська',
                        "name_en": 'Kiptivska Hromada',
                    },
                    {
                        "uid": 1583,
                        "name": 'Любецька',
                        "name_en": 'Liubetska Hromada',
                    },
                    {
                        "uid": 1584,
                        "name": 'Михайло-Коцюбинська',
                        "name_en": 'Mykhailo-Kotsiubynska Hromada',
                    },
                    {
                        "uid": 1585,
                        "name": 'Новобілоуська',
                        "name_en": 'Novobilouska Hromada',
                    },
                    {
                        "uid": 1586,
                        "name": 'Олишівська',
                        "name_en": 'Olyshivska Hromada',
                    },
                    {
                        "uid": 1587,
                        "name": 'Остерська',
                        "name_en": 'Osterska Hromada',
                    },
                    {
                        "uid": 1588,
                        "name": 'Ріпкинська',
                        "name_en": 'Ripkynska Hromada',
                    },
                    {
                        "uid": 1589,
                        "name": 'Седнівська',
                        "name_en": 'Sednivska Hromada',
                    },
                    {
                        "uid": 1590,
                        "name": 'Тупичівська',
                        "name_en": 'Tupychivska Hromada',
                    },
                    {
                        "uid": 1591,
                        "name": 'м. Чернігів та Чернігівська',
                        "name_en": 'Chernihiv and Chernihivska Hromada',
                    },
                    {
                        "uid": 1577,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
        ],
    },
    {
        "uid": 13,
        "name": 'Івано-Франківська область',
        "type": LocationType.OBLAST,
        "name_en": 'Ivano-Frankivska Oblast',
        "districts": [
            {
                "uid": 67,
                "name": 'Верховинський',
                "name_en": 'Verkhovynskyi Raion',
                "hromadas": [
                    {
                        "uid": 620,
                        "name": 'Білоберізька',
                        "name_en": 'Biloberizka Hromada',
                    },
                    {
                        "uid": 621,
                        "name": 'Верховинська',
                        "name_en": 'Verkhovynska Hromada',
                    },
                    {
                        "uid": 622,
                        "name": 'Зеленська',
                        "name_en": 'Zelenska Hromada',
                    },
                ],
            },
            {
                "uid": 71,
                "name": 'Калуський',
                "name_en": 'Kaluskyi Raion',
                "hromadas": [
                    {
                        "uid": 643,
                        "name": 'м. Болехів та Болехівська',
                        "name_en": 'Bolekhiv and Bolekhivska Hromada',
                    },
                    {
                        "uid": 644,
                        "name": 'Брошнів-Осадська',
                        "name_en": 'Broshniv-Osadska Hromada',
                    },
                    {
                        "uid": 645,
                        "name": 'Верхнянська',
                        "name_en": 'Verkhnianska Hromada',
                    },
                    {
                        "uid": 646,
                        "name": 'Вигодська',
                        "name_en": 'Vyhodska Hromada',
                    },
                    {
                        "uid": 647,
                        "name": 'Витвицька',
                        "name_en": 'Vytvytska Hromada',
                    },
                    {
                        "uid": 648,
                        "name": 'Войнилівська',
                        "name_en": 'Voinylivska Hromada',
                    },
                    {
                        "uid": 649,
                        "name": 'м. Долина та Долинська',
                        "name_en": 'Dolyna and Dolynska Hromada',
                    },
                    {
                        "uid": 650,
                        "name": 'Дубівська',
                        "name_en": 'Dubivska Hromada',
                    },
                    {
                        "uid": 651,
                        "name": 'м. Калуш та Калуська',
                        "name_en": 'Kalush and Kaluska Hromada',
                    },
                    {
                        "uid": 652,
                        "name": 'Новицька',
                        "name_en": 'Novytska Hromada',
                    },
                    {
                        "uid": 653,
                        "name": 'Перегінська',
                        "name_en": 'Perehinska Hromada',
                    },
                    {
                        "uid": 654,
                        "name": 'Рожнятівська',
                        "name_en": 'Rozhniativska Hromada',
                    },
                    {
                        "uid": 655,
                        "name": 'Спаська',
                        "name_en": 'Spaska Hromada',
                    },
                ],
            },
            {
                "uid": 70,
                "name": 'Коломийський',
                "name_en": 'Kolomyiskyi Raion',
                "hromadas": [
                    {
                        "uid": 664,
                        "name": 'Гвіздецька',
                        "name_en": 'Hvizdetska Hromada',
                    },
                    {
                        "uid": 665,
                        "name": 'Городенківська',
                        "name_en": 'Horodenkivska Hromada',
                    },
                    {
                        "uid": 666,
                        "name": 'Заболотівська',
                        "name_en": 'Zabolotivska Hromada',
                    },
                    {
                        "uid": 667,
                        "name": 'м. Коломия та Коломийська',
                        "name_en": 'Kolomyia and Kolomyiska Hromada',
                    },
                    {
                        "uid": 668,
                        "name": 'Коршівська',
                        "name_en": 'Korshivska Hromada',
                    },
                    {
                        "uid": 669,
                        "name": 'Матеївецька',
                        "name_en": 'Mateivetska Hromada',
                    },
                    {
                        "uid": 670,
                        "name": 'Нижньовербізька',
                        "name_en": 'Nyzhnoverbizka Hromada',
                    },
                    {
                        "uid": 671,
                        "name": 'Отинійська',
                        "name_en": 'Otyniiska Hromada',
                    },
                    {
                        "uid": 674,
                        "name": "П'ядицька",
                        "name_en": 'Piadytska Hromada',
                    },
                    {
                        "uid": 672,
                        "name": 'Печеніжинська',
                        "name_en": 'Pechenizhynska Hromada',
                    },
                    {
                        "uid": 673,
                        "name": 'Підгайчиківська',
                        "name_en": 'Pidhaichykivska Hromada',
                    },
                    {
                        "uid": 675,
                        "name": 'Снятинська',
                        "name_en": 'Sniatynska Hromada',
                    },
                    {
                        "uid": 676,
                        "name": 'Чернелицька',
                        "name_en": 'Chernelytska Hromada',
                    },
                ],
            },
            {
                "uid": 69,
                "name": 'Косівський',
                "name_en": 'Kosivskyi Raion',
                "hromadas": [
                    {
                        "uid": 678,
                        "name": 'Космацька',
                        "name_en": 'Kosmatska Hromada',
                    },
                    {
                        "uid": 677,
                        "name": 'Косівська',
                        "name_en": 'Kosivska Hromada',
                    },
                    {
                        "uid": 679,
                        "name": 'Кутська',
                        "name_en": 'Kutska Hromada',
                    },
                    {
                        "uid": 680,
                        "name": 'Рожнівська',
                        "name_en": 'Rozhnivska Hromada',
                    },
                    {
                        "uid": 681,
                        "name": 'Яблунівська',
                        "name_en": 'Yablunivska Hromada',
                    },
                ],
            },
            {
                "uid": 72,
                "name": 'Надвірнянський',
                "name_en": 'Nadvirnianskyi Raion',
                "hromadas": [
                    {
                        "uid": 656,
                        "name": 'Ворохтянська',
                        "name_en": 'Vorokhtianska Hromada',
                    },
                    {
                        "uid": 657,
                        "name": 'Делятинська',
                        "name_en": 'Deliatynska Hromada',
                    },
                    {
                        "uid": 658,
                        "name": 'Ланчинська',
                        "name_en": 'Lanchynska Hromada',
                    },
                    {
                        "uid": 659,
                        "name": 'м. Надвірна та Надвірнянська',
                        "name_en": 'Nadvirna and Nadvirnianska Hromada',
                    },
                    {
                        "uid": 660,
                        "name": 'Пасічнянська',
                        "name_en": 'Pasichnianska Hromada',
                    },
                    {
                        "uid": 661,
                        "name": 'Переріслянська',
                        "name_en": 'Pererislianska Hromada',
                    },
                    {
                        "uid": 662,
                        "name": 'Поляницька',
                        "name_en": 'Polianytska Hromada',
                    },
                    {
                        "uid": 663,
                        "name": 'м. Яремче та Яремчанська',
                        "name_en": 'Yaremche and Yaremchanska Hromada',
                    },
                ],
            },
            {
                "uid": 68,
                "name": 'Івано-Франківський',
                "name_en": 'Ivano-Frankivskyi Raion',
                "hromadas": [
                    {
                        "uid": 624,
                        "name": 'Богородчанська',
                        "name_en": 'Bohorodchanska Hromada',
                    },
                    {
                        "uid": 625,
                        "name": 'Букачівська',
                        "name_en": 'Bukachivska Hromada',
                    },
                    {
                        "uid": 626,
                        "name": 'м. Бурштин та Бурштинська',
                        "name_en": 'Burshtyn and Burshtynska Hromada',
                    },
                    {
                        "uid": 623,
                        "name": 'Більшівцівська',
                        "name_en": 'Bilshivtsivska Hromada',
                    },
                    {
                        "uid": 627,
                        "name": 'Галицька',
                        "name_en": 'Halytska Hromada',
                    },
                    {
                        "uid": 628,
                        "name": 'Дзвиняцька',
                        "name_en": 'Dzvyniatska Hromada',
                    },
                    {
                        "uid": 629,
                        "name": 'Дубовецька',
                        "name_en": 'Dubovetska Hromada',
                    },
                    {
                        "uid": 631,
                        "name": 'Загвіздянська',
                        "name_en": 'Zahvizdianska Hromada',
                    },
                    {
                        "uid": 633,
                        "name": 'Лисецька',
                        "name_en": 'Lysetska Hromada',
                    },
                    {
                        "uid": 634,
                        "name": 'Обертинська',
                        "name_en": 'Obertynska Hromada',
                    },
                    {
                        "uid": 635,
                        "name": 'Олешанська',
                        "name_en": 'Oleshanska Hromada',
                    },
                    {
                        "uid": 636,
                        "name": 'Рогатинська',
                        "name_en": 'Rohatynska Hromada',
                    },
                    {
                        "uid": 637,
                        "name": 'Солотвинська',
                        "name_en": 'Solotvynska Hromada',
                    },
                    {
                        "uid": 638,
                        "name": 'Старобогородчанська',
                        "name_en": 'Starobohorodchanska Hromada',
                    },
                    {
                        "uid": 639,
                        "name": 'Тисменицька',
                        "name_en": 'Tysmenytska Hromada',
                    },
                    {
                        "uid": 640,
                        "name": 'Тлумацька',
                        "name_en": 'Tlumatska Hromada',
                    },
                    {
                        "uid": 641,
                        "name": 'Угринівська',
                        "name_en": 'Uhrynivska Hromada',
                    },
                    {
                        "uid": 642,
                        "name": 'Ямницька',
                        "name_en": 'Yamnytska Hromada',
                    },
                    {
                        "uid": 630,
                        "name": 'Єзупільська',
                        "name_en": 'Yezupilska Hromada',
                    },
                    {
                        "uid": 632,
                        "name": 'м. Івано-Франківськ та Івано-Франківська',
                        "name_en": 'Ivano-Frankivsk and Ivano-Frankivska Hromada',
                    },
                ],
            },
        ],
    },
]
