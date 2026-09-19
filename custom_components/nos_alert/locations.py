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
                "name": 'Володимирський район',
                "name_en": 'Volodymyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 255,
                        "name": 'м. Володимир та Володимирська територіальна громада',
                        "name_en": 'Volodymyr and Volodymyrska Hromada',
                    },
                    {
                        "uid": 256,
                        "name": 'Затурцівська територіальна громада',
                        "name_en": 'Zaturtsivska Hromada',
                    },
                    {
                        "uid": 257,
                        "name": 'Зимнівська територіальна громада',
                        "name_en": 'Zymnivska Hromada',
                    },
                    {
                        "uid": 259,
                        "name": 'Литовезька територіальна громада',
                        "name_en": 'Lytovezka Hromada',
                    },
                    {
                        "uid": 260,
                        "name": 'Локачинська територіальна громада',
                        "name_en": 'Lokachynska Hromada',
                    },
                    {
                        "uid": 261,
                        "name": 'м. Нововолинськ та Нововолинська територіальна громада',
                        "name_en": 'Novovolynsk and Novovolynska Hromada',
                    },
                    {
                        "uid": 262,
                        "name": 'Оваднівська територіальна громада',
                        "name_en": 'Ovadnivska Hromada',
                    },
                    {
                        "uid": 263,
                        "name": 'Павлівська територіальна громада',
                        "name_en": 'Pavlivska Hromada',
                    },
                    {
                        "uid": 264,
                        "name": 'Поромівська територіальна громада',
                        "name_en": 'Poromivska Hromada',
                    },
                    {
                        "uid": 265,
                        "name": 'Устилузька територіальна громада',
                        "name_en": 'Ustyluzka Hromada',
                    },
                    {
                        "uid": 258,
                        "name": 'Іваничівська територіальна громада',
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
                "name": 'Камінь-Каширський район',
                "name_en": 'Kamin-Kashyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 266,
                        "name": 'Камінь-Каширська територіальна громада',
                        "name_en": 'Kamin-Kashyrska Hromada',
                    },
                    {
                        "uid": 267,
                        "name": 'Любешівська територіальна громада',
                        "name_en": 'Liubeshivska Hromada',
                    },
                    {
                        "uid": 268,
                        "name": 'Маневицька територіальна громада',
                        "name_en": 'Manevytska Hromada',
                    },
                    {
                        "uid": 269,
                        "name": 'Прилісненська територіальна громада',
                        "name_en": 'Prylisnenska Hromada',
                    },
                    {
                        "uid": 270,
                        "name": 'Сошичненська територіальна громада',
                        "name_en": 'Soshychnenska Hromada',
                    },
                ],
            },
            {
                "uid": 40,
                "name": 'Ковельський район',
                "name_en": 'Kovelskyi Raion',
                "hromadas": [
                    {
                        "uid": 232,
                        "name": 'Велимченська територіальна громада',
                        "name_en": 'Velymchenska Hromada',
                    },
                    {
                        "uid": 233,
                        "name": 'Велицька територіальна громада',
                        "name_en": 'Velytska Hromada',
                    },
                    {
                        "uid": 234,
                        "name": 'Вишнівська територіальна громада',
                        "name_en": 'Vyshnivska Hromada',
                    },
                    {
                        "uid": 235,
                        "name": 'Голобська територіальна громада',
                        "name_en": 'Holobska Hromada',
                    },
                    {
                        "uid": 236,
                        "name": 'Головненська територіальна громада',
                        "name_en": 'Holovnenska Hromada',
                    },
                    {
                        "uid": 237,
                        "name": 'Дубечненська територіальна громада',
                        "name_en": 'Dubechnenska Hromada',
                    },
                    {
                        "uid": 238,
                        "name": 'Дубівська територіальна громада',
                        "name_en": 'Dubivska Hromada',
                    },
                    {
                        "uid": 239,
                        "name": 'Заболоттівська територіальна громада',
                        "name_en": 'Zabolottivska Hromada',
                    },
                    {
                        "uid": 240,
                        "name": 'Забродівська територіальна громада',
                        "name_en": 'Zabrodivska Hromada',
                    },
                    {
                        "uid": 241,
                        "name": 'м. Ковель та Ковельська територіальна громада',
                        "name_en": 'Kovel and Kovelska Hromada',
                    },
                    {
                        "uid": 242,
                        "name": 'Колодяжненська територіальна громада',
                        "name_en": 'Kolodiazhnenska Hromada',
                    },
                    {
                        "uid": 243,
                        "name": 'Луківська територіальна громада',
                        "name_en": 'Lukivska Hromada',
                    },
                    {
                        "uid": 244,
                        "name": 'Люблинецька територіальна громада',
                        "name_en": 'Liublynetska Hromada',
                    },
                    {
                        "uid": 245,
                        "name": 'м. Любомиль та Любомльська територіальна громада',
                        "name_en": 'Liubomyl and Liubomlska Hromada',
                    },
                    {
                        "uid": 246,
                        "name": 'Поворська територіальна громада',
                        "name_en": 'Povorska Hromada',
                    },
                    {
                        "uid": 247,
                        "name": 'Ратнівська територіальна громада',
                        "name_en": 'Ratnivska Hromada',
                    },
                    {
                        "uid": 248,
                        "name": 'Рівненська територіальна громада',
                        "name_en": 'Rivnenska Hromada',
                    },
                    {
                        "uid": 249,
                        "name": 'Самарівська територіальна громада',
                        "name_en": 'Samarivska Hromada',
                    },
                    {
                        "uid": 250,
                        "name": 'Сереховичівська територіальна громада',
                        "name_en": 'Serekhovychivska Hromada',
                    },
                    {
                        "uid": 251,
                        "name": 'Смідинська територіальна громада',
                        "name_en": 'Smidynska Hromada',
                    },
                    {
                        "uid": 252,
                        "name": 'Старовижівська територіальна громада',
                        "name_en": 'Starovyzhivska Hromada',
                    },
                    {
                        "uid": 253,
                        "name": 'Турійська територіальна громада',
                        "name_en": 'Turiiska Hromada',
                    },
                    {
                        "uid": 254,
                        "name": 'м. Шацьк та Шацька територіальна громада',
                        "name_en": 'Shatsk and Shatska Hromada',
                    },
                ],
            },
            {
                "uid": 39,
                "name": 'Луцький район',
                "name_en": 'Lutskyi Raion',
                "hromadas": [
                    {
                        "uid": 217,
                        "name": 'Берестечківська територіальна громада',
                        "name_en": 'Berestechkivska Hromada',
                    },
                    {
                        "uid": 218,
                        "name": 'Боратинська територіальна громада',
                        "name_en": 'Boratynska Hromada',
                    },
                    {
                        "uid": 219,
                        "name": 'Городищенська територіальна громада',
                        "name_en": 'Horodyshchenska Hromada',
                    },
                    {
                        "uid": 220,
                        "name": 'Горохівська територіальна громада',
                        "name_en": 'Horokhivska Hromada',
                    },
                    {
                        "uid": 221,
                        "name": 'Доросинівська територіальна громада',
                        "name_en": 'Dorosynivska Hromada',
                    },
                    {
                        "uid": 223,
                        "name": 'Колківська територіальна громада',
                        "name_en": 'Kolkivska Hromada',
                    },
                    {
                        "uid": 224,
                        "name": 'Копачівська територіальна громада',
                        "name_en": 'Kopachivska Hromada',
                    },
                    {
                        "uid": 222,
                        "name": 'Ківерцівська територіальна громада',
                        "name_en": 'Kivertsivska Hromada',
                    },
                    {
                        "uid": 225,
                        "name": 'м. Луцьк та Луцька територіальна громада',
                        "name_en": 'Lutsk and Lutska Hromada',
                    },
                    {
                        "uid": 226,
                        "name": "Мар'янівська територіальна громада",
                        "name_en": 'Marianivska Hromada',
                    },
                    {
                        "uid": 227,
                        "name": 'Олицька територіальна громада',
                        "name_en": 'Olytska Hromada',
                    },
                    {
                        "uid": 228,
                        "name": 'Підгайцівська територіальна громада',
                        "name_en": 'Pidhaitsivska Hromada',
                    },
                    {
                        "uid": 229,
                        "name": 'Рожищенська територіальна громада',
                        "name_en": 'Rozhyshchenska Hromada',
                    },
                    {
                        "uid": 230,
                        "name": 'Торчинська територіальна громада',
                        "name_en": 'Torchynska Hromada',
                    },
                    {
                        "uid": 231,
                        "name": 'Цуманська територіальна громада',
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
                "name": 'Вінницький район',
                "name_en": 'Vinnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 154,
                        "name": 'Агрономічна територіальна громада',
                        "name_en": 'Ahronomichna Hromada',
                    },
                    {
                        "uid": 156,
                        "name": 'Вороновицька територіальна громада',
                        "name_en": 'Voronovytska Hromada',
                    },
                    {
                        "uid": 155,
                        "name": 'м. Вінниця та Вінницька територіальна громада',
                        "name_en": 'Vinnytsia and Vinnytska Hromada',
                    },
                    {
                        "uid": 157,
                        "name": 'Гніванська територіальна громада',
                        "name_en": 'Hnivanska Hromada',
                    },
                    {
                        "uid": 159,
                        "name": 'Липовецька територіальна громада',
                        "name_en": 'Lypovetska Hromada',
                    },
                    {
                        "uid": 161,
                        "name": 'Лука-Мелешківська територіальна громада',
                        "name_en": 'Luka-Meleshkivska Hromada',
                    },
                    {
                        "uid": 160,
                        "name": 'Літинська територіальна громада',
                        "name_en": 'Litynska Hromada',
                    },
                    {
                        "uid": 162,
                        "name": 'Немирівська територіальна громада',
                        "name_en": 'Nemyrivska Hromada',
                    },
                    {
                        "uid": 163,
                        "name": 'Оратівська територіальна громада',
                        "name_en": 'Orativska Hromada',
                    },
                    {
                        "uid": 164,
                        "name": 'Погребищенська територіальна громада',
                        "name_en": 'Pohrebyshchenska Hromada',
                    },
                    {
                        "uid": 165,
                        "name": 'Стрижавська територіальна громада',
                        "name_en": 'Stryzhavska Hromada',
                    },
                    {
                        "uid": 166,
                        "name": 'Сутисківська територіальна громада',
                        "name_en": 'Sutyskivska Hromada',
                    },
                    {
                        "uid": 167,
                        "name": 'Тиврівська територіальна громада',
                        "name_en": 'Tyvrivska Hromada',
                    },
                    {
                        "uid": 168,
                        "name": 'Турбівська територіальна громада',
                        "name_en": 'Turbivska Hromada',
                    },
                    {
                        "uid": 169,
                        "name": 'Якушинецька територіальна громада',
                        "name_en": 'Yakushynetska Hromada',
                    },
                    {
                        "uid": 158,
                        "name": 'Іллінецька територіальна громада',
                        "name_en": 'Illinetska Hromada',
                    },
                ],
            },
            {
                "uid": 37,
                "name": 'Гайсинський район',
                "name_en": 'Haisynskyi Raion',
                "hromadas": [
                    {
                        "uid": 185,
                        "name": 'Бершадська територіальна громада',
                        "name_en": 'Bershadska Hromada',
                    },
                    {
                        "uid": 186,
                        "name": 'Гайсинська територіальна громада',
                        "name_en": 'Haisynska Hromada',
                    },
                    {
                        "uid": 187,
                        "name": 'Дашівська територіальна громада',
                        "name_en": 'Dashivska Hromada',
                    },
                    {
                        "uid": 188,
                        "name": 'Джулинська територіальна громада',
                        "name_en": 'Dzhulynska Hromada',
                    },
                    {
                        "uid": 189,
                        "name": 'Краснопільська територіальна громада',
                        "name_en": 'Krasnopilska Hromada',
                    },
                    {
                        "uid": 190,
                        "name": 'Кунківська територіальна громада',
                        "name_en": 'Kunkivska Hromada',
                    },
                    {
                        "uid": 191,
                        "name": 'м. Ладижин та Ладижинська територіальна громада',
                        "name_en": 'Ladyzhyn and Ladyzhynska Hromada',
                    },
                    {
                        "uid": 192,
                        "name": 'Ободівська територіальна громада',
                        "name_en": 'Obodivska Hromada',
                    },
                    {
                        "uid": 193,
                        "name": 'Ольгопільська територіальна громада',
                        "name_en": 'Olhopilska Hromada',
                    },
                    {
                        "uid": 194,
                        "name": 'Райгородська територіальна громада',
                        "name_en": 'Raihorodska Hromada',
                    },
                    {
                        "uid": 195,
                        "name": 'Соболівська територіальна громада',
                        "name_en": 'Sobolivska Hromada',
                    },
                    {
                        "uid": 196,
                        "name": 'Теплицька територіальна громада',
                        "name_en": 'Teplytska Hromada',
                    },
                    {
                        "uid": 197,
                        "name": 'Тростянецька територіальна громада',
                        "name_en": 'Trostianetska Hromada',
                    },
                    {
                        "uid": 198,
                        "name": 'Чечельницька територіальна громада',
                        "name_en": 'Chechelnytska Hromada',
                    },
                ],
            },
            {
                "uid": 35,
                "name": 'Жмеринський район',
                "name_en": 'Zhmerynskyi Raion',
                "hromadas": [
                    {
                        "uid": 177,
                        "name": 'Барська територіальна громада',
                        "name_en": 'Barska Hromada',
                    },
                    {
                        "uid": 178,
                        "name": 'Джуринська територіальна громада',
                        "name_en": 'Dzhurynska Hromada',
                    },
                    {
                        "uid": 179,
                        "name": 'м. Жмеринка та Жмеринська територіальна громада',
                        "name_en": 'Zhmerynka and Zhmerynska Hromada',
                    },
                    {
                        "uid": 180,
                        "name": 'Копайгородська територіальна громада',
                        "name_en": 'Kopaihorodska Hromada',
                    },
                    {
                        "uid": 181,
                        "name": 'Мурафська територіальна громада',
                        "name_en": 'Murafska Hromada',
                    },
                    {
                        "uid": 182,
                        "name": 'Северинівська територіальна громада',
                        "name_en": 'Severynivska Hromada',
                    },
                    {
                        "uid": 183,
                        "name": 'Станіславчицька територіальна громада',
                        "name_en": 'Stanislavchytska Hromada',
                    },
                    {
                        "uid": 184,
                        "name": 'Шаргородська територіальна громада',
                        "name_en": 'Sharhorodska Hromada',
                    },
                ],
            },
            {
                "uid": 33,
                "name": 'Могилів-Подільський район',
                "name_en": 'Mohyliv-Podilskyi Raion',
                "hromadas": [
                    {
                        "uid": 170,
                        "name": 'Бабчинецька територіальна громада',
                        "name_en": 'Babchynetska Hromada',
                    },
                    {
                        "uid": 171,
                        "name": 'Вендичанська територіальна громада',
                        "name_en": 'Vendychanska Hromada',
                    },
                    {
                        "uid": 172,
                        "name": 'м. Могилів-Подільський та Могилів-Подільська територіальна громада',
                        "name_en": 'Mohyliv-Podilskyi and Mohyliv-Podilska Hromada',
                    },
                    {
                        "uid": 173,
                        "name": 'Мурованокуриловецька територіальна громада',
                        "name_en": 'Murovanokurylovetska Hromada',
                    },
                    {
                        "uid": 174,
                        "name": 'Чернівецька територіальна громада',
                        "name_en": 'Chernivetska Hromada',
                    },
                    {
                        "uid": 175,
                        "name": 'Ямпільська територіальна громада',
                        "name_en": 'Yampilska Hromada',
                    },
                    {
                        "uid": 176,
                        "name": 'Яришівська територіальна громада',
                        "name_en": 'Yaryshivska Hromada',
                    },
                ],
            },
            {
                "uid": 32,
                "name": 'Тульчинський район',
                "name_en": 'Tulchynskyi Raion',
                "hromadas": [
                    {
                        "uid": 199,
                        "name": 'Брацлавська територіальна громада',
                        "name_en": 'Bratslavska Hromada',
                    },
                    {
                        "uid": 200,
                        "name": 'Вапнярська територіальна громада',
                        "name_en": 'Vapniarska Hromada',
                    },
                    {
                        "uid": 201,
                        "name": 'Городківська територіальна громада',
                        "name_en": 'Horodkivska Hromada',
                    },
                    {
                        "uid": 202,
                        "name": 'Крижопільська територіальна громада',
                        "name_en": 'Kryzhopilska Hromada',
                    },
                    {
                        "uid": 203,
                        "name": 'Піщанська територіальна громада',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 204,
                        "name": 'Студенянська територіальна громада',
                        "name_en": 'Studenianska Hromada',
                    },
                    {
                        "uid": 205,
                        "name": 'Томашпільська територіальна громада',
                        "name_en": 'Tomashpilska Hromada',
                    },
                    {
                        "uid": 206,
                        "name": 'Тульчинська територіальна громада',
                        "name_en": 'Tulchynska Hromada',
                    },
                    {
                        "uid": 207,
                        "name": 'Шпиківська територіальна громада',
                        "name_en": 'Shpykivska Hromada',
                    },
                ],
            },
            {
                "uid": 34,
                "name": 'Хмільницький район',
                "name_en": 'Khmilnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 208,
                        "name": 'Глуховецька територіальна громада',
                        "name_en": 'Hlukhovetska Hromada',
                    },
                    {
                        "uid": 209,
                        "name": 'Жданівська територіальна громада',
                        "name_en": 'Zhdanivska Hromada',
                    },
                    {
                        "uid": 211,
                        "name": 'Калинівська територіальна громада',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 212,
                        "name": 'м. Козятин та Козятинська територіальна громада',
                        "name_en": 'Koziatyn and Koziatynska Hromada',
                    },
                    {
                        "uid": 213,
                        "name": 'Махнівська територіальна громада',
                        "name_en": 'Makhnivska Hromada',
                    },
                    {
                        "uid": 214,
                        "name": 'Самгородоцька територіальна громада',
                        "name_en": 'Samhorodotska Hromada',
                    },
                    {
                        "uid": 215,
                        "name": 'Уланівська територіальна громада',
                        "name_en": 'Ulanivska Hromada',
                    },
                    {
                        "uid": 216,
                        "name": 'м. Хмільник та Хмільницька територіальна громада',
                        "name_en": 'Khmilnyk and Khmilnytska Hromada',
                    },
                    {
                        "uid": 210,
                        "name": 'Іванівська територіальна громада',
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
                "name": 'Дніпровський район',
                "name_en": 'Dniprovskyi Raion',
                "hromadas": [
                    {
                        "uid": 332,
                        "name": 'м. Дніпро та Дніпровська територіальна громада',
                        "name_en": 'Dnipro and Dniprovska Hromada',
                    },
                    {
                        "uid": 333,
                        "name": 'Китайгородська територіальна громада',
                        "name_en": 'Kytaihorodska Hromada',
                    },
                    {
                        "uid": 334,
                        "name": 'Любимівська територіальна громада',
                        "name_en": 'Liubymivska Hromada',
                    },
                    {
                        "uid": 335,
                        "name": 'Ляшківська територіальна громада',
                        "name_en": 'Liashkivska Hromada',
                    },
                    {
                        "uid": 336,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 337,
                        "name": 'Могилівська територіальна громада',
                        "name_en": 'Mohylivska Hromada',
                    },
                    {
                        "uid": 338,
                        "name": 'Новоолександрівська територіальна громада',
                        "name_en": 'Novooleksandrivska Hromada',
                    },
                    {
                        "uid": 339,
                        "name": 'Новопокровська територіальна громада',
                        "name_en": 'Novopokrovska Hromada',
                    },
                    {
                        "uid": 340,
                        "name": 'Обухівська територіальна громада',
                        "name_en": 'Obukhivska Hromada',
                    },
                    {
                        "uid": 341,
                        "name": 'Петриківська територіальна громада',
                        "name_en": 'Petrykivska Hromada',
                    },
                    {
                        "uid": 342,
                        "name": 'Підгородненська територіальна громада',
                        "name_en": 'Pidhorodnenska Hromada',
                    },
                    {
                        "uid": 343,
                        "name": 'Святовасилівська територіальна громада',
                        "name_en": 'Sviatovasylivska Hromada',
                    },
                    {
                        "uid": 344,
                        "name": 'Слобожанська територіальна громада',
                        "name_en": 'Slobozhanska Hromada',
                    },
                    {
                        "uid": 345,
                        "name": 'Солонянська територіальна громада',
                        "name_en": 'Solonianska Hromada',
                    },
                    {
                        "uid": 346,
                        "name": 'Сурсько-Литовська територіальна громада',
                        "name_en": 'Sursko-Lytovska Hromada',
                    },
                    {
                        "uid": 347,
                        "name": 'Царичанська територіальна громада',
                        "name_en": 'Tsarychanska Hromada',
                    },
                    {
                        "uid": 348,
                        "name": 'Чумаківська територіальна громада',
                        "name_en": 'Chumakivska Hromada',
                    },
                ],
            },
            {
                "uid": 42,
                "name": "Кам'янський район",
                "name_en": 'Kamianskyi Raion',
                "hromadas": [
                    {
                        "uid": 293,
                        "name": 'Божедарівська територіальна громада',
                        "name_en": 'Bozhedarivska Hromada',
                    },
                    {
                        "uid": 295,
                        "name": 'Верхньодніпровська територіальна громада',
                        "name_en": 'Verkhnodniprovska Hromada',
                    },
                    {
                        "uid": 294,
                        "name": 'Верхівцівська територіальна громада',
                        "name_en": 'Verkhivtsivska Hromada',
                    },
                    {
                        "uid": 296,
                        "name": 'Вишнівська територіальна громада',
                        "name_en": 'Vyshnivska Hromada',
                    },
                    {
                        "uid": 297,
                        "name": 'м. Вільногірськ та Вільногірська територіальна громада',
                        "name_en": 'Vilnohirsk and Vilnohirska Hromada',
                    },
                    {
                        "uid": 298,
                        "name": 'м. Жовті Води та Жовтоводська територіальна громада',
                        "name_en": 'Zhovti Vody and Zhovtovodska Hromada',
                    },
                    {
                        "uid": 299,
                        "name": 'Затишнянська територіальна громада',
                        "name_en": 'Zatyshnianska Hromada',
                    },
                    {
                        "uid": 300,
                        "name": 'м. Кам’янське та Кам’янська територіальна громада',
                        "name_en": 'Kamyanske and Kamyanska Hromada',
                    },
                    {
                        "uid": 301,
                        "name": 'Криничанська територіальна громада',
                        "name_en": 'Krynychanska Hromada',
                    },
                    {
                        "uid": 302,
                        "name": 'Лихівська територіальна громада',
                        "name_en": 'Lykhivska Hromada',
                    },
                    {
                        "uid": 303,
                        "name": "П'ятихатська територіальна громада",
                        "name_en": 'Piatykhatska Hromada',
                    },
                    {
                        "uid": 304,
                        "name": 'Саксаганська територіальна громада',
                        "name_en": 'Saksahanska Hromada',
                    },
                ],
            },
            {
                "uid": 46,
                "name": 'Криворізький район',
                "name_en": 'Kryvorizkyi Raion',
                "hromadas": [
                    {
                        "uid": 271,
                        "name": 'Апостолівська територіальна громада',
                        "name_en": 'Apostolivska Hromada',
                    },
                    {
                        "uid": 272,
                        "name": 'Вакулівська територіальна громада',
                        "name_en": 'Vakulivska Hromada',
                    },
                    {
                        "uid": 273,
                        "name": 'Глеюватська територіальна громада',
                        "name_en": 'Hleiuvatska Hromada',
                    },
                    {
                        "uid": 274,
                        "name": 'Гречаноподівська територіальна громада',
                        "name_en": 'Hrechanopodivska Hromada',
                    },
                    {
                        "uid": 275,
                        "name": 'Грушівська територіальна громада',
                        "name_en": 'Hrushivska Hromada',
                    },
                    {
                        "uid": 276,
                        "name": 'Девладівська територіальна громада',
                        "name_en": 'Devladivska Hromada',
                    },
                    {
                        "uid": 277,
                        "name": 'Зеленодольська територіальна громада',
                        "name_en": 'Zelenodolska Hromada',
                    },
                    {
                        "uid": 278,
                        "name": 'Карпівська територіальна громада',
                        "name_en": 'Karpivska Hromada',
                    },
                    {
                        "uid": 279,
                        "name": 'м. Кривий Ріг та Криворізька територіальна громада',
                        "name_en": 'Kryvyi Rih and Kryvorizka Hromada',
                    },
                    {
                        "uid": 280,
                        "name": 'Лозуватська територіальна громада',
                        "name_en": 'Lozuvatska Hromada',
                    },
                    {
                        "uid": 281,
                        "name": 'Нивотрудівська територіальна громада',
                        "name_en": 'Nyvotrudivska Hromada',
                    },
                    {
                        "uid": 282,
                        "name": 'Новолатівська територіальна громада',
                        "name_en": 'Novolativska Hromada',
                    },
                    {
                        "uid": 283,
                        "name": 'Новопільська територіальна громада',
                        "name_en": 'Novopilska Hromada',
                    },
                    {
                        "uid": 284,
                        "name": 'Софіївська територіальна громада',
                        "name_en": 'Sofiivska Hromada',
                    },
                    {
                        "uid": 285,
                        "name": 'Широківська територіальна громада',
                        "name_en": 'Shyrokivska Hromada',
                    },
                ],
            },
            {
                "uid": 47,
                "name": 'Нікопольський район',
                "name_en": 'Nikopolskyi Raion',
                "hromadas": [
                    {
                        "uid": 349,
                        "name": 'м. Марганець та Марганецька територіальна громада',
                        "name_en": 'Marhanets and Marhanetska Hromada',
                    },
                    {
                        "uid": 350,
                        "name": 'Мирівська територіальна громада',
                        "name_en": 'Myrivska Hromada',
                    },
                    {
                        "uid": 351,
                        "name": 'м. Нікополь та Нікопольська територіальна громада',
                        "name_en": 'Nikopol and Nikopolska Hromada',
                    },
                    {
                        "uid": 352,
                        "name": 'Першотравневська територіальна громада',
                        "name_en": 'Pershotravnevska Hromada',
                    },
                    {
                        "uid": 354,
                        "name": 'м. Покров та Покровська територіальна громада',
                        "name_en": 'Pokrov and Pokrovska Hromada',
                    },
                    {
                        "uid": 353,
                        "name": 'Покровська територіальна громада',
                        "name_en": 'Pokrovska Hromada',
                    },
                    {
                        "uid": 355,
                        "name": 'Томаківська територіальна громада',
                        "name_en": 'Tomakivska Hromada',
                    },
                    {
                        "uid": 356,
                        "name": 'Червоногригорівська територіальна громада',
                        "name_en": 'Chervonohryhorivska Hromada',
                    },
                ],
            },
            {
                "uid": 45,
                "name": 'Павлоградський район',
                "name_en": 'Pavlohradskyi Raion',
                "hromadas": [
                    {
                        "uid": 286,
                        "name": 'Богданівська територіальна громада',
                        "name_en": 'Bohdanivska Hromada',
                    },
                    {
                        "uid": 287,
                        "name": 'Вербківська територіальна громада',
                        "name_en": 'Verbkivska Hromada',
                    },
                    {
                        "uid": 288,
                        "name": 'Межиріцька територіальна громада',
                        "name_en": 'Mezhyritska Hromada',
                    },
                    {
                        "uid": 289,
                        "name": 'м. Павлоград та Павлоградська територіальна громада',
                        "name_en": 'Pavlohrad and Pavlohradska Hromada',
                    },
                    {
                        "uid": 290,
                        "name": 'м. Тернівка та Тернівська територіальна громада',
                        "name_en": 'Ternivka and Ternivska Hromada',
                    },
                    {
                        "uid": 291,
                        "name": 'Троїцька територіальна громада',
                        "name_en": 'Troitska Hromada',
                    },
                    {
                        "uid": 292,
                        "name": 'Юр’ївська територіальна громада',
                        "name_en": 'Yuryivska Hromada',
                    },
                ],
            },
            {
                "uid": 43,
                "name": 'Самарівський район',
                "name_en": 'Samarivskyi Raion',
                "hromadas": [
                    {
                        "uid": 324,
                        "name": 'Губиниська територіальна громада',
                        "name_en": 'Hubynyska Hromada',
                    },
                    {
                        "uid": 325,
                        "name": 'Личківська територіальна громада',
                        "name_en": 'Lychkivska Hromada',
                    },
                    {
                        "uid": 326,
                        "name": 'Магдалинівська територіальна громада',
                        "name_en": 'Mahdalynivska Hromada',
                    },
                    {
                        "uid": 328,
                        "name": 'Перещепинська територіальна громада',
                        "name_en": 'Pereshchepynska Hromada',
                    },
                    {
                        "uid": 329,
                        "name": 'Піщанська територіальна громада',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 327,
                        "name": 'м. Самар та Самарівська територіальна громада',
                        "name_en": 'Samar and Samarivska Hromada',
                    },
                    {
                        "uid": 330,
                        "name": 'Черкаська територіальна громада',
                        "name_en": 'Cherkaska Hromada',
                    },
                    {
                        "uid": 331,
                        "name": 'Чернеччинська територіальна громада',
                        "name_en": 'Chernechchynska Hromada',
                    },
                ],
            },
            {
                "uid": 48,
                "name": 'Синельниківський район',
                "name_en": 'Synelnykivskyi Raion',
                "hromadas": [
                    {
                        "uid": 305,
                        "name": 'Брагинівська територіальна громада',
                        "name_en": 'Brahynivska Hromada',
                    },
                    {
                        "uid": 306,
                        "name": 'Васильківська територіальна громада',
                        "name_en": 'Vasylkivska Hromada',
                    },
                    {
                        "uid": 307,
                        "name": 'Великомихайлівська територіальна громада',
                        "name_en": 'Velykomykhailivska Hromada',
                    },
                    {
                        "uid": 308,
                        "name": 'Дубовиківська територіальна громада',
                        "name_en": 'Dubovykivska Hromada',
                    },
                    {
                        "uid": 309,
                        "name": 'Зайцівська територіальна громада',
                        "name_en": 'Zaitsivska Hromada',
                    },
                    {
                        "uid": 311,
                        "name": 'Маломихайлівська територіальна громада',
                        "name_en": 'Malomykhailivska Hromada',
                    },
                    {
                        "uid": 312,
                        "name": 'Межівська територіальна громада',
                        "name_en": 'Mezhivska Hromada',
                    },
                    {
                        "uid": 313,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 314,
                        "name": 'Новопавлівська територіальна громада',
                        "name_en": 'Novopavlivska Hromada',
                    },
                    {
                        "uid": 316,
                        "name": 'Петропавлівська територіальна громада',
                        "name_en": 'Petropavlivska Hromada',
                    },
                    {
                        "uid": 317,
                        "name": 'Покровська територіальна громада',
                        "name_en": 'Pokrovska Hromada',
                    },
                    {
                        "uid": 318,
                        "name": 'Раївська територіальна громада',
                        "name_en": 'Raivska Hromada',
                    },
                    {
                        "uid": 319,
                        "name": 'Роздорська територіальна громада',
                        "name_en": 'Rozdorska Hromada',
                    },
                    {
                        "uid": 320,
                        "name": 'м. Синельникове та Синельниківська територіальна громада',
                        "name_en": 'Synelnykove and Synelnykivska Hromada',
                    },
                    {
                        "uid": 321,
                        "name": 'Славгородська територіальна громада',
                        "name_en": 'Slavhorodska Hromada',
                    },
                    {
                        "uid": 322,
                        "name": "Слов'янська територіальна громада",
                        "name_en": 'Slovianska Hromada',
                    },
                    {
                        "uid": 323,
                        "name": 'Українська територіальна громада',
                        "name_en": 'Ukrainska Hromada',
                    },
                    {
                        "uid": 315,
                        "name": 'м. Шахтарськ та Шахтарська територіальна громада',
                        "name_en": 'Shakhtarsk and Shakhtarska Hromada',
                    },
                    {
                        "uid": 310,
                        "name": 'Іларіонівська територіальна громада',
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
                "name": 'Бахмутський район',
                "name_en": 'Bakhmutskyi Raion',
                "hromadas": [
                    {
                        "uid": 383,
                        "name": 'Бахмутська територіальна громада',
                        "name_en": 'Bakhmutska Hromada',
                    },
                    {
                        "uid": 384,
                        "name": 'Званівська територіальна громада',
                        "name_en": 'Zvanivska Hromada',
                    },
                    {
                        "uid": 385,
                        "name": 'Світлодарська територіальна громада',
                        "name_en": 'Svitlodarska Hromada',
                    },
                    {
                        "uid": 387,
                        "name": 'Соледарська територіальна громада',
                        "name_en": 'Soledarska Hromada',
                    },
                    {
                        "uid": 386,
                        "name": 'Сіверська територіальна громада',
                        "name_en": 'Siverska Hromada',
                    },
                    {
                        "uid": 388,
                        "name": 'Торецька територіальна громада',
                        "name_en": 'Toretska Hromada',
                    },
                    {
                        "uid": 389,
                        "name": 'Часовоярська територіальна громада',
                        "name_en": 'Chasovoiarska Hromada',
                    },
                ],
            },
            {
                "uid": 55,
                "name": 'Волноваський район',
                "name_en": 'Volnovaskyi Raion',
                "hromadas": [
                    {
                        "uid": 390,
                        "name": 'Великоновосілківська територіальна громада',
                        "name_en": 'Velykonovosilkivska Hromada',
                    },
                    {
                        "uid": 391,
                        "name": 'Волноваська територіальна громада',
                        "name_en": 'Volnovaska Hromada',
                    },
                    {
                        "uid": 392,
                        "name": 'Вугледарська територіальна громада',
                        "name_en": 'Vuhledarska Hromada',
                    },
                    {
                        "uid": 393,
                        "name": 'Комарська територіальна громада',
                        "name_en": 'Komarska Hromada',
                    },
                    {
                        "uid": 394,
                        "name": 'Мирненська територіальна громада',
                        "name_en": 'Myrnenska Hromada',
                    },
                    {
                        "uid": 395,
                        "name": 'Ольгинська територіальна громада',
                        "name_en": 'Olhynska Hromada',
                    },
                    {
                        "uid": 396,
                        "name": 'Старомлинівська територіальна громада',
                        "name_en": 'Staromlynivska Hromada',
                    },
                    {
                        "uid": 397,
                        "name": 'Хлібодарівська територіальна громада',
                        "name_en": 'Khlibodarivska Hromada',
                    },
                ],
            },
            {
                "uid": 51,
                "name": 'Горлівський район',
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
                "name": 'Донецький район',
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
                "name": 'Кальміуський район',
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
                "name": 'Краматорський район',
                "name_en": 'Kramatorskyi Raion',
                "hromadas": [
                    {
                        "uid": 371,
                        "name": 'Андріївська територіальна громада',
                        "name_en": 'Andriivska Hromada',
                    },
                    {
                        "uid": 372,
                        "name": 'Дружківська територіальна громада',
                        "name_en": 'Druzhkivska Hromada',
                    },
                    {
                        "uid": 374,
                        "name": 'Костянтинівська територіальна громада',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 375,
                        "name": 'м. Краматорськ та Краматорська територіальна громада',
                        "name_en": 'Kramatorsk and Kramatorska Hromada',
                    },
                    {
                        "uid": 376,
                        "name": 'Лиманська територіальна громада',
                        "name_en": 'Lymanska Hromada',
                    },
                    {
                        "uid": 377,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 378,
                        "name": 'Новодонецька територіальна громада',
                        "name_en": 'Novodonetska Hromada',
                    },
                    {
                        "uid": 379,
                        "name": 'Олександрівська територіальна громада',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 380,
                        "name": 'Святогірська територіальна громада',
                        "name_en": 'Sviatohirska Hromada',
                    },
                    {
                        "uid": 381,
                        "name": "м. Слов'янськ та Слов'янська територіальна громада",
                        "name_en": 'Sloviansk and Slovianska Hromada',
                    },
                    {
                        "uid": 382,
                        "name": 'Черкаська територіальна громада',
                        "name_en": 'Cherkaska Hromada',
                    },
                    {
                        "uid": 373,
                        "name": 'Іллінівська територіальна громада',
                        "name_en": 'Illinivska Hromada',
                    },
                ],
            },
            {
                "uid": 52,
                "name": 'Маріупольський район',
                "name_en": 'Mariupolskyi Raion',
                "hromadas": [
                    {
                        "uid": 398,
                        "name": 'Кальчицька територіальна громада',
                        "name_en": 'Kalchytska Hromada',
                    },
                    {
                        "uid": 399,
                        "name": 'Мангушська територіальна громада',
                        "name_en": 'Manhushska Hromada',
                    },
                    {
                        "uid": 400,
                        "name": 'м. Маріуполь та Маріупольська територіальна громада',
                        "name_en": 'Mariupol and Mariupolska Hromada',
                    },
                    {
                        "uid": 401,
                        "name": 'Нікольська територіальна громада',
                        "name_en": 'Nikolska Hromada',
                    },
                    {
                        "uid": 402,
                        "name": 'Сартанська територіальна громада',
                        "name_en": 'Sartanska Hromada',
                    },
                ],
            },
            {
                "uid": 56,
                "name": 'Покровський район',
                "name_en": 'Pokrovskyi Raion',
                "hromadas": [
                    {
                        "uid": 357,
                        "name": 'Авдіївська територіальна громада',
                        "name_en": 'Avdiivska Hromada',
                    },
                    {
                        "uid": 358,
                        "name": 'Білозерська територіальна громада',
                        "name_en": 'Bilozerska Hromada',
                    },
                    {
                        "uid": 359,
                        "name": 'Гродівська територіальна громада',
                        "name_en": 'Hrodivska Hromada',
                    },
                    {
                        "uid": 360,
                        "name": 'Добропільська територіальна громада',
                        "name_en": 'Dobropilska Hromada',
                    },
                    {
                        "uid": 361,
                        "name": 'Криворізька територіальна громада',
                        "name_en": 'Kryvorizka Hromada',
                    },
                    {
                        "uid": 362,
                        "name": 'Курахівська територіальна громада',
                        "name_en": 'Kurakhivska Hromada',
                    },
                    {
                        "uid": 363,
                        "name": "Мар'їнська територіальна громада",
                        "name_en": 'Marinska Hromada',
                    },
                    {
                        "uid": 364,
                        "name": 'Мирноградська територіальна громада',
                        "name_en": 'Myrnohradska Hromada',
                    },
                    {
                        "uid": 365,
                        "name": 'Новогродівська територіальна громада',
                        "name_en": 'Novohrodivska Hromada',
                    },
                    {
                        "uid": 366,
                        "name": 'Очеретинська територіальна громада',
                        "name_en": 'Ocheretynska Hromada',
                    },
                    {
                        "uid": 367,
                        "name": 'Покровська територіальна громада',
                        "name_en": 'Pokrovska Hromada',
                    },
                    {
                        "uid": 368,
                        "name": 'Селидівська територіальна громада',
                        "name_en": 'Selydivska Hromada',
                    },
                    {
                        "uid": 369,
                        "name": 'Удачненська територіальна громада',
                        "name_en": 'Udachnenska Hromada',
                    },
                    {
                        "uid": 370,
                        "name": 'Шахівська територіальна громада',
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
                "name": 'Бердичівський район',
                "name_en": 'Berdychivskyi Raion',
                "hromadas": [
                    {
                        "uid": 423,
                        "name": 'Андрушівська територіальна громада',
                        "name_en": 'Andrushivska Hromada',
                    },
                    {
                        "uid": 424,
                        "name": 'м. Бердичів та Бердичівська територіальна громада',
                        "name_en": 'Berdychiv and Berdychivska Hromada',
                    },
                    {
                        "uid": 425,
                        "name": 'Вчорайшенська територіальна громада',
                        "name_en": 'Vchoraishenska Hromada',
                    },
                    {
                        "uid": 426,
                        "name": 'Гришковецька територіальна громада',
                        "name_en": 'Hryshkovetska Hromada',
                    },
                    {
                        "uid": 427,
                        "name": 'Краснопільська територіальна громада',
                        "name_en": 'Krasnopilska Hromada',
                    },
                    {
                        "uid": 428,
                        "name": 'Райгородська територіальна громада',
                        "name_en": 'Raihorodska Hromada',
                    },
                    {
                        "uid": 429,
                        "name": 'Ружинська територіальна громада',
                        "name_en": 'Ruzhynska Hromada',
                    },
                    {
                        "uid": 430,
                        "name": 'Семенівська територіальна громада',
                        "name_en": 'Semenivska Hromada',
                    },
                    {
                        "uid": 431,
                        "name": 'Червоненська територіальна громада',
                        "name_en": 'Chervonenska Hromada',
                    },
                    {
                        "uid": 432,
                        "name": 'Швайківська територіальна громада',
                        "name_en": 'Shvaikivska Hromada',
                    },
                ],
            },
            {
                "uid": 59,
                "name": 'Житомирський район',
                "name_en": 'Zhytomyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 433,
                        "name": 'Андрушківська територіальна громада',
                        "name_en": 'Andrushkivska Hromada',
                    },
                    {
                        "uid": 434,
                        "name": 'Березівська територіальна громада',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 435,
                        "name": 'Брусилівська територіальна громада',
                        "name_en": 'Brusylivska Hromada',
                    },
                    {
                        "uid": 436,
                        "name": 'Високівська територіальна громада',
                        "name_en": 'Vysokivska Hromada',
                    },
                    {
                        "uid": 437,
                        "name": 'Вишевицька територіальна громада',
                        "name_en": 'Vyshevytska Hromada',
                    },
                    {
                        "uid": 439,
                        "name": 'Волицька територіальна громада',
                        "name_en": 'Volytska Hromada',
                    },
                    {
                        "uid": 438,
                        "name": 'Вільшанська територіальна громада',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 440,
                        "name": 'Глибочицька територіальна громада',
                        "name_en": 'Hlybochytska Hromada',
                    },
                    {
                        "uid": 441,
                        "name": 'Городоцька територіальна громада',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 442,
                        "name": 'м. Житомир та Житомирська територіальна громада',
                        "name_en": 'Zhytomyr and Zhytomyrska Hromada',
                    },
                    {
                        "uid": 443,
                        "name": 'Квітнева територіальна громада',
                        "name_en": 'Kvitneva Hromada',
                    },
                    {
                        "uid": 444,
                        "name": 'Корнинська територіальна громада',
                        "name_en": 'Kornynska Hromada',
                    },
                    {
                        "uid": 445,
                        "name": 'Коростишівська територіальна громада',
                        "name_en": 'Korostyshivska Hromada',
                    },
                    {
                        "uid": 446,
                        "name": 'Курненська територіальна громада',
                        "name_en": 'Kurnenska Hromada',
                    },
                    {
                        "uid": 447,
                        "name": 'Любарська територіальна громада',
                        "name_en": 'Liubarska Hromada',
                    },
                    {
                        "uid": 448,
                        "name": 'Миропільська територіальна громада',
                        "name_en": 'Myropilska Hromada',
                    },
                    {
                        "uid": 449,
                        "name": 'Новоборівська територіальна громада',
                        "name_en": 'Novoborivska Hromada',
                    },
                    {
                        "uid": 450,
                        "name": 'Новогуйвинська територіальна громада',
                        "name_en": 'Novohuivynska Hromada',
                    },
                    {
                        "uid": 451,
                        "name": 'Оліївська територіальна громада',
                        "name_en": 'Oliivska Hromada',
                    },
                    {
                        "uid": 452,
                        "name": 'Попільнянська територіальна громада',
                        "name_en": 'Popilnianska Hromada',
                    },
                    {
                        "uid": 453,
                        "name": 'Потіївська територіальна громада',
                        "name_en": 'Potiivska Hromada',
                    },
                    {
                        "uid": 454,
                        "name": 'Пулинська територіальна громада',
                        "name_en": 'Pulynska Hromada',
                    },
                    {
                        "uid": 455,
                        "name": 'Радомишльська територіальна громада',
                        "name_en": 'Radomyshlska Hromada',
                    },
                    {
                        "uid": 456,
                        "name": 'Романівська територіальна громада',
                        "name_en": 'Romanivska Hromada',
                    },
                    {
                        "uid": 457,
                        "name": 'Станишівська територіальна громада',
                        "name_en": 'Stanyshivska Hromada',
                    },
                    {
                        "uid": 458,
                        "name": 'Старосілецька територіальна громада',
                        "name_en": 'Starosiletska Hromada',
                    },
                    {
                        "uid": 459,
                        "name": 'Тетерівська територіальна громада',
                        "name_en": 'Teterivska Hromada',
                    },
                    {
                        "uid": 460,
                        "name": 'Харитонівська територіальна громада',
                        "name_en": 'Kharytonivska Hromada',
                    },
                    {
                        "uid": 461,
                        "name": 'Хорошівська територіальна громада',
                        "name_en": 'Khoroshivska Hromada',
                    },
                    {
                        "uid": 462,
                        "name": 'Черняхівська територіальна громада',
                        "name_en": 'Cherniakhivska Hromada',
                    },
                    {
                        "uid": 463,
                        "name": 'Чуднівська територіальна громада',
                        "name_en": 'Chudnivska Hromada',
                    },
                ],
            },
            {
                "uid": 60,
                "name": 'Звягельський район',
                "name_en": 'Zviahelskyi Raion',
                "hromadas": [
                    {
                        "uid": 464,
                        "name": 'Баранівська територіальна громада',
                        "name_en": 'Baranivska Hromada',
                    },
                    {
                        "uid": 465,
                        "name": 'Барашівська територіальна громада',
                        "name_en": 'Barashivska Hromada',
                    },
                    {
                        "uid": 466,
                        "name": 'Брониківська територіальна громада',
                        "name_en": 'Bronykivska Hromada',
                    },
                    {
                        "uid": 467,
                        "name": 'Городницька територіальна громада',
                        "name_en": 'Horodnytska Hromada',
                    },
                    {
                        "uid": 468,
                        "name": 'Довбиська територіальна громада',
                        "name_en": 'Dovbyska Hromada',
                    },
                    {
                        "uid": 469,
                        "name": 'Дубрівська територіальна громада',
                        "name_en": 'Dubrivska Hromada',
                    },
                    {
                        "uid": 471,
                        "name": 'м. Звягель та Звягельська територіальна громада',
                        "name_en": 'Zviahel and Zviahelska Hromada',
                    },
                    {
                        "uid": 472,
                        "name": 'Піщівська територіальна громада',
                        "name_en": 'Pishchivska Hromada',
                    },
                    {
                        "uid": 473,
                        "name": 'Стриївська територіальна громада',
                        "name_en": 'Stryivska Hromada',
                    },
                    {
                        "uid": 474,
                        "name": 'Чижівська територіальна громада',
                        "name_en": 'Chyzhivska Hromada',
                    },
                    {
                        "uid": 475,
                        "name": 'Ярунська територіальна громада',
                        "name_en": 'Yarunska Hromada',
                    },
                    {
                        "uid": 470,
                        "name": 'Ємільчинська територіальна громада',
                        "name_en": 'Yemilchynska Hromada',
                    },
                ],
            },
            {
                "uid": 58,
                "name": 'Коростенський район',
                "name_en": 'Korostenskyi Raion',
                "hromadas": [
                    {
                        "uid": 476,
                        "name": 'Білокоровицька територіальна громада',
                        "name_en": 'Bilokorovytska Hromada',
                    },
                    {
                        "uid": 477,
                        "name": 'Гладковицька територіальна громада',
                        "name_en": 'Hladkovytska Hromada',
                    },
                    {
                        "uid": 478,
                        "name": 'Горщиківська територіальна громада',
                        "name_en": 'Horshchykivska Hromada',
                    },
                    {
                        "uid": 480,
                        "name": 'м. Коростень та Коростенська територіальна громада',
                        "name_en": 'Korosten and Korostenska Hromada',
                    },
                    {
                        "uid": 481,
                        "name": 'Лугинська територіальна громада',
                        "name_en": 'Luhynska Hromada',
                    },
                    {
                        "uid": 482,
                        "name": 'м. Малин та Малинська територіальна громада',
                        "name_en": 'Malyn and Malynska Hromada',
                    },
                    {
                        "uid": 483,
                        "name": 'Народицька територіальна громада',
                        "name_en": 'Narodytska Hromada',
                    },
                    {
                        "uid": 484,
                        "name": 'Овруцька територіальна громада',
                        "name_en": 'Ovrutska Hromada',
                    },
                    {
                        "uid": 485,
                        "name": 'Олевська територіальна громада',
                        "name_en": 'Olevska Hromada',
                    },
                    {
                        "uid": 486,
                        "name": 'Словечанська територіальна громада',
                        "name_en": 'Slovechanska Hromada',
                    },
                    {
                        "uid": 487,
                        "name": 'Ушомирська територіальна громада',
                        "name_en": 'Ushomyrska Hromada',
                    },
                    {
                        "uid": 488,
                        "name": 'Чоповицька територіальна громада',
                        "name_en": 'Chopovytska Hromada',
                    },
                    {
                        "uid": 479,
                        "name": 'Іршанська територіальна громада',
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
                "name": 'Берегівський район',
                "name_en": 'Berehivskyi Raion',
                "hromadas": [
                    {
                        "uid": 503,
                        "name": 'Батівська територіальна громада',
                        "name_en": 'Bativska Hromada',
                    },
                    {
                        "uid": 504,
                        "name": 'м. Берегове та Берегівська територіальна громада',
                        "name_en": 'Berehove and Berehivska Hromada',
                    },
                    {
                        "uid": 505,
                        "name": 'Великоберезька територіальна громада',
                        "name_en": 'Velykoberezka Hromada',
                    },
                    {
                        "uid": 506,
                        "name": 'Великобийганська територіальна громада',
                        "name_en": 'Velykobyihanska Hromada',
                    },
                    {
                        "uid": 507,
                        "name": 'Вилоцька територіальна громада',
                        "name_en": 'Vylotska Hromada',
                    },
                    {
                        "uid": 508,
                        "name": 'м. Виноградів та Виноградівська територіальна громада',
                        "name_en": 'Vynohradiv and Vynohradivska Hromada',
                    },
                    {
                        "uid": 509,
                        "name": "Кам'янська територіальна громада",
                        "name_en": 'Kamianska Hromada',
                    },
                    {
                        "uid": 510,
                        "name": 'Королівська територіальна громада',
                        "name_en": 'Korolivska Hromada',
                    },
                    {
                        "uid": 511,
                        "name": 'Косоньська територіальна громада',
                        "name_en": 'Kosonska Hromada',
                    },
                    {
                        "uid": 512,
                        "name": 'Пийтерфолвівська територіальна громада',
                        "name_en": 'Pyiterfolvivska Hromada',
                    },
                ],
            },
            {
                "uid": 65,
                "name": 'Мукачівський район',
                "name_en": 'Mukachivskyi Raion',
                "hromadas": [
                    {
                        "uid": 540,
                        "name": 'Великолучківська територіальна громада',
                        "name_en": 'Velykoluchkivska Hromada',
                    },
                    {
                        "uid": 541,
                        "name": 'Верхньокоропецька територіальна громада',
                        "name_en": 'Verkhnokoropetska Hromada',
                    },
                    {
                        "uid": 542,
                        "name": 'Воловецька територіальна громада',
                        "name_en": 'Volovetska Hromada',
                    },
                    {
                        "uid": 543,
                        "name": 'Горондівська територіальна громада',
                        "name_en": 'Horondivska Hromada',
                    },
                    {
                        "uid": 544,
                        "name": 'Жденіївська територіальна громада',
                        "name_en": 'Zhdeniivska Hromada',
                    },
                    {
                        "uid": 546,
                        "name": 'Кольчинська територіальна громада',
                        "name_en": 'Kolchynska Hromada',
                    },
                    {
                        "uid": 547,
                        "name": 'м. Мукачево та Мукачівська територіальна громада',
                        "name_en": 'Mukachevo and Mukachivska Hromada',
                    },
                    {
                        "uid": 548,
                        "name": 'Неліпинська територіальна громада',
                        "name_en": 'Nelipynska Hromada',
                    },
                    {
                        "uid": 549,
                        "name": 'Нижньоворітська територіальна громада',
                        "name_en": 'Nyzhnovoritska Hromada',
                    },
                    {
                        "uid": 550,
                        "name": 'Полянська територіальна громада',
                        "name_en": 'Polianska Hromada',
                    },
                    {
                        "uid": 551,
                        "name": 'Свалявська територіальна громада',
                        "name_en": 'Svaliavska Hromada',
                    },
                    {
                        "uid": 552,
                        "name": 'Чинадіївська територіальна громада',
                        "name_en": 'Chynadiivska Hromada',
                    },
                    {
                        "uid": 545,
                        "name": 'Івановецька територіальна громада',
                        "name_en": 'Ivanovetska Hromada',
                    },
                ],
            },
            {
                "uid": 63,
                "name": 'Рахівський район',
                "name_en": 'Rakhivskyi Raion',
                "hromadas": [
                    {
                        "uid": 536,
                        "name": 'Богданська територіальна громада',
                        "name_en": 'Bohdanska Hromada',
                    },
                    {
                        "uid": 537,
                        "name": 'Великобичківська територіальна громада',
                        "name_en": 'Velykobychkivska Hromada',
                    },
                    {
                        "uid": 538,
                        "name": 'м. Рахів та Рахівська територіальна громада',
                        "name_en": 'Rakhiv and Rakhivska Hromada',
                    },
                    {
                        "uid": 539,
                        "name": 'Ясінянська територіальна громада',
                        "name_en": 'Yasinianska Hromada',
                    },
                ],
            },
            {
                "uid": 64,
                "name": 'Тячівський район',
                "name_en": 'Tiachivskyi Raion',
                "hromadas": [
                    {
                        "uid": 513,
                        "name": 'Бедевлянська територіальна громада',
                        "name_en": 'Bedevlianska Hromada',
                    },
                    {
                        "uid": 514,
                        "name": 'Буштинська територіальна громада',
                        "name_en": 'Bushtynska Hromada',
                    },
                    {
                        "uid": 515,
                        "name": 'Вільховецька територіальна громада',
                        "name_en": 'Vilkhovetska Hromada',
                    },
                    {
                        "uid": 516,
                        "name": 'Дубівська територіальна громада',
                        "name_en": 'Dubivska Hromada',
                    },
                    {
                        "uid": 517,
                        "name": 'Нересницька територіальна громада',
                        "name_en": 'Neresnytska Hromada',
                    },
                    {
                        "uid": 518,
                        "name": 'Солотвинська територіальна громада',
                        "name_en": 'Solotvynska Hromada',
                    },
                    {
                        "uid": 519,
                        "name": 'Тересвянська територіальна громада',
                        "name_en": 'Teresvianska Hromada',
                    },
                    {
                        "uid": 520,
                        "name": 'м. Тячів та Тячівська територіальна громада',
                        "name_en": 'Tiachiv and Tiachivska Hromada',
                    },
                    {
                        "uid": 521,
                        "name": 'Углянська територіальна громада',
                        "name_en": 'Uhlianska Hromada',
                    },
                    {
                        "uid": 522,
                        "name": 'Усть-Чорнянська територіальна громада',
                        "name_en": 'Ust-Chornianska Hromada',
                    },
                ],
            },
            {
                "uid": 66,
                "name": 'Ужгородський район',
                "name_en": 'Uzhhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 489,
                        "name": 'Баранинська територіальна громада',
                        "name_en": 'Baranynska Hromada',
                    },
                    {
                        "uid": 490,
                        "name": 'Великоберезнянська територіальна громада',
                        "name_en": 'Velykobereznianska Hromada',
                    },
                    {
                        "uid": 491,
                        "name": 'Великодобронська територіальна громада',
                        "name_en": 'Velykodobronska Hromada',
                    },
                    {
                        "uid": 492,
                        "name": 'Дубриницько-Малоберезня територіальна громада',
                        "name_en": 'Dubrynytsko-Malobereznia Hromada',
                    },
                    {
                        "uid": 493,
                        "name": 'Костринська територіальна громада',
                        "name_en": 'Kostrynska Hromada',
                    },
                    {
                        "uid": 494,
                        "name": 'Оноківська територіальна громада',
                        "name_en": 'Onokivska Hromada',
                    },
                    {
                        "uid": 495,
                        "name": 'Перечинська територіальна громада',
                        "name_en": 'Perechynska Hromada',
                    },
                    {
                        "uid": 496,
                        "name": 'Середнянська територіальна громада',
                        "name_en": 'Serednianska Hromada',
                    },
                    {
                        "uid": 497,
                        "name": 'Ставненська територіальна громада',
                        "name_en": 'Stavnenska Hromada',
                    },
                    {
                        "uid": 498,
                        "name": 'Сюртівська територіальна громада',
                        "name_en": 'Siurtivska Hromada',
                    },
                    {
                        "uid": 499,
                        "name": "Тур'є-Реметівська територіальна громада",
                        "name_en": 'Turie-Remetivska Hromada',
                    },
                    {
                        "uid": 500,
                        "name": 'м. Ужгород та Ужгородська територіальна громада',
                        "name_en": 'Uzhhorod and Uzhhorodska Hromada',
                    },
                    {
                        "uid": 501,
                        "name": 'Холмківська територіальна громада',
                        "name_en": 'Kholmkivska Hromada',
                    },
                    {
                        "uid": 502,
                        "name": 'м. Чоп та Чопська територіальна громада',
                        "name_en": 'Chop and Chopska Hromada',
                    },
                ],
            },
            {
                "uid": 62,
                "name": 'Хустський район',
                "name_en": 'Khustskyi Raion',
                "hromadas": [
                    {
                        "uid": 523,
                        "name": 'Білківська територіальна громада',
                        "name_en": 'Bilkivska Hromada',
                    },
                    {
                        "uid": 524,
                        "name": 'Вишківська територіальна громада',
                        "name_en": 'Vyshkivska Hromada',
                    },
                    {
                        "uid": 525,
                        "name": 'Горінчівська територіальна громада',
                        "name_en": 'Horinchivska Hromada',
                    },
                    {
                        "uid": 526,
                        "name": 'Довжанська територіальна громада',
                        "name_en": 'Dovzhanska Hromada',
                    },
                    {
                        "uid": 527,
                        "name": 'Драгівська територіальна громада',
                        "name_en": 'Drahivska Hromada',
                    },
                    {
                        "uid": 528,
                        "name": 'Зарічанська територіальна громада',
                        "name_en": 'Zarichanska Hromada',
                    },
                    {
                        "uid": 530,
                        "name": 'Керецьківська територіальна громада',
                        "name_en": 'Keretskivska Hromada',
                    },
                    {
                        "uid": 531,
                        "name": 'Колочавська територіальна громада',
                        "name_en": 'Kolochavska Hromada',
                    },
                    {
                        "uid": 532,
                        "name": "м. Міжгір'я та Міжгірська територіальна громада",
                        "name_en": 'Mizhhiria and Mizhhirska Hromada',
                    },
                    {
                        "uid": 533,
                        "name": 'Пилипецька територіальна громада',
                        "name_en": 'Pylypetska Hromada',
                    },
                    {
                        "uid": 534,
                        "name": 'Синевирська територіальна громада',
                        "name_en": 'Synevyrska Hromada',
                    },
                    {
                        "uid": 535,
                        "name": 'м. Хуст та Хустська територіальна громада',
                        "name_en": 'Khust and Khustska Hromada',
                    },
                    {
                        "uid": 529,
                        "name": 'м. Іршава та Іршавська територіальна громада',
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
                "name": 'Бердянський район',
                "name_en": 'Berdianskyi Raion',
                "hromadas": [
                    {
                        "uid": 553,
                        "name": 'Андрівська територіальна громада',
                        "name_en": 'Andrivska Hromada',
                    },
                    {
                        "uid": 554,
                        "name": 'Андріївська територіальна громада',
                        "name_en": 'Andriivska Hromada',
                    },
                    {
                        "uid": 555,
                        "name": 'м. Бердянськ та Бердянська територіальна громада',
                        "name_en": 'Berdiansk and Berdianska Hromada',
                    },
                    {
                        "uid": 556,
                        "name": 'Берестівська територіальна громада',
                        "name_en": 'Berestivska Hromada',
                    },
                    {
                        "uid": 557,
                        "name": 'Коларівська територіальна громада',
                        "name_en": 'Kolarivska Hromada',
                    },
                    {
                        "uid": 558,
                        "name": 'Осипенківська територіальна громада',
                        "name_en": 'Osypenkivska Hromada',
                    },
                    {
                        "uid": 559,
                        "name": 'Приморська територіальна громада',
                        "name_en": 'Prymorska Hromada',
                    },
                    {
                        "uid": 560,
                        "name": 'Чернігівська територіальна громада',
                        "name_en": 'Chernihivska Hromada',
                    },
                ],
            },
            {
                "uid": 146,
                "name": 'Василівський район',
                "name_en": 'Vasylivskyi Raion',
                "hromadas": [
                    {
                        "uid": 593,
                        "name": 'Благовіщенська територіальна громада',
                        "name_en": 'Blahovishchenska Hromada',
                    },
                    {
                        "uid": 594,
                        "name": 'Василівська територіальна громада',
                        "name_en": 'Vasylivska Hromada',
                    },
                    {
                        "uid": 595,
                        "name": 'Великобілозерська територіальна громада',
                        "name_en": 'Velykobilozerska Hromada',
                    },
                    {
                        "uid": 596,
                        "name": 'Водянська територіальна громада',
                        "name_en": 'Vodianska Hromada',
                    },
                    {
                        "uid": 597,
                        "name": 'Дніпрорудненська територіальна громада',
                        "name_en": 'Dniprorudnenska Hromada',
                    },
                    {
                        "uid": 598,
                        "name": 'м. Енергодар та Енергодарська територіальна громада',
                        "name_en": 'Enerhodar and Enerhodarska Hromada',
                    },
                    {
                        "uid": 599,
                        "name": "Кам'янсько-Дніпровська територіальна громада",
                        "name_en": 'Kamiansko-Dniprovska Hromada',
                    },
                    {
                        "uid": 600,
                        "name": 'Малобілозерська територіальна громада',
                        "name_en": 'Malobilozerska Hromada',
                    },
                    {
                        "uid": 601,
                        "name": 'Михайлівська територіальна громада',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 602,
                        "name": 'Роздольська територіальна громада',
                        "name_en": 'Rozdolska Hromada',
                    },
                    {
                        "uid": 603,
                        "name": 'Степногірська територіальна громада',
                        "name_en": 'Stepnohirska Hromada',
                    },
                ],
            },
            {
                "uid": 149,
                "name": 'Запорізький район',
                "name_en": 'Zaporizkyi Raion',
                "hromadas": [
                    {
                        "uid": 561,
                        "name": 'Біленьківська територіальна громада',
                        "name_en": 'Bilenkivska Hromada',
                    },
                    {
                        "uid": 562,
                        "name": 'Вільнянська територіальна громада',
                        "name_en": 'Vilnianska Hromada',
                    },
                    {
                        "uid": 563,
                        "name": 'Долинська територіальна громада',
                        "name_en": 'Dolynska Hromada',
                    },
                    {
                        "uid": 564,
                        "name": 'м. Запоріжжя та Запорізька територіальна громада',
                        "name_en": 'Zaporizhzhia and Zaporizka Hromada',
                    },
                    {
                        "uid": 565,
                        "name": 'Комишуваська територіальна громада',
                        "name_en": 'Komyshuvaska Hromada',
                    },
                    {
                        "uid": 566,
                        "name": 'Кушугумська територіальна громада',
                        "name_en": 'Kushuhumska Hromada',
                    },
                    {
                        "uid": 567,
                        "name": 'Матвіївська територіальна громада',
                        "name_en": 'Matviivska Hromada',
                    },
                    {
                        "uid": 569,
                        "name": 'Михайло-Лукашівська територіальна громада',
                        "name_en": 'Mykhailo-Lukashivska Hromada',
                    },
                    {
                        "uid": 568,
                        "name": 'Михайлівська територіальна громада',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 570,
                        "name": 'Новомиколаївська територіальна громада',
                        "name_en": 'Novomykolaivska Hromada',
                    },
                    {
                        "uid": 571,
                        "name": 'Новоолександрівська територіальна громада',
                        "name_en": 'Novooleksandrivska Hromada',
                    },
                    {
                        "uid": 572,
                        "name": 'Павлівська територіальна громада',
                        "name_en": 'Pavlivska Hromada',
                    },
                    {
                        "uid": 573,
                        "name": 'Петро-Михайлівська територіальна громада',
                        "name_en": 'Petro-Mykhailivska Hromada',
                    },
                    {
                        "uid": 574,
                        "name": 'Степненська територіальна громада',
                        "name_en": 'Stepnenska Hromada',
                    },
                    {
                        "uid": 575,
                        "name": 'Таврійська територіальна громада',
                        "name_en": 'Tavriiska Hromada',
                    },
                    {
                        "uid": 576,
                        "name": 'Тернуватська територіальна громада',
                        "name_en": 'Ternuvatska Hromada',
                    },
                    {
                        "uid": 577,
                        "name": 'Широківська територіальна громада',
                        "name_en": 'Shyrokivska Hromada',
                    },
                ],
            },
            {
                "uid": 148,
                "name": 'Мелітопольський район',
                "name_en": 'Melitopolskyi Raion',
                "hromadas": [
                    {
                        "uid": 604,
                        "name": 'Веселівська територіальна громада',
                        "name_en": 'Veselivska Hromada',
                    },
                    {
                        "uid": 605,
                        "name": 'Кирилівська територіальна громада',
                        "name_en": 'Kyrylivska Hromada',
                    },
                    {
                        "uid": 606,
                        "name": 'Костянтинівська територіальна громада',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 607,
                        "name": 'м. Мелітополь та Мелітопольська територіальна громада',
                        "name_en": 'Melitopol and Melitopolska Hromada',
                    },
                    {
                        "uid": 608,
                        "name": 'Мирненська територіальна громада',
                        "name_en": 'Myrnenska Hromada',
                    },
                    {
                        "uid": 609,
                        "name": 'Новенська територіальна громада',
                        "name_en": 'Novenska Hromada',
                    },
                    {
                        "uid": 610,
                        "name": 'Новобогданівська територіальна громада',
                        "name_en": 'Novobohdanivska Hromada',
                    },
                    {
                        "uid": 611,
                        "name": 'Нововасилівська територіальна громада',
                        "name_en": 'Novovasylivska Hromada',
                    },
                    {
                        "uid": 612,
                        "name": 'Новоуспенівська територіальна громада',
                        "name_en": 'Novouspenivska Hromada',
                    },
                    {
                        "uid": 613,
                        "name": 'Олександрівська територіальна громада',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 614,
                        "name": 'Плодородненська територіальна громада',
                        "name_en": 'Plodorodnenska Hromada',
                    },
                    {
                        "uid": 615,
                        "name": 'Приазовська територіальна громада',
                        "name_en": 'Pryazovska Hromada',
                    },
                    {
                        "uid": 616,
                        "name": 'Семенівська територіальна громада',
                        "name_en": 'Semenivska Hromada',
                    },
                    {
                        "uid": 617,
                        "name": 'Терпіннівська територіальна громада',
                        "name_en": 'Terpinnivska Hromada',
                    },
                    {
                        "uid": 618,
                        "name": 'Чкаловська територіальна громада',
                        "name_en": 'Chkalovska Hromada',
                    },
                    {
                        "uid": 619,
                        "name": 'Якимівська територіальна громада',
                        "name_en": 'Yakymivska Hromada',
                    },
                ],
            },
            {
                "uid": 145,
                "name": 'Пологівський район',
                "name_en": 'Polohivskyi Raion',
                "hromadas": [
                    {
                        "uid": 578,
                        "name": 'Більмацька територіальна громада',
                        "name_en": 'Bilmatska Hromada',
                    },
                    {
                        "uid": 579,
                        "name": 'Воздвижівська територіальна громада',
                        "name_en": 'Vozdvyzhivska Hromada',
                    },
                    {
                        "uid": 580,
                        "name": 'Воскресенська територіальна громада',
                        "name_en": 'Voskresenska Hromada',
                    },
                    {
                        "uid": 581,
                        "name": 'Гуляйпільська територіальна громада',
                        "name_en": 'Huliaipilska Hromada',
                    },
                    {
                        "uid": 582,
                        "name": 'Комиш-Зорянська територіальна громада',
                        "name_en": 'Komysh-Zorianska Hromada',
                    },
                    {
                        "uid": 583,
                        "name": 'Малинівська територіальна громада',
                        "name_en": 'Malynivska Hromada',
                    },
                    {
                        "uid": 584,
                        "name": 'Малотокмачанська територіальна громада',
                        "name_en": 'Malotokmachanska Hromada',
                    },
                    {
                        "uid": 585,
                        "name": 'Молочанська територіальна громада',
                        "name_en": 'Molochanska Hromada',
                    },
                    {
                        "uid": 586,
                        "name": 'Оріхівська територіальна громада',
                        "name_en": 'Orikhivska Hromada',
                    },
                    {
                        "uid": 587,
                        "name": 'Пологівська територіальна громада',
                        "name_en": 'Polohivska Hromada',
                    },
                    {
                        "uid": 588,
                        "name": 'Преображенська територіальна громада',
                        "name_en": 'Preobrazhenska Hromada',
                    },
                    {
                        "uid": 589,
                        "name": 'Розівська територіальна громада',
                        "name_en": 'Rozivska Hromada',
                    },
                    {
                        "uid": 590,
                        "name": 'Смирновська територіальна громада',
                        "name_en": 'Smyrnovska Hromada',
                    },
                    {
                        "uid": 591,
                        "name": 'м. Токмак та Токмацька територіальна громада',
                        "name_en": 'Tokmak and Tokmatska Hromada',
                    },
                    {
                        "uid": 592,
                        "name": 'Федорівська територіальна громада',
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
                "name": 'Бориспільський район',
                "name_en": 'Boryspilskyi Raion',
                "hromadas": [
                    {
                        "uid": 733,
                        "name": 'м. Бориспіль та Бориспільська територіальна громада',
                        "name_en": 'Boryspil and Boryspilska Hromada',
                    },
                    {
                        "uid": 734,
                        "name": 'Вороньківська територіальна громада',
                        "name_en": 'Voronkivska Hromada',
                    },
                    {
                        "uid": 735,
                        "name": 'Гірська територіальна громада',
                        "name_en": 'Hirska Hromada',
                    },
                    {
                        "uid": 736,
                        "name": 'Дівичківська територіальна громада',
                        "name_en": 'Divychkivska Hromada',
                    },
                    {
                        "uid": 737,
                        "name": 'Золочівська територіальна громада',
                        "name_en": 'Zolochivska Hromada',
                    },
                    {
                        "uid": 738,
                        "name": 'м. Переяслав та Переяславська територіальна громада',
                        "name_en": 'Pereiaslav and Pereiaslavska Hromada',
                    },
                    {
                        "uid": 739,
                        "name": 'Пристолична територіальна громада',
                        "name_en": 'Prystolychna Hromada',
                    },
                    {
                        "uid": 740,
                        "name": 'Студениківська територіальна громада',
                        "name_en": 'Studenykivska Hromada',
                    },
                    {
                        "uid": 741,
                        "name": 'Ташанська територіальна громада',
                        "name_en": 'Tashanska Hromada',
                    },
                    {
                        "uid": 742,
                        "name": 'Циблівська територіальна громада',
                        "name_en": 'Tsyblivska Hromada',
                    },
                    {
                        "uid": 743,
                        "name": 'Яготинська територіальна громада',
                        "name_en": 'Yahotynska Hromada',
                    },
                ],
            },
            {
                "uid": 79,
                "name": 'Броварський район',
                "name_en": 'Brovarskyi Raion',
                "hromadas": [
                    {
                        "uid": 682,
                        "name": 'Баришівська територіальна громада',
                        "name_en": 'Baryshivska Hromada',
                    },
                    {
                        "uid": 683,
                        "name": 'м. Березань та Березанська територіальна громада',
                        "name_en": 'Berezan and Berezanska Hromada',
                    },
                    {
                        "uid": 684,
                        "name": 'м. Бровари та Броварська територіальна громада',
                        "name_en": 'Brovary and Brovarska Hromada',
                    },
                    {
                        "uid": 685,
                        "name": 'Великодимерська територіальна громада',
                        "name_en": 'Velykodymerska Hromada',
                    },
                    {
                        "uid": 686,
                        "name": 'Зазимська територіальна громада',
                        "name_en": 'Zazymska Hromada',
                    },
                    {
                        "uid": 687,
                        "name": 'Згурівська територіальна громада',
                        "name_en": 'Zghurivska Hromada',
                    },
                    {
                        "uid": 688,
                        "name": 'Калинівська територіальна громада',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 689,
                        "name": 'Калитянська територіальна громада',
                        "name_en": 'Kalytianska Hromada',
                    },
                ],
            },
            {
                "uid": 75,
                "name": 'Бучанський район',
                "name_en": 'Buchanskyi Raion',
                "hromadas": [
                    {
                        "uid": 700,
                        "name": 'Бородянська територіальна громада',
                        "name_en": 'Borodianska Hromada',
                    },
                    {
                        "uid": 701,
                        "name": 'Борщагівська територіальна громада',
                        "name_en": 'Borshchahivska Hromada',
                    },
                    {
                        "uid": 702,
                        "name": 'м. Буча та Бучанська територіальна громада',
                        "name_en": 'Bucha and Buchanska Hromada',
                    },
                    {
                        "uid": 699,
                        "name": 'Білогородська територіальна громада',
                        "name_en": 'Bilohorodska Hromada',
                    },
                    {
                        "uid": 703,
                        "name": 'Вишнева територіальна громада',
                        "name_en": 'Vyshneva Hromada',
                    },
                    {
                        "uid": 704,
                        "name": 'Гостомелська територіальна громада',
                        "name_en": 'Hostomelska Hromada',
                    },
                    {
                        "uid": 705,
                        "name": 'Дмитрівська територіальна громада',
                        "name_en": 'Dmytrivska Hromada',
                    },
                    {
                        "uid": 707,
                        "name": 'Коцюбинська територіальна громада',
                        "name_en": 'Kotsiubynska Hromada',
                    },
                    {
                        "uid": 708,
                        "name": 'Макарівська територіальна громада',
                        "name_en": 'Makarivska Hromada',
                    },
                    {
                        "uid": 709,
                        "name": 'Немішаївська територіальна громада',
                        "name_en": 'Nemishaivska Hromada',
                    },
                    {
                        "uid": 710,
                        "name": 'Пісківська територіальна громада',
                        "name_en": 'Piskivska Hromada',
                    },
                    {
                        "uid": 706,
                        "name": 'м. Ірпінь та Ірпінська територіальна громада',
                        "name_en": 'Irpin and Irpinska Hromada',
                    },
                ],
            },
            {
                "uid": 73,
                "name": 'Білоцерківський район',
                "name_en": 'Bilotserkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 711,
                        "name": 'м. Біла Церква та Білоцерківська територіальна громада',
                        "name_en": 'Bila Tserkva and Bilotserkivska Hromada',
                    },
                    {
                        "uid": 712,
                        "name": 'Володарська територіальна громада',
                        "name_en": 'Volodarska Hromada',
                    },
                    {
                        "uid": 713,
                        "name": 'Гребінківська територіальна громада',
                        "name_en": 'Hrebinkivska Hromada',
                    },
                    {
                        "uid": 714,
                        "name": 'Ковалівська територіальна громада',
                        "name_en": 'Kovalivska Hromada',
                    },
                    {
                        "uid": 715,
                        "name": 'Маловільшанська територіальна громада',
                        "name_en": 'Malovilshanska Hromada',
                    },
                    {
                        "uid": 716,
                        "name": 'Медвинська територіальна громада',
                        "name_en": 'Medvynska Hromada',
                    },
                    {
                        "uid": 717,
                        "name": 'Рокитнянська територіальна громада',
                        "name_en": 'Rokytnianska Hromada',
                    },
                    {
                        "uid": 718,
                        "name": 'Сквирська територіальна громада',
                        "name_en": 'Skvyrska Hromada',
                    },
                    {
                        "uid": 719,
                        "name": 'Ставищенська територіальна громада',
                        "name_en": 'Stavyshchenska Hromada',
                    },
                    {
                        "uid": 720,
                        "name": 'Таращанська територіальна громада',
                        "name_en": 'Tarashchanska Hromada',
                    },
                    {
                        "uid": 721,
                        "name": 'Тетіївська територіальна громада',
                        "name_en": 'Tetiivska Hromada',
                    },
                    {
                        "uid": 722,
                        "name": 'Узинська територіальна громада',
                        "name_en": 'Uzynska Hromada',
                    },
                    {
                        "uid": 723,
                        "name": 'Фурсівська територіальна громада',
                        "name_en": 'Fursivska Hromada',
                    },
                ],
            },
            {
                "uid": 74,
                "name": 'Вишгородський район',
                "name_en": 'Vyshhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 744,
                        "name": 'Вишгородська територіальна громада',
                        "name_en": 'Vyshhorodska Hromada',
                    },
                    {
                        "uid": 745,
                        "name": 'Димерська територіальна громада',
                        "name_en": 'Dymerska Hromada',
                    },
                    {
                        "uid": 747,
                        "name": 'Петрівська територіальна громада',
                        "name_en": 'Petrivska Hromada',
                    },
                    {
                        "uid": 749,
                        "name": 'Поліська територіальна громада',
                        "name_en": 'Poliska Hromada',
                    },
                    {
                        "uid": 748,
                        "name": 'Пірнівська територіальна громада',
                        "name_en": 'Pirnivska Hromada',
                    },
                    {
                        "uid": 750,
                        "name": 'м. Славутич та Славутицька територіальна громада',
                        "name_en": 'Slavutych and Slavutytska Hromada',
                    },
                    {
                        "uid": 746,
                        "name": 'Іванківська територіальна громада',
                        "name_en": 'Ivankivska Hromada',
                    },
                ],
            },
            {
                "uid": 76,
                "name": 'Обухівський район',
                "name_en": 'Obukhivskyi Raion',
                "hromadas": [
                    {
                        "uid": 724,
                        "name": 'Богуславська територіальна громада',
                        "name_en": 'Bohuslavska Hromada',
                    },
                    {
                        "uid": 725,
                        "name": 'м. Васильків та Васильківська територіальна громада',
                        "name_en": 'Vasylkiv and Vasylkivska Hromada',
                    },
                    {
                        "uid": 726,
                        "name": 'Кагарлицька територіальна громада',
                        "name_en": 'Kaharlytska Hromada',
                    },
                    {
                        "uid": 727,
                        "name": 'Козинська територіальна громада',
                        "name_en": 'Kozynska Hromada',
                    },
                    {
                        "uid": 728,
                        "name": 'Миронівська територіальна громада',
                        "name_en": 'Myronivska Hromada',
                    },
                    {
                        "uid": 729,
                        "name": 'м. Обухів та Обухівська територіальна громада',
                        "name_en": 'Obukhiv and Obukhivska Hromada',
                    },
                    {
                        "uid": 730,
                        "name": 'м. Ржищів та Ржищівська територіальна громада',
                        "name_en": 'Rzhyshchiv and Rzhyshchivska Hromada',
                    },
                    {
                        "uid": 731,
                        "name": 'Українська територіальна громада',
                        "name_en": 'Ukrainska Hromada',
                    },
                    {
                        "uid": 732,
                        "name": 'Феодосіївська територіальна громада',
                        "name_en": 'Feodosiivska Hromada',
                    },
                ],
            },
            {
                "uid": 77,
                "name": 'Фастівський район',
                "name_en": 'Fastivskyi Raion',
                "hromadas": [
                    {
                        "uid": 690,
                        "name": 'Бишівська територіальна громада',
                        "name_en": 'Byshivska Hromada',
                    },
                    {
                        "uid": 691,
                        "name": 'Боярська територіальна громада',
                        "name_en": 'Boiarska Hromada',
                    },
                    {
                        "uid": 692,
                        "name": 'Гатненська територіальна громада',
                        "name_en": 'Hatnenska Hromada',
                    },
                    {
                        "uid": 693,
                        "name": 'Глевахівська територіальна громада',
                        "name_en": 'Hlevakhivska Hromada',
                    },
                    {
                        "uid": 694,
                        "name": 'Калинівська територіальна громада',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 695,
                        "name": 'Кожанська територіальна громада',
                        "name_en": 'Kozhanska Hromada',
                    },
                    {
                        "uid": 696,
                        "name": 'Томашівська територіальна громада',
                        "name_en": 'Tomashivska Hromada',
                    },
                    {
                        "uid": 697,
                        "name": 'м. Фастів та Фастівська територіальна громада',
                        "name_en": 'Fastiv and Fastivska Hromada',
                    },
                    {
                        "uid": 698,
                        "name": 'Чабанівська територіальна громада',
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
                "name": 'Голованівський район',
                "name_en": 'Holovanivskyi Raion',
                "hromadas": [
                    {
                        "uid": 768,
                        "name": 'Благовіщенська територіальна громада',
                        "name_en": 'Blahovishchenska Hromada',
                    },
                    {
                        "uid": 769,
                        "name": 'Вільшанська територіальна громада',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 770,
                        "name": 'Гайворонська територіальна громада',
                        "name_en": 'Haivoronska Hromada',
                    },
                    {
                        "uid": 771,
                        "name": 'Голованівська територіальна громада',
                        "name_en": 'Holovanivska Hromada',
                    },
                    {
                        "uid": 772,
                        "name": 'Заваллівська територіальна громада',
                        "name_en": 'Zavallivska Hromada',
                    },
                    {
                        "uid": 773,
                        "name": 'Надлацька територіальна громада',
                        "name_en": 'Nadlatska Hromada',
                    },
                    {
                        "uid": 774,
                        "name": 'Новоархангельська територіальна громада',
                        "name_en": 'Novoarkhanhelska Hromada',
                    },
                    {
                        "uid": 775,
                        "name": 'Перегонівська територіальна громада',
                        "name_en": 'Perehonivska Hromada',
                    },
                    {
                        "uid": 777,
                        "name": 'Побузька територіальна громада',
                        "name_en": 'Pobuzka Hromada',
                    },
                    {
                        "uid": 776,
                        "name": 'Підвисоцька територіальна громада',
                        "name_en": 'Pidvysotska Hromada',
                    },
                ],
            },
            {
                "uid": 81,
                "name": 'Кропивницький район',
                "name_en": 'Kropyvnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 751,
                        "name": 'Аджамська територіальна громада',
                        "name_en": 'Adzhamska Hromada',
                    },
                    {
                        "uid": 752,
                        "name": 'Бобринецька територіальна громада',
                        "name_en": 'Bobrynetska Hromada',
                    },
                    {
                        "uid": 753,
                        "name": 'Великосеверинівська територіальна громада',
                        "name_en": 'Velykoseverynivska Hromada',
                    },
                    {
                        "uid": 754,
                        "name": 'Гурівська територіальна громада',
                        "name_en": 'Hurivska Hromada',
                    },
                    {
                        "uid": 755,
                        "name": 'Дмитрівська територіальна громада',
                        "name_en": 'Dmytrivska Hromada',
                    },
                    {
                        "uid": 756,
                        "name": 'Долинська територіальна громада',
                        "name_en": 'Dolynska Hromada',
                    },
                    {
                        "uid": 757,
                        "name": "м. Знам'янка та Знам’янська територіальна громада",
                        "name_en": 'Znamianka and Znamyanska Hromada',
                    },
                    {
                        "uid": 758,
                        "name": 'Катеринівська територіальна громада',
                        "name_en": 'Katerynivska Hromada',
                    },
                    {
                        "uid": 759,
                        "name": 'Кетрисанівська територіальна громада',
                        "name_en": 'Ketrysanivska Hromada',
                    },
                    {
                        "uid": 760,
                        "name": 'Компаніївська територіальна громада',
                        "name_en": 'Kompaniivska Hromada',
                    },
                    {
                        "uid": 761,
                        "name": 'м. Кропивницький та Кропивницька територіальна громада',
                        "name_en": 'Kropyvnytskyi and Kropyvnytska Hromada',
                    },
                    {
                        "uid": 762,
                        "name": 'Новгородківська територіальна громада',
                        "name_en": 'Novhorodkivska Hromada',
                    },
                    {
                        "uid": 763,
                        "name": 'Олександрівська територіальна громада',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 764,
                        "name": 'Первозванівська територіальна громада',
                        "name_en": 'Pervozvanivska Hromada',
                    },
                    {
                        "uid": 765,
                        "name": 'Соколівська територіальна громада',
                        "name_en": 'Sokolivska Hromada',
                    },
                    {
                        "uid": 766,
                        "name": 'Суботцівська територіальна громада',
                        "name_en": 'Subottsivska Hromada',
                    },
                    {
                        "uid": 767,
                        "name": 'Устинівська територіальна громада',
                        "name_en": 'Ustynivska Hromada',
                    },
                ],
            },
            {
                "uid": 83,
                "name": 'Новоукраїнський район',
                "name_en": 'Novoukrainskyi Raion',
                "hromadas": [
                    {
                        "uid": 787,
                        "name": 'Ганнівська територіальна громада',
                        "name_en": 'Hannivska Hromada',
                    },
                    {
                        "uid": 788,
                        "name": 'Глодоська територіальна громада',
                        "name_en": 'Hlodoska Hromada',
                    },
                    {
                        "uid": 789,
                        "name": 'Добровеличківська територіальна громада',
                        "name_en": 'Dobrovelychkivska Hromada',
                    },
                    {
                        "uid": 790,
                        "name": 'Злинська територіальна громада',
                        "name_en": 'Zlynska Hromada',
                    },
                    {
                        "uid": 791,
                        "name": 'Маловисківська територіальна громада',
                        "name_en": 'Malovyskivska Hromada',
                    },
                    {
                        "uid": 792,
                        "name": 'Мар’янівська територіальна громада',
                        "name_en": 'Maryanivska Hromada',
                    },
                    {
                        "uid": 793,
                        "name": 'Новомиргородська територіальна громада',
                        "name_en": 'Novomyrhorodska Hromada',
                    },
                    {
                        "uid": 794,
                        "name": 'Новоукраїнська територіальна громада',
                        "name_en": 'Novoukrainska Hromada',
                    },
                    {
                        "uid": 796,
                        "name": 'Помічнянська територіальна громада',
                        "name_en": 'Pomichnianska Hromada',
                    },
                    {
                        "uid": 795,
                        "name": 'Піщанобрідська територіальна громада',
                        "name_en": 'Pishchanobridska Hromada',
                    },
                    {
                        "uid": 797,
                        "name": 'Рівнянська територіальна громада',
                        "name_en": 'Rivnianska Hromada',
                    },
                    {
                        "uid": 798,
                        "name": 'Смолінська територіальна громада',
                        "name_en": 'Smolinska Hromada',
                    },
                    {
                        "uid": 799,
                        "name": 'Тишківська територіальна громада',
                        "name_en": 'Tyshkivska Hromada',
                    },
                ],
            },
            {
                "uid": 80,
                "name": 'Олександрійський район',
                "name_en": 'Oleksandriiskyi Raion',
                "hromadas": [
                    {
                        "uid": 778,
                        "name": 'Великоандрусівська територіальна громада',
                        "name_en": 'Velykoandrusivska Hromada',
                    },
                    {
                        "uid": 779,
                        "name": 'Новопразька територіальна громада',
                        "name_en": 'Novoprazka Hromada',
                    },
                    {
                        "uid": 780,
                        "name": 'м. Олександрія та Олександрійська територіальна громада',
                        "name_en": 'Oleksandriia and Oleksandriiska Hromada',
                    },
                    {
                        "uid": 781,
                        "name": 'Онуфріївська територіальна громада',
                        "name_en": 'Onufriivska Hromada',
                    },
                    {
                        "uid": 782,
                        "name": 'Пантаївська територіальна громада',
                        "name_en": 'Pantaivska Hromada',
                    },
                    {
                        "uid": 783,
                        "name": 'Петрівська територіальна громада',
                        "name_en": 'Petrivska Hromada',
                    },
                    {
                        "uid": 784,
                        "name": 'Попельнастівська територіальна громада',
                        "name_en": 'Popelnastivska Hromada',
                    },
                    {
                        "uid": 785,
                        "name": 'Приютівська територіальна громада',
                        "name_en": 'Pryiutivska Hromada',
                    },
                    {
                        "uid": 786,
                        "name": 'м. Світловодськ та Світловодська територіальна громада',
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
                "name": 'Алчевський район',
                "name_en": 'Alchevskyi Raion',
                "hromadas": [
                    {
                        "uid": 1903,
                        "name": 'м. Алчевськ та Алчевська територіальна громада',
                        "name_en": 'Alchevsk and Alchevska Hromada',
                    },
                    {
                        "uid": 1911,
                        "name": "м. Зимогір'я та Зимогір'ївська територіальна громада",
                        "name_en": 'Zymohiria and Zymohirivska Hromada',
                    },
                    {
                        "uid": 1909,
                        "name": 'м. Кадіївка та Кадіївська територіальна громада',
                        "name_en": 'Kadiivka and Kadiivska Hromada',
                    },
                ],
            },
            {
                "uid": 1804,
                "name": 'Довжанський район',
                "name_en": 'Dovzhanskyi Raion',
                "hromadas": [
                    {
                        "uid": 1908,
                        "name": 'м. Довжанськ та Довжанська територіальна громада',
                        "name_en": 'Dovzhansk and Dovzhanska Hromada',
                    },
                    {
                        "uid": 1905,
                        "name": 'м. Сорокине та Сорокинська територіальна громада',
                        "name_en": 'Sorokyne and Sorokynska Hromada',
                    },
                ],
            },
            {
                "uid": 1801,
                "name": 'Луганський район',
                "name_en": 'Luhanskyi Raion',
                "hromadas": [
                    {
                        "uid": 1901,
                        "name": 'м. Луганськ та Луганська територіальна громада',
                        "name_en": 'Luhansk and Luhanska Hromada',
                    },
                    {
                        "uid": 1910,
                        "name": 'м. Лутугине та Лутугинська територіальна громада',
                        "name_en": 'Lutuhyne and Lutuhynska Hromada',
                    },
                    {
                        "uid": 1904,
                        "name": 'м. Молодогвардійськ та Молодогвардійська територіальна громада',
                        "name_en": 'Molodohvardiisk and Molodohvardiiska Hromada',
                    },
                ],
            },
            {
                "uid": 1802,
                "name": 'Ровеньківський район',
                "name_en": 'Rovenkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1902,
                        "name": 'м. Антрацит та Антрацитівська територіальна громада',
                        "name_en": 'Antratsyt and Antratsytivska Hromada',
                    },
                    {
                        "uid": 1907,
                        "name": 'м. Ровеньки та Ровеньківська територіальна громада',
                        "name_en": 'Rovenky and Rovenkivska Hromada',
                    },
                    {
                        "uid": 1906,
                        "name": 'м. Хрустальний та Хрустальненська територіальна громада',
                        "name_en": 'Khrustalnyi and Khrustalnenska Hromada',
                    },
                ],
            },
            {
                "uid": 85,
                "name": 'Сватівський район',
                "name_en": 'Svativskyi Raion',
                "hromadas": [
                    {
                        "uid": 808,
                        "name": 'Білокуракинська територіальна громада',
                        "name_en": 'Bilokurakynska Hromada',
                    },
                    {
                        "uid": 809,
                        "name": 'Коломийчиська територіальна громада',
                        "name_en": 'Kolomyichyska Hromada',
                    },
                    {
                        "uid": 810,
                        "name": 'Красноріченська територіальна громада',
                        "name_en": 'Krasnorichenska Hromada',
                    },
                    {
                        "uid": 811,
                        "name": 'Лозно-Олександрівська територіальна громада',
                        "name_en": 'Lozno-Oleksandrivska Hromada',
                    },
                    {
                        "uid": 812,
                        "name": 'Нижньодуванська територіальна громада',
                        "name_en": 'Nyzhnoduvanska Hromada',
                    },
                    {
                        "uid": 813,
                        "name": 'Сватівська територіальна громада',
                        "name_en": 'Svativska Hromada',
                    },
                    {
                        "uid": 814,
                        "name": 'Троїцька територіальна громада',
                        "name_en": 'Troitska Hromada',
                    },
                ],
            },
            {
                "uid": 86,
                "name": 'Старобільський район',
                "name_en": 'Starobilskyi Raion',
                "hromadas": [
                    {
                        "uid": 800,
                        "name": 'Біловодська територіальна громада',
                        "name_en": 'Bilovodska Hromada',
                    },
                    {
                        "uid": 801,
                        "name": 'Білолуцька територіальна громада',
                        "name_en": 'Bilolutska Hromada',
                    },
                    {
                        "uid": 802,
                        "name": 'Марківська територіальна громада',
                        "name_en": 'Markivska Hromada',
                    },
                    {
                        "uid": 803,
                        "name": 'Міловська територіальна громада',
                        "name_en": 'Milovska Hromada',
                    },
                    {
                        "uid": 804,
                        "name": 'Новопсковська територіальна громада',
                        "name_en": 'Novopskovska Hromada',
                    },
                    {
                        "uid": 805,
                        "name": 'Старобільська територіальна громада',
                        "name_en": 'Starobilska Hromada',
                    },
                    {
                        "uid": 806,
                        "name": 'Чмирівська територіальна громада',
                        "name_en": 'Chmyrivska Hromada',
                    },
                    {
                        "uid": 807,
                        "name": 'Шульгинська територіальна громада',
                        "name_en": 'Shulhynska Hromada',
                    },
                ],
            },
            {
                "uid": 84,
                "name": 'Сіверськодонецький район',
                "name_en": 'Siverskodonetskyi Raion',
                "hromadas": [
                    {
                        "uid": 815,
                        "name": 'Гірська територіальна громада',
                        "name_en": 'Hirska Hromada',
                    },
                    {
                        "uid": 816,
                        "name": 'м. Кремінна та Кремінська територіальна громада',
                        "name_en": 'Kreminna and Kreminska Hromada',
                    },
                    {
                        "uid": 817,
                        "name": 'м. Лисичанськ та Лисичанська територіальна громада',
                        "name_en": 'Lysychansk and Lysychanska Hromada',
                    },
                    {
                        "uid": 818,
                        "name": 'Попаснянська територіальна громада',
                        "name_en": 'Popasnianska Hromada',
                    },
                    {
                        "uid": 819,
                        "name": 'м. Рубіжне та Рубіжанська територіальна громада',
                        "name_en": 'Rubizhne and Rubizhanska Hromada',
                    },
                    {
                        "uid": 820,
                        "name": 'м. Сіверськодонецьк та Сіверськодонецька територіальна громада',
                        "name_en": 'Siverskodonetsk and Siverskodonetska Hromada',
                    },
                ],
            },
            {
                "uid": 87,
                "name": 'Щастинський район',
                "name_en": 'Shchastynskyi Raion',
                "hromadas": [
                    {
                        "uid": 821,
                        "name": 'Нижньотеплівська територіальна громада',
                        "name_en": 'Nyzhnoteplivska Hromada',
                    },
                    {
                        "uid": 822,
                        "name": 'Новоайдарська територіальна громада',
                        "name_en": 'Novoaidarska Hromada',
                    },
                    {
                        "uid": 823,
                        "name": 'Станично-Луганська територіальна громада',
                        "name_en": 'Stanychno-Luhanska Hromada',
                    },
                    {
                        "uid": 824,
                        "name": 'Широківська територіальна громада',
                        "name_en": 'Shyrokivska Hromada',
                    },
                    {
                        "uid": 825,
                        "name": 'Щастинська територіальна громада',
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
                "name": 'Дрогобицький район',
                "name_en": 'Drohobytskyi Raion',
                "hromadas": [
                    {
                        "uid": 867,
                        "name": 'м. Борислав та Бориславська територіальна громада',
                        "name_en": 'Boryslav and Boryslavska Hromada',
                    },
                    {
                        "uid": 868,
                        "name": 'м. Дрогобич та Дрогобицька територіальна громада',
                        "name_en": 'Drohobych and Drohobytska Hromada',
                    },
                    {
                        "uid": 869,
                        "name": 'Меденицька територіальна громада',
                        "name_en": 'Medenytska Hromada',
                    },
                    {
                        "uid": 870,
                        "name": 'Східницька територіальна громада',
                        "name_en": 'Skhidnytska Hromada',
                    },
                    {
                        "uid": 871,
                        "name": 'м. Трускавець та Трускавецька територіальна громада',
                        "name_en": 'Truskavets and Truskavetska Hromada',
                    },
                ],
            },
            {
                "uid": 94,
                "name": 'Золочівський район',
                "name_en": 'Zolochivskyi Raion',
                "hromadas": [
                    {
                        "uid": 872,
                        "name": 'Бродівська територіальна громада',
                        "name_en": 'Brodivska Hromada',
                    },
                    {
                        "uid": 873,
                        "name": 'Буська територіальна громада',
                        "name_en": 'Buska Hromada',
                    },
                    {
                        "uid": 874,
                        "name": 'Заболотцівська територіальна громада',
                        "name_en": 'Zabolottsivska Hromada',
                    },
                    {
                        "uid": 875,
                        "name": 'Золочівська територіальна громада',
                        "name_en": 'Zolochivska Hromada',
                    },
                    {
                        "uid": 876,
                        "name": 'Красненська територіальна громада',
                        "name_en": 'Krasnenska Hromada',
                    },
                    {
                        "uid": 878,
                        "name": 'Поморянська територіальна громада',
                        "name_en": 'Pomorianska Hromada',
                    },
                    {
                        "uid": 877,
                        "name": 'Підкамінська територіальна громада',
                        "name_en": 'Pidkaminska Hromada',
                    },
                ],
            },
            {
                "uid": 90,
                "name": 'Львівський район',
                "name_en": 'Lvivskyi Raion',
                "hromadas": [
                    {
                        "uid": 833,
                        "name": 'Бібрська територіальна громада',
                        "name_en": 'Bibrska Hromada',
                    },
                    {
                        "uid": 834,
                        "name": 'Великолюбінська територіальна громада',
                        "name_en": 'Velykoliubinska Hromada',
                    },
                    {
                        "uid": 835,
                        "name": 'Глинянська територіальна громада',
                        "name_en": 'Hlynianska Hromada',
                    },
                    {
                        "uid": 836,
                        "name": 'Городоцька територіальна громада',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 837,
                        "name": 'Давидівська територіальна громада',
                        "name_en": 'Davydivska Hromada',
                    },
                    {
                        "uid": 838,
                        "name": 'Добросинсько-Магерівська територіальна громада',
                        "name_en": 'Dobrosynsko-Maherivska Hromada',
                    },
                    {
                        "uid": 839,
                        "name": 'Жовківська територіальна громада',
                        "name_en": 'Zhovkivska Hromada',
                    },
                    {
                        "uid": 840,
                        "name": 'Жовтанецька територіальна громада',
                        "name_en": 'Zhovtanetska Hromada',
                    },
                    {
                        "uid": 841,
                        "name": 'Зимноводівська територіальна громада',
                        "name_en": 'Zymnovodivska Hromada',
                    },
                    {
                        "uid": 842,
                        "name": 'Кам’янка-Бузька територіальна громада',
                        "name_en": 'Kamyanka-Buzka Hromada',
                    },
                    {
                        "uid": 843,
                        "name": 'Комарнівська територіальна громада',
                        "name_en": 'Komarnivska Hromada',
                    },
                    {
                        "uid": 844,
                        "name": 'Куликівська територіальна громада',
                        "name_en": 'Kulykivska Hromada',
                    },
                    {
                        "uid": 845,
                        "name": 'м. Львів та Львівська територіальна громада',
                        "name_en": 'Lviv and Lvivska Hromada',
                    },
                    {
                        "uid": 846,
                        "name": 'Мурованська територіальна громада',
                        "name_en": 'Murovanska Hromada',
                    },
                    {
                        "uid": 847,
                        "name": 'Новояричівська територіальна громада',
                        "name_en": 'Novoiarychivska Hromada',
                    },
                    {
                        "uid": 848,
                        "name": 'Оброшинська територіальна громада',
                        "name_en": 'Obroshynska Hromada',
                    },
                    {
                        "uid": 849,
                        "name": 'Перемишлянська територіальна громада',
                        "name_en": 'Peremyshlianska Hromada',
                    },
                    {
                        "uid": 851,
                        "name": 'Пустомитівська територіальна громада',
                        "name_en": 'Pustomytivska Hromada',
                    },
                    {
                        "uid": 850,
                        "name": 'Підберізцівська територіальна громада',
                        "name_en": 'Pidberiztsivska Hromada',
                    },
                    {
                        "uid": 852,
                        "name": 'Рава-Руська територіальна громада',
                        "name_en": 'Rava-Ruska Hromada',
                    },
                    {
                        "uid": 853,
                        "name": 'Сокільницька територіальна громада',
                        "name_en": 'Sokilnytska Hromada',
                    },
                    {
                        "uid": 854,
                        "name": 'Солонківська територіальна громада',
                        "name_en": 'Solonkivska Hromada',
                    },
                    {
                        "uid": 855,
                        "name": 'Щирецька територіальна громада',
                        "name_en": 'Shchyretska Hromada',
                    },
                ],
            },
            {
                "uid": 88,
                "name": 'Самбірський район',
                "name_en": 'Sambirskyi Raion',
                "hromadas": [
                    {
                        "uid": 857,
                        "name": 'Боринська територіальна громада',
                        "name_en": 'Borynska Hromada',
                    },
                    {
                        "uid": 856,
                        "name": 'Бісковицька територіальна громада',
                        "name_en": 'Biskovytska Hromada',
                    },
                    {
                        "uid": 858,
                        "name": 'Добромильська територіальна громада',
                        "name_en": 'Dobromylska Hromada',
                    },
                    {
                        "uid": 859,
                        "name": 'Новокалинівська територіальна громада',
                        "name_en": 'Novokalynivska Hromada',
                    },
                    {
                        "uid": 860,
                        "name": 'Ралівська територіальна громада',
                        "name_en": 'Ralivska Hromada',
                    },
                    {
                        "uid": 861,
                        "name": 'Рудківська територіальна громада',
                        "name_en": 'Rudkivska Hromada',
                    },
                    {
                        "uid": 862,
                        "name": 'м. Самбір та Самбірська територіальна громада',
                        "name_en": 'Sambir and Sambirska Hromada',
                    },
                    {
                        "uid": 863,
                        "name": 'Старосамбірська територіальна громада',
                        "name_en": 'Starosambirska Hromada',
                    },
                    {
                        "uid": 864,
                        "name": 'Стрілківська територіальна громада',
                        "name_en": 'Strilkivska Hromada',
                    },
                    {
                        "uid": 865,
                        "name": 'Турківська територіальна громада',
                        "name_en": 'Turkivska Hromada',
                    },
                    {
                        "uid": 866,
                        "name": 'Хирівська територіальна громада',
                        "name_en": 'Khyrivska Hromada',
                    },
                ],
            },
            {
                "uid": 89,
                "name": 'Стрийський район',
                "name_en": 'Stryiskyi Raion',
                "hromadas": [
                    {
                        "uid": 879,
                        "name": 'Гніздичівська територіальна громада',
                        "name_en": 'Hnizdychivska Hromada',
                    },
                    {
                        "uid": 880,
                        "name": 'Грабовецько-Дулібівська територіальна громада',
                        "name_en": 'Hrabovetsko-Dulibivska Hromada',
                    },
                    {
                        "uid": 881,
                        "name": 'Жидачівська територіальна громада',
                        "name_en": 'Zhydachivska Hromada',
                    },
                    {
                        "uid": 882,
                        "name": 'Журавненська територіальна громада',
                        "name_en": 'Zhuravnenska Hromada',
                    },
                    {
                        "uid": 883,
                        "name": 'Козівська територіальна громада',
                        "name_en": 'Kozivska Hromada',
                    },
                    {
                        "uid": 884,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 885,
                        "name": 'м. Моршин та Моршинська територіальна громада',
                        "name_en": 'Morshyn and Morshynska Hromada',
                    },
                    {
                        "uid": 886,
                        "name": 'м. Новий Розділ та Новороздільська територіальна громада',
                        "name_en": 'Novyi Rozdil and Novorozdilska Hromada',
                    },
                    {
                        "uid": 887,
                        "name": 'Розвадівська територіальна громада',
                        "name_en": 'Rozvadivska Hromada',
                    },
                    {
                        "uid": 888,
                        "name": 'Сколівська територіальна громада',
                        "name_en": 'Skolivska Hromada',
                    },
                    {
                        "uid": 889,
                        "name": 'Славська територіальна громада',
                        "name_en": 'Slavska Hromada',
                    },
                    {
                        "uid": 890,
                        "name": 'м. Стрий та Стрийська територіальна громада',
                        "name_en": 'Stryi and Stryiska Hromada',
                    },
                    {
                        "uid": 891,
                        "name": 'Тростянецька територіальна громада',
                        "name_en": 'Trostianetska Hromada',
                    },
                    {
                        "uid": 892,
                        "name": 'Ходорівська територіальна громада',
                        "name_en": 'Khodorivska Hromada',
                    },
                ],
            },
            {
                "uid": 92,
                "name": 'Шептицький район',
                "name_en": 'Sheptytskyi Raion',
                "hromadas": [
                    {
                        "uid": 826,
                        "name": 'Белзька територіальна громада',
                        "name_en": 'Belzka Hromada',
                    },
                    {
                        "uid": 827,
                        "name": 'Великомостівська територіальна громада',
                        "name_en": 'Velykomostivska Hromada',
                    },
                    {
                        "uid": 828,
                        "name": 'Добротвірська територіальна громада',
                        "name_en": 'Dobrotvirska Hromada',
                    },
                    {
                        "uid": 829,
                        "name": 'Лопатинська територіальна громада',
                        "name_en": 'Lopatynska Hromada',
                    },
                    {
                        "uid": 830,
                        "name": 'Радехівська територіальна громада',
                        "name_en": 'Radekhivska Hromada',
                    },
                    {
                        "uid": 831,
                        "name": 'Сокальська територіальна громада',
                        "name_en": 'Sokalska Hromada',
                    },
                    {
                        "uid": 832,
                        "name": 'м. Шептицький та Шептицька територіальна громада',
                        "name_en": 'Sheptytskyi and Sheptytska Hromada',
                    },
                ],
            },
            {
                "uid": 93,
                "name": 'Яворівський район',
                "name_en": 'Yavorivskyi Raion',
                "hromadas": [
                    {
                        "uid": 894,
                        "name": 'Мостиська територіальна громада',
                        "name_en": 'Mostyska Hromada',
                    },
                    {
                        "uid": 895,
                        "name": 'Новояворівськ територіальна громада',
                        "name_en": 'Novoiavorivsk Hromada',
                    },
                    {
                        "uid": 896,
                        "name": 'Судововишнянська територіальна громада',
                        "name_en": 'Sudovovyshnianska Hromada',
                    },
                    {
                        "uid": 897,
                        "name": 'Шегинівська територіальна громада',
                        "name_en": 'Shehynivska Hromada',
                    },
                    {
                        "uid": 898,
                        "name": 'Яворівська територіальна громада',
                        "name_en": 'Yavorivska Hromada',
                    },
                    {
                        "uid": 893,
                        "name": 'Івано-Франківська територіальна громада',
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
                "name": 'Баштанський район',
                "name_en": 'Bashtanskyi Raion',
                "hromadas": [
                    {
                        "uid": 907,
                        "name": 'м. Баштанка та Баштанська територіальна громада',
                        "name_en": 'Bashtanka and Bashtanska Hromada',
                    },
                    {
                        "uid": 908,
                        "name": 'Березнегуватська територіальна громада',
                        "name_en": 'Bereznehuvatska Hromada',
                    },
                    {
                        "uid": 910,
                        "name": 'Володимирівська територіальна громада',
                        "name_en": 'Volodymyrivska Hromada',
                    },
                    {
                        "uid": 909,
                        "name": 'Вільнозапорізька територіальна громада',
                        "name_en": 'Vilnozaporizka Hromada',
                    },
                    {
                        "uid": 911,
                        "name": 'Горохівська територіальна громада',
                        "name_en": 'Horokhivska Hromada',
                    },
                    {
                        "uid": 913,
                        "name": 'Казанківська територіальна громада',
                        "name_en": 'Kazankivska Hromada',
                    },
                    {
                        "uid": 914,
                        "name": 'Новобузька територіальна громада',
                        "name_en": 'Novobuzka Hromada',
                    },
                    {
                        "uid": 915,
                        "name": 'Привільненська територіальна громада',
                        "name_en": 'Pryvilnenska Hromada',
                    },
                    {
                        "uid": 916,
                        "name": 'м. Снігурівка та Снігурівська територіальна громада',
                        "name_en": 'Snihurivka and Snihurivska Hromada',
                    },
                    {
                        "uid": 917,
                        "name": 'Софіївська територіальна громада',
                        "name_en": 'Sofiivska Hromada',
                    },
                    {
                        "uid": 918,
                        "name": 'Широківська територіальна громада',
                        "name_en": 'Shyrokivska Hromada',
                    },
                    {
                        "uid": 912,
                        "name": 'Інгульська територіальна громада',
                        "name_en": 'Inhulska Hromada',
                    },
                ],
            },
            {
                "uid": 95,
                "name": 'Вознесенський район',
                "name_en": 'Voznesenskyi Raion',
                "hromadas": [
                    {
                        "uid": 938,
                        "name": 'Братська територіальна громада',
                        "name_en": 'Bratska Hromada',
                    },
                    {
                        "uid": 939,
                        "name": 'Бузька територіальна громада',
                        "name_en": 'Buzka Hromada',
                    },
                    {
                        "uid": 940,
                        "name": 'Веселинівська територіальна громада',
                        "name_en": 'Veselynivska Hromada',
                    },
                    {
                        "uid": 941,
                        "name": 'м. Вознесенськ та Вознесенська територіальна громада',
                        "name_en": 'Voznesensk and Voznesenska Hromada',
                    },
                    {
                        "uid": 942,
                        "name": 'Доманівська територіальна громада',
                        "name_en": 'Domanivska Hromada',
                    },
                    {
                        "uid": 943,
                        "name": 'Дорошівська територіальна громада',
                        "name_en": 'Doroshivska Hromada',
                    },
                    {
                        "uid": 945,
                        "name": 'Мостівська територіальна громада',
                        "name_en": 'Mostivska Hromada',
                    },
                    {
                        "uid": 946,
                        "name": "Новомар'ївська територіальна громада",
                        "name_en": 'Novomarivska Hromada',
                    },
                    {
                        "uid": 947,
                        "name": 'Олександрівська територіальна громада',
                        "name_en": 'Oleksandrivska Hromada',
                    },
                    {
                        "uid": 948,
                        "name": 'Прибужанівська територіальна громада',
                        "name_en": 'Prybuzhanivska Hromada',
                    },
                    {
                        "uid": 949,
                        "name": 'Прибузька територіальна громада',
                        "name_en": 'Prybuzka Hromada',
                    },
                    {
                        "uid": 950,
                        "name": 'м. Южноукраїнськ та Южноукраїнська територіальна громада',
                        "name_en": 'Yuzhnoukrainsk and Yuzhnoukrainska Hromada',
                    },
                    {
                        "uid": 944,
                        "name": 'Єланецька територіальна громада',
                        "name_en": 'Yelanetska Hromada',
                    },
                ],
            },
            {
                "uid": 98,
                "name": 'Миколаївський район',
                "name_en": 'Mykolaivskyi Raion',
                "hromadas": [
                    {
                        "uid": 919,
                        "name": 'Березанська територіальна громада',
                        "name_en": 'Berezanska Hromada',
                    },
                    {
                        "uid": 920,
                        "name": 'Веснянська територіальна громада',
                        "name_en": 'Vesnianska Hromada',
                    },
                    {
                        "uid": 921,
                        "name": 'Воскресенська територіальна громада',
                        "name_en": 'Voskresenska Hromada',
                    },
                    {
                        "uid": 922,
                        "name": 'Галицинівська територіальна громада',
                        "name_en": 'Halytsynivska Hromada',
                    },
                    {
                        "uid": 923,
                        "name": 'Коблівська територіальна громада',
                        "name_en": 'Koblivska Hromada',
                    },
                    {
                        "uid": 924,
                        "name": 'Костянтинівська територіальна громада',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 925,
                        "name": 'Куцурубська територіальна громада',
                        "name_en": 'Kutsurubska Hromada',
                    },
                    {
                        "uid": 926,
                        "name": 'м. Миколаїв та Миколаївська територіальна громада',
                        "name_en": 'Mykolaiv and Mykolaivska Hromada',
                    },
                    {
                        "uid": 927,
                        "name": 'Мішково-Погорілівська територіальна громада',
                        "name_en": 'Mishkovo-Pohorilivska Hromada',
                    },
                    {
                        "uid": 928,
                        "name": 'Нечаянська територіальна громада',
                        "name_en": 'Nechaianska Hromada',
                    },
                    {
                        "uid": 929,
                        "name": 'м. Нова-Одеса та Новоодеська територіальна громада',
                        "name_en": 'Nova-Odesa and Novoodeska Hromada',
                    },
                    {
                        "uid": 930,
                        "name": 'Ольшанська територіальна громада',
                        "name_en": 'Olshanska Hromada',
                    },
                    {
                        "uid": 931,
                        "name": 'м. Очаків та Очаківська територіальна громада',
                        "name_en": 'Ochakiv and Ochakivska Hromada',
                    },
                    {
                        "uid": 932,
                        "name": 'Первомайська територіальна громада',
                        "name_en": 'Pervomaiska Hromada',
                    },
                    {
                        "uid": 933,
                        "name": 'Радсадівська територіальна громада',
                        "name_en": 'Radsadivska Hromada',
                    },
                    {
                        "uid": 934,
                        "name": 'Степівська територіальна громада',
                        "name_en": 'Stepivska Hromada',
                    },
                    {
                        "uid": 935,
                        "name": 'Сухоєланецька територіальна громада',
                        "name_en": 'Sukhoielanetska Hromada',
                    },
                    {
                        "uid": 936,
                        "name": 'Чорноморська територіальна громада',
                        "name_en": 'Chornomorska Hromada',
                    },
                    {
                        "uid": 937,
                        "name": 'Шевченківська територіальна громада',
                        "name_en": 'Shevchenkivska Hromada',
                    },
                ],
            },
            {
                "uid": 97,
                "name": 'Первомайський район',
                "name_en": 'Pervomaiskyi Raion',
                "hromadas": [
                    {
                        "uid": 899,
                        "name": 'Арбузинська територіальна громада',
                        "name_en": 'Arbuzynska Hromada',
                    },
                    {
                        "uid": 900,
                        "name": 'Благодатненська територіальна громада',
                        "name_en": 'Blahodatnenska Hromada',
                    },
                    {
                        "uid": 901,
                        "name": 'Врадіївська територіальна громада',
                        "name_en": 'Vradiivska Hromada',
                    },
                    {
                        "uid": 902,
                        "name": "Кам'яномостівська територіальна громада",
                        "name_en": 'Kamianomostivska Hromada',
                    },
                    {
                        "uid": 903,
                        "name": 'Кривоозерська територіальна громада',
                        "name_en": 'Kryvoozerska Hromada',
                    },
                    {
                        "uid": 904,
                        "name": 'Мигіївська територіальна громада',
                        "name_en": 'Myhiivska Hromada',
                    },
                    {
                        "uid": 905,
                        "name": 'м. Первомайськ та Первомайська територіальна громада',
                        "name_en": 'Pervomaisk and Pervomaiska Hromada',
                    },
                    {
                        "uid": 906,
                        "name": 'Синюхинобрідська територіальна громада',
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
                "name": 'Березівський район',
                "name_en": 'Berezivskyi Raion',
                "hromadas": [
                    {
                        "uid": 985,
                        "name": 'Андрієво-Іванівська територіальна громада',
                        "name_en": 'Andriievo-Ivanivska Hromada',
                    },
                    {
                        "uid": 986,
                        "name": 'Березівська територіальна громада',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 987,
                        "name": 'Великобуялицька територіальна громада',
                        "name_en": 'Velykobuialytska Hromada',
                    },
                    {
                        "uid": 988,
                        "name": 'Знам’янська територіальна громада',
                        "name_en": 'Znamyanska Hromada',
                    },
                    {
                        "uid": 990,
                        "name": 'Коноплянська територіальна громада',
                        "name_en": 'Konoplianska Hromada',
                    },
                    {
                        "uid": 991,
                        "name": 'Курісовська територіальна громада',
                        "name_en": 'Kurisovska Hromada',
                    },
                    {
                        "uid": 992,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 993,
                        "name": 'Новокальчевська територіальна громада',
                        "name_en": 'Novokalchevska Hromada',
                    },
                    {
                        "uid": 994,
                        "name": 'Петровірівська територіальна громада',
                        "name_en": 'Petrovirivska Hromada',
                    },
                    {
                        "uid": 995,
                        "name": 'Раухівська територіальна громада',
                        "name_en": 'Raukhivska Hromada',
                    },
                    {
                        "uid": 996,
                        "name": 'Розквітівська територіальна громада',
                        "name_en": 'Rozkvitivska Hromada',
                    },
                    {
                        "uid": 997,
                        "name": 'Старомаяківська територіальна громада',
                        "name_en": 'Staromaiakivska Hromada',
                    },
                    {
                        "uid": 998,
                        "name": 'Стрюківська територіальна громада',
                        "name_en": 'Striukivska Hromada',
                    },
                    {
                        "uid": 999,
                        "name": 'Чогодарівська територіальна громада',
                        "name_en": 'Chohodarivska Hromada',
                    },
                    {
                        "uid": 1000,
                        "name": 'Ширяївська територіальна громада',
                        "name_en": 'Shyriaivska Hromada',
                    },
                    {
                        "uid": 989,
                        "name": 'Іванівська територіальна громада',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
            {
                "uid": 105,
                "name": 'Болградський район',
                "name_en": 'Bolhradskyi Raion',
                "hromadas": [
                    {
                        "uid": 1001,
                        "name": 'Арцизька територіальна громада',
                        "name_en": 'Artsyzka Hromada',
                    },
                    {
                        "uid": 1002,
                        "name": 'Болградська територіальна громада',
                        "name_en": 'Bolhradska Hromada',
                    },
                    {
                        "uid": 1003,
                        "name": 'Бородінська територіальна громада',
                        "name_en": 'Borodinska Hromada',
                    },
                    {
                        "uid": 1004,
                        "name": 'Василівська територіальна громада',
                        "name_en": 'Vasylivska Hromada',
                    },
                    {
                        "uid": 1005,
                        "name": 'Городненська територіальна громада',
                        "name_en": 'Horodnenska Hromada',
                    },
                    {
                        "uid": 1006,
                        "name": 'Криниченська територіальна громада',
                        "name_en": 'Krynychenska Hromada',
                    },
                    {
                        "uid": 1007,
                        "name": 'Кубейська територіальна громада',
                        "name_en": 'Kubeiska Hromada',
                    },
                    {
                        "uid": 1008,
                        "name": 'Павлівська територіальна громада',
                        "name_en": 'Pavlivska Hromada',
                    },
                    {
                        "uid": 1009,
                        "name": 'Тарутинська територіальна громада',
                        "name_en": 'Tarutynska Hromada',
                    },
                    {
                        "uid": 1010,
                        "name": 'Теплицька територіальна громада',
                        "name_en": 'Teplytska Hromada',
                    },
                ],
            },
            {
                "uid": 102,
                "name": 'Білгород-Дністровський район',
                "name_en": 'Bilhorod-Dnistrovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1011,
                        "name": 'м. Білгород-Дністровський та Білгород-Дністровська територіальна громада',
                        "name_en": 'Bilhorod-Dnistrovskyi and Bilhorod-Dnistrovska Hromada',
                    },
                    {
                        "uid": 1012,
                        "name": 'Дивізійська територіальна громада',
                        "name_en": 'Dyviziiska Hromada',
                    },
                    {
                        "uid": 1013,
                        "name": 'Кароліно-Бугазька територіальна громада',
                        "name_en": 'Karolino-Buhazka Hromada',
                    },
                    {
                        "uid": 1014,
                        "name": 'Кулевчанська територіальна громада',
                        "name_en": 'Kulevchanska Hromada',
                    },
                    {
                        "uid": 1015,
                        "name": 'Лиманська територіальна громада',
                        "name_en": 'Lymanska Hromada',
                    },
                    {
                        "uid": 1016,
                        "name": 'Маразліївська територіальна громада',
                        "name_en": 'Marazliivska Hromada',
                    },
                    {
                        "uid": 1017,
                        "name": 'Мологівська територіальна громада',
                        "name_en": 'Molohivska Hromada',
                    },
                    {
                        "uid": 1018,
                        "name": 'Петропавлівська територіальна громада',
                        "name_en": 'Petropavlivska Hromada',
                    },
                    {
                        "uid": 1019,
                        "name": 'Плахтіївська територіальна громада',
                        "name_en": 'Plakhtiivska Hromada',
                    },
                    {
                        "uid": 1020,
                        "name": 'Саратська територіальна громада',
                        "name_en": 'Saratska Hromada',
                    },
                    {
                        "uid": 1021,
                        "name": 'Сергіївська територіальна громада',
                        "name_en": 'Serhiivska Hromada',
                    },
                    {
                        "uid": 1022,
                        "name": 'Старокозацька територіальна громада',
                        "name_en": 'Starokozatska Hromada',
                    },
                    {
                        "uid": 1023,
                        "name": 'Татарбунарська територіальна громада',
                        "name_en": 'Tatarbunarska Hromada',
                    },
                    {
                        "uid": 1024,
                        "name": 'Тузлівська територіальна громада',
                        "name_en": 'Tuzlivska Hromada',
                    },
                    {
                        "uid": 1025,
                        "name": 'Успенівська територіальна громада',
                        "name_en": 'Uspenivska Hromada',
                    },
                    {
                        "uid": 1026,
                        "name": 'Шабівська територіальна громада',
                        "name_en": 'Shabivska Hromada',
                    },
                ],
            },
            {
                "uid": 104,
                "name": 'Одеський район',
                "name_en": 'Odeskyi Raion',
                "hromadas": [
                    {
                        "uid": 951,
                        "name": 'Авангардівська територіальна громада',
                        "name_en": 'Avanhardivska Hromada',
                    },
                    {
                        "uid": 952,
                        "name": 'Біляївська територіальна громада',
                        "name_en": 'Biliaivska Hromada',
                    },
                    {
                        "uid": 953,
                        "name": 'Великодальницька територіальна громада',
                        "name_en": 'Velykodalnytska Hromada',
                    },
                    {
                        "uid": 954,
                        "name": 'Великодолинська територіальна громада',
                        "name_en": 'Velykodolynska Hromada',
                    },
                    {
                        "uid": 955,
                        "name": 'Вигодянська територіальна громада',
                        "name_en": 'Vyhodianska Hromada',
                    },
                    {
                        "uid": 956,
                        "name": 'Визирська територіальна громада',
                        "name_en": 'Vyzyrska Hromada',
                    },
                    {
                        "uid": 957,
                        "name": 'Дальницька територіальна громада',
                        "name_en": 'Dalnytska Hromada',
                    },
                    {
                        "uid": 958,
                        "name": 'Дачненська територіальна громада',
                        "name_en": 'Dachnenska Hromada',
                    },
                    {
                        "uid": 959,
                        "name": 'Доброславська територіальна громада',
                        "name_en": 'Dobroslavska Hromada',
                    },
                    {
                        "uid": 960,
                        "name": 'Красносільська територіальна громада',
                        "name_en": 'Krasnosilska Hromada',
                    },
                    {
                        "uid": 961,
                        "name": 'Маяківська територіальна громада',
                        "name_en": 'Maiakivska Hromada',
                    },
                    {
                        "uid": 962,
                        "name": 'Нерубайська територіальна громада',
                        "name_en": 'Nerubaiska Hromada',
                    },
                    {
                        "uid": 963,
                        "name": 'Овідіопольська територіальна громада',
                        "name_en": 'Ovidiopolska Hromada',
                    },
                    {
                        "uid": 964,
                        "name": 'м. Одеса та Одеська територіальна громада',
                        "name_en": 'Odesa and Odeska Hromada',
                    },
                    {
                        "uid": 971,
                        "name": 'м. Південне та Південна територіальна громада',
                        "name_en": 'Pivdenne and Pivdenna Hromada',
                    },
                    {
                        "uid": 965,
                        "name": 'Таїровська територіальна громада',
                        "name_en": 'Tairovska Hromada',
                    },
                    {
                        "uid": 966,
                        "name": 'Теплодарська територіальна громада',
                        "name_en": 'Teplodarska Hromada',
                    },
                    {
                        "uid": 967,
                        "name": 'Усатівська територіальна громада',
                        "name_en": 'Usativska Hromada',
                    },
                    {
                        "uid": 968,
                        "name": 'Фонтанська територіальна громада',
                        "name_en": 'Fontanska Hromada',
                    },
                    {
                        "uid": 969,
                        "name": 'м. Чорноморськ та Чорноморська територіальна громада',
                        "name_en": 'Chornomorsk and Chornomorska Hromada',
                    },
                    {
                        "uid": 970,
                        "name": 'Чорноморська територіальна громада',
                        "name_en": 'Chornomorska Hromada',
                    },
                    {
                        "uid": 972,
                        "name": 'Яськівська територіальна громада',
                        "name_en": 'Yaskivska Hromada',
                    },
                ],
            },
            {
                "uid": 99,
                "name": 'Подільський район',
                "name_en": 'Podilskyi Raion',
                "hromadas": [
                    {
                        "uid": 973,
                        "name": 'Ананьївська територіальна громада',
                        "name_en": 'Ananivska Hromada',
                    },
                    {
                        "uid": 974,
                        "name": 'Балтська територіальна громада',
                        "name_en": 'Baltska Hromada',
                    },
                    {
                        "uid": 975,
                        "name": 'Долинська територіальна громада',
                        "name_en": 'Dolynska Hromada',
                    },
                    {
                        "uid": 976,
                        "name": 'Зеленогірська територіальна громада',
                        "name_en": 'Zelenohirska Hromada',
                    },
                    {
                        "uid": 977,
                        "name": 'Кодимська територіальна громада',
                        "name_en": 'Kodymska Hromada',
                    },
                    {
                        "uid": 978,
                        "name": 'Куяльницька територіальна громада',
                        "name_en": 'Kuialnytska Hromada',
                    },
                    {
                        "uid": 979,
                        "name": 'Любашівська територіальна громада',
                        "name_en": 'Liubashivska Hromada',
                    },
                    {
                        "uid": 980,
                        "name": 'Окнянська територіальна громада',
                        "name_en": 'Oknianska Hromada',
                    },
                    {
                        "uid": 982,
                        "name": 'Подільська територіальна громада',
                        "name_en": 'Podilska Hromada',
                    },
                    {
                        "uid": 981,
                        "name": 'Піщанська територіальна громада',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 983,
                        "name": 'Савранська територіальна громада',
                        "name_en": 'Savranska Hromada',
                    },
                    {
                        "uid": 984,
                        "name": 'Слобідська територіальна громада',
                        "name_en": 'Slobidska Hromada',
                    },
                ],
            },
            {
                "uid": 103,
                "name": 'Роздільнянський район',
                "name_en": 'Rozdilnianskyi Raion',
                "hromadas": [
                    {
                        "uid": 1027,
                        "name": 'Великомихайлівська територіальна громада',
                        "name_en": 'Velykomykhailivska Hromada',
                    },
                    {
                        "uid": 1028,
                        "name": 'Великоплосківська територіальна громада',
                        "name_en": 'Velykoploskivska Hromada',
                    },
                    {
                        "uid": 1029,
                        "name": 'Затишанська територіальна громада',
                        "name_en": 'Zatyshanska Hromada',
                    },
                    {
                        "uid": 1030,
                        "name": 'Захарівська територіальна громада',
                        "name_en": 'Zakharivska Hromada',
                    },
                    {
                        "uid": 1031,
                        "name": 'Лиманська територіальна громада',
                        "name_en": 'Lymanska Hromada',
                    },
                    {
                        "uid": 1032,
                        "name": 'Новоборисівська територіальна громада',
                        "name_en": 'Novoborysivska Hromada',
                    },
                    {
                        "uid": 1033,
                        "name": 'Роздільнянська територіальна громада',
                        "name_en": 'Rozdilnianska Hromada',
                    },
                    {
                        "uid": 1034,
                        "name": 'Степанівська територіальна громада',
                        "name_en": 'Stepanivska Hromada',
                    },
                    {
                        "uid": 1035,
                        "name": 'Цебриківська територіальна громада',
                        "name_en": 'Tsebrykivska Hromada',
                    },
                ],
            },
            {
                "uid": 101,
                "name": 'Ізмаїльський район',
                "name_en": 'Izmailskyi Raion',
                "hromadas": [
                    {
                        "uid": 1036,
                        "name": 'Вилківська територіальна громада',
                        "name_en": 'Vylkivska Hromada',
                    },
                    {
                        "uid": 1038,
                        "name": 'Кілійська територіальна громада',
                        "name_en": 'Kiliiska Hromada',
                    },
                    {
                        "uid": 1039,
                        "name": 'Ренійська територіальна громада',
                        "name_en": 'Reniiska Hromada',
                    },
                    {
                        "uid": 1040,
                        "name": "Саф'янівська територіальна громада",
                        "name_en": 'Safianivska Hromada',
                    },
                    {
                        "uid": 1041,
                        "name": 'Суворовська територіальна громада',
                        "name_en": 'Suvorovska Hromada',
                    },
                    {
                        "uid": 1037,
                        "name": 'м. Ізмаїл та Ізмаїльська територіальна громада',
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
                "name": 'Кременчуцький район',
                "name_en": 'Kremenchutskyi Raion',
                "hromadas": [
                    {
                        "uid": 1083,
                        "name": 'Глобинська територіальна громада',
                        "name_en": 'Hlobynska Hromada',
                    },
                    {
                        "uid": 1084,
                        "name": 'м. Горішні плавні та Горішньоплавнівська територіальна громада',
                        "name_en": 'Horishni plavni and Horishnoplavnivska Hromada',
                    },
                    {
                        "uid": 1085,
                        "name": 'Градизька територіальна громада',
                        "name_en": 'Hradyzka Hromada',
                    },
                    {
                        "uid": 1086,
                        "name": "Кам'янопотоківська територіальна громада",
                        "name_en": 'Kamianopotokivska Hromada',
                    },
                    {
                        "uid": 1087,
                        "name": 'Козельщинська територіальна громада',
                        "name_en": 'Kozelshchynska Hromada',
                    },
                    {
                        "uid": 1088,
                        "name": 'м. Кременчук та Кременчуцька територіальна громада',
                        "name_en": 'Kremenchuk and Kremenchutska Hromada',
                    },
                    {
                        "uid": 1089,
                        "name": 'Новогалещинська територіальна громада',
                        "name_en": 'Novohaleshchynska Hromada',
                    },
                    {
                        "uid": 1090,
                        "name": 'Оболонська територіальна громада',
                        "name_en": 'Obolonska Hromada',
                    },
                    {
                        "uid": 1091,
                        "name": 'Омельницька територіальна громада',
                        "name_en": 'Omelnytska Hromada',
                    },
                    {
                        "uid": 1093,
                        "name": 'Пришибська територіальна громада',
                        "name_en": 'Pryshybska Hromada',
                    },
                    {
                        "uid": 1092,
                        "name": 'Піщанська територіальна громада',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 1094,
                        "name": 'Семенівська територіальна громада',
                        "name_en": 'Semenivska Hromada',
                    },
                ],
            },
            {
                "uid": 106,
                "name": 'Лубенський район',
                "name_en": 'Lubenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1095,
                        "name": 'Гребінківська територіальна громада',
                        "name_en": 'Hrebinkivska Hromada',
                    },
                    {
                        "uid": 1096,
                        "name": 'м. Лубни та Лубенська територіальна громада',
                        "name_en": 'Lubny and Lubenska Hromada',
                    },
                    {
                        "uid": 1097,
                        "name": 'Новооржицька територіальна громада',
                        "name_en": 'Novoorzhytska Hromada',
                    },
                    {
                        "uid": 1098,
                        "name": 'Оржицька територіальна громада',
                        "name_en": 'Orzhytska Hromada',
                    },
                    {
                        "uid": 1099,
                        "name": 'м. Пирятин та Пирятинська територіальна громада',
                        "name_en": 'Pyriatyn and Pyriatynska Hromada',
                    },
                    {
                        "uid": 1100,
                        "name": 'Хорольська територіальна громада',
                        "name_en": 'Khorolska Hromada',
                    },
                    {
                        "uid": 1101,
                        "name": 'Чорнухинська територіальна громада',
                        "name_en": 'Chornukhynska Hromada',
                    },
                ],
            },
            {
                "uid": 108,
                "name": 'Миргородський район',
                "name_en": 'Myrhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 1066,
                        "name": 'Білоцерківська територіальна громада',
                        "name_en": 'Bilotserkivska Hromada',
                    },
                    {
                        "uid": 1067,
                        "name": 'Великобагачанська територіальна громада',
                        "name_en": 'Velykobahachanska Hromada',
                    },
                    {
                        "uid": 1068,
                        "name": 'Великобудищанська територіальна громада',
                        "name_en": 'Velykobudyshchanska Hromada',
                    },
                    {
                        "uid": 1069,
                        "name": 'Великосорочинська територіальна громада',
                        "name_en": 'Velykosorochynska Hromada',
                    },
                    {
                        "uid": 1070,
                        "name": 'Гадяцька територіальна громада',
                        "name_en": 'Hadiatska Hromada',
                    },
                    {
                        "uid": 1071,
                        "name": 'Гоголівська територіальна громада',
                        "name_en": 'Hoholivska Hromada',
                    },
                    {
                        "uid": 1072,
                        "name": 'Заводська територіальна громада',
                        "name_en": 'Zavodska Hromada',
                    },
                    {
                        "uid": 1073,
                        "name": 'Комишнянська територіальна громада',
                        "name_en": 'Komyshnianska Hromada',
                    },
                    {
                        "uid": 1074,
                        "name": 'Краснолуцька територіальна громада',
                        "name_en": 'Krasnolutska Hromada',
                    },
                    {
                        "uid": 1075,
                        "name": 'м. Лохвиця та Лохвицька територіальна громада',
                        "name_en": 'Lokhvytsia and Lokhvytska Hromada',
                    },
                    {
                        "uid": 1076,
                        "name": 'Лютенська територіальна громада',
                        "name_en": 'Liutenska Hromada',
                    },
                    {
                        "uid": 1077,
                        "name": 'м. Миргород та Миргородська територіальна громада',
                        "name_en": 'Myrhorod and Myrhorodska Hromada',
                    },
                    {
                        "uid": 1078,
                        "name": 'Петрівсько-Роменська територіальна громада',
                        "name_en": 'Petrivsko-Romenska Hromada',
                    },
                    {
                        "uid": 1079,
                        "name": 'Ромоданівська територіальна громада',
                        "name_en": 'Romodanivska Hromada',
                    },
                    {
                        "uid": 1080,
                        "name": 'Сенчанська територіальна громада',
                        "name_en": 'Senchanska Hromada',
                    },
                    {
                        "uid": 1081,
                        "name": 'Сергіївська територіальна громада',
                        "name_en": 'Serhiivska Hromada',
                    },
                    {
                        "uid": 1082,
                        "name": 'Шишацька територіальна громада',
                        "name_en": 'Shyshatska Hromada',
                    },
                ],
            },
            {
                "uid": 109,
                "name": 'Полтавський район',
                "name_en": 'Poltavskyi Raion',
                "hromadas": [
                    {
                        "uid": 1042,
                        "name": 'Білицька територіальна громада',
                        "name_en": 'Bilytska Hromada',
                    },
                    {
                        "uid": 1043,
                        "name": 'Великорублівська територіальна громада',
                        "name_en": 'Velykorublivska Hromada',
                    },
                    {
                        "uid": 1044,
                        "name": 'Диканьська територіальна громада',
                        "name_en": 'Dykanska Hromada',
                    },
                    {
                        "uid": 1045,
                        "name": 'Драбинівська територіальна громада',
                        "name_en": 'Drabynivska Hromada',
                    },
                    {
                        "uid": 1046,
                        "name": 'Зіньківська територіальна громада',
                        "name_en": 'Zinkivska Hromada',
                    },
                    {
                        "uid": 1047,
                        "name": 'Карлівська територіальна громада',
                        "name_en": 'Karlivska Hromada',
                    },
                    {
                        "uid": 1048,
                        "name": 'Кобеляцька територіальна громада',
                        "name_en": 'Kobeliatska Hromada',
                    },
                    {
                        "uid": 1049,
                        "name": 'Коломацька територіальна громада',
                        "name_en": 'Kolomatska Hromada',
                    },
                    {
                        "uid": 1050,
                        "name": 'Котелевська територіальна громада',
                        "name_en": 'Kotelevska Hromada',
                    },
                    {
                        "uid": 1051,
                        "name": 'Ланнівська територіальна громада',
                        "name_en": 'Lannivska Hromada',
                    },
                    {
                        "uid": 1052,
                        "name": 'Мартинівська територіальна громада',
                        "name_en": 'Martynivska Hromada',
                    },
                    {
                        "uid": 1053,
                        "name": 'Мачухівська територіальна громада',
                        "name_en": 'Machukhivska Hromada',
                    },
                    {
                        "uid": 1054,
                        "name": 'Машівська територіальна громада',
                        "name_en": 'Mashivska Hromada',
                    },
                    {
                        "uid": 1055,
                        "name": 'Михайлівська територіальна громада',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 1056,
                        "name": 'Нехворощанська територіальна громада',
                        "name_en": 'Nekhvoroshchanska Hromada',
                    },
                    {
                        "uid": 1057,
                        "name": 'Новосанжарська територіальна громада',
                        "name_en": 'Novosanzharska Hromada',
                    },
                    {
                        "uid": 1058,
                        "name": 'Новоселівська територіальна громада',
                        "name_en": 'Novoselivska Hromada',
                    },
                    {
                        "uid": 1059,
                        "name": 'Опішнянська територіальна громада',
                        "name_en": 'Opishnianska Hromada',
                    },
                    {
                        "uid": 1060,
                        "name": 'м. Полтава та Полтавська територіальна громада',
                        "name_en": 'Poltava and Poltavska Hromada',
                    },
                    {
                        "uid": 1061,
                        "name": 'Решетилівська територіальна громада',
                        "name_en": 'Reshetylivska Hromada',
                    },
                    {
                        "uid": 1062,
                        "name": 'Скороходівська територіальна громада',
                        "name_en": 'Skorokhodivska Hromada',
                    },
                    {
                        "uid": 1063,
                        "name": 'Терешківська територіальна громада',
                        "name_en": 'Tereshkivska Hromada',
                    },
                    {
                        "uid": 1064,
                        "name": 'Чутівська територіальна громада',
                        "name_en": 'Chutivska Hromada',
                    },
                    {
                        "uid": 1065,
                        "name": 'Щербанівська територіальна громада',
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
                "name": 'Вараський район',
                "name_en": 'Varaskyi Raion',
                "hromadas": [
                    {
                        "uid": 1102,
                        "name": 'Антонівська територіальна громада',
                        "name_en": 'Antonivska Hromada',
                    },
                    {
                        "uid": 1103,
                        "name": 'м. Вараш та Вараська територіальна громада',
                        "name_en": 'Varash and Varaska Hromada',
                    },
                    {
                        "uid": 1104,
                        "name": 'Володимирецька територіальна громада',
                        "name_en": 'Volodymyretska Hromada',
                    },
                    {
                        "uid": 1105,
                        "name": 'Зарічненська територіальна громада',
                        "name_en": 'Zarichnenska Hromada',
                    },
                    {
                        "uid": 1106,
                        "name": 'Каноницька територіальна громада',
                        "name_en": 'Kanonytska Hromada',
                    },
                    {
                        "uid": 1107,
                        "name": 'Локницька територіальна громада',
                        "name_en": 'Loknytska Hromada',
                    },
                    {
                        "uid": 1108,
                        "name": 'Полицька територіальна громада',
                        "name_en": 'Polytska Hromada',
                    },
                    {
                        "uid": 1109,
                        "name": 'Рафалівська територіальна громада',
                        "name_en": 'Rafalivska Hromada',
                    },
                ],
            },
            {
                "uid": 111,
                "name": 'Дубенський район',
                "name_en": 'Dubenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1147,
                        "name": 'Бокіймівська територіальна громада',
                        "name_en": 'Bokiimivska Hromada',
                    },
                    {
                        "uid": 1148,
                        "name": 'Боремельська територіальна громада',
                        "name_en": 'Boremelska Hromada',
                    },
                    {
                        "uid": 1149,
                        "name": 'Варковицька територіальна громада',
                        "name_en": 'Varkovytska Hromada',
                    },
                    {
                        "uid": 1150,
                        "name": 'Вербська територіальна громада',
                        "name_en": 'Verbska Hromada',
                    },
                    {
                        "uid": 1151,
                        "name": 'Демидівська територіальна громада',
                        "name_en": 'Demydivska Hromada',
                    },
                    {
                        "uid": 1152,
                        "name": 'м. Дубно та Дубенська територіальна громада',
                        "name_en": 'Dubno and Dubenska Hromada',
                    },
                    {
                        "uid": 1153,
                        "name": 'Козинська територіальна громада',
                        "name_en": 'Kozynska Hromada',
                    },
                    {
                        "uid": 1154,
                        "name": 'Крупецька територіальна громада',
                        "name_en": 'Krupetska Hromada',
                    },
                    {
                        "uid": 1155,
                        "name": 'Мирогощанська територіальна громада',
                        "name_en": 'Myrohoshchanska Hromada',
                    },
                    {
                        "uid": 1156,
                        "name": 'Млинівська територіальна громада',
                        "name_en": 'Mlynivska Hromada',
                    },
                    {
                        "uid": 1157,
                        "name": 'Острожецька територіальна громада',
                        "name_en": 'Ostrozhetska Hromada',
                    },
                    {
                        "uid": 1159,
                        "name": 'Повчанська територіальна громада',
                        "name_en": 'Povchanska Hromada',
                    },
                    {
                        "uid": 1160,
                        "name": 'Привільненська територіальна громада',
                        "name_en": 'Pryvilnenska Hromada',
                    },
                    {
                        "uid": 1158,
                        "name": 'Підлозцівська територіальна громада',
                        "name_en": 'Pidloztsivska Hromada',
                    },
                    {
                        "uid": 1161,
                        "name": 'Радивилівська територіальна громада',
                        "name_en": 'Radyvylivska Hromada',
                    },
                    {
                        "uid": 1162,
                        "name": 'Семидубська територіальна громада',
                        "name_en": 'Semydubska Hromada',
                    },
                    {
                        "uid": 1163,
                        "name": 'Смизька територіальна громада',
                        "name_en": 'Smyzka Hromada',
                    },
                    {
                        "uid": 1164,
                        "name": 'Тараканівська територіальна громада',
                        "name_en": 'Tarakanivska Hromada',
                    },
                    {
                        "uid": 1165,
                        "name": 'Ярославицька територіальна громада',
                        "name_en": 'Yaroslavytska Hromada',
                    },
                ],
            },
            {
                "uid": 112,
                "name": 'Рівненський район',
                "name_en": 'Rivnenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1110,
                        "name": 'Бабинська територіальна громада',
                        "name_en": 'Babynska Hromada',
                    },
                    {
                        "uid": 1111,
                        "name": 'Березнівська територіальна громада',
                        "name_en": 'Bereznivska Hromada',
                    },
                    {
                        "uid": 1113,
                        "name": 'Бугринська територіальна громада',
                        "name_en": 'Buhrynska Hromada',
                    },
                    {
                        "uid": 1112,
                        "name": 'Білокриницька територіальна громада',
                        "name_en": 'Bilokrynytska Hromada',
                    },
                    {
                        "uid": 1114,
                        "name": 'Великомежиріцька територіальна громада',
                        "name_en": 'Velykomezhyritska Hromada',
                    },
                    {
                        "uid": 1115,
                        "name": 'Великоомелянська територіальна громада',
                        "name_en": 'Velykoomelianska Hromada',
                    },
                    {
                        "uid": 1116,
                        "name": 'Головинська територіальна громада',
                        "name_en": 'Holovynska Hromada',
                    },
                    {
                        "uid": 1117,
                        "name": 'Городоцька територіальна громада',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 1118,
                        "name": 'Гощанська територіальна громада',
                        "name_en": 'Hoshchanska Hromada',
                    },
                    {
                        "uid": 1119,
                        "name": 'Деражненська територіальна громада',
                        "name_en": 'Derazhnenska Hromada',
                    },
                    {
                        "uid": 1120,
                        "name": 'Дядьковицька територіальна громада',
                        "name_en": 'Diadkovytska Hromada',
                    },
                    {
                        "uid": 1121,
                        "name": 'Здовбицька територіальна громада',
                        "name_en": 'Zdovbytska Hromada',
                    },
                    {
                        "uid": 1122,
                        "name": 'Здолбунівська територіальна громада',
                        "name_en": 'Zdolbunivska Hromada',
                    },
                    {
                        "uid": 1123,
                        "name": 'Зорянська територіальна громада',
                        "name_en": 'Zorianska Hromada',
                    },
                    {
                        "uid": 1124,
                        "name": 'Клеванська територіальна громада',
                        "name_en": 'Klevanska Hromada',
                    },
                    {
                        "uid": 1125,
                        "name": 'Корецька територіальна громада',
                        "name_en": 'Koretska Hromada',
                    },
                    {
                        "uid": 1126,
                        "name": 'Корнинська територіальна громада',
                        "name_en": 'Kornynska Hromada',
                    },
                    {
                        "uid": 1127,
                        "name": 'Костопільська територіальна громада',
                        "name_en": 'Kostopilska Hromada',
                    },
                    {
                        "uid": 1128,
                        "name": 'Малинська територіальна громада',
                        "name_en": 'Malynska Hromada',
                    },
                    {
                        "uid": 1129,
                        "name": 'Малолюбашанська територіальна громада',
                        "name_en": 'Maloliubashanska Hromada',
                    },
                    {
                        "uid": 1130,
                        "name": 'Мізоцька територіальна громада',
                        "name_en": 'Mizotska Hromada',
                    },
                    {
                        "uid": 1131,
                        "name": 'Олександрійська територіальна громада',
                        "name_en": 'Oleksandriiska Hromada',
                    },
                    {
                        "uid": 1132,
                        "name": 'м. Острог та Острозька територіальна громада',
                        "name_en": 'Ostroh and Ostrozka Hromada',
                    },
                    {
                        "uid": 1133,
                        "name": 'м. Рівне та Рівненська територіальна громада',
                        "name_en": 'Rivne and Rivnenska Hromada',
                    },
                    {
                        "uid": 1134,
                        "name": 'Соснівська територіальна громада',
                        "name_en": 'Sosnivska Hromada',
                    },
                    {
                        "uid": 1135,
                        "name": 'Шпанівська територіальна громада',
                        "name_en": 'Shpanivska Hromada',
                    },
                ],
            },
            {
                "uid": 113,
                "name": 'Сарненський район',
                "name_en": 'Sarnenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1136,
                        "name": 'Березівська територіальна громада',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 1137,
                        "name": 'Вирівська територіальна громада',
                        "name_en": 'Vyrivska Hromada',
                    },
                    {
                        "uid": 1138,
                        "name": 'Висоцька територіальна громада',
                        "name_en": 'Vysotska Hromada',
                    },
                    {
                        "uid": 1139,
                        "name": 'Дубровицька територіальна громада',
                        "name_en": 'Dubrovytska Hromada',
                    },
                    {
                        "uid": 1140,
                        "name": 'Клесівська територіальна громада',
                        "name_en": 'Klesivska Hromada',
                    },
                    {
                        "uid": 1141,
                        "name": 'Миляцька територіальна громада',
                        "name_en": 'Myliatska Hromada',
                    },
                    {
                        "uid": 1142,
                        "name": 'Немовицька територіальна громада',
                        "name_en": 'Nemovytska Hromada',
                    },
                    {
                        "uid": 1143,
                        "name": 'Рокитнівська територіальна громада',
                        "name_en": 'Rokytnivska Hromada',
                    },
                    {
                        "uid": 1144,
                        "name": 'м. Сарни та Сарненська територіальна громада',
                        "name_en": 'Sarny and Sarnenska Hromada',
                    },
                    {
                        "uid": 1145,
                        "name": 'Старосільська територіальна громада',
                        "name_en": 'Starosilska Hromada',
                    },
                    {
                        "uid": 1146,
                        "name": 'Степанська територіальна громада',
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
                "name": 'Конотопський район',
                "name_en": 'Konotopskyi Raion',
                "hromadas": [
                    {
                        "uid": 1209,
                        "name": 'Бочечківська територіальна громада',
                        "name_en": 'Bochechkivska Hromada',
                    },
                    {
                        "uid": 1210,
                        "name": 'м. Буринь та Буринська територіальна громада',
                        "name_en": 'Buryn and Burynska Hromada',
                    },
                    {
                        "uid": 1211,
                        "name": 'Дубов’язівська територіальна громада',
                        "name_en": 'Dubovyazivska Hromada',
                    },
                    {
                        "uid": 1212,
                        "name": 'м. Конотоп та Конотопська територіальна громада',
                        "name_en": 'Konotop and Konotopska Hromada',
                    },
                    {
                        "uid": 1213,
                        "name": 'м. Кролевець та Кролевецька територіальна громада',
                        "name_en": 'Krolevets and Krolevetska Hromada',
                    },
                    {
                        "uid": 1214,
                        "name": 'Новослобідська територіальна громада',
                        "name_en": 'Novoslobidska Hromada',
                    },
                    {
                        "uid": 1215,
                        "name": 'Попівська територіальна громада',
                        "name_en": 'Popivska Hromada',
                    },
                    {
                        "uid": 1216,
                        "name": 'м. Путивль та Путивльська територіальна громада',
                        "name_en": 'Putyvl and Putyvlska Hromada',
                    },
                ],
            },
            {
                "uid": 118,
                "name": 'Охтирський район',
                "name_en": 'Okhtyrskyi Raion',
                "hromadas": [
                    {
                        "uid": 1200,
                        "name": 'Боромлянська територіальна громада',
                        "name_en": 'Boromlianska Hromada',
                    },
                    {
                        "uid": 1201,
                        "name": 'м. Велика Писарівка та Великописарівська територіальна громада',
                        "name_en": 'Velyka Pysarivka and Velykopysarivska Hromada',
                    },
                    {
                        "uid": 1202,
                        "name": 'Грунська територіальна громада',
                        "name_en": 'Hrunska Hromada',
                    },
                    {
                        "uid": 1203,
                        "name": 'Кириківська територіальна громада',
                        "name_en": 'Kyrykivska Hromada',
                    },
                    {
                        "uid": 1204,
                        "name": 'Комишанська територіальна громада',
                        "name_en": 'Komyshanska Hromada',
                    },
                    {
                        "uid": 1205,
                        "name": 'м. Охтирка та Охтирська територіальна громада',
                        "name_en": 'Okhtyrka and Okhtyrska Hromada',
                    },
                    {
                        "uid": 1206,
                        "name": 'м. Тростянець та Тростянецька територіальна громада',
                        "name_en": 'Trostianets and Trostianetska Hromada',
                    },
                    {
                        "uid": 1207,
                        "name": 'Чернеччинська територіальна громада',
                        "name_en": 'Chernechchynska Hromada',
                    },
                    {
                        "uid": 1208,
                        "name": 'Чупахівська територіальна громада',
                        "name_en": 'Chupakhivska Hromada',
                    },
                ],
            },
            {
                "uid": 116,
                "name": 'Роменський район',
                "name_en": 'Romenskyi Raion',
                "hromadas": [
                    {
                        "uid": 1166,
                        "name": 'Андріяшівська територіальна громада',
                        "name_en": 'Andriiashivska Hromada',
                    },
                    {
                        "uid": 1167,
                        "name": 'Вільшанська територіальна громада',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 1168,
                        "name": 'Коровинська територіальна громада',
                        "name_en": 'Korovynska Hromada',
                    },
                    {
                        "uid": 1169,
                        "name": 'м. Липова Долина та Липоводолинська територіальна громада',
                        "name_en": 'Lypova Dolyna and Lypovodolynska Hromada',
                    },
                    {
                        "uid": 1170,
                        "name": 'м. Недригайлів та Недригайлівська територіальна громада',
                        "name_en": 'Nedryhailiv and Nedryhailivska Hromada',
                    },
                    {
                        "uid": 1171,
                        "name": 'м. Ромни та Роменська територіальна громада',
                        "name_en": 'Romny and Romenska Hromada',
                    },
                    {
                        "uid": 1172,
                        "name": 'Синівська територіальна громада',
                        "name_en": 'Synivska Hromada',
                    },
                    {
                        "uid": 1173,
                        "name": 'Хмелівська територіальна громада',
                        "name_en": 'Khmelivska Hromada',
                    },
                ],
            },
            {
                "uid": 114,
                "name": 'Сумський район',
                "name_en": 'Sumskyi Raion',
                "hromadas": [
                    {
                        "uid": 1174,
                        "name": 'Бездрицька територіальна громада',
                        "name_en": 'Bezdrytska Hromada',
                    },
                    {
                        "uid": 1175,
                        "name": 'м. Білопілля та Білопільська територіальна громада',
                        "name_en": 'Bilopillia and Bilopilska Hromada',
                    },
                    {
                        "uid": 1176,
                        "name": 'Верхньосироватська територіальна громада',
                        "name_en": 'Verkhnosyrovatska Hromada',
                    },
                    {
                        "uid": 1177,
                        "name": 'Ворожбянська територіальна громада',
                        "name_en": 'Vorozhbianska Hromada',
                    },
                    {
                        "uid": 1178,
                        "name": 'м. Краснопілля та Краснопільська територіальна громада',
                        "name_en": 'Krasnopillia and Krasnopilska Hromada',
                    },
                    {
                        "uid": 1179,
                        "name": 'м. Лебедин та Лебединська територіальна громада',
                        "name_en": 'Lebedyn and Lebedynska Hromada',
                    },
                    {
                        "uid": 1181,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 1180,
                        "name": 'Миколаївська територіальна громада',
                        "name_en": 'Mykolaivska Hromada',
                    },
                    {
                        "uid": 1182,
                        "name": 'Миропільська територіальна громада',
                        "name_en": 'Myropilska Hromada',
                    },
                    {
                        "uid": 1183,
                        "name": 'Нижньосироватська територіальна громада',
                        "name_en": 'Nyzhnosyrovatska Hromada',
                    },
                    {
                        "uid": 1184,
                        "name": 'Річківська територіальна громада',
                        "name_en": 'Richkivska Hromada',
                    },
                    {
                        "uid": 1185,
                        "name": 'Садівська територіальна громада',
                        "name_en": 'Sadivska Hromada',
                    },
                    {
                        "uid": 1186,
                        "name": 'Степанівська територіальна громада',
                        "name_en": 'Stepanivska Hromada',
                    },
                    {
                        "uid": 1187,
                        "name": 'м. Суми та Сумська територіальна громада',
                        "name_en": 'Sumy and Sumska Hromada',
                    },
                    {
                        "uid": 1188,
                        "name": 'Хотінська територіальна громада',
                        "name_en": 'Khotinska Hromada',
                    },
                    {
                        "uid": 1189,
                        "name": 'Юнаківська територіальна громада',
                        "name_en": 'Yunakivska Hromada',
                    },
                ],
            },
            {
                "uid": 115,
                "name": 'Шосткинський район',
                "name_en": 'Shostkynskyi Raion',
                "hromadas": [
                    {
                        "uid": 1190,
                        "name": 'Березівська територіальна громада',
                        "name_en": 'Berezivska Hromada',
                    },
                    {
                        "uid": 1191,
                        "name": 'м. Глухів та Глухівська територіальна громада',
                        "name_en": 'Hlukhiv and Hlukhivska Hromada',
                    },
                    {
                        "uid": 1192,
                        "name": 'Дружбівська територіальна громада',
                        "name_en": 'Druzhbivska Hromada',
                    },
                    {
                        "uid": 1193,
                        "name": 'Есманьська територіальна громада',
                        "name_en": 'Esmanska Hromada',
                    },
                    {
                        "uid": 1194,
                        "name": 'Зноб-Новгородська територіальна громада',
                        "name_en": 'Znob-Novhorodska Hromada',
                    },
                    {
                        "uid": 1195,
                        "name": 'Свеська територіальна громада',
                        "name_en": 'Sveska Hromada',
                    },
                    {
                        "uid": 1196,
                        "name": 'м. Середина-Буда та Середино-Будська територіальна громада',
                        "name_en": 'Seredyna-Buda and Seredyno-Budska Hromada',
                    },
                    {
                        "uid": 1197,
                        "name": 'Шалигинська територіальна громада',
                        "name_en": 'Shalyhynska Hromada',
                    },
                    {
                        "uid": 1198,
                        "name": 'м. Шостка та Шосткинська територіальна громада',
                        "name_en": 'Shostka and Shostkynska Hromada',
                    },
                    {
                        "uid": 1199,
                        "name": 'м. Ямпіль та Ямпільська територіальна громада',
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
                "name": 'Кременецький район',
                "name_en": 'Kremenetskyi Raion',
                "hromadas": [
                    {
                        "uid": 1264,
                        "name": 'Борсуківська територіальна громада',
                        "name_en": 'Borsukivska Hromada',
                    },
                    {
                        "uid": 1265,
                        "name": 'Великодедеркальська територіальна громада',
                        "name_en": 'Velykodederkalska Hromada',
                    },
                    {
                        "uid": 1266,
                        "name": 'Вишнівецька територіальна громада',
                        "name_en": 'Vyshnivetska Hromada',
                    },
                    {
                        "uid": 1267,
                        "name": 'м. Кременець та Кременецька територіальна громада',
                        "name_en": 'Kremenets and Kremenetska Hromada',
                    },
                    {
                        "uid": 1268,
                        "name": 'Лановецька територіальна громада',
                        "name_en": 'Lanovetska Hromada',
                    },
                    {
                        "uid": 1269,
                        "name": 'Лопушненська територіальна громада',
                        "name_en": 'Lopushnenska Hromada',
                    },
                    {
                        "uid": 1270,
                        "name": 'Почаївська територіальна громада',
                        "name_en": 'Pochaivska Hromada',
                    },
                    {
                        "uid": 1271,
                        "name": 'Шумська територіальна громада',
                        "name_en": 'Shumska Hromada',
                    },
                ],
            },
            {
                "uid": 119,
                "name": 'Тернопільський район',
                "name_en": 'Ternopilskyi Raion',
                "hromadas": [
                    {
                        "uid": 1217,
                        "name": 'Байковецька територіальна громада',
                        "name_en": 'Baikovetska Hromada',
                    },
                    {
                        "uid": 1218,
                        "name": 'м. Бережани та Бережанська територіальна громада',
                        "name_en": 'Berezhany and Berezhanska Hromada',
                    },
                    {
                        "uid": 1219,
                        "name": 'Білецька територіальна громада',
                        "name_en": 'Biletska Hromada',
                    },
                    {
                        "uid": 1220,
                        "name": 'Великоберезовицька територіальна громада',
                        "name_en": 'Velykoberezovytska Hromada',
                    },
                    {
                        "uid": 1221,
                        "name": 'Великобірківська територіальна громада',
                        "name_en": 'Velykobirkivska Hromada',
                    },
                    {
                        "uid": 1222,
                        "name": 'Великогаївська територіальна громада',
                        "name_en": 'Velykohaivska Hromada',
                    },
                    {
                        "uid": 1223,
                        "name": 'Залозецька територіальна громада',
                        "name_en": 'Zalozetska Hromada',
                    },
                    {
                        "uid": 1224,
                        "name": 'Збаразька територіальна громада',
                        "name_en": 'Zbarazka Hromada',
                    },
                    {
                        "uid": 1225,
                        "name": 'Зборівська територіальна громада',
                        "name_en": 'Zborivska Hromada',
                    },
                    {
                        "uid": 1226,
                        "name": 'Золотниківська територіальна громада',
                        "name_en": 'Zolotnykivska Hromada',
                    },
                    {
                        "uid": 1229,
                        "name": 'Козлівська територіальна громада',
                        "name_en": 'Kozlivska Hromada',
                    },
                    {
                        "uid": 1228,
                        "name": 'Козівська територіальна громада',
                        "name_en": 'Kozivska Hromada',
                    },
                    {
                        "uid": 1230,
                        "name": 'Купчинецька територіальна громада',
                        "name_en": 'Kupchynetska Hromada',
                    },
                    {
                        "uid": 1231,
                        "name": 'Микулинецька територіальна громада',
                        "name_en": 'Mykulynetska Hromada',
                    },
                    {
                        "uid": 1232,
                        "name": 'Нараївська територіальна громада',
                        "name_en": 'Naraivska Hromada',
                    },
                    {
                        "uid": 1233,
                        "name": 'Озернянська територіальна громада',
                        "name_en": 'Ozernianska Hromada',
                    },
                    {
                        "uid": 1234,
                        "name": 'Підволочиська територіальна громада',
                        "name_en": 'Pidvolochyska Hromada',
                    },
                    {
                        "uid": 1235,
                        "name": 'Підгаєцька територіальна громада',
                        "name_en": 'Pidhaietska Hromada',
                    },
                    {
                        "uid": 1236,
                        "name": 'Підгороднянська територіальна громада',
                        "name_en": 'Pidhorodnianska Hromada',
                    },
                    {
                        "uid": 1237,
                        "name": 'Саранчуківська територіальна громада',
                        "name_en": 'Saranchukivska Hromada',
                    },
                    {
                        "uid": 1238,
                        "name": 'Скалатська територіальна громада',
                        "name_en": 'Skalatska Hromada',
                    },
                    {
                        "uid": 1239,
                        "name": 'Скориківська територіальна громада',
                        "name_en": 'Skorykivska Hromada',
                    },
                    {
                        "uid": 1240,
                        "name": 'Теребовлянська територіальна громада',
                        "name_en": 'Terebovlianska Hromada',
                    },
                    {
                        "uid": 1241,
                        "name": 'м. Тернопіль та Тернопільська територіальна громада',
                        "name_en": 'Ternopil and Ternopilska Hromada',
                    },
                    {
                        "uid": 1227,
                        "name": 'Іванівська територіальна громада',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
            {
                "uid": 121,
                "name": 'Чортківський район',
                "name_en": 'Chortkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1244,
                        "name": 'Борщівська територіальна громада',
                        "name_en": 'Borshchivska Hromada',
                    },
                    {
                        "uid": 1245,
                        "name": 'Бучацька територіальна громада',
                        "name_en": 'Buchatska Hromada',
                    },
                    {
                        "uid": 1242,
                        "name": 'Білобожницька територіальна громада',
                        "name_en": 'Bilobozhnytska Hromada',
                    },
                    {
                        "uid": 1243,
                        "name": 'Більче-Золотецька територіальна громада',
                        "name_en": 'Bilche-Zolotetska Hromada',
                    },
                    {
                        "uid": 1246,
                        "name": 'Васильковецька територіальна громада',
                        "name_en": 'Vasylkovetska Hromada',
                    },
                    {
                        "uid": 1247,
                        "name": 'Гримайлівська територіальна громада',
                        "name_en": 'Hrymailivska Hromada',
                    },
                    {
                        "uid": 1248,
                        "name": 'Гусятинська територіальна громада',
                        "name_en": 'Husiatynska Hromada',
                    },
                    {
                        "uid": 1249,
                        "name": 'Заводська територіальна громада',
                        "name_en": 'Zavodska Hromada',
                    },
                    {
                        "uid": 1250,
                        "name": 'Заліщицька територіальна громада',
                        "name_en": 'Zalishchytska Hromada',
                    },
                    {
                        "uid": 1251,
                        "name": 'Золотопотіцька територіальна громада',
                        "name_en": 'Zolotopotitska Hromada',
                    },
                    {
                        "uid": 1253,
                        "name": 'Колиндянська територіальна громада',
                        "name_en": 'Kolyndianska Hromada',
                    },
                    {
                        "uid": 1254,
                        "name": 'Копичинецька територіальна громада',
                        "name_en": 'Kopychynetska Hromada',
                    },
                    {
                        "uid": 1255,
                        "name": 'Коропецька територіальна громада',
                        "name_en": 'Koropetska Hromada',
                    },
                    {
                        "uid": 1256,
                        "name": 'Мельнице-Подільська територіальна громада',
                        "name_en": 'Melnytse-Podilska Hromada',
                    },
                    {
                        "uid": 1257,
                        "name": 'Монастириська територіальна громада',
                        "name_en": 'Monastyryska Hromada',
                    },
                    {
                        "uid": 1258,
                        "name": 'Нагірянська територіальна громада',
                        "name_en": 'Nahirianska Hromada',
                    },
                    {
                        "uid": 1259,
                        "name": 'Скала-Подільська територіальна громада',
                        "name_en": 'Skala-Podilska Hromada',
                    },
                    {
                        "uid": 1260,
                        "name": 'Товстенська територіальна громада',
                        "name_en": 'Tovstenska Hromada',
                    },
                    {
                        "uid": 1261,
                        "name": 'Трибухівська територіальна громада',
                        "name_en": 'Trybukhivska Hromada',
                    },
                    {
                        "uid": 1262,
                        "name": 'Хоростківська територіальна громада',
                        "name_en": 'Khorostkivska Hromada',
                    },
                    {
                        "uid": 1263,
                        "name": 'м. Чортків та Чортківська територіальна громада',
                        "name_en": 'Chortkiv and Chortkivska Hromada',
                    },
                    {
                        "uid": 1252,
                        "name": 'Іване-Пустенська територіальна громада',
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
                "name": 'Берестинський район',
                "name_en": 'Berestynskyi Raion',
                "hromadas": [
                    {
                        "uid": 1324,
                        "name": 'Берестинська територіальна громада',
                        "name_en": 'Berestynska Hromada',
                    },
                    {
                        "uid": 1322,
                        "name": 'Зачепилівська територіальна громада',
                        "name_en": 'Zachepylivska Hromada',
                    },
                    {
                        "uid": 1323,
                        "name": 'Кегичівська територіальна громада',
                        "name_en": 'Kehychivska Hromada',
                    },
                    {
                        "uid": 1325,
                        "name": 'Наталинська територіальна громада',
                        "name_en": 'Natalynska Hromada',
                    },
                    {
                        "uid": 1326,
                        "name": 'Сахновщинська територіальна громада',
                        "name_en": 'Sakhnovshchynska Hromada',
                    },
                    {
                        "uid": 1327,
                        "name": 'Старовірівська територіальна громада',
                        "name_en": 'Starovirivska Hromada',
                    },
                ],
            },
            {
                "uid": 126,
                "name": 'Богодухівський район',
                "name_en": 'Bohodukhivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1300,
                        "name": 'м. Богодухів та Богодухівська територіальна громада',
                        "name_en": 'Bohodukhiv and Bohodukhivska Hromada',
                    },
                    {
                        "uid": 1301,
                        "name": 'Валківська територіальна громада',
                        "name_en": 'Valkivska Hromada',
                    },
                    {
                        "uid": 1302,
                        "name": 'Золочівська територіальна громада',
                        "name_en": 'Zolochivska Hromada',
                    },
                    {
                        "uid": 1303,
                        "name": 'Коломацька територіальна громада',
                        "name_en": 'Kolomatska Hromada',
                    },
                    {
                        "uid": 1304,
                        "name": 'Краснокутська територіальна громада',
                        "name_en": 'Krasnokutska Hromada',
                    },
                ],
            },
            {
                "uid": 123,
                "name": "Куп'янський район",
                "name_en": 'Kupianskyi Raion',
                "hromadas": [
                    {
                        "uid": 1305,
                        "name": 'Великобурлуцька територіальна громада',
                        "name_en": 'Velykoburlutska Hromada',
                    },
                    {
                        "uid": 1306,
                        "name": 'Вільхуватська територіальна громада',
                        "name_en": 'Vilkhuvatska Hromada',
                    },
                    {
                        "uid": 1307,
                        "name": 'Дворічанська територіальна громада',
                        "name_en": 'Dvorichanska Hromada',
                    },
                    {
                        "uid": 1309,
                        "name": "м. Куп'янськ та Куп'янська територіальна громада",
                        "name_en": 'Kupiansk and Kupianska Hromada',
                    },
                    {
                        "uid": 1310,
                        "name": 'Курилівська територіальна громада',
                        "name_en": 'Kurylivska Hromada',
                    },
                    {
                        "uid": 1308,
                        "name": 'Кіндрашівська територіальна громада',
                        "name_en": 'Kindrashivska Hromada',
                    },
                    {
                        "uid": 1311,
                        "name": 'Петропавлівська територіальна громада',
                        "name_en": 'Petropavlivska Hromada',
                    },
                    {
                        "uid": 1312,
                        "name": 'Шевченківська територіальна громада',
                        "name_en": 'Shevchenkivska Hromada',
                    },
                ],
            },
            {
                "uid": 128,
                "name": 'Лозівський район',
                "name_en": 'Lozivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1296,
                        "name": 'Близнюківська територіальна громада',
                        "name_en": 'Blyzniukivska Hromada',
                    },
                    {
                        "uid": 1295,
                        "name": 'Біляївська територіальна громада',
                        "name_en": 'Biliaivska Hromada',
                    },
                    {
                        "uid": 1299,
                        "name": 'м. Златопіль та Златопільська територіальна громада',
                        "name_en": 'Zlatopil and Zlatopilska Hromada',
                    },
                    {
                        "uid": 1297,
                        "name": 'м. Лозова та Лозівська територіальна громада',
                        "name_en": 'Lozova and Lozivska Hromada',
                    },
                    {
                        "uid": 1298,
                        "name": 'Олексіївська територіальна громада',
                        "name_en": 'Oleksiivska Hromada',
                    },
                ],
            },
            {
                "uid": 124,
                "name": 'Харківський район',
                "name_en": 'Kharkivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1280,
                        "name": 'Безлюдівська територіальна громада',
                        "name_en": 'Bezliudivska Hromada',
                    },
                    {
                        "uid": 1281,
                        "name": 'Височанська територіальна громада',
                        "name_en": 'Vysochanska Hromada',
                    },
                    {
                        "uid": 1282,
                        "name": 'Вільхівська територіальна громада',
                        "name_en": 'Vilkhivska Hromada',
                    },
                    {
                        "uid": 1283,
                        "name": 'Дергачівська територіальна громада',
                        "name_en": 'Derhachivska Hromada',
                    },
                    {
                        "uid": 1284,
                        "name": 'Липецька територіальна громада',
                        "name_en": 'Lypetska Hromada',
                    },
                    {
                        "uid": 1285,
                        "name": 'м. Люботин та Люботинська територіальна громада',
                        "name_en": 'Liubotyn and Liubotynska Hromada',
                    },
                    {
                        "uid": 1286,
                        "name": 'Малоданилівська територіальна громада',
                        "name_en": 'Malodanylivska Hromada',
                    },
                    {
                        "uid": 1287,
                        "name": "Мереф'янська територіальна громада",
                        "name_en": 'Merefianska Hromada',
                    },
                    {
                        "uid": 1288,
                        "name": 'Нововодолазька територіальна громада',
                        "name_en": 'Novovodolazka Hromada',
                    },
                    {
                        "uid": 1289,
                        "name": 'Південноміська територіальна громада',
                        "name_en": 'Pivdennomiska Hromada',
                    },
                    {
                        "uid": 1290,
                        "name": 'Пісочинська територіальна громада',
                        "name_en": 'Pisochynska Hromada',
                    },
                    {
                        "uid": 1291,
                        "name": 'Роганська територіальна громада',
                        "name_en": 'Rohanska Hromada',
                    },
                    {
                        "uid": 1292,
                        "name": 'Солоницівська територіальна громада',
                        "name_en": 'Solonytsivska Hromada',
                    },
                    {
                        "uid": 1293,
                        "name": 'м. Харків та Харківська територіальна громада',
                        "name_en": 'Kharkiv and Kharkivska Hromada',
                    },
                    {
                        "uid": 1294,
                        "name": 'Циркунівська територіальна громада',
                        "name_en": 'Tsyrkunivska Hromada',
                    },
                ],
            },
            {
                "uid": 122,
                "name": 'Чугуївський район',
                "name_en": 'Chuhuivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1313,
                        "name": 'Вовчанська територіальна громада',
                        "name_en": 'Vovchanska Hromada',
                    },
                    {
                        "uid": 1314,
                        "name": 'Зміївська територіальна громада',
                        "name_en": 'Zmiivska Hromada',
                    },
                    {
                        "uid": 1315,
                        "name": 'Малинівська територіальна громада',
                        "name_en": 'Malynivska Hromada',
                    },
                    {
                        "uid": 1316,
                        "name": 'Новопокровська територіальна громада',
                        "name_en": 'Novopokrovska Hromada',
                    },
                    {
                        "uid": 1317,
                        "name": 'Печенізька територіальна громада',
                        "name_en": 'Pechenizka Hromada',
                    },
                    {
                        "uid": 1318,
                        "name": 'Слобожанська територіальна громада',
                        "name_en": 'Slobozhanska Hromada',
                    },
                    {
                        "uid": 1319,
                        "name": 'Старосалтівська територіальна громада',
                        "name_en": 'Starosaltivska Hromada',
                    },
                    {
                        "uid": 1320,
                        "name": 'Чкаловська територіальна громада',
                        "name_en": 'Chkalovska Hromada',
                    },
                    {
                        "uid": 1321,
                        "name": 'м. Чугуїв та Чугуївська територіальна громада',
                        "name_en": 'Chuhuiv and Chuhuivska Hromada',
                    },
                ],
            },
            {
                "uid": 125,
                "name": 'Ізюмський район',
                "name_en": 'Iziumskyi Raion',
                "hromadas": [
                    {
                        "uid": 1272,
                        "name": 'Балаклійська територіальна громада',
                        "name_en": 'Balakliiska Hromada',
                    },
                    {
                        "uid": 1273,
                        "name": 'Барвінківська територіальна громада',
                        "name_en": 'Barvinkivska Hromada',
                    },
                    {
                        "uid": 1274,
                        "name": 'Борівська територіальна громада',
                        "name_en": 'Borivska Hromada',
                    },
                    {
                        "uid": 1275,
                        "name": 'Донецька територіальна громада',
                        "name_en": 'Donetska Hromada',
                    },
                    {
                        "uid": 1277,
                        "name": 'Куньєвська територіальна громада',
                        "name_en": 'Kunievska Hromada',
                    },
                    {
                        "uid": 1278,
                        "name": 'Оскільська територіальна громада',
                        "name_en": 'Oskilska Hromada',
                    },
                    {
                        "uid": 1279,
                        "name": 'Савинська територіальна громада',
                        "name_en": 'Savynska Hromada',
                    },
                    {
                        "uid": 1276,
                        "name": 'м. Ізюм та Ізюмська територіальна громада',
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
                "name": 'Бериславський район',
                "name_en": 'Beryslavskyi Raion',
                "hromadas": [
                    {
                        "uid": 1343,
                        "name": 'Бериславська територіальна громада',
                        "name_en": 'Beryslavska Hromada',
                    },
                    {
                        "uid": 1344,
                        "name": 'Борозенська територіальна громада',
                        "name_en": 'Borozenska Hromada',
                    },
                    {
                        "uid": 1345,
                        "name": 'Великоолександрівська територіальна громада',
                        "name_en": 'Velykooleksandrivska Hromada',
                    },
                    {
                        "uid": 1346,
                        "name": 'Високопільська територіальна громада',
                        "name_en": 'Vysokopilska Hromada',
                    },
                    {
                        "uid": 1347,
                        "name": 'Калинівська територіальна громада',
                        "name_en": 'Kalynivska Hromada',
                    },
                    {
                        "uid": 1348,
                        "name": 'Кочубеївська територіальна громада',
                        "name_en": 'Kochubeivska Hromada',
                    },
                    {
                        "uid": 1349,
                        "name": 'Милівська територіальна громада',
                        "name_en": 'Mylivska Hromada',
                    },
                    {
                        "uid": 1350,
                        "name": 'Нововоронцовська територіальна громада',
                        "name_en": 'Novovorontsovska Hromada',
                    },
                    {
                        "uid": 1351,
                        "name": 'Новоолександрівська територіальна громада',
                        "name_en": 'Novooleksandrivska Hromada',
                    },
                    {
                        "uid": 1352,
                        "name": 'Новорайська територіальна громада',
                        "name_en": 'Novoraiska Hromada',
                    },
                    {
                        "uid": 1353,
                        "name": 'Тягинська територіальна громада',
                        "name_en": 'Tiahynska Hromada',
                    },
                ],
            },
            {
                "uid": 133,
                "name": 'Генічеський район',
                "name_en": 'Henicheskyi Raion',
                "hromadas": [
                    {
                        "uid": 1373,
                        "name": 'Генічеська територіальна громада',
                        "name_en": 'Henicheska Hromada',
                    },
                    {
                        "uid": 1375,
                        "name": 'Нижньосірогозька територіальна громада',
                        "name_en": 'Nyzhnosirohozka Hromada',
                    },
                    {
                        "uid": 1376,
                        "name": 'Новотроїцька територіальна громада',
                        "name_en": 'Novotroitska Hromada',
                    },
                    {
                        "uid": 1374,
                        "name": 'Іванівська територіальна громада',
                        "name_en": 'Ivanivska Hromada',
                    },
                ],
            },
            {
                "uid": 131,
                "name": 'Каховський район',
                "name_en": 'Kakhovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1328,
                        "name": 'Асканія-Нова територіальна громада',
                        "name_en": 'Askaniia-Nova Hromada',
                    },
                    {
                        "uid": 1329,
                        "name": 'Великолепетиська територіальна громада',
                        "name_en": 'Velykolepetyska Hromada',
                    },
                    {
                        "uid": 1330,
                        "name": 'Верхньорогачицька територіальна громада',
                        "name_en": 'Verkhnorohachytska Hromada',
                    },
                    {
                        "uid": 1331,
                        "name": 'Горностаївська територіальна громада',
                        "name_en": 'Hornostaivska Hromada',
                    },
                    {
                        "uid": 1332,
                        "name": 'Зеленопідська територіальна громада',
                        "name_en": 'Zelenopidska Hromada',
                    },
                    {
                        "uid": 1333,
                        "name": 'м. Каховка та Каховська територіальна громада',
                        "name_en": 'Kakhovka and Kakhovska Hromada',
                    },
                    {
                        "uid": 1334,
                        "name": 'Костянтинівська територіальна громада',
                        "name_en": 'Kostiantynivska Hromada',
                    },
                    {
                        "uid": 1335,
                        "name": 'Любимівська територіальна громада',
                        "name_en": 'Liubymivska Hromada',
                    },
                    {
                        "uid": 1336,
                        "name": 'м. Нова Каховка та Новокаховська територіальна громада',
                        "name_en": 'Nova Kakhovka and Novokakhovska Hromada',
                    },
                    {
                        "uid": 1337,
                        "name": 'Присиваська територіальна громада',
                        "name_en": 'Prysyvaska Hromada',
                    },
                    {
                        "uid": 1338,
                        "name": 'Рубанівська територіальна громада',
                        "name_en": 'Rubanivska Hromada',
                    },
                    {
                        "uid": 1339,
                        "name": 'Тавричанська територіальна громада',
                        "name_en": 'Tavrychanska Hromada',
                    },
                    {
                        "uid": 1340,
                        "name": 'Таврійська територіальна громада',
                        "name_en": 'Tavriiska Hromada',
                    },
                    {
                        "uid": 1341,
                        "name": 'Хрестівська територіальна громада',
                        "name_en": 'Khrestivska Hromada',
                    },
                    {
                        "uid": 1342,
                        "name": 'Чаплинська територіальна громада',
                        "name_en": 'Chaplynska Hromada',
                    },
                ],
            },
            {
                "uid": 130,
                "name": 'Скадовський район',
                "name_en": 'Skadovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1354,
                        "name": 'Бехтерська територіальна громада',
                        "name_en": 'Bekhterska Hromada',
                    },
                    {
                        "uid": 1355,
                        "name": 'м. Гола Пристань та Голопристанська територіальна громада',
                        "name_en": 'Hola Prystan and Holoprystanska Hromada',
                    },
                    {
                        "uid": 1356,
                        "name": 'Долматівська територіальна громада',
                        "name_en": 'Dolmativska Hromada',
                    },
                    {
                        "uid": 1357,
                        "name": 'Каланчацька територіальна громада',
                        "name_en": 'Kalanchatska Hromada',
                    },
                    {
                        "uid": 1358,
                        "name": 'Лазурненська територіальна громада',
                        "name_en": 'Lazurnenska Hromada',
                    },
                    {
                        "uid": 1359,
                        "name": 'Мирненська територіальна громада',
                        "name_en": 'Myrnenska Hromada',
                    },
                    {
                        "uid": 1360,
                        "name": 'Новомиколаївська територіальна громада',
                        "name_en": 'Novomykolaivska Hromada',
                    },
                    {
                        "uid": 1361,
                        "name": 'Скадовська територіальна громада',
                        "name_en": 'Skadovska Hromada',
                    },
                    {
                        "uid": 1362,
                        "name": 'Чулаківська територіальна громада',
                        "name_en": 'Chulakivska Hromada',
                    },
                ],
            },
            {
                "uid": 132,
                "name": 'Херсонський район',
                "name_en": 'Khersonskyi Raion',
                "hromadas": [
                    {
                        "uid": 1363,
                        "name": 'Білозерська територіальна громада',
                        "name_en": 'Bilozerska Hromada',
                    },
                    {
                        "uid": 1364,
                        "name": 'Великокопанівська територіальна громада',
                        "name_en": 'Velykokopanivska Hromada',
                    },
                    {
                        "uid": 1365,
                        "name": 'Виноградівська територіальна громада',
                        "name_en": 'Vynohradivska Hromada',
                    },
                    {
                        "uid": 1366,
                        "name": 'Дар’ївська територіальна громада',
                        "name_en": 'Daryivska Hromada',
                    },
                    {
                        "uid": 1367,
                        "name": 'Музиківська територіальна громада',
                        "name_en": 'Muzykivska Hromada',
                    },
                    {
                        "uid": 1368,
                        "name": 'Олешківська територіальна громада',
                        "name_en": 'Oleshkivska Hromada',
                    },
                    {
                        "uid": 1369,
                        "name": 'Станіславська територіальна громада',
                        "name_en": 'Stanislavska Hromada',
                    },
                    {
                        "uid": 1370,
                        "name": 'м. Херсон та Херсонська територіальна громада',
                        "name_en": 'Kherson and Khersonska Hromada',
                    },
                    {
                        "uid": 1371,
                        "name": 'Чорнобаївська територіальна громада',
                        "name_en": 'Chornobaivska Hromada',
                    },
                    {
                        "uid": 1372,
                        "name": 'Ювілейна територіальна громада',
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
                "name": "Кам'янець-Подільський район",
                "name_en": 'Kamianets-Podilskyi Raion',
                "hromadas": [
                    {
                        "uid": 1422,
                        "name": 'Гуківська територіальна громада',
                        "name_en": 'Hukivska Hromada',
                    },
                    {
                        "uid": 1423,
                        "name": 'Гуменецька територіальна громада',
                        "name_en": 'Humenetska Hromada',
                    },
                    {
                        "uid": 1424,
                        "name": 'Дунаєвецька територіальна громада',
                        "name_en": 'Dunaievetska Hromada',
                    },
                    {
                        "uid": 1425,
                        "name": 'Жванецька територіальна громада',
                        "name_en": 'Zhvanetska Hromada',
                    },
                    {
                        "uid": 1426,
                        "name": 'Закупненська територіальна громада',
                        "name_en": 'Zakupnenska Hromada',
                    },
                    {
                        "uid": 1427,
                        "name": "м. Кам'янець-Подільський та Кам'янець-Подільська територіальна громада",
                        "name_en": 'Kamianets-Podilskyi and Kamianets-Podilska Hromada',
                    },
                    {
                        "uid": 1428,
                        "name": 'Китайгородська територіальна громада',
                        "name_en": 'Kytaihorodska Hromada',
                    },
                    {
                        "uid": 1429,
                        "name": 'Маківська територіальна громада',
                        "name_en": 'Makivska Hromada',
                    },
                    {
                        "uid": 1430,
                        "name": 'Новодунаєвецька територіальна громада',
                        "name_en": 'Novodunaievetska Hromada',
                    },
                    {
                        "uid": 1431,
                        "name": 'Новоушицька територіальна громада',
                        "name_en": 'Novoushytska Hromada',
                    },
                    {
                        "uid": 1432,
                        "name": 'Орининська територіальна громада',
                        "name_en": 'Orynynska Hromada',
                    },
                    {
                        "uid": 1433,
                        "name": 'Слобідсько-Кульчієвецьк територіальна громада',
                        "name_en": 'Slobidsko-Kulchiievetsk Hromada',
                    },
                    {
                        "uid": 1434,
                        "name": 'Смотрицька територіальна громада',
                        "name_en": 'Smotrytska Hromada',
                    },
                    {
                        "uid": 1435,
                        "name": 'Староушицька територіальна громада',
                        "name_en": 'Staroushytska Hromada',
                    },
                    {
                        "uid": 1436,
                        "name": 'Чемеровецька територіальна громада',
                        "name_en": 'Chemerovetska Hromada',
                    },
                ],
            },
            {
                "uid": 134,
                "name": 'Хмельницький район',
                "name_en": 'Khmelnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 1377,
                        "name": 'Антонінська територіальна громада',
                        "name_en": 'Antoninska Hromada',
                    },
                    {
                        "uid": 1380,
                        "name": 'Вовковинецька територіальна громада',
                        "name_en": 'Vovkovynetska Hromada',
                    },
                    {
                        "uid": 1381,
                        "name": 'Волочиська територіальна громада',
                        "name_en": 'Volochyska Hromada',
                    },
                    {
                        "uid": 1378,
                        "name": 'Війтовецька територіальна громада',
                        "name_en": 'Viitovetska Hromada',
                    },
                    {
                        "uid": 1379,
                        "name": 'Віньковецька територіальна громада',
                        "name_en": 'Vinkovetska Hromada',
                    },
                    {
                        "uid": 1382,
                        "name": 'Гвардійська територіальна громада',
                        "name_en": 'Hvardiiska Hromada',
                    },
                    {
                        "uid": 1383,
                        "name": 'Городоцька територіальна громада',
                        "name_en": 'Horodotska Hromada',
                    },
                    {
                        "uid": 1384,
                        "name": 'Деражнянська територіальна громада',
                        "name_en": 'Derazhnianska Hromada',
                    },
                    {
                        "uid": 1385,
                        "name": 'Заслучненська територіальна громада',
                        "name_en": 'Zasluchnenska Hromada',
                    },
                    {
                        "uid": 1386,
                        "name": 'Зіньківська територіальна громада',
                        "name_en": 'Zinkivska Hromada',
                    },
                    {
                        "uid": 1387,
                        "name": 'Красилівська територіальна громада',
                        "name_en": 'Krasylivska Hromada',
                    },
                    {
                        "uid": 1388,
                        "name": 'Летичівська територіальна громада',
                        "name_en": 'Letychivska Hromada',
                    },
                    {
                        "uid": 1389,
                        "name": 'Лісовогринівецька територіальна громада',
                        "name_en": 'Lisovohrynivetska Hromada',
                    },
                    {
                        "uid": 1390,
                        "name": 'Меджибізька територіальна громада',
                        "name_en": 'Medzhybizka Hromada',
                    },
                    {
                        "uid": 1391,
                        "name": 'Миролюбненська територіальна громада',
                        "name_en": 'Myroliubnenska Hromada',
                    },
                    {
                        "uid": 1392,
                        "name": 'Наркевицька територіальна громада',
                        "name_en": 'Narkevytska Hromada',
                    },
                    {
                        "uid": 1393,
                        "name": 'Розсошанська територіальна громада',
                        "name_en": 'Rozsoshanska Hromada',
                    },
                    {
                        "uid": 1394,
                        "name": 'Сатанівська територіальна громада',
                        "name_en": 'Satanivska Hromada',
                    },
                    {
                        "uid": 1395,
                        "name": 'Солобковецька територіальна громада',
                        "name_en": 'Solobkovetska Hromada',
                    },
                    {
                        "uid": 1396,
                        "name": 'м. Старокостянтинів та Старокостянтинівська територіальна громада',
                        "name_en": 'Starokostiantyniv and Starokostiantynivska Hromada',
                    },
                    {
                        "uid": 1397,
                        "name": 'Староостропільська територіальна громада',
                        "name_en": 'Staroostropilska Hromada',
                    },
                    {
                        "uid": 1398,
                        "name": 'Старосинявська територіальна громада',
                        "name_en": 'Starosyniavska Hromada',
                    },
                    {
                        "uid": 1399,
                        "name": 'Теофіпольська територіальна громада',
                        "name_en": 'Teofipolska Hromada',
                    },
                    {
                        "uid": 1400,
                        "name": 'м. Хмельницький та Хмельницька територіальна громада',
                        "name_en": 'Khmelnytskyi and Khmelnytska Hromada',
                    },
                    {
                        "uid": 1401,
                        "name": 'Чорноострівська територіальна громада',
                        "name_en": 'Chornoostrivska Hromada',
                    },
                    {
                        "uid": 1402,
                        "name": 'Щиборівська територіальна громада',
                        "name_en": 'Shchyborivska Hromada',
                    },
                    {
                        "uid": 1403,
                        "name": 'Ярмолинецька територіальна громада',
                        "name_en": 'Yarmolynetska Hromada',
                    },
                ],
            },
            {
                "uid": 136,
                "name": 'Шепетівський район',
                "name_en": 'Shepetivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1404,
                        "name": 'Берездівська територіальна громада',
                        "name_en": 'Berezdivska Hromada',
                    },
                    {
                        "uid": 1405,
                        "name": 'Білогірська територіальна громада',
                        "name_en": 'Bilohirska Hromada',
                    },
                    {
                        "uid": 1406,
                        "name": 'Ганнопільська територіальна громада',
                        "name_en": 'Hannopilska Hromada',
                    },
                    {
                        "uid": 1407,
                        "name": 'Грицівська територіальна громада',
                        "name_en": 'Hrytsivska Hromada',
                    },
                    {
                        "uid": 1409,
                        "name": 'Крупецька територіальна громада',
                        "name_en": 'Krupetska Hromada',
                    },
                    {
                        "uid": 1410,
                        "name": 'Ленковецька територіальна громада',
                        "name_en": 'Lenkovetska Hromada',
                    },
                    {
                        "uid": 1411,
                        "name": 'Михайлюцька територіальна громада',
                        "name_en": 'Mykhailiutska Hromada',
                    },
                    {
                        "uid": 1412,
                        "name": 'м. Нетішин та Нетішинська територіальна громада',
                        "name_en": 'Netishyn and Netishynska Hromada',
                    },
                    {
                        "uid": 1413,
                        "name": 'Плужненська територіальна громада',
                        "name_en": 'Pluzhnenska Hromada',
                    },
                    {
                        "uid": 1414,
                        "name": 'Полонська територіальна громада',
                        "name_en": 'Polonska Hromada',
                    },
                    {
                        "uid": 1415,
                        "name": 'Понінківська територіальна громада',
                        "name_en": 'Poninkivska Hromada',
                    },
                    {
                        "uid": 1416,
                        "name": 'Сахновецька територіальна громада',
                        "name_en": 'Sakhnovetska Hromada',
                    },
                    {
                        "uid": 1417,
                        "name": 'м. Славута та Славутська територіальна громада',
                        "name_en": 'Slavuta and Slavutska Hromada',
                    },
                    {
                        "uid": 1418,
                        "name": 'Судилківська територіальна громада',
                        "name_en": 'Sudylkivska Hromada',
                    },
                    {
                        "uid": 1419,
                        "name": 'Улашанівська територіальна громада',
                        "name_en": 'Ulashanivska Hromada',
                    },
                    {
                        "uid": 1420,
                        "name": 'м. Шепетівка та Шепетівська територіальна громада',
                        "name_en": 'Shepetivka and Shepetivska Hromada',
                    },
                    {
                        "uid": 1421,
                        "name": 'Ямпільська територіальна громада',
                        "name_en": 'Yampilska Hromada',
                    },
                    {
                        "uid": 1408,
                        "name": 'Ізяславська територіальна громада',
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
                "name": 'Звенигородський район',
                "name_en": 'Zvenyhorodskyi Raion',
                "hromadas": [
                    {
                        "uid": 1475,
                        "name": 'Бужанська територіальна громада',
                        "name_en": 'Buzhanska Hromada',
                    },
                    {
                        "uid": 1476,
                        "name": 'м. Ватутіне та Ватутінська територіальна громада',
                        "name_en": 'Vatutine and Vatutinska Hromada',
                    },
                    {
                        "uid": 1477,
                        "name": 'Виноградська територіальна громада',
                        "name_en": 'Vynohradska Hromada',
                    },
                    {
                        "uid": 1479,
                        "name": 'Водяницька територіальна громада',
                        "name_en": 'Vodianytska Hromada',
                    },
                    {
                        "uid": 1478,
                        "name": 'Вільшанська територіальна громада',
                        "name_en": 'Vilshanska Hromada',
                    },
                    {
                        "uid": 1481,
                        "name": 'Звенигородська територіальна громада',
                        "name_en": 'Zvenyhorodska Hromada',
                    },
                    {
                        "uid": 1482,
                        "name": 'Катеринопільська територіальна громада',
                        "name_en": 'Katerynopilska Hromada',
                    },
                    {
                        "uid": 1483,
                        "name": "Лип'янська територіальна громада",
                        "name_en": 'Lypianska Hromada',
                    },
                    {
                        "uid": 1484,
                        "name": 'Лисянська територіальна громада',
                        "name_en": 'Lysianska Hromada',
                    },
                    {
                        "uid": 1485,
                        "name": 'Матусівська територіальна громада',
                        "name_en": 'Matusivska Hromada',
                    },
                    {
                        "uid": 1486,
                        "name": 'Мокрокалигірська територіальна громада',
                        "name_en": 'Mokrokalyhirska Hromada',
                    },
                    {
                        "uid": 1487,
                        "name": 'Селищенська територіальна громада',
                        "name_en": 'Selyshchenska Hromada',
                    },
                    {
                        "uid": 1488,
                        "name": 'Стеблівська територіальна громада',
                        "name_en": 'Steblivska Hromada',
                    },
                    {
                        "uid": 1489,
                        "name": 'м. Тальне та Тальнівська територіальна громада',
                        "name_en": 'Talne and Talnivska Hromada',
                    },
                    {
                        "uid": 1490,
                        "name": 'Шевченківська територіальна громада',
                        "name_en": 'Shevchenkivska Hromada',
                    },
                    {
                        "uid": 1491,
                        "name": 'м. Шпола та Шполянська територіальна громада',
                        "name_en": 'Shpola and Shpolianska Hromada',
                    },
                    {
                        "uid": 1480,
                        "name": 'Єрківська територіальна громада',
                        "name_en": 'Yerkivska Hromada',
                    },
                ],
            },
            {
                "uid": 153,
                "name": 'Золотоніський район',
                "name_en": 'Zolotoniskyi Raion',
                "hromadas": [
                    {
                        "uid": 1492,
                        "name": 'Великохутірська територіальна громада',
                        "name_en": 'Velykokhutirska Hromada',
                    },
                    {
                        "uid": 1493,
                        "name": 'Вознесенська територіальна громада',
                        "name_en": 'Voznesenska Hromada',
                    },
                    {
                        "uid": 1494,
                        "name": 'Гельмязівська територіальна громада',
                        "name_en": 'Helmiazivska Hromada',
                    },
                    {
                        "uid": 1495,
                        "name": 'Драбівська територіальна громада',
                        "name_en": 'Drabivska Hromada',
                    },
                    {
                        "uid": 1496,
                        "name": 'Золотоніська територіальна громада',
                        "name_en": 'Zolotoniska Hromada',
                    },
                    {
                        "uid": 1497,
                        "name": 'Зорівська територіальна громада',
                        "name_en": 'Zorivska Hromada',
                    },
                    {
                        "uid": 1499,
                        "name": 'Новодмитрівська територіальна громада',
                        "name_en": 'Novodmytrivska Hromada',
                    },
                    {
                        "uid": 1500,
                        "name": 'Піщанська територіальна громада',
                        "name_en": 'Pishchanska Hromada',
                    },
                    {
                        "uid": 1501,
                        "name": 'Чорнобаївська територіальна громада',
                        "name_en": 'Chornobaivska Hromada',
                    },
                    {
                        "uid": 1502,
                        "name": 'Шрамківська територіальна громада',
                        "name_en": 'Shramkivska Hromada',
                    },
                    {
                        "uid": 1498,
                        "name": 'Іркліївська територіальна громада',
                        "name_en": 'Irkliivska Hromada',
                    },
                ],
            },
            {
                "uid": 151,
                "name": 'Уманський район',
                "name_en": 'Umanskyi Raion',
                "hromadas": [
                    {
                        "uid": 1437,
                        "name": 'Бабанська територіальна громада',
                        "name_en": 'Babanska Hromada',
                    },
                    {
                        "uid": 1438,
                        "name": 'Баштечківська територіальна громада',
                        "name_en": 'Bashtechkivska Hromada',
                    },
                    {
                        "uid": 1439,
                        "name": 'Буцька територіальна громада',
                        "name_en": 'Butska Hromada',
                    },
                    {
                        "uid": 1440,
                        "name": 'Дмитрушківська територіальна громада',
                        "name_en": 'Dmytrushkivska Hromada',
                    },
                    {
                        "uid": 1441,
                        "name": 'Жашківська територіальна громада',
                        "name_en": 'Zhashkivska Hromada',
                    },
                    {
                        "uid": 1443,
                        "name": 'Ладижинська територіальна громада',
                        "name_en": 'Ladyzhynska Hromada',
                    },
                    {
                        "uid": 1444,
                        "name": 'Маньківська територіальна громада',
                        "name_en": 'Mankivska Hromada',
                    },
                    {
                        "uid": 1445,
                        "name": 'м. Монастирище та Монастрищенська територіальна громада',
                        "name_en": 'Monastyryshche and Monastryshchenska Hromada',
                    },
                    {
                        "uid": 1446,
                        "name": 'Паланська територіальна громада',
                        "name_en": 'Palanska Hromada',
                    },
                    {
                        "uid": 1447,
                        "name": 'Уманська територіальна громада',
                        "name_en": 'Umanska Hromada',
                    },
                    {
                        "uid": 1448,
                        "name": 'м. Христинівка та Христинівська територіальна громада',
                        "name_en": 'Khrystynivka and Khrystynivska Hromada',
                    },
                    {
                        "uid": 1442,
                        "name": 'Іваньківська територіальна громада',
                        "name_en": 'Ivankivska Hromada',
                    },
                ],
            },
            {
                "uid": 152,
                "name": 'Черкаський район',
                "name_en": 'Cherkaskyi Raion',
                "hromadas": [
                    {
                        "uid": 1449,
                        "name": 'Балаклеївська територіальна громада',
                        "name_en": 'Balakleivska Hromada',
                    },
                    {
                        "uid": 1450,
                        "name": 'Березняківська територіальна громада',
                        "name_en": 'Berezniakivska Hromada',
                    },
                    {
                        "uid": 1452,
                        "name": 'Бобрицька територіальна громада',
                        "name_en": 'Bobrytska Hromada',
                    },
                    {
                        "uid": 1453,
                        "name": 'Будищенська територіальна громада',
                        "name_en": 'Budyshchenska Hromada',
                    },
                    {
                        "uid": 1451,
                        "name": 'Білозірська територіальна громада',
                        "name_en": 'Bilozirska Hromada',
                    },
                    {
                        "uid": 1454,
                        "name": 'Городищенська територіальна громада',
                        "name_en": 'Horodyshchenska Hromada',
                    },
                    {
                        "uid": 1455,
                        "name": 'Кам’янська територіальна громада',
                        "name_en": 'Kamyanska Hromada',
                    },
                    {
                        "uid": 1456,
                        "name": 'Канівська територіальна громада',
                        "name_en": 'Kanivska Hromada',
                    },
                    {
                        "uid": 1457,
                        "name": 'м. Корсунь-Шевченківський та Корсунь-Шевченківська територіальна громада',
                        "name_en": 'Korsun-Shevchenkivskyi and Korsun-Shevchenkivska Hromada',
                    },
                    {
                        "uid": 1458,
                        "name": 'Леськівська територіальна громада',
                        "name_en": 'Leskivska Hromada',
                    },
                    {
                        "uid": 1459,
                        "name": 'Ліплявська територіальна громада',
                        "name_en": 'Lipliavska Hromada',
                    },
                    {
                        "uid": 1460,
                        "name": 'Медведівська територіальна громада',
                        "name_en": 'Medvedivska Hromada',
                    },
                    {
                        "uid": 1461,
                        "name": 'Михайлівська територіальна громада',
                        "name_en": 'Mykhailivska Hromada',
                    },
                    {
                        "uid": 1462,
                        "name": 'Мліївська територіальна громада',
                        "name_en": 'Mliivska Hromada',
                    },
                    {
                        "uid": 1463,
                        "name": 'Мошнівська територіальна громада',
                        "name_en": 'Moshnivska Hromada',
                    },
                    {
                        "uid": 1464,
                        "name": 'Набутівська територіальна громада',
                        "name_en": 'Nabutivska Hromada',
                    },
                    {
                        "uid": 1465,
                        "name": 'Ротмістрівська територіальна громада',
                        "name_en": 'Rotmistrivska Hromada',
                    },
                    {
                        "uid": 1466,
                        "name": 'Русько-Полянська територіальна громада',
                        "name_en": 'Rusko-Polianska Hromada',
                    },
                    {
                        "uid": 1467,
                        "name": 'Сагунівська територіальна громада',
                        "name_en": 'Sahunivska Hromada',
                    },
                    {
                        "uid": 1468,
                        "name": 'Смілянська територіальна громада',
                        "name_en": 'Smilianska Hromada',
                    },
                    {
                        "uid": 1469,
                        "name": 'Степанецька територіальна громада',
                        "name_en": 'Stepanetska Hromada',
                    },
                    {
                        "uid": 1470,
                        "name": 'Степанківська територіальна громада',
                        "name_en": 'Stepankivska Hromada',
                    },
                    {
                        "uid": 1471,
                        "name": 'Тернівська територіальна громада',
                        "name_en": 'Ternivska Hromada',
                    },
                    {
                        "uid": 1472,
                        "name": 'Червонослобідська територіальна громада',
                        "name_en": 'Chervonoslobidska Hromada',
                    },
                    {
                        "uid": 1473,
                        "name": 'м. Черкаси та Черкаська територіальна громада',
                        "name_en": 'Cherkasy and Cherkaska Hromada',
                    },
                    {
                        "uid": 1474,
                        "name": 'м. Чигирин та Чигиринська територіальна громада',
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
                "name": 'Вижницький район',
                "name_en": 'Vyzhnytskyi Raion',
                "hromadas": [
                    {
                        "uid": 1503,
                        "name": 'Банилівська територіальна громада',
                        "name_en": 'Banylivska Hromada',
                    },
                    {
                        "uid": 1504,
                        "name": 'Берегометська територіальна громада',
                        "name_en": 'Berehometska Hromada',
                    },
                    {
                        "uid": 1505,
                        "name": 'Брусницька територіальна громада',
                        "name_en": 'Brusnytska Hromada',
                    },
                    {
                        "uid": 1506,
                        "name": 'Вашківецька територіальна громада',
                        "name_en": 'Vashkivetska Hromada',
                    },
                    {
                        "uid": 1507,
                        "name": 'Вижницька територіальна громада',
                        "name_en": 'Vyzhnytska Hromada',
                    },
                    {
                        "uid": 1508,
                        "name": 'Конятинська територіальна громада',
                        "name_en": 'Koniatynska Hromada',
                    },
                    {
                        "uid": 1509,
                        "name": 'Путильська територіальна громада',
                        "name_en": 'Putylska Hromada',
                    },
                    {
                        "uid": 1510,
                        "name": 'Селятинська територіальна громада',
                        "name_en": 'Seliatynska Hromada',
                    },
                    {
                        "uid": 1511,
                        "name": 'Усть-Путильська територіальна громада',
                        "name_en": 'Ust-Putylska Hromada',
                    },
                ],
            },
            {
                "uid": 139,
                "name": 'Дністровський район',
                "name_en": 'Dnistrovskyi Raion',
                "hromadas": [
                    {
                        "uid": 1545,
                        "name": 'Вашковецька територіальна громада',
                        "name_en": 'Vashkovetska Hromada',
                    },
                    {
                        "uid": 1546,
                        "name": 'Кельменецька територіальна громада',
                        "name_en": 'Kelmenetska Hromada',
                    },
                    {
                        "uid": 1547,
                        "name": 'Клішковецька територіальна громада',
                        "name_en": 'Klishkovetska Hromada',
                    },
                    {
                        "uid": 1548,
                        "name": 'Лівинецька територіальна громада',
                        "name_en": 'Livynetska Hromada',
                    },
                    {
                        "uid": 1549,
                        "name": 'Мамалигівська територіальна громада',
                        "name_en": 'Mamalyhivska Hromada',
                    },
                    {
                        "uid": 1550,
                        "name": 'Недобоївська територіальна громада',
                        "name_en": 'Nedoboivska Hromada',
                    },
                    {
                        "uid": 1551,
                        "name": 'м. Новодністровськ та Новодністровська територіальна громада',
                        "name_en": 'Novodnistrovsk and Novodnistrovska Hromada',
                    },
                    {
                        "uid": 1552,
                        "name": 'Рукшинська територіальна громада',
                        "name_en": 'Rukshynska Hromada',
                    },
                    {
                        "uid": 1553,
                        "name": 'Сокирянська територіальна громада',
                        "name_en": 'Sokyrianska Hromada',
                    },
                    {
                        "uid": 1554,
                        "name": 'Хотинська територіальна громада',
                        "name_en": 'Khotynska Hromada',
                    },
                ],
            },
            {
                "uid": 137,
                "name": 'Чернівецький район',
                "name_en": 'Chernivetskyi Raion',
                "hromadas": [
                    {
                        "uid": 1512,
                        "name": 'Боянська територіальна громада',
                        "name_en": 'Boianska Hromada',
                    },
                    {
                        "uid": 1513,
                        "name": 'Ванчиковецька територіальна громада',
                        "name_en": 'Vanchykovetska Hromada',
                    },
                    {
                        "uid": 1514,
                        "name": 'Великокучурівська територіальна громада',
                        "name_en": 'Velykokuchurivska Hromada',
                    },
                    {
                        "uid": 1515,
                        "name": 'Веренчацька територіальна громада',
                        "name_en": 'Verenchatska Hromada',
                    },
                    {
                        "uid": 1517,
                        "name": 'Волоківська територіальна громада',
                        "name_en": 'Volokivska Hromada',
                    },
                    {
                        "uid": 1516,
                        "name": 'Вікнянська територіальна громада',
                        "name_en": 'Viknianska Hromada',
                    },
                    {
                        "uid": 1518,
                        "name": 'Герцаївська територіальна громада',
                        "name_en": 'Hertsaivska Hromada',
                    },
                    {
                        "uid": 1519,
                        "name": 'Глибоцька територіальна громада',
                        "name_en": 'Hlybotska Hromada',
                    },
                    {
                        "uid": 1520,
                        "name": 'Горішньошеровецька територіальна громада',
                        "name_en": 'Horishnosherovetska Hromada',
                    },
                    {
                        "uid": 1521,
                        "name": 'Заставнівська територіальна громада',
                        "name_en": 'Zastavnivska Hromada',
                    },
                    {
                        "uid": 1522,
                        "name": 'Кадубовецька територіальна громада',
                        "name_en": 'Kadubovetska Hromada',
                    },
                    {
                        "uid": 1523,
                        "name": "Кам'янецька територіальна громада",
                        "name_en": 'Kamianetska Hromada',
                    },
                    {
                        "uid": 1524,
                        "name": "Кам'янська територіальна громада",
                        "name_en": 'Kamianska Hromada',
                    },
                    {
                        "uid": 1525,
                        "name": 'Карапачівська територіальна громада',
                        "name_en": 'Karapachivska Hromada',
                    },
                    {
                        "uid": 1527,
                        "name": 'Кострижівська територіальна громада',
                        "name_en": 'Kostryzhivska Hromada',
                    },
                    {
                        "uid": 1528,
                        "name": 'Красноїльська територіальна громада',
                        "name_en": 'Krasnoilska Hromada',
                    },
                    {
                        "uid": 1526,
                        "name": 'Кіцманська територіальна громада',
                        "name_en": 'Kitsmanska Hromada',
                    },
                    {
                        "uid": 1529,
                        "name": 'Магальська територіальна громада',
                        "name_en": 'Mahalska Hromada',
                    },
                    {
                        "uid": 1530,
                        "name": 'Мамаївська територіальна громада',
                        "name_en": 'Mamaivska Hromada',
                    },
                    {
                        "uid": 1531,
                        "name": 'Неполоковецька територіальна громада',
                        "name_en": 'Nepolokovetska Hromada',
                    },
                    {
                        "uid": 1532,
                        "name": 'Новоселицька територіальна громада',
                        "name_en": 'Novoselytska Hromada',
                    },
                    {
                        "uid": 1533,
                        "name": 'Острицька територіальна громада',
                        "name_en": 'Ostrytska Hromada',
                    },
                    {
                        "uid": 1534,
                        "name": 'Петровецька територіальна громада',
                        "name_en": 'Petrovetska Hromada',
                    },
                    {
                        "uid": 1535,
                        "name": 'Ставчанська територіальна громада',
                        "name_en": 'Stavchanska Hromada',
                    },
                    {
                        "uid": 1536,
                        "name": 'Сторожинецька територіальна громада',
                        "name_en": 'Storozhynetska Hromada',
                    },
                    {
                        "uid": 1537,
                        "name": 'Сучевенська територіальна громада',
                        "name_en": 'Suchevenska Hromada',
                    },
                    {
                        "uid": 1538,
                        "name": 'Тарашанська територіальна громада',
                        "name_en": 'Tarashanska Hromada',
                    },
                    {
                        "uid": 1539,
                        "name": 'Тереблеченська територіальна громада',
                        "name_en": 'Tereblechenska Hromada',
                    },
                    {
                        "uid": 1540,
                        "name": 'Топорівська територіальна громада',
                        "name_en": 'Toporivska Hromada',
                    },
                    {
                        "uid": 1541,
                        "name": 'Чагорська територіальна громада',
                        "name_en": 'Chahorska Hromada',
                    },
                    {
                        "uid": 1542,
                        "name": 'м. Чернівці та Чернівецька територіальна громада',
                        "name_en": 'Chernivtsi and Chernivetska Hromada',
                    },
                    {
                        "uid": 1543,
                        "name": 'Чудейська територіальна громада',
                        "name_en": 'Chudeiska Hromada',
                    },
                    {
                        "uid": 1544,
                        "name": 'Юрковецька територіальна громада',
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
                "name": 'Корюківський район',
                "name_en": 'Koriukivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1607,
                        "name": 'Корюківська територіальна громада',
                        "name_en": 'Koriukivska Hromada',
                    },
                    {
                        "uid": 1608,
                        "name": 'Менська територіальна громада',
                        "name_en": 'Menska Hromada',
                    },
                    {
                        "uid": 1609,
                        "name": 'Сновська територіальна громада',
                        "name_en": 'Snovska Hromada',
                    },
                    {
                        "uid": 1610,
                        "name": 'Сосницька територіальна громада',
                        "name_en": 'Sosnytska Hromada',
                    },
                    {
                        "uid": 1611,
                        "name": 'Холминська територіальна громада',
                        "name_en": 'Kholmynska Hromada',
                    },
                ],
            },
            {
                "uid": 141,
                "name": 'Новгород-Сіверський район',
                "name_en": 'Novhorod-Siverskyi Raion',
                "hromadas": [
                    {
                        "uid": 1603,
                        "name": 'Коропська територіальна громада',
                        "name_en": 'Koropska Hromada',
                    },
                    {
                        "uid": 1604,
                        "name": 'м. Новгород-Сіверський та Новгород-Сіверська територіальна громада',
                        "name_en": 'Novhorod-Siverskyi and Novhorod-Siverska Hromada',
                    },
                    {
                        "uid": 1605,
                        "name": 'Понорницька територіальна громада',
                        "name_en": 'Ponornytska Hromada',
                    },
                    {
                        "uid": 1606,
                        "name": 'Семенівська територіальна громада',
                        "name_en": 'Semenivska Hromada',
                    },
                ],
            },
            {
                "uid": 142,
                "name": 'Ніжинський район',
                "name_en": 'Nizhynskyi Raion',
                "hromadas": [
                    {
                        "uid": 1555,
                        "name": 'Батуринська територіальна громада',
                        "name_en": 'Baturynska Hromada',
                    },
                    {
                        "uid": 1556,
                        "name": 'Бахмацька територіальна громада',
                        "name_en": 'Bakhmatska Hromada',
                    },
                    {
                        "uid": 1557,
                        "name": 'Бобровицька територіальна громада',
                        "name_en": 'Bobrovytska Hromada',
                    },
                    {
                        "uid": 1558,
                        "name": 'Борзнянська територіальна громада',
                        "name_en": 'Borznianska Hromada',
                    },
                    {
                        "uid": 1559,
                        "name": 'Вертіївська територіальна громада',
                        "name_en": 'Vertiivska Hromada',
                    },
                    {
                        "uid": 1560,
                        "name": 'Височанська територіальна громада',
                        "name_en": 'Vysochanska Hromada',
                    },
                    {
                        "uid": 1561,
                        "name": 'Дмитрівська територіальна громада',
                        "name_en": 'Dmytrivska Hromada',
                    },
                    {
                        "uid": 1562,
                        "name": 'Комарівська територіальна громада',
                        "name_en": 'Komarivska Hromada',
                    },
                    {
                        "uid": 1563,
                        "name": 'Крутівська територіальна громада',
                        "name_en": 'Krutivska Hromada',
                    },
                    {
                        "uid": 1564,
                        "name": 'Лосинівська територіальна громада',
                        "name_en": 'Losynivska Hromada',
                    },
                    {
                        "uid": 1565,
                        "name": 'Макіївська територіальна громада',
                        "name_en": 'Makiivska Hromada',
                    },
                    {
                        "uid": 1566,
                        "name": 'Мринська територіальна громада',
                        "name_en": 'Mrynska Hromada',
                    },
                    {
                        "uid": 1568,
                        "name": 'Новобасанська територіальна громада',
                        "name_en": 'Novobasanska Hromada',
                    },
                    {
                        "uid": 1569,
                        "name": 'Носівська територіальна громада',
                        "name_en": 'Nosivska Hromada',
                    },
                    {
                        "uid": 1567,
                        "name": 'м. Ніжин та Ніжинська територіальна громада',
                        "name_en": 'Nizhyn and Nizhynska Hromada',
                    },
                    {
                        "uid": 1570,
                        "name": 'Плисківська територіальна громада',
                        "name_en": 'Plyskivska Hromada',
                    },
                    {
                        "uid": 1571,
                        "name": 'Талалаївська територіальна громада',
                        "name_en": 'Talalaivska Hromada',
                    },
                ],
            },
            {
                "uid": 143,
                "name": 'Прилуцький район',
                "name_en": 'Prylutskyi Raion',
                "hromadas": [
                    {
                        "uid": 1592,
                        "name": 'Варвинська територіальна громада',
                        "name_en": 'Varvynska Hromada',
                    },
                    {
                        "uid": 1594,
                        "name": 'Ладанська територіальна громада',
                        "name_en": 'Ladanska Hromada',
                    },
                    {
                        "uid": 1595,
                        "name": 'Линовицька територіальна громада',
                        "name_en": 'Lynovytska Hromada',
                    },
                    {
                        "uid": 1596,
                        "name": 'Малодівицька територіальна громада',
                        "name_en": 'Malodivytska Hromada',
                    },
                    {
                        "uid": 1597,
                        "name": 'Парафіївська територіальна громада',
                        "name_en": 'Parafiivska Hromada',
                    },
                    {
                        "uid": 1598,
                        "name": 'м. Прилуки та Прилуцька територіальна громада',
                        "name_en": 'Pryluky and Prylutska Hromada',
                    },
                    {
                        "uid": 1599,
                        "name": 'Срібнянська територіальна громада',
                        "name_en": 'Sribnianska Hromada',
                    },
                    {
                        "uid": 1600,
                        "name": "Сухополов'янська територіальна громада",
                        "name_en": 'Sukhopolovianska Hromada',
                    },
                    {
                        "uid": 1601,
                        "name": 'Талалаївська територіальна громада',
                        "name_en": 'Talalaivska Hromada',
                    },
                    {
                        "uid": 1602,
                        "name": 'Яблунівська територіальна громада',
                        "name_en": 'Yablunivska Hromada',
                    },
                    {
                        "uid": 1593,
                        "name": 'Ічнянська територіальна громада',
                        "name_en": 'Ichnianska Hromada',
                    },
                ],
            },
            {
                "uid": 140,
                "name": 'Чернігівський район',
                "name_en": 'Chernihivskyi Raion',
                "hromadas": [
                    {
                        "uid": 1572,
                        "name": 'Березнянська територіальна громада',
                        "name_en": 'Bereznianska Hromada',
                    },
                    {
                        "uid": 1573,
                        "name": 'Гончарівська територіальна громада',
                        "name_en": 'Honcharivska Hromada',
                    },
                    {
                        "uid": 1574,
                        "name": 'Городнянська територіальна громада',
                        "name_en": 'Horodnianska Hromada',
                    },
                    {
                        "uid": 1575,
                        "name": 'Деснянська територіальна громада',
                        "name_en": 'Desnianska Hromada',
                    },
                    {
                        "uid": 1576,
                        "name": 'Добрянська територіальна громада',
                        "name_en": 'Dobrianska Hromada',
                    },
                    {
                        "uid": 1579,
                        "name": 'Киселівська територіальна громада',
                        "name_en": 'Kyselivska Hromada',
                    },
                    {
                        "uid": 1578,
                        "name": 'Киїнська територіальна громада',
                        "name_en": 'Kyinska Hromada',
                    },
                    {
                        "uid": 1581,
                        "name": 'Козелецька територіальна громада',
                        "name_en": 'Kozeletska Hromada',
                    },
                    {
                        "uid": 1582,
                        "name": 'Куликівська територіальна громада',
                        "name_en": 'Kulykivska Hromada',
                    },
                    {
                        "uid": 1580,
                        "name": 'Кіптівська територіальна громада',
                        "name_en": 'Kiptivska Hromada',
                    },
                    {
                        "uid": 1583,
                        "name": 'Любецька територіальна громада',
                        "name_en": 'Liubetska Hromada',
                    },
                    {
                        "uid": 1584,
                        "name": 'Михайло-Коцюбинська територіальна громада',
                        "name_en": 'Mykhailo-Kotsiubynska Hromada',
                    },
                    {
                        "uid": 1585,
                        "name": 'Новобілоуська територіальна громада',
                        "name_en": 'Novobilouska Hromada',
                    },
                    {
                        "uid": 1586,
                        "name": 'Олишівська територіальна громада',
                        "name_en": 'Olyshivska Hromada',
                    },
                    {
                        "uid": 1587,
                        "name": 'Остерська територіальна громада',
                        "name_en": 'Osterska Hromada',
                    },
                    {
                        "uid": 1588,
                        "name": 'Ріпкинська територіальна громада',
                        "name_en": 'Ripkynska Hromada',
                    },
                    {
                        "uid": 1589,
                        "name": 'Седнівська територіальна громада',
                        "name_en": 'Sednivska Hromada',
                    },
                    {
                        "uid": 1590,
                        "name": 'Тупичівська територіальна громада',
                        "name_en": 'Tupychivska Hromada',
                    },
                    {
                        "uid": 1591,
                        "name": 'м. Чернігів та Чернігівська територіальна громада',
                        "name_en": 'Chernihiv and Chernihivska Hromada',
                    },
                    {
                        "uid": 1577,
                        "name": 'Іванівська територіальна громада',
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
                "name": 'Верховинський район',
                "name_en": 'Verkhovynskyi Raion',
                "hromadas": [
                    {
                        "uid": 620,
                        "name": 'Білоберізька територіальна громада',
                        "name_en": 'Biloberizka Hromada',
                    },
                    {
                        "uid": 621,
                        "name": 'Верховинська територіальна громада',
                        "name_en": 'Verkhovynska Hromada',
                    },
                    {
                        "uid": 622,
                        "name": 'Зеленська територіальна громада',
                        "name_en": 'Zelenska Hromada',
                    },
                ],
            },
            {
                "uid": 71,
                "name": 'Калуський район',
                "name_en": 'Kaluskyi Raion',
                "hromadas": [
                    {
                        "uid": 643,
                        "name": 'м. Болехів та Болехівська територіальна громада',
                        "name_en": 'Bolekhiv and Bolekhivska Hromada',
                    },
                    {
                        "uid": 644,
                        "name": 'Брошнів-Осадська територіальна громада',
                        "name_en": 'Broshniv-Osadska Hromada',
                    },
                    {
                        "uid": 645,
                        "name": 'Верхнянська територіальна громада',
                        "name_en": 'Verkhnianska Hromada',
                    },
                    {
                        "uid": 646,
                        "name": 'Вигодська територіальна громада',
                        "name_en": 'Vyhodska Hromada',
                    },
                    {
                        "uid": 647,
                        "name": 'Витвицька територіальна громада',
                        "name_en": 'Vytvytska Hromada',
                    },
                    {
                        "uid": 648,
                        "name": 'Войнилівська територіальна громада',
                        "name_en": 'Voinylivska Hromada',
                    },
                    {
                        "uid": 649,
                        "name": 'м. Долина та Долинська територіальна громада',
                        "name_en": 'Dolyna and Dolynska Hromada',
                    },
                    {
                        "uid": 650,
                        "name": 'Дубівська територіальна громада',
                        "name_en": 'Dubivska Hromada',
                    },
                    {
                        "uid": 651,
                        "name": 'м. Калуш та Калуська територіальна громада',
                        "name_en": 'Kalush and Kaluska Hromada',
                    },
                    {
                        "uid": 652,
                        "name": 'Новицька територіальна громада',
                        "name_en": 'Novytska Hromada',
                    },
                    {
                        "uid": 653,
                        "name": 'Перегінська територіальна громада',
                        "name_en": 'Perehinska Hromada',
                    },
                    {
                        "uid": 654,
                        "name": 'Рожнятівська територіальна громада',
                        "name_en": 'Rozhniativska Hromada',
                    },
                    {
                        "uid": 655,
                        "name": 'Спаська територіальна громада',
                        "name_en": 'Spaska Hromada',
                    },
                ],
            },
            {
                "uid": 70,
                "name": 'Коломийський район',
                "name_en": 'Kolomyiskyi Raion',
                "hromadas": [
                    {
                        "uid": 664,
                        "name": 'Гвіздецька територіальна громада',
                        "name_en": 'Hvizdetska Hromada',
                    },
                    {
                        "uid": 665,
                        "name": 'Городенківська територіальна громада',
                        "name_en": 'Horodenkivska Hromada',
                    },
                    {
                        "uid": 666,
                        "name": 'Заболотівська територіальна громада',
                        "name_en": 'Zabolotivska Hromada',
                    },
                    {
                        "uid": 667,
                        "name": 'м. Коломия та Коломийська територіальна громада',
                        "name_en": 'Kolomyia and Kolomyiska Hromada',
                    },
                    {
                        "uid": 668,
                        "name": 'Коршівська територіальна громада',
                        "name_en": 'Korshivska Hromada',
                    },
                    {
                        "uid": 669,
                        "name": 'Матеївецька територіальна громада',
                        "name_en": 'Mateivetska Hromada',
                    },
                    {
                        "uid": 670,
                        "name": 'Нижньовербізька територіальна громада',
                        "name_en": 'Nyzhnoverbizka Hromada',
                    },
                    {
                        "uid": 671,
                        "name": 'Отинійська територіальна громада',
                        "name_en": 'Otyniiska Hromada',
                    },
                    {
                        "uid": 674,
                        "name": "П'ядицька територіальна громада",
                        "name_en": 'Piadytska Hromada',
                    },
                    {
                        "uid": 672,
                        "name": 'Печеніжинська територіальна громада',
                        "name_en": 'Pechenizhynska Hromada',
                    },
                    {
                        "uid": 673,
                        "name": 'Підгайчиківська територіальна громада',
                        "name_en": 'Pidhaichykivska Hromada',
                    },
                    {
                        "uid": 675,
                        "name": 'Снятинська територіальна громада',
                        "name_en": 'Sniatynska Hromada',
                    },
                    {
                        "uid": 676,
                        "name": 'Чернелицька територіальна громада',
                        "name_en": 'Chernelytska Hromada',
                    },
                ],
            },
            {
                "uid": 69,
                "name": 'Косівський район',
                "name_en": 'Kosivskyi Raion',
                "hromadas": [
                    {
                        "uid": 678,
                        "name": 'Космацька територіальна громада',
                        "name_en": 'Kosmatska Hromada',
                    },
                    {
                        "uid": 677,
                        "name": 'Косівська територіальна громада',
                        "name_en": 'Kosivska Hromada',
                    },
                    {
                        "uid": 679,
                        "name": 'Кутська територіальна громада',
                        "name_en": 'Kutska Hromada',
                    },
                    {
                        "uid": 680,
                        "name": 'Рожнівська територіальна громада',
                        "name_en": 'Rozhnivska Hromada',
                    },
                    {
                        "uid": 681,
                        "name": 'Яблунівська територіальна громада',
                        "name_en": 'Yablunivska Hromada',
                    },
                ],
            },
            {
                "uid": 72,
                "name": 'Надвірнянський район',
                "name_en": 'Nadvirnianskyi Raion',
                "hromadas": [
                    {
                        "uid": 656,
                        "name": 'Ворохтянська територіальна громада',
                        "name_en": 'Vorokhtianska Hromada',
                    },
                    {
                        "uid": 657,
                        "name": 'Делятинська територіальна громада',
                        "name_en": 'Deliatynska Hromada',
                    },
                    {
                        "uid": 658,
                        "name": 'Ланчинська територіальна громада',
                        "name_en": 'Lanchynska Hromada',
                    },
                    {
                        "uid": 659,
                        "name": 'м. Надвірна та Надвірнянська територіальна громада',
                        "name_en": 'Nadvirna and Nadvirnianska Hromada',
                    },
                    {
                        "uid": 660,
                        "name": 'Пасічнянська територіальна громада',
                        "name_en": 'Pasichnianska Hromada',
                    },
                    {
                        "uid": 661,
                        "name": 'Переріслянська територіальна громада',
                        "name_en": 'Pererislianska Hromada',
                    },
                    {
                        "uid": 662,
                        "name": 'Поляницька територіальна громада',
                        "name_en": 'Polianytska Hromada',
                    },
                    {
                        "uid": 663,
                        "name": 'м. Яремче та Яремчанська територіальна громада',
                        "name_en": 'Yaremche and Yaremchanska Hromada',
                    },
                ],
            },
            {
                "uid": 68,
                "name": 'Івано-Франківський район',
                "name_en": 'Ivano-Frankivskyi Raion',
                "hromadas": [
                    {
                        "uid": 624,
                        "name": 'Богородчанська територіальна громада',
                        "name_en": 'Bohorodchanska Hromada',
                    },
                    {
                        "uid": 625,
                        "name": 'Букачівська територіальна громада',
                        "name_en": 'Bukachivska Hromada',
                    },
                    {
                        "uid": 626,
                        "name": 'м. Бурштин та Бурштинська територіальна громада',
                        "name_en": 'Burshtyn and Burshtynska Hromada',
                    },
                    {
                        "uid": 623,
                        "name": 'Більшівцівська територіальна громада',
                        "name_en": 'Bilshivtsivska Hromada',
                    },
                    {
                        "uid": 627,
                        "name": 'Галицька територіальна громада',
                        "name_en": 'Halytska Hromada',
                    },
                    {
                        "uid": 628,
                        "name": 'Дзвиняцька територіальна громада',
                        "name_en": 'Dzvyniatska Hromada',
                    },
                    {
                        "uid": 629,
                        "name": 'Дубовецька територіальна громада',
                        "name_en": 'Dubovetska Hromada',
                    },
                    {
                        "uid": 631,
                        "name": 'Загвіздянська територіальна громада',
                        "name_en": 'Zahvizdianska Hromada',
                    },
                    {
                        "uid": 633,
                        "name": 'Лисецька територіальна громада',
                        "name_en": 'Lysetska Hromada',
                    },
                    {
                        "uid": 634,
                        "name": 'Обертинська територіальна громада',
                        "name_en": 'Obertynska Hromada',
                    },
                    {
                        "uid": 635,
                        "name": 'Олешанська територіальна громада',
                        "name_en": 'Oleshanska Hromada',
                    },
                    {
                        "uid": 636,
                        "name": 'Рогатинська територіальна громада',
                        "name_en": 'Rohatynska Hromada',
                    },
                    {
                        "uid": 637,
                        "name": 'Солотвинська територіальна громада',
                        "name_en": 'Solotvynska Hromada',
                    },
                    {
                        "uid": 638,
                        "name": 'Старобогородчанська територіальна громада',
                        "name_en": 'Starobohorodchanska Hromada',
                    },
                    {
                        "uid": 639,
                        "name": 'Тисменицька територіальна громада',
                        "name_en": 'Tysmenytska Hromada',
                    },
                    {
                        "uid": 640,
                        "name": 'Тлумацька територіальна громада',
                        "name_en": 'Tlumatska Hromada',
                    },
                    {
                        "uid": 641,
                        "name": 'Угринівська територіальна громада',
                        "name_en": 'Uhrynivska Hromada',
                    },
                    {
                        "uid": 642,
                        "name": 'Ямницька територіальна громада',
                        "name_en": 'Yamnytska Hromada',
                    },
                    {
                        "uid": 630,
                        "name": 'Єзупільська територіальна громада',
                        "name_en": 'Yezupilska Hromada',
                    },
                    {
                        "uid": 632,
                        "name": 'м. Івано-Франківськ та Івано-Франківська територіальна громада',
                        "name_en": 'Ivano-Frankivsk and Ivano-Frankivska Hromada',
                    },
                ],
            },
        ],
    },
]
