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
        "name": 'Волинська',
        "type": LocationType.OBLAST,
        "name_en": 'Volynska',
        "districts": [
            {
                "uid": 38,
                "name": 'Володимирський',
                "name_en": 'Volodymyrskyi',
                "hromadas": [
                    {
                        "uid": 255,
                        "name": 'м. Володимир та Володимирська',
                        "name_en": 'Volodymyr and Volodymyrska',
                    },
                    {
                        "uid": 256,
                        "name": 'Затурцівська',
                        "name_en": 'Zaturtsivska',
                    },
                    {
                        "uid": 257,
                        "name": 'Зимнівська',
                        "name_en": 'Zymnivska',
                    },
                    {
                        "uid": 259,
                        "name": 'Литовезька',
                        "name_en": 'Lytovezka',
                    },
                    {
                        "uid": 260,
                        "name": 'Локачинська',
                        "name_en": 'Lokachynska',
                    },
                    {
                        "uid": 261,
                        "name": 'м. Нововолинськ та Нововолинська',
                        "name_en": 'Novovolynsk and Novovolynska',
                    },
                    {
                        "uid": 262,
                        "name": 'Оваднівська',
                        "name_en": 'Ovadnivska',
                    },
                    {
                        "uid": 263,
                        "name": 'Павлівська',
                        "name_en": 'Pavlivska',
                    },
                    {
                        "uid": 264,
                        "name": 'Поромівська',
                        "name_en": 'Poromivska',
                    },
                    {
                        "uid": 265,
                        "name": 'Устилузька',
                        "name_en": 'Ustyluzka',
                    },
                    {
                        "uid": 258,
                        "name": 'Іваничівська',
                        "name_en": 'Ivanychivska',
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
                "name_en": 'Kamin-Kashyrskyi',
                "hromadas": [
                    {
                        "uid": 266,
                        "name": 'Камінь-Каширська',
                        "name_en": 'Kamin-Kashyrska',
                    },
                    {
                        "uid": 267,
                        "name": 'Любешівська',
                        "name_en": 'Liubeshivska',
                    },
                    {
                        "uid": 268,
                        "name": 'Маневицька',
                        "name_en": 'Manevytska',
                    },
                    {
                        "uid": 269,
                        "name": 'Прилісненська',
                        "name_en": 'Prylisnenska',
                    },
                    {
                        "uid": 270,
                        "name": 'Сошичненська',
                        "name_en": 'Soshychnenska',
                    },
                ],
            },
            {
                "uid": 40,
                "name": 'Ковельський',
                "name_en": 'Kovelskyi',
                "hromadas": [
                    {
                        "uid": 232,
                        "name": 'Велимченська',
                        "name_en": 'Velymchenska',
                    },
                    {
                        "uid": 233,
                        "name": 'Велицька',
                        "name_en": 'Velytska',
                    },
                    {
                        "uid": 234,
                        "name": 'Вишнівська',
                        "name_en": 'Vyshnivska',
                    },
                    {
                        "uid": 235,
                        "name": 'Голобська',
                        "name_en": 'Holobska',
                    },
                    {
                        "uid": 236,
                        "name": 'Головненська',
                        "name_en": 'Holovnenska',
                    },
                    {
                        "uid": 237,
                        "name": 'Дубечненська',
                        "name_en": 'Dubechnenska',
                    },
                    {
                        "uid": 238,
                        "name": 'Дубівська',
                        "name_en": 'Dubivska',
                    },
                    {
                        "uid": 239,
                        "name": 'Заболоттівська',
                        "name_en": 'Zabolottivska',
                    },
                    {
                        "uid": 240,
                        "name": 'Забродівська',
                        "name_en": 'Zabrodivska',
                    },
                    {
                        "uid": 241,
                        "name": 'м. Ковель та Ковельська',
                        "name_en": 'Kovel and Kovelska',
                    },
                    {
                        "uid": 242,
                        "name": 'Колодяжненська',
                        "name_en": 'Kolodiazhnenska',
                    },
                    {
                        "uid": 243,
                        "name": 'Луківська',
                        "name_en": 'Lukivska',
                    },
                    {
                        "uid": 244,
                        "name": 'Люблинецька',
                        "name_en": 'Liublynetska',
                    },
                    {
                        "uid": 245,
                        "name": 'м. Любомиль та Любомльська',
                        "name_en": 'Liubomyl and Liubomlska',
                    },
                    {
                        "uid": 246,
                        "name": 'Поворська',
                        "name_en": 'Povorska',
                    },
                    {
                        "uid": 247,
                        "name": 'Ратнівська',
                        "name_en": 'Ratnivska',
                    },
                    {
                        "uid": 248,
                        "name": 'Рівненська',
                        "name_en": 'Rivnenska',
                    },
                    {
                        "uid": 249,
                        "name": 'Самарівська',
                        "name_en": 'Samarivska',
                    },
                    {
                        "uid": 250,
                        "name": 'Сереховичівська',
                        "name_en": 'Serekhovychivska',
                    },
                    {
                        "uid": 251,
                        "name": 'Смідинська',
                        "name_en": 'Smidynska',
                    },
                    {
                        "uid": 252,
                        "name": 'Старовижівська',
                        "name_en": 'Starovyzhivska',
                    },
                    {
                        "uid": 253,
                        "name": 'Турійська',
                        "name_en": 'Turiiska',
                    },
                    {
                        "uid": 254,
                        "name": 'м. Шацьк та Шацька',
                        "name_en": 'Shatsk and Shatska',
                    },
                ],
            },
            {
                "uid": 39,
                "name": 'Луцький',
                "name_en": 'Lutskyi',
                "hromadas": [
                    {
                        "uid": 217,
                        "name": 'Берестечківська',
                        "name_en": 'Berestechkivska',
                    },
                    {
                        "uid": 218,
                        "name": 'Боратинська',
                        "name_en": 'Boratynska',
                    },
                    {
                        "uid": 219,
                        "name": 'Городищенська',
                        "name_en": 'Horodyshchenska',
                    },
                    {
                        "uid": 220,
                        "name": 'Горохівська',
                        "name_en": 'Horokhivska',
                    },
                    {
                        "uid": 221,
                        "name": 'Доросинівська',
                        "name_en": 'Dorosynivska',
                    },
                    {
                        "uid": 223,
                        "name": 'Колківська',
                        "name_en": 'Kolkivska',
                    },
                    {
                        "uid": 224,
                        "name": 'Копачівська',
                        "name_en": 'Kopachivska',
                    },
                    {
                        "uid": 222,
                        "name": 'Ківерцівська',
                        "name_en": 'Kivertsivska',
                    },
                    {
                        "uid": 225,
                        "name": 'м. Луцьк та Луцька',
                        "name_en": 'Lutsk and Lutska',
                    },
                    {
                        "uid": 226,
                        "name": "Мар'янівська",
                        "name_en": 'Marianivska',
                    },
                    {
                        "uid": 227,
                        "name": 'Олицька',
                        "name_en": 'Olytska',
                    },
                    {
                        "uid": 228,
                        "name": 'Підгайцівська',
                        "name_en": 'Pidhaitsivska',
                    },
                    {
                        "uid": 229,
                        "name": 'Рожищенська',
                        "name_en": 'Rozhyshchenska',
                    },
                    {
                        "uid": 230,
                        "name": 'Торчинська',
                        "name_en": 'Torchynska',
                    },
                    {
                        "uid": 231,
                        "name": 'Цуманська',
                        "name_en": 'Tsumanska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 4,
        "name": 'Вінницька',
        "type": LocationType.OBLAST,
        "name_en": 'Vinnytska',
        "districts": [
            {
                "uid": 36,
                "name": 'Вінницький',
                "name_en": 'Vinnytskyi',
                "hromadas": [
                    {
                        "uid": 154,
                        "name": 'Агрономічна',
                        "name_en": 'Ahronomichna',
                    },
                    {
                        "uid": 156,
                        "name": 'Вороновицька',
                        "name_en": 'Voronovytska',
                    },
                    {
                        "uid": 155,
                        "name": 'м. Вінниця та Вінницька',
                        "name_en": 'Vinnytsia and Vinnytska',
                    },
                    {
                        "uid": 157,
                        "name": 'Гніванська',
                        "name_en": 'Hnivanska',
                    },
                    {
                        "uid": 159,
                        "name": 'Липовецька',
                        "name_en": 'Lypovetska',
                    },
                    {
                        "uid": 161,
                        "name": 'Лука-Мелешківська',
                        "name_en": 'Luka-Meleshkivska',
                    },
                    {
                        "uid": 160,
                        "name": 'Літинська',
                        "name_en": 'Litynska',
                    },
                    {
                        "uid": 162,
                        "name": 'Немирівська',
                        "name_en": 'Nemyrivska',
                    },
                    {
                        "uid": 163,
                        "name": 'Оратівська',
                        "name_en": 'Orativska',
                    },
                    {
                        "uid": 164,
                        "name": 'Погребищенська',
                        "name_en": 'Pohrebyshchenska',
                    },
                    {
                        "uid": 165,
                        "name": 'Стрижавська',
                        "name_en": 'Stryzhavska',
                    },
                    {
                        "uid": 166,
                        "name": 'Сутисківська',
                        "name_en": 'Sutyskivska',
                    },
                    {
                        "uid": 167,
                        "name": 'Тиврівська',
                        "name_en": 'Tyvrivska',
                    },
                    {
                        "uid": 168,
                        "name": 'Турбівська',
                        "name_en": 'Turbivska',
                    },
                    {
                        "uid": 169,
                        "name": 'Якушинецька',
                        "name_en": 'Yakushynetska',
                    },
                    {
                        "uid": 158,
                        "name": 'Іллінецька',
                        "name_en": 'Illinetska',
                    },
                ],
            },
            {
                "uid": 37,
                "name": 'Гайсинський',
                "name_en": 'Haisynskyi',
                "hromadas": [
                    {
                        "uid": 185,
                        "name": 'Бершадська',
                        "name_en": 'Bershadska',
                    },
                    {
                        "uid": 186,
                        "name": 'Гайсинська',
                        "name_en": 'Haisynska',
                    },
                    {
                        "uid": 187,
                        "name": 'Дашівська',
                        "name_en": 'Dashivska',
                    },
                    {
                        "uid": 188,
                        "name": 'Джулинська',
                        "name_en": 'Dzhulynska',
                    },
                    {
                        "uid": 189,
                        "name": 'Краснопільська',
                        "name_en": 'Krasnopilska',
                    },
                    {
                        "uid": 190,
                        "name": 'Кунківська',
                        "name_en": 'Kunkivska',
                    },
                    {
                        "uid": 191,
                        "name": 'м. Ладижин та Ладижинська',
                        "name_en": 'Ladyzhyn and Ladyzhynska',
                    },
                    {
                        "uid": 192,
                        "name": 'Ободівська',
                        "name_en": 'Obodivska',
                    },
                    {
                        "uid": 193,
                        "name": 'Ольгопільська',
                        "name_en": 'Olhopilska',
                    },
                    {
                        "uid": 194,
                        "name": 'Райгородська',
                        "name_en": 'Raihorodska',
                    },
                    {
                        "uid": 195,
                        "name": 'Соболівська',
                        "name_en": 'Sobolivska',
                    },
                    {
                        "uid": 196,
                        "name": 'Теплицька',
                        "name_en": 'Teplytska',
                    },
                    {
                        "uid": 197,
                        "name": 'Тростянецька',
                        "name_en": 'Trostianetska',
                    },
                    {
                        "uid": 198,
                        "name": 'Чечельницька',
                        "name_en": 'Chechelnytska',
                    },
                ],
            },
            {
                "uid": 35,
                "name": 'Жмеринський',
                "name_en": 'Zhmerynskyi',
                "hromadas": [
                    {
                        "uid": 177,
                        "name": 'Барська',
                        "name_en": 'Barska',
                    },
                    {
                        "uid": 178,
                        "name": 'Джуринська',
                        "name_en": 'Dzhurynska',
                    },
                    {
                        "uid": 179,
                        "name": 'м. Жмеринка та Жмеринська',
                        "name_en": 'Zhmerynka and Zhmerynska',
                    },
                    {
                        "uid": 180,
                        "name": 'Копайгородська',
                        "name_en": 'Kopaihorodska',
                    },
                    {
                        "uid": 181,
                        "name": 'Мурафська',
                        "name_en": 'Murafska',
                    },
                    {
                        "uid": 182,
                        "name": 'Северинівська',
                        "name_en": 'Severynivska',
                    },
                    {
                        "uid": 183,
                        "name": 'Станіславчицька',
                        "name_en": 'Stanislavchytska',
                    },
                    {
                        "uid": 184,
                        "name": 'Шаргородська',
                        "name_en": 'Sharhorodska',
                    },
                ],
            },
            {
                "uid": 33,
                "name": 'Могилів-Подільський',
                "name_en": 'Mohyliv-Podilskyi',
                "hromadas": [
                    {
                        "uid": 170,
                        "name": 'Бабчинецька',
                        "name_en": 'Babchynetska',
                    },
                    {
                        "uid": 171,
                        "name": 'Вендичанська',
                        "name_en": 'Vendychanska',
                    },
                    {
                        "uid": 172,
                        "name": 'м. Могилів-Подільський та Могилів-Подільська',
                        "name_en": 'Mohyliv-Podilskyi and Mohyliv-Podilska',
                    },
                    {
                        "uid": 173,
                        "name": 'Мурованокуриловецька',
                        "name_en": 'Murovanokurylovetska',
                    },
                    {
                        "uid": 174,
                        "name": 'Чернівецька',
                        "name_en": 'Chernivetska',
                    },
                    {
                        "uid": 175,
                        "name": 'Ямпільська',
                        "name_en": 'Yampilska',
                    },
                    {
                        "uid": 176,
                        "name": 'Яришівська',
                        "name_en": 'Yaryshivska',
                    },
                ],
            },
            {
                "uid": 32,
                "name": 'Тульчинський',
                "name_en": 'Tulchynskyi',
                "hromadas": [
                    {
                        "uid": 199,
                        "name": 'Брацлавська',
                        "name_en": 'Bratslavska',
                    },
                    {
                        "uid": 200,
                        "name": 'Вапнярська',
                        "name_en": 'Vapniarska',
                    },
                    {
                        "uid": 201,
                        "name": 'Городківська',
                        "name_en": 'Horodkivska',
                    },
                    {
                        "uid": 202,
                        "name": 'Крижопільська',
                        "name_en": 'Kryzhopilska',
                    },
                    {
                        "uid": 203,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska',
                    },
                    {
                        "uid": 204,
                        "name": 'Студенянська',
                        "name_en": 'Studenianska',
                    },
                    {
                        "uid": 205,
                        "name": 'Томашпільська',
                        "name_en": 'Tomashpilska',
                    },
                    {
                        "uid": 206,
                        "name": 'Тульчинська',
                        "name_en": 'Tulchynska',
                    },
                    {
                        "uid": 207,
                        "name": 'Шпиківська',
                        "name_en": 'Shpykivska',
                    },
                ],
            },
            {
                "uid": 34,
                "name": 'Хмільницький',
                "name_en": 'Khmilnytskyi',
                "hromadas": [
                    {
                        "uid": 208,
                        "name": 'Глуховецька',
                        "name_en": 'Hlukhovetska',
                    },
                    {
                        "uid": 209,
                        "name": 'Жданівська',
                        "name_en": 'Zhdanivska',
                    },
                    {
                        "uid": 211,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska',
                    },
                    {
                        "uid": 212,
                        "name": 'м. Козятин та Козятинська',
                        "name_en": 'Koziatyn and Koziatynska',
                    },
                    {
                        "uid": 213,
                        "name": 'Махнівська',
                        "name_en": 'Makhnivska',
                    },
                    {
                        "uid": 214,
                        "name": 'Самгородоцька',
                        "name_en": 'Samhorodotska',
                    },
                    {
                        "uid": 215,
                        "name": 'Уланівська',
                        "name_en": 'Ulanivska',
                    },
                    {
                        "uid": 216,
                        "name": 'м. Хмільник та Хмільницька',
                        "name_en": 'Khmilnyk and Khmilnytska',
                    },
                    {
                        "uid": 210,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 9,
        "name": 'Дніпропетровська',
        "type": LocationType.OBLAST,
        "name_en": 'Dnipropetrovska',
        "districts": [
            {
                "uid": 44,
                "name": 'Дніпровський',
                "name_en": 'Dniprovskyi',
                "hromadas": [
                    {
                        "uid": 332,
                        "name": 'м. Дніпро та Дніпровська',
                        "name_en": 'Dnipro and Dniprovska',
                    },
                    {
                        "uid": 333,
                        "name": 'Китайгородська',
                        "name_en": 'Kytaihorodska',
                    },
                    {
                        "uid": 334,
                        "name": 'Любимівська',
                        "name_en": 'Liubymivska',
                    },
                    {
                        "uid": 335,
                        "name": 'Ляшківська',
                        "name_en": 'Liashkivska',
                    },
                    {
                        "uid": 336,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 337,
                        "name": 'Могилівська',
                        "name_en": 'Mohylivska',
                    },
                    {
                        "uid": 338,
                        "name": 'Новоолександрівська',
                        "name_en": 'Novooleksandrivska',
                    },
                    {
                        "uid": 339,
                        "name": 'Новопокровська',
                        "name_en": 'Novopokrovska',
                    },
                    {
                        "uid": 340,
                        "name": 'Обухівська',
                        "name_en": 'Obukhivska',
                    },
                    {
                        "uid": 341,
                        "name": 'Петриківська',
                        "name_en": 'Petrykivska',
                    },
                    {
                        "uid": 342,
                        "name": 'Підгородненська',
                        "name_en": 'Pidhorodnenska',
                    },
                    {
                        "uid": 343,
                        "name": 'Святовасилівська',
                        "name_en": 'Sviatovasylivska',
                    },
                    {
                        "uid": 344,
                        "name": 'Слобожанська',
                        "name_en": 'Slobozhanska',
                    },
                    {
                        "uid": 345,
                        "name": 'Солонянська',
                        "name_en": 'Solonianska',
                    },
                    {
                        "uid": 346,
                        "name": 'Сурсько-Литовська',
                        "name_en": 'Sursko-Lytovska',
                    },
                    {
                        "uid": 347,
                        "name": 'Царичанська',
                        "name_en": 'Tsarychanska',
                    },
                    {
                        "uid": 348,
                        "name": 'Чумаківська',
                        "name_en": 'Chumakivska',
                    },
                ],
            },
            {
                "uid": 42,
                "name": "Кам'янський",
                "name_en": 'Kamianskyi',
                "hromadas": [
                    {
                        "uid": 293,
                        "name": 'Божедарівська',
                        "name_en": 'Bozhedarivska',
                    },
                    {
                        "uid": 295,
                        "name": 'Верхньодніпровська',
                        "name_en": 'Verkhnodniprovska',
                    },
                    {
                        "uid": 294,
                        "name": 'Верхівцівська',
                        "name_en": 'Verkhivtsivska',
                    },
                    {
                        "uid": 296,
                        "name": 'Вишнівська',
                        "name_en": 'Vyshnivska',
                    },
                    {
                        "uid": 297,
                        "name": 'м. Вільногірськ та Вільногірська',
                        "name_en": 'Vilnohirsk and Vilnohirska',
                    },
                    {
                        "uid": 298,
                        "name": 'м. Жовті Води та Жовтоводська',
                        "name_en": 'Zhovti Vody and Zhovtovodska',
                    },
                    {
                        "uid": 299,
                        "name": 'Затишнянська',
                        "name_en": 'Zatyshnianska',
                    },
                    {
                        "uid": 300,
                        "name": 'м. Кам’янське та Кам’янська',
                        "name_en": 'Kamyanske and Kamyanska',
                    },
                    {
                        "uid": 301,
                        "name": 'Криничанська',
                        "name_en": 'Krynychanska',
                    },
                    {
                        "uid": 302,
                        "name": 'Лихівська',
                        "name_en": 'Lykhivska',
                    },
                    {
                        "uid": 303,
                        "name": "П'ятихатська",
                        "name_en": 'Piatykhatska',
                    },
                    {
                        "uid": 304,
                        "name": 'Саксаганська',
                        "name_en": 'Saksahanska',
                    },
                ],
            },
            {
                "uid": 46,
                "name": 'Криворізький',
                "name_en": 'Kryvorizkyi',
                "hromadas": [
                    {
                        "uid": 271,
                        "name": 'Апостолівська',
                        "name_en": 'Apostolivska',
                    },
                    {
                        "uid": 272,
                        "name": 'Вакулівська',
                        "name_en": 'Vakulivska',
                    },
                    {
                        "uid": 273,
                        "name": 'Глеюватська',
                        "name_en": 'Hleiuvatska',
                    },
                    {
                        "uid": 274,
                        "name": 'Гречаноподівська',
                        "name_en": 'Hrechanopodivska',
                    },
                    {
                        "uid": 275,
                        "name": 'Грушівська',
                        "name_en": 'Hrushivska',
                    },
                    {
                        "uid": 276,
                        "name": 'Девладівська',
                        "name_en": 'Devladivska',
                    },
                    {
                        "uid": 277,
                        "name": 'Зеленодольська',
                        "name_en": 'Zelenodolska',
                    },
                    {
                        "uid": 278,
                        "name": 'Карпівська',
                        "name_en": 'Karpivska',
                    },
                    {
                        "uid": 279,
                        "name": 'м. Кривий Ріг та Криворізька',
                        "name_en": 'Kryvyi Rih and Kryvorizka',
                    },
                    {
                        "uid": 280,
                        "name": 'Лозуватська',
                        "name_en": 'Lozuvatska',
                    },
                    {
                        "uid": 281,
                        "name": 'Нивотрудівська',
                        "name_en": 'Nyvotrudivska',
                    },
                    {
                        "uid": 282,
                        "name": 'Новолатівська',
                        "name_en": 'Novolativska',
                    },
                    {
                        "uid": 283,
                        "name": 'Новопільська',
                        "name_en": 'Novopilska',
                    },
                    {
                        "uid": 284,
                        "name": 'Софіївська',
                        "name_en": 'Sofiivska',
                    },
                    {
                        "uid": 285,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska',
                    },
                ],
            },
            {
                "uid": 47,
                "name": 'Нікопольський',
                "name_en": 'Nikopolskyi',
                "hromadas": [
                    {
                        "uid": 349,
                        "name": 'м. Марганець та Марганецька',
                        "name_en": 'Marhanets and Marhanetska',
                    },
                    {
                        "uid": 350,
                        "name": 'Мирівська',
                        "name_en": 'Myrivska',
                    },
                    {
                        "uid": 351,
                        "name": 'м. Нікополь та Нікопольська',
                        "name_en": 'Nikopol and Nikopolska',
                    },
                    {
                        "uid": 352,
                        "name": 'Першотравневська',
                        "name_en": 'Pershotravnevska',
                    },
                    {
                        "uid": 354,
                        "name": 'м. Покров та Покровська',
                        "name_en": 'Pokrov and Pokrovska',
                    },
                    {
                        "uid": 353,
                        "name": 'Покровська',
                        "name_en": 'Pokrovska',
                    },
                    {
                        "uid": 355,
                        "name": 'Томаківська',
                        "name_en": 'Tomakivska',
                    },
                    {
                        "uid": 356,
                        "name": 'Червоногригорівська',
                        "name_en": 'Chervonohryhorivska',
                    },
                ],
            },
            {
                "uid": 45,
                "name": 'Павлоградський',
                "name_en": 'Pavlohradskyi',
                "hromadas": [
                    {
                        "uid": 286,
                        "name": 'Богданівська',
                        "name_en": 'Bohdanivska',
                    },
                    {
                        "uid": 287,
                        "name": 'Вербківська',
                        "name_en": 'Verbkivska',
                    },
                    {
                        "uid": 288,
                        "name": 'Межиріцька',
                        "name_en": 'Mezhyritska',
                    },
                    {
                        "uid": 289,
                        "name": 'м. Павлоград та Павлоградська',
                        "name_en": 'Pavlohrad and Pavlohradska',
                    },
                    {
                        "uid": 290,
                        "name": 'м. Тернівка та Тернівська',
                        "name_en": 'Ternivka and Ternivska',
                    },
                    {
                        "uid": 291,
                        "name": 'Троїцька',
                        "name_en": 'Troitska',
                    },
                    {
                        "uid": 292,
                        "name": 'Юр’ївська',
                        "name_en": 'Yuryivska',
                    },
                ],
            },
            {
                "uid": 43,
                "name": 'Самарівський',
                "name_en": 'Samarivskyi',
                "hromadas": [
                    {
                        "uid": 324,
                        "name": 'Губиниська',
                        "name_en": 'Hubynyska',
                    },
                    {
                        "uid": 325,
                        "name": 'Личківська',
                        "name_en": 'Lychkivska',
                    },
                    {
                        "uid": 326,
                        "name": 'Магдалинівська',
                        "name_en": 'Mahdalynivska',
                    },
                    {
                        "uid": 328,
                        "name": 'Перещепинська',
                        "name_en": 'Pereshchepynska',
                    },
                    {
                        "uid": 329,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska',
                    },
                    {
                        "uid": 327,
                        "name": 'м. Самар та Самарівська',
                        "name_en": 'Samar and Samarivska',
                    },
                    {
                        "uid": 330,
                        "name": 'Черкаська',
                        "name_en": 'Cherkaska',
                    },
                    {
                        "uid": 331,
                        "name": 'Чернеччинська',
                        "name_en": 'Chernechchynska',
                    },
                ],
            },
            {
                "uid": 48,
                "name": 'Синельниківський',
                "name_en": 'Synelnykivskyi',
                "hromadas": [
                    {
                        "uid": 305,
                        "name": 'Брагинівська',
                        "name_en": 'Brahynivska',
                    },
                    {
                        "uid": 306,
                        "name": 'Васильківська',
                        "name_en": 'Vasylkivska',
                    },
                    {
                        "uid": 307,
                        "name": 'Великомихайлівська',
                        "name_en": 'Velykomykhailivska',
                    },
                    {
                        "uid": 308,
                        "name": 'Дубовиківська',
                        "name_en": 'Dubovykivska',
                    },
                    {
                        "uid": 309,
                        "name": 'Зайцівська',
                        "name_en": 'Zaitsivska',
                    },
                    {
                        "uid": 311,
                        "name": 'Маломихайлівська',
                        "name_en": 'Malomykhailivska',
                    },
                    {
                        "uid": 312,
                        "name": 'Межівська',
                        "name_en": 'Mezhivska',
                    },
                    {
                        "uid": 313,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 314,
                        "name": 'Новопавлівська',
                        "name_en": 'Novopavlivska',
                    },
                    {
                        "uid": 316,
                        "name": 'Петропавлівська',
                        "name_en": 'Petropavlivska',
                    },
                    {
                        "uid": 317,
                        "name": 'Покровська',
                        "name_en": 'Pokrovska',
                    },
                    {
                        "uid": 318,
                        "name": 'Раївська',
                        "name_en": 'Raivska',
                    },
                    {
                        "uid": 319,
                        "name": 'Роздорська',
                        "name_en": 'Rozdorska',
                    },
                    {
                        "uid": 320,
                        "name": 'м. Синельникове та Синельниківська',
                        "name_en": 'Synelnykove and Synelnykivska',
                    },
                    {
                        "uid": 321,
                        "name": 'Славгородська',
                        "name_en": 'Slavhorodska',
                    },
                    {
                        "uid": 322,
                        "name": "Слов'янська",
                        "name_en": 'Slovianska',
                    },
                    {
                        "uid": 323,
                        "name": 'Українська',
                        "name_en": 'Ukrainska',
                    },
                    {
                        "uid": 315,
                        "name": 'м. Шахтарськ та Шахтарська',
                        "name_en": 'Shakhtarsk and Shakhtarska',
                    },
                    {
                        "uid": 310,
                        "name": 'Іларіонівська',
                        "name_en": 'Ilarionivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 28,
        "name": 'Донецька',
        "type": LocationType.OBLAST,
        "name_en": 'Donetska',
        "districts": [
            {
                "uid": 54,
                "name": 'Бахмутський',
                "name_en": 'Bakhmutskyi',
                "hromadas": [
                    {
                        "uid": 383,
                        "name": 'Бахмутська',
                        "name_en": 'Bakhmutska',
                    },
                    {
                        "uid": 384,
                        "name": 'Званівська',
                        "name_en": 'Zvanivska',
                    },
                    {
                        "uid": 385,
                        "name": 'Світлодарська',
                        "name_en": 'Svitlodarska',
                    },
                    {
                        "uid": 387,
                        "name": 'Соледарська',
                        "name_en": 'Soledarska',
                    },
                    {
                        "uid": 386,
                        "name": 'Сіверська',
                        "name_en": 'Siverska',
                    },
                    {
                        "uid": 388,
                        "name": 'Торецька',
                        "name_en": 'Toretska',
                    },
                    {
                        "uid": 389,
                        "name": 'Часовоярська',
                        "name_en": 'Chasovoiarska',
                    },
                ],
            },
            {
                "uid": 55,
                "name": 'Волноваський',
                "name_en": 'Volnovaskyi',
                "hromadas": [
                    {
                        "uid": 390,
                        "name": 'Великоновосілківська',
                        "name_en": 'Velykonovosilkivska',
                    },
                    {
                        "uid": 391,
                        "name": 'Волноваська',
                        "name_en": 'Volnovaska',
                    },
                    {
                        "uid": 392,
                        "name": 'Вугледарська',
                        "name_en": 'Vuhledarska',
                    },
                    {
                        "uid": 393,
                        "name": 'Комарська',
                        "name_en": 'Komarska',
                    },
                    {
                        "uid": 394,
                        "name": 'Мирненська',
                        "name_en": 'Myrnenska',
                    },
                    {
                        "uid": 395,
                        "name": 'Ольгинська',
                        "name_en": 'Olhynska',
                    },
                    {
                        "uid": 396,
                        "name": 'Старомлинівська',
                        "name_en": 'Staromlynivska',
                    },
                    {
                        "uid": 397,
                        "name": 'Хлібодарівська',
                        "name_en": 'Khlibodarivska',
                    },
                ],
            },
            {
                "uid": 51,
                "name": 'Горлівський',
                "name_en": 'Horlivskyi',
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
                "name_en": 'Donetskyi',
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
                "name_en": 'Kalmiuskyi',
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
                "name_en": 'Kramatorskyi',
                "hromadas": [
                    {
                        "uid": 371,
                        "name": 'Андріївська',
                        "name_en": 'Andriivska',
                    },
                    {
                        "uid": 372,
                        "name": 'Дружківська',
                        "name_en": 'Druzhkivska',
                    },
                    {
                        "uid": 374,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska',
                    },
                    {
                        "uid": 375,
                        "name": 'м. Краматорськ та Краматорська',
                        "name_en": 'Kramatorsk and Kramatorska',
                    },
                    {
                        "uid": 376,
                        "name": 'Лиманська',
                        "name_en": 'Lymanska',
                    },
                    {
                        "uid": 377,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 378,
                        "name": 'Новодонецька',
                        "name_en": 'Novodonetska',
                    },
                    {
                        "uid": 379,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska',
                    },
                    {
                        "uid": 380,
                        "name": 'Святогірська',
                        "name_en": 'Sviatohirska',
                    },
                    {
                        "uid": 381,
                        "name": "м. Слов'янськ та Слов'янська",
                        "name_en": 'Sloviansk and Slovianska',
                    },
                    {
                        "uid": 382,
                        "name": 'Черкаська',
                        "name_en": 'Cherkaska',
                    },
                    {
                        "uid": 373,
                        "name": 'Іллінівська',
                        "name_en": 'Illinivska',
                    },
                ],
            },
            {
                "uid": 52,
                "name": 'Маріупольський',
                "name_en": 'Mariupolskyi',
                "hromadas": [
                    {
                        "uid": 398,
                        "name": 'Кальчицька',
                        "name_en": 'Kalchytska',
                    },
                    {
                        "uid": 399,
                        "name": 'Мангушська',
                        "name_en": 'Manhushska',
                    },
                    {
                        "uid": 400,
                        "name": 'м. Маріуполь та Маріупольська',
                        "name_en": 'Mariupol and Mariupolska',
                    },
                    {
                        "uid": 401,
                        "name": 'Нікольська',
                        "name_en": 'Nikolska',
                    },
                    {
                        "uid": 402,
                        "name": 'Сартанська',
                        "name_en": 'Sartanska',
                    },
                ],
            },
            {
                "uid": 56,
                "name": 'Покровський',
                "name_en": 'Pokrovskyi',
                "hromadas": [
                    {
                        "uid": 357,
                        "name": 'Авдіївська',
                        "name_en": 'Avdiivska',
                    },
                    {
                        "uid": 358,
                        "name": 'Білозерська',
                        "name_en": 'Bilozerska',
                    },
                    {
                        "uid": 359,
                        "name": 'Гродівська',
                        "name_en": 'Hrodivska',
                    },
                    {
                        "uid": 360,
                        "name": 'Добропільська',
                        "name_en": 'Dobropilska',
                    },
                    {
                        "uid": 361,
                        "name": 'Криворізька',
                        "name_en": 'Kryvorizka',
                    },
                    {
                        "uid": 362,
                        "name": 'Курахівська',
                        "name_en": 'Kurakhivska',
                    },
                    {
                        "uid": 363,
                        "name": "Мар'їнська",
                        "name_en": 'Marinska',
                    },
                    {
                        "uid": 364,
                        "name": 'Мирноградська',
                        "name_en": 'Myrnohradska',
                    },
                    {
                        "uid": 365,
                        "name": 'Новогродівська',
                        "name_en": 'Novohrodivska',
                    },
                    {
                        "uid": 366,
                        "name": 'Очеретинська',
                        "name_en": 'Ocheretynska',
                    },
                    {
                        "uid": 367,
                        "name": 'Покровська',
                        "name_en": 'Pokrovska',
                    },
                    {
                        "uid": 368,
                        "name": 'Селидівська',
                        "name_en": 'Selydivska',
                    },
                    {
                        "uid": 369,
                        "name": 'Удачненська',
                        "name_en": 'Udachnenska',
                    },
                    {
                        "uid": 370,
                        "name": 'Шахівська',
                        "name_en": 'Shakhivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 10,
        "name": 'Житомирська',
        "type": LocationType.OBLAST,
        "name_en": 'Zhytomyrska',
        "districts": [
            {
                "uid": 57,
                "name": 'Бердичівський',
                "name_en": 'Berdychivskyi',
                "hromadas": [
                    {
                        "uid": 423,
                        "name": 'Андрушівська',
                        "name_en": 'Andrushivska',
                    },
                    {
                        "uid": 424,
                        "name": 'м. Бердичів та Бердичівська',
                        "name_en": 'Berdychiv and Berdychivska',
                    },
                    {
                        "uid": 425,
                        "name": 'Вчорайшенська',
                        "name_en": 'Vchoraishenska',
                    },
                    {
                        "uid": 426,
                        "name": 'Гришковецька',
                        "name_en": 'Hryshkovetska',
                    },
                    {
                        "uid": 427,
                        "name": 'Краснопільська',
                        "name_en": 'Krasnopilska',
                    },
                    {
                        "uid": 428,
                        "name": 'Райгородська',
                        "name_en": 'Raihorodska',
                    },
                    {
                        "uid": 429,
                        "name": 'Ружинська',
                        "name_en": 'Ruzhynska',
                    },
                    {
                        "uid": 430,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska',
                    },
                    {
                        "uid": 431,
                        "name": 'Червоненська',
                        "name_en": 'Chervonenska',
                    },
                    {
                        "uid": 432,
                        "name": 'Швайківська',
                        "name_en": 'Shvaikivska',
                    },
                ],
            },
            {
                "uid": 59,
                "name": 'Житомирський',
                "name_en": 'Zhytomyrskyi',
                "hromadas": [
                    {
                        "uid": 433,
                        "name": 'Андрушківська',
                        "name_en": 'Andrushkivska',
                    },
                    {
                        "uid": 434,
                        "name": 'Березівська',
                        "name_en": 'Berezivska',
                    },
                    {
                        "uid": 435,
                        "name": 'Брусилівська',
                        "name_en": 'Brusylivska',
                    },
                    {
                        "uid": 436,
                        "name": 'Високівська',
                        "name_en": 'Vysokivska',
                    },
                    {
                        "uid": 437,
                        "name": 'Вишевицька',
                        "name_en": 'Vyshevytska',
                    },
                    {
                        "uid": 439,
                        "name": 'Волицька',
                        "name_en": 'Volytska',
                    },
                    {
                        "uid": 438,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska',
                    },
                    {
                        "uid": 440,
                        "name": 'Глибочицька',
                        "name_en": 'Hlybochytska',
                    },
                    {
                        "uid": 441,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska',
                    },
                    {
                        "uid": 442,
                        "name": 'м. Житомир та Житомирська',
                        "name_en": 'Zhytomyr and Zhytomyrska',
                    },
                    {
                        "uid": 443,
                        "name": 'Квітнева',
                        "name_en": 'Kvitneva',
                    },
                    {
                        "uid": 444,
                        "name": 'Корнинська',
                        "name_en": 'Kornynska',
                    },
                    {
                        "uid": 445,
                        "name": 'Коростишівська',
                        "name_en": 'Korostyshivska',
                    },
                    {
                        "uid": 446,
                        "name": 'Курненська',
                        "name_en": 'Kurnenska',
                    },
                    {
                        "uid": 447,
                        "name": 'Любарська',
                        "name_en": 'Liubarska',
                    },
                    {
                        "uid": 448,
                        "name": 'Миропільська',
                        "name_en": 'Myropilska',
                    },
                    {
                        "uid": 449,
                        "name": 'Новоборівська',
                        "name_en": 'Novoborivska',
                    },
                    {
                        "uid": 450,
                        "name": 'Новогуйвинська',
                        "name_en": 'Novohuivynska',
                    },
                    {
                        "uid": 451,
                        "name": 'Оліївська',
                        "name_en": 'Oliivska',
                    },
                    {
                        "uid": 452,
                        "name": 'Попільнянська',
                        "name_en": 'Popilnianska',
                    },
                    {
                        "uid": 453,
                        "name": 'Потіївська',
                        "name_en": 'Potiivska',
                    },
                    {
                        "uid": 454,
                        "name": 'Пулинська',
                        "name_en": 'Pulynska',
                    },
                    {
                        "uid": 455,
                        "name": 'Радомишльська',
                        "name_en": 'Radomyshlska',
                    },
                    {
                        "uid": 456,
                        "name": 'Романівська',
                        "name_en": 'Romanivska',
                    },
                    {
                        "uid": 457,
                        "name": 'Станишівська',
                        "name_en": 'Stanyshivska',
                    },
                    {
                        "uid": 458,
                        "name": 'Старосілецька',
                        "name_en": 'Starosiletska',
                    },
                    {
                        "uid": 459,
                        "name": 'Тетерівська',
                        "name_en": 'Teterivska',
                    },
                    {
                        "uid": 460,
                        "name": 'Харитонівська',
                        "name_en": 'Kharytonivska',
                    },
                    {
                        "uid": 461,
                        "name": 'Хорошівська',
                        "name_en": 'Khoroshivska',
                    },
                    {
                        "uid": 462,
                        "name": 'Черняхівська',
                        "name_en": 'Cherniakhivska',
                    },
                    {
                        "uid": 463,
                        "name": 'Чуднівська',
                        "name_en": 'Chudnivska',
                    },
                ],
            },
            {
                "uid": 60,
                "name": 'Звягельський',
                "name_en": 'Zviahelskyi',
                "hromadas": [
                    {
                        "uid": 464,
                        "name": 'Баранівська',
                        "name_en": 'Baranivska',
                    },
                    {
                        "uid": 465,
                        "name": 'Барашівська',
                        "name_en": 'Barashivska',
                    },
                    {
                        "uid": 466,
                        "name": 'Брониківська',
                        "name_en": 'Bronykivska',
                    },
                    {
                        "uid": 467,
                        "name": 'Городницька',
                        "name_en": 'Horodnytska',
                    },
                    {
                        "uid": 468,
                        "name": 'Довбиська',
                        "name_en": 'Dovbyska',
                    },
                    {
                        "uid": 469,
                        "name": 'Дубрівська',
                        "name_en": 'Dubrivska',
                    },
                    {
                        "uid": 471,
                        "name": 'м. Звягель та Звягельська',
                        "name_en": 'Zviahel and Zviahelska',
                    },
                    {
                        "uid": 472,
                        "name": 'Піщівська',
                        "name_en": 'Pishchivska',
                    },
                    {
                        "uid": 473,
                        "name": 'Стриївська',
                        "name_en": 'Stryivska',
                    },
                    {
                        "uid": 474,
                        "name": 'Чижівська',
                        "name_en": 'Chyzhivska',
                    },
                    {
                        "uid": 475,
                        "name": 'Ярунська',
                        "name_en": 'Yarunska',
                    },
                    {
                        "uid": 470,
                        "name": 'Ємільчинська',
                        "name_en": 'Yemilchynska',
                    },
                ],
            },
            {
                "uid": 58,
                "name": 'Коростенський',
                "name_en": 'Korostenskyi',
                "hromadas": [
                    {
                        "uid": 476,
                        "name": 'Білокоровицька',
                        "name_en": 'Bilokorovytska',
                    },
                    {
                        "uid": 477,
                        "name": 'Гладковицька',
                        "name_en": 'Hladkovytska',
                    },
                    {
                        "uid": 478,
                        "name": 'Горщиківська',
                        "name_en": 'Horshchykivska',
                    },
                    {
                        "uid": 480,
                        "name": 'м. Коростень та Коростенська',
                        "name_en": 'Korosten and Korostenska',
                    },
                    {
                        "uid": 481,
                        "name": 'Лугинська',
                        "name_en": 'Luhynska',
                    },
                    {
                        "uid": 482,
                        "name": 'м. Малин та Малинська',
                        "name_en": 'Malyn and Malynska',
                    },
                    {
                        "uid": 483,
                        "name": 'Народицька',
                        "name_en": 'Narodytska',
                    },
                    {
                        "uid": 484,
                        "name": 'Овруцька',
                        "name_en": 'Ovrutska',
                    },
                    {
                        "uid": 485,
                        "name": 'Олевська',
                        "name_en": 'Olevska',
                    },
                    {
                        "uid": 486,
                        "name": 'Словечанська',
                        "name_en": 'Slovechanska',
                    },
                    {
                        "uid": 487,
                        "name": 'Ушомирська',
                        "name_en": 'Ushomyrska',
                    },
                    {
                        "uid": 488,
                        "name": 'Чоповицька',
                        "name_en": 'Chopovytska',
                    },
                    {
                        "uid": 479,
                        "name": 'Іршанська',
                        "name_en": 'Irshanska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 11,
        "name": 'Закарпатська',
        "type": LocationType.OBLAST,
        "name_en": 'Zakarpatska',
        "districts": [
            {
                "uid": 61,
                "name": 'Берегівський',
                "name_en": 'Berehivskyi',
                "hromadas": [
                    {
                        "uid": 503,
                        "name": 'Батівська',
                        "name_en": 'Bativska',
                    },
                    {
                        "uid": 504,
                        "name": 'м. Берегове та Берегівська',
                        "name_en": 'Berehove and Berehivska',
                    },
                    {
                        "uid": 505,
                        "name": 'Великоберезька',
                        "name_en": 'Velykoberezka',
                    },
                    {
                        "uid": 506,
                        "name": 'Великобийганська',
                        "name_en": 'Velykobyihanska',
                    },
                    {
                        "uid": 507,
                        "name": 'Вилоцька',
                        "name_en": 'Vylotska',
                    },
                    {
                        "uid": 508,
                        "name": 'м. Виноградів та Виноградівська',
                        "name_en": 'Vynohradiv and Vynohradivska',
                    },
                    {
                        "uid": 509,
                        "name": "Кам'янська",
                        "name_en": 'Kamianska',
                    },
                    {
                        "uid": 510,
                        "name": 'Королівська',
                        "name_en": 'Korolivska',
                    },
                    {
                        "uid": 511,
                        "name": 'Косоньська',
                        "name_en": 'Kosonska',
                    },
                    {
                        "uid": 512,
                        "name": 'Пийтерфолвівська',
                        "name_en": 'Pyiterfolvivska',
                    },
                ],
            },
            {
                "uid": 65,
                "name": 'Мукачівський',
                "name_en": 'Mukachivskyi',
                "hromadas": [
                    {
                        "uid": 540,
                        "name": 'Великолучківська',
                        "name_en": 'Velykoluchkivska',
                    },
                    {
                        "uid": 541,
                        "name": 'Верхньокоропецька',
                        "name_en": 'Verkhnokoropetska',
                    },
                    {
                        "uid": 542,
                        "name": 'Воловецька',
                        "name_en": 'Volovetska',
                    },
                    {
                        "uid": 543,
                        "name": 'Горондівська',
                        "name_en": 'Horondivska',
                    },
                    {
                        "uid": 544,
                        "name": 'Жденіївська',
                        "name_en": 'Zhdeniivska',
                    },
                    {
                        "uid": 546,
                        "name": 'Кольчинська',
                        "name_en": 'Kolchynska',
                    },
                    {
                        "uid": 547,
                        "name": 'м. Мукачево та Мукачівська',
                        "name_en": 'Mukachevo and Mukachivska',
                    },
                    {
                        "uid": 548,
                        "name": 'Неліпинська',
                        "name_en": 'Nelipynska',
                    },
                    {
                        "uid": 549,
                        "name": 'Нижньоворітська',
                        "name_en": 'Nyzhnovoritska',
                    },
                    {
                        "uid": 550,
                        "name": 'Полянська',
                        "name_en": 'Polianska',
                    },
                    {
                        "uid": 551,
                        "name": 'Свалявська',
                        "name_en": 'Svaliavska',
                    },
                    {
                        "uid": 552,
                        "name": 'Чинадіївська',
                        "name_en": 'Chynadiivska',
                    },
                    {
                        "uid": 545,
                        "name": 'Івановецька',
                        "name_en": 'Ivanovetska',
                    },
                ],
            },
            {
                "uid": 63,
                "name": 'Рахівський',
                "name_en": 'Rakhivskyi',
                "hromadas": [
                    {
                        "uid": 536,
                        "name": 'Богданська',
                        "name_en": 'Bohdanska',
                    },
                    {
                        "uid": 537,
                        "name": 'Великобичківська',
                        "name_en": 'Velykobychkivska',
                    },
                    {
                        "uid": 538,
                        "name": 'м. Рахів та Рахівська',
                        "name_en": 'Rakhiv and Rakhivska',
                    },
                    {
                        "uid": 539,
                        "name": 'Ясінянська',
                        "name_en": 'Yasinianska',
                    },
                ],
            },
            {
                "uid": 64,
                "name": 'Тячівський',
                "name_en": 'Tiachivskyi',
                "hromadas": [
                    {
                        "uid": 513,
                        "name": 'Бедевлянська',
                        "name_en": 'Bedevlianska',
                    },
                    {
                        "uid": 514,
                        "name": 'Буштинська',
                        "name_en": 'Bushtynska',
                    },
                    {
                        "uid": 515,
                        "name": 'Вільховецька',
                        "name_en": 'Vilkhovetska',
                    },
                    {
                        "uid": 516,
                        "name": 'Дубівська',
                        "name_en": 'Dubivska',
                    },
                    {
                        "uid": 517,
                        "name": 'Нересницька',
                        "name_en": 'Neresnytska',
                    },
                    {
                        "uid": 518,
                        "name": 'Солотвинська',
                        "name_en": 'Solotvynska',
                    },
                    {
                        "uid": 519,
                        "name": 'Тересвянська',
                        "name_en": 'Teresvianska',
                    },
                    {
                        "uid": 520,
                        "name": 'м. Тячів та Тячівська',
                        "name_en": 'Tiachiv and Tiachivska',
                    },
                    {
                        "uid": 521,
                        "name": 'Углянська',
                        "name_en": 'Uhlianska',
                    },
                    {
                        "uid": 522,
                        "name": 'Усть-Чорнянська',
                        "name_en": 'Ust-Chornianska',
                    },
                ],
            },
            {
                "uid": 66,
                "name": 'Ужгородський',
                "name_en": 'Uzhhorodskyi',
                "hromadas": [
                    {
                        "uid": 489,
                        "name": 'Баранинська',
                        "name_en": 'Baranynska',
                    },
                    {
                        "uid": 490,
                        "name": 'Великоберезнянська',
                        "name_en": 'Velykobereznianska',
                    },
                    {
                        "uid": 491,
                        "name": 'Великодобронська',
                        "name_en": 'Velykodobronska',
                    },
                    {
                        "uid": 492,
                        "name": 'Дубриницько-Малоберезня',
                        "name_en": 'Dubrynytsko-Malobereznia',
                    },
                    {
                        "uid": 493,
                        "name": 'Костринська',
                        "name_en": 'Kostrynska',
                    },
                    {
                        "uid": 494,
                        "name": 'Оноківська',
                        "name_en": 'Onokivska',
                    },
                    {
                        "uid": 495,
                        "name": 'Перечинська',
                        "name_en": 'Perechynska',
                    },
                    {
                        "uid": 496,
                        "name": 'Середнянська',
                        "name_en": 'Serednianska',
                    },
                    {
                        "uid": 497,
                        "name": 'Ставненська',
                        "name_en": 'Stavnenska',
                    },
                    {
                        "uid": 498,
                        "name": 'Сюртівська',
                        "name_en": 'Siurtivska',
                    },
                    {
                        "uid": 499,
                        "name": "Тур'є-Реметівська",
                        "name_en": 'Turie-Remetivska',
                    },
                    {
                        "uid": 500,
                        "name": 'м. Ужгород та Ужгородська',
                        "name_en": 'Uzhhorod and Uzhhorodska',
                    },
                    {
                        "uid": 501,
                        "name": 'Холмківська',
                        "name_en": 'Kholmkivska',
                    },
                    {
                        "uid": 502,
                        "name": 'м. Чоп та Чопська',
                        "name_en": 'Chop and Chopska',
                    },
                ],
            },
            {
                "uid": 62,
                "name": 'Хустський',
                "name_en": 'Khustskyi',
                "hromadas": [
                    {
                        "uid": 523,
                        "name": 'Білківська',
                        "name_en": 'Bilkivska',
                    },
                    {
                        "uid": 524,
                        "name": 'Вишківська',
                        "name_en": 'Vyshkivska',
                    },
                    {
                        "uid": 525,
                        "name": 'Горінчівська',
                        "name_en": 'Horinchivska',
                    },
                    {
                        "uid": 526,
                        "name": 'Довжанська',
                        "name_en": 'Dovzhanska',
                    },
                    {
                        "uid": 527,
                        "name": 'Драгівська',
                        "name_en": 'Drahivska',
                    },
                    {
                        "uid": 528,
                        "name": 'Зарічанська',
                        "name_en": 'Zarichanska',
                    },
                    {
                        "uid": 530,
                        "name": 'Керецьківська',
                        "name_en": 'Keretskivska',
                    },
                    {
                        "uid": 531,
                        "name": 'Колочавська',
                        "name_en": 'Kolochavska',
                    },
                    {
                        "uid": 532,
                        "name": "м. Міжгір'я та Міжгірська",
                        "name_en": 'Mizhhiria and Mizhhirska',
                    },
                    {
                        "uid": 533,
                        "name": 'Пилипецька',
                        "name_en": 'Pylypetska',
                    },
                    {
                        "uid": 534,
                        "name": 'Синевирська',
                        "name_en": 'Synevyrska',
                    },
                    {
                        "uid": 535,
                        "name": 'м. Хуст та Хустська',
                        "name_en": 'Khust and Khustska',
                    },
                    {
                        "uid": 529,
                        "name": 'м. Іршава та Іршавська',
                        "name_en": 'Irshava and Irshavska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 12,
        "name": 'Запорізька',
        "type": LocationType.OBLAST,
        "name_en": 'Zaporizka',
        "districts": [
            {
                "uid": 147,
                "name": 'Бердянський',
                "name_en": 'Berdianskyi',
                "hromadas": [
                    {
                        "uid": 553,
                        "name": 'Андрівська',
                        "name_en": 'Andrivska',
                    },
                    {
                        "uid": 554,
                        "name": 'Андріївська',
                        "name_en": 'Andriivska',
                    },
                    {
                        "uid": 555,
                        "name": 'м. Бердянськ та Бердянська',
                        "name_en": 'Berdiansk and Berdianska',
                    },
                    {
                        "uid": 556,
                        "name": 'Берестівська',
                        "name_en": 'Berestivska',
                    },
                    {
                        "uid": 557,
                        "name": 'Коларівська',
                        "name_en": 'Kolarivska',
                    },
                    {
                        "uid": 558,
                        "name": 'Осипенківська',
                        "name_en": 'Osypenkivska',
                    },
                    {
                        "uid": 559,
                        "name": 'Приморська',
                        "name_en": 'Prymorska',
                    },
                    {
                        "uid": 560,
                        "name": 'Чернігівська',
                        "name_en": 'Chernihivska',
                    },
                ],
            },
            {
                "uid": 146,
                "name": 'Василівський',
                "name_en": 'Vasylivskyi',
                "hromadas": [
                    {
                        "uid": 593,
                        "name": 'Благовіщенська',
                        "name_en": 'Blahovishchenska',
                    },
                    {
                        "uid": 594,
                        "name": 'Василівська',
                        "name_en": 'Vasylivska',
                    },
                    {
                        "uid": 595,
                        "name": 'Великобілозерська',
                        "name_en": 'Velykobilozerska',
                    },
                    {
                        "uid": 596,
                        "name": 'Водянська',
                        "name_en": 'Vodianska',
                    },
                    {
                        "uid": 597,
                        "name": 'Дніпрорудненська',
                        "name_en": 'Dniprorudnenska',
                    },
                    {
                        "uid": 598,
                        "name": 'м. Енергодар та Енергодарська',
                        "name_en": 'Enerhodar and Enerhodarska',
                    },
                    {
                        "uid": 599,
                        "name": "Кам'янсько-Дніпровська",
                        "name_en": 'Kamiansko-Dniprovska',
                    },
                    {
                        "uid": 600,
                        "name": 'Малобілозерська',
                        "name_en": 'Malobilozerska',
                    },
                    {
                        "uid": 601,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska',
                    },
                    {
                        "uid": 602,
                        "name": 'Роздольська',
                        "name_en": 'Rozdolska',
                    },
                    {
                        "uid": 603,
                        "name": 'Степногірська',
                        "name_en": 'Stepnohirska',
                    },
                ],
            },
            {
                "uid": 149,
                "name": 'Запорізький',
                "name_en": 'Zaporizkyi',
                "hromadas": [
                    {
                        "uid": 561,
                        "name": 'Біленьківська',
                        "name_en": 'Bilenkivska',
                    },
                    {
                        "uid": 562,
                        "name": 'Вільнянська',
                        "name_en": 'Vilnianska',
                    },
                    {
                        "uid": 563,
                        "name": 'Долинська',
                        "name_en": 'Dolynska',
                    },
                    {
                        "uid": 564,
                        "name": 'м. Запоріжжя та Запорізька',
                        "name_en": 'Zaporizhzhia and Zaporizka',
                    },
                    {
                        "uid": 565,
                        "name": 'Комишуваська',
                        "name_en": 'Komyshuvaska',
                    },
                    {
                        "uid": 566,
                        "name": 'Кушугумська',
                        "name_en": 'Kushuhumska',
                    },
                    {
                        "uid": 567,
                        "name": 'Матвіївська',
                        "name_en": 'Matviivska',
                    },
                    {
                        "uid": 569,
                        "name": 'Михайло-Лукашівська',
                        "name_en": 'Mykhailo-Lukashivska',
                    },
                    {
                        "uid": 568,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska',
                    },
                    {
                        "uid": 570,
                        "name": 'Новомиколаївська',
                        "name_en": 'Novomykolaivska',
                    },
                    {
                        "uid": 571,
                        "name": 'Новоолександрівська',
                        "name_en": 'Novooleksandrivska',
                    },
                    {
                        "uid": 572,
                        "name": 'Павлівська',
                        "name_en": 'Pavlivska',
                    },
                    {
                        "uid": 573,
                        "name": 'Петро-Михайлівська',
                        "name_en": 'Petro-Mykhailivska',
                    },
                    {
                        "uid": 574,
                        "name": 'Степненська',
                        "name_en": 'Stepnenska',
                    },
                    {
                        "uid": 575,
                        "name": 'Таврійська',
                        "name_en": 'Tavriiska',
                    },
                    {
                        "uid": 576,
                        "name": 'Тернуватська',
                        "name_en": 'Ternuvatska',
                    },
                    {
                        "uid": 577,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska',
                    },
                ],
            },
            {
                "uid": 148,
                "name": 'Мелітопольський',
                "name_en": 'Melitopolskyi',
                "hromadas": [
                    {
                        "uid": 604,
                        "name": 'Веселівська',
                        "name_en": 'Veselivska',
                    },
                    {
                        "uid": 605,
                        "name": 'Кирилівська',
                        "name_en": 'Kyrylivska',
                    },
                    {
                        "uid": 606,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska',
                    },
                    {
                        "uid": 607,
                        "name": 'м. Мелітополь та Мелітопольська',
                        "name_en": 'Melitopol and Melitopolska',
                    },
                    {
                        "uid": 608,
                        "name": 'Мирненська',
                        "name_en": 'Myrnenska',
                    },
                    {
                        "uid": 609,
                        "name": 'Новенська',
                        "name_en": 'Novenska',
                    },
                    {
                        "uid": 610,
                        "name": 'Новобогданівська',
                        "name_en": 'Novobohdanivska',
                    },
                    {
                        "uid": 611,
                        "name": 'Нововасилівська',
                        "name_en": 'Novovasylivska',
                    },
                    {
                        "uid": 612,
                        "name": 'Новоуспенівська',
                        "name_en": 'Novouspenivska',
                    },
                    {
                        "uid": 613,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska',
                    },
                    {
                        "uid": 614,
                        "name": 'Плодородненська',
                        "name_en": 'Plodorodnenska',
                    },
                    {
                        "uid": 615,
                        "name": 'Приазовська',
                        "name_en": 'Pryazovska',
                    },
                    {
                        "uid": 616,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska',
                    },
                    {
                        "uid": 617,
                        "name": 'Терпіннівська',
                        "name_en": 'Terpinnivska',
                    },
                    {
                        "uid": 618,
                        "name": 'Чкаловська',
                        "name_en": 'Chkalovska',
                    },
                    {
                        "uid": 619,
                        "name": 'Якимівська',
                        "name_en": 'Yakymivska',
                    },
                ],
            },
            {
                "uid": 145,
                "name": 'Пологівський',
                "name_en": 'Polohivskyi',
                "hromadas": [
                    {
                        "uid": 578,
                        "name": 'Більмацька',
                        "name_en": 'Bilmatska',
                    },
                    {
                        "uid": 579,
                        "name": 'Воздвижівська',
                        "name_en": 'Vozdvyzhivska',
                    },
                    {
                        "uid": 580,
                        "name": 'Воскресенська',
                        "name_en": 'Voskresenska',
                    },
                    {
                        "uid": 581,
                        "name": 'Гуляйпільська',
                        "name_en": 'Huliaipilska',
                    },
                    {
                        "uid": 582,
                        "name": 'Комиш-Зорянська',
                        "name_en": 'Komysh-Zorianska',
                    },
                    {
                        "uid": 583,
                        "name": 'Малинівська',
                        "name_en": 'Malynivska',
                    },
                    {
                        "uid": 584,
                        "name": 'Малотокмачанська',
                        "name_en": 'Malotokmachanska',
                    },
                    {
                        "uid": 585,
                        "name": 'Молочанська',
                        "name_en": 'Molochanska',
                    },
                    {
                        "uid": 586,
                        "name": 'Оріхівська',
                        "name_en": 'Orikhivska',
                    },
                    {
                        "uid": 587,
                        "name": 'Пологівська',
                        "name_en": 'Polohivska',
                    },
                    {
                        "uid": 588,
                        "name": 'Преображенська',
                        "name_en": 'Preobrazhenska',
                    },
                    {
                        "uid": 589,
                        "name": 'Розівська',
                        "name_en": 'Rozivska',
                    },
                    {
                        "uid": 590,
                        "name": 'Смирновська',
                        "name_en": 'Smyrnovska',
                    },
                    {
                        "uid": 591,
                        "name": 'м. Токмак та Токмацька',
                        "name_en": 'Tokmak and Tokmatska',
                    },
                    {
                        "uid": 592,
                        "name": 'Федорівська',
                        "name_en": 'Fedorivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 14,
        "name": 'Київська',
        "type": LocationType.OBLAST,
        "name_en": 'Kyivska',
        "districts": [
            {
                "uid": 78,
                "name": 'Бориспільський',
                "name_en": 'Boryspilskyi',
                "hromadas": [
                    {
                        "uid": 733,
                        "name": 'м. Бориспіль та Бориспільська',
                        "name_en": 'Boryspil and Boryspilska',
                    },
                    {
                        "uid": 734,
                        "name": 'Вороньківська',
                        "name_en": 'Voronkivska',
                    },
                    {
                        "uid": 735,
                        "name": 'Гірська',
                        "name_en": 'Hirska',
                    },
                    {
                        "uid": 736,
                        "name": 'Дівичківська',
                        "name_en": 'Divychkivska',
                    },
                    {
                        "uid": 737,
                        "name": 'Золочівська',
                        "name_en": 'Zolochivska',
                    },
                    {
                        "uid": 738,
                        "name": 'м. Переяслав та Переяславська',
                        "name_en": 'Pereiaslav and Pereiaslavska',
                    },
                    {
                        "uid": 739,
                        "name": 'Пристолична',
                        "name_en": 'Prystolychna',
                    },
                    {
                        "uid": 740,
                        "name": 'Студениківська',
                        "name_en": 'Studenykivska',
                    },
                    {
                        "uid": 741,
                        "name": 'Ташанська',
                        "name_en": 'Tashanska',
                    },
                    {
                        "uid": 742,
                        "name": 'Циблівська',
                        "name_en": 'Tsyblivska',
                    },
                    {
                        "uid": 743,
                        "name": 'Яготинська',
                        "name_en": 'Yahotynska',
                    },
                ],
            },
            {
                "uid": 79,
                "name": 'Броварський',
                "name_en": 'Brovarskyi',
                "hromadas": [
                    {
                        "uid": 682,
                        "name": 'Баришівська',
                        "name_en": 'Baryshivska',
                    },
                    {
                        "uid": 683,
                        "name": 'м. Березань та Березанська',
                        "name_en": 'Berezan and Berezanska',
                    },
                    {
                        "uid": 684,
                        "name": 'м. Бровари та Броварська',
                        "name_en": 'Brovary and Brovarska',
                    },
                    {
                        "uid": 685,
                        "name": 'Великодимерська',
                        "name_en": 'Velykodymerska',
                    },
                    {
                        "uid": 686,
                        "name": 'Зазимська',
                        "name_en": 'Zazymska',
                    },
                    {
                        "uid": 687,
                        "name": 'Згурівська',
                        "name_en": 'Zghurivska',
                    },
                    {
                        "uid": 688,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska',
                    },
                    {
                        "uid": 689,
                        "name": 'Калитянська',
                        "name_en": 'Kalytianska',
                    },
                ],
            },
            {
                "uid": 75,
                "name": 'Бучанський',
                "name_en": 'Buchanskyi',
                "hromadas": [
                    {
                        "uid": 700,
                        "name": 'Бородянська',
                        "name_en": 'Borodianska',
                    },
                    {
                        "uid": 701,
                        "name": 'Борщагівська',
                        "name_en": 'Borshchahivska',
                    },
                    {
                        "uid": 702,
                        "name": 'м. Буча та Бучанська',
                        "name_en": 'Bucha and Buchanska',
                    },
                    {
                        "uid": 699,
                        "name": 'Білогородська',
                        "name_en": 'Bilohorodska',
                    },
                    {
                        "uid": 703,
                        "name": 'Вишнева',
                        "name_en": 'Vyshneva',
                    },
                    {
                        "uid": 704,
                        "name": 'Гостомелська',
                        "name_en": 'Hostomelska',
                    },
                    {
                        "uid": 705,
                        "name": 'Дмитрівська',
                        "name_en": 'Dmytrivska',
                    },
                    {
                        "uid": 707,
                        "name": 'Коцюбинська',
                        "name_en": 'Kotsiubynska',
                    },
                    {
                        "uid": 708,
                        "name": 'Макарівська',
                        "name_en": 'Makarivska',
                    },
                    {
                        "uid": 709,
                        "name": 'Немішаївська',
                        "name_en": 'Nemishaivska',
                    },
                    {
                        "uid": 710,
                        "name": 'Пісківська',
                        "name_en": 'Piskivska',
                    },
                    {
                        "uid": 706,
                        "name": 'м. Ірпінь та Ірпінська',
                        "name_en": 'Irpin and Irpinska',
                    },
                ],
            },
            {
                "uid": 73,
                "name": 'Білоцерківський',
                "name_en": 'Bilotserkivskyi',
                "hromadas": [
                    {
                        "uid": 711,
                        "name": 'м. Біла Церква та Білоцерківська',
                        "name_en": 'Bila Tserkva and Bilotserkivska',
                    },
                    {
                        "uid": 712,
                        "name": 'Володарська',
                        "name_en": 'Volodarska',
                    },
                    {
                        "uid": 713,
                        "name": 'Гребінківська',
                        "name_en": 'Hrebinkivska',
                    },
                    {
                        "uid": 714,
                        "name": 'Ковалівська',
                        "name_en": 'Kovalivska',
                    },
                    {
                        "uid": 715,
                        "name": 'Маловільшанська',
                        "name_en": 'Malovilshanska',
                    },
                    {
                        "uid": 716,
                        "name": 'Медвинська',
                        "name_en": 'Medvynska',
                    },
                    {
                        "uid": 717,
                        "name": 'Рокитнянська',
                        "name_en": 'Rokytnianska',
                    },
                    {
                        "uid": 718,
                        "name": 'Сквирська',
                        "name_en": 'Skvyrska',
                    },
                    {
                        "uid": 719,
                        "name": 'Ставищенська',
                        "name_en": 'Stavyshchenska',
                    },
                    {
                        "uid": 720,
                        "name": 'Таращанська',
                        "name_en": 'Tarashchanska',
                    },
                    {
                        "uid": 721,
                        "name": 'Тетіївська',
                        "name_en": 'Tetiivska',
                    },
                    {
                        "uid": 722,
                        "name": 'Узинська',
                        "name_en": 'Uzynska',
                    },
                    {
                        "uid": 723,
                        "name": 'Фурсівська',
                        "name_en": 'Fursivska',
                    },
                ],
            },
            {
                "uid": 74,
                "name": 'Вишгородський',
                "name_en": 'Vyshhorodskyi',
                "hromadas": [
                    {
                        "uid": 744,
                        "name": 'Вишгородська',
                        "name_en": 'Vyshhorodska',
                    },
                    {
                        "uid": 745,
                        "name": 'Димерська',
                        "name_en": 'Dymerska',
                    },
                    {
                        "uid": 747,
                        "name": 'Петрівська',
                        "name_en": 'Petrivska',
                    },
                    {
                        "uid": 749,
                        "name": 'Поліська',
                        "name_en": 'Poliska',
                    },
                    {
                        "uid": 748,
                        "name": 'Пірнівська',
                        "name_en": 'Pirnivska',
                    },
                    {
                        "uid": 750,
                        "name": 'м. Славутич та Славутицька',
                        "name_en": 'Slavutych and Slavutytska',
                    },
                    {
                        "uid": 746,
                        "name": 'Іванківська',
                        "name_en": 'Ivankivska',
                    },
                ],
            },
            {
                "uid": 76,
                "name": 'Обухівський',
                "name_en": 'Obukhivskyi',
                "hromadas": [
                    {
                        "uid": 724,
                        "name": 'Богуславська',
                        "name_en": 'Bohuslavska',
                    },
                    {
                        "uid": 725,
                        "name": 'м. Васильків та Васильківська',
                        "name_en": 'Vasylkiv and Vasylkivska',
                    },
                    {
                        "uid": 726,
                        "name": 'Кагарлицька',
                        "name_en": 'Kaharlytska',
                    },
                    {
                        "uid": 727,
                        "name": 'Козинська',
                        "name_en": 'Kozynska',
                    },
                    {
                        "uid": 728,
                        "name": 'Миронівська',
                        "name_en": 'Myronivska',
                    },
                    {
                        "uid": 729,
                        "name": 'м. Обухів та Обухівська',
                        "name_en": 'Obukhiv and Obukhivska',
                    },
                    {
                        "uid": 730,
                        "name": 'м. Ржищів та Ржищівська',
                        "name_en": 'Rzhyshchiv and Rzhyshchivska',
                    },
                    {
                        "uid": 731,
                        "name": 'Українська',
                        "name_en": 'Ukrainska',
                    },
                    {
                        "uid": 732,
                        "name": 'Феодосіївська',
                        "name_en": 'Feodosiivska',
                    },
                ],
            },
            {
                "uid": 77,
                "name": 'Фастівський',
                "name_en": 'Fastivskyi',
                "hromadas": [
                    {
                        "uid": 690,
                        "name": 'Бишівська',
                        "name_en": 'Byshivska',
                    },
                    {
                        "uid": 691,
                        "name": 'Боярська',
                        "name_en": 'Boiarska',
                    },
                    {
                        "uid": 692,
                        "name": 'Гатненська',
                        "name_en": 'Hatnenska',
                    },
                    {
                        "uid": 693,
                        "name": 'Глевахівська',
                        "name_en": 'Hlevakhivska',
                    },
                    {
                        "uid": 694,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska',
                    },
                    {
                        "uid": 695,
                        "name": 'Кожанська',
                        "name_en": 'Kozhanska',
                    },
                    {
                        "uid": 696,
                        "name": 'Томашівська',
                        "name_en": 'Tomashivska',
                    },
                    {
                        "uid": 697,
                        "name": 'м. Фастів та Фастівська',
                        "name_en": 'Fastiv and Fastivska',
                    },
                    {
                        "uid": 698,
                        "name": 'Чабанівська',
                        "name_en": 'Chabanivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 15,
        "name": 'Кіровоградська',
        "type": LocationType.OBLAST,
        "name_en": 'Kirovohradska',
        "districts": [
            {
                "uid": 82,
                "name": 'Голованівський',
                "name_en": 'Holovanivskyi',
                "hromadas": [
                    {
                        "uid": 768,
                        "name": 'Благовіщенська',
                        "name_en": 'Blahovishchenska',
                    },
                    {
                        "uid": 769,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska',
                    },
                    {
                        "uid": 770,
                        "name": 'Гайворонська',
                        "name_en": 'Haivoronska',
                    },
                    {
                        "uid": 771,
                        "name": 'Голованівська',
                        "name_en": 'Holovanivska',
                    },
                    {
                        "uid": 772,
                        "name": 'Заваллівська',
                        "name_en": 'Zavallivska',
                    },
                    {
                        "uid": 773,
                        "name": 'Надлацька',
                        "name_en": 'Nadlatska',
                    },
                    {
                        "uid": 774,
                        "name": 'Новоархангельська',
                        "name_en": 'Novoarkhanhelska',
                    },
                    {
                        "uid": 775,
                        "name": 'Перегонівська',
                        "name_en": 'Perehonivska',
                    },
                    {
                        "uid": 777,
                        "name": 'Побузька',
                        "name_en": 'Pobuzka',
                    },
                    {
                        "uid": 776,
                        "name": 'Підвисоцька',
                        "name_en": 'Pidvysotska',
                    },
                ],
            },
            {
                "uid": 81,
                "name": 'Кропивницький',
                "name_en": 'Kropyvnytskyi',
                "hromadas": [
                    {
                        "uid": 751,
                        "name": 'Аджамська',
                        "name_en": 'Adzhamska',
                    },
                    {
                        "uid": 752,
                        "name": 'Бобринецька',
                        "name_en": 'Bobrynetska',
                    },
                    {
                        "uid": 753,
                        "name": 'Великосеверинівська',
                        "name_en": 'Velykoseverynivska',
                    },
                    {
                        "uid": 754,
                        "name": 'Гурівська',
                        "name_en": 'Hurivska',
                    },
                    {
                        "uid": 755,
                        "name": 'Дмитрівська',
                        "name_en": 'Dmytrivska',
                    },
                    {
                        "uid": 756,
                        "name": 'Долинська',
                        "name_en": 'Dolynska',
                    },
                    {
                        "uid": 757,
                        "name": "м. Знам'янка та Знам’янська",
                        "name_en": 'Znamianka and Znamyanska',
                    },
                    {
                        "uid": 758,
                        "name": 'Катеринівська',
                        "name_en": 'Katerynivska',
                    },
                    {
                        "uid": 759,
                        "name": 'Кетрисанівська',
                        "name_en": 'Ketrysanivska',
                    },
                    {
                        "uid": 760,
                        "name": 'Компаніївська',
                        "name_en": 'Kompaniivska',
                    },
                    {
                        "uid": 761,
                        "name": 'м. Кропивницький та Кропивницька',
                        "name_en": 'Kropyvnytskyi and Kropyvnytska',
                    },
                    {
                        "uid": 762,
                        "name": 'Новгородківська',
                        "name_en": 'Novhorodkivska',
                    },
                    {
                        "uid": 763,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska',
                    },
                    {
                        "uid": 764,
                        "name": 'Первозванівська',
                        "name_en": 'Pervozvanivska',
                    },
                    {
                        "uid": 765,
                        "name": 'Соколівська',
                        "name_en": 'Sokolivska',
                    },
                    {
                        "uid": 766,
                        "name": 'Суботцівська',
                        "name_en": 'Subottsivska',
                    },
                    {
                        "uid": 767,
                        "name": 'Устинівська',
                        "name_en": 'Ustynivska',
                    },
                ],
            },
            {
                "uid": 83,
                "name": 'Новоукраїнський',
                "name_en": 'Novoukrainskyi',
                "hromadas": [
                    {
                        "uid": 787,
                        "name": 'Ганнівська',
                        "name_en": 'Hannivska',
                    },
                    {
                        "uid": 788,
                        "name": 'Глодоська',
                        "name_en": 'Hlodoska',
                    },
                    {
                        "uid": 789,
                        "name": 'Добровеличківська',
                        "name_en": 'Dobrovelychkivska',
                    },
                    {
                        "uid": 790,
                        "name": 'Злинська',
                        "name_en": 'Zlynska',
                    },
                    {
                        "uid": 791,
                        "name": 'Маловисківська',
                        "name_en": 'Malovyskivska',
                    },
                    {
                        "uid": 792,
                        "name": 'Мар’янівська',
                        "name_en": 'Maryanivska',
                    },
                    {
                        "uid": 793,
                        "name": 'Новомиргородська',
                        "name_en": 'Novomyrhorodska',
                    },
                    {
                        "uid": 794,
                        "name": 'Новоукраїнська',
                        "name_en": 'Novoukrainska',
                    },
                    {
                        "uid": 796,
                        "name": 'Помічнянська',
                        "name_en": 'Pomichnianska',
                    },
                    {
                        "uid": 795,
                        "name": 'Піщанобрідська',
                        "name_en": 'Pishchanobridska',
                    },
                    {
                        "uid": 797,
                        "name": 'Рівнянська',
                        "name_en": 'Rivnianska',
                    },
                    {
                        "uid": 798,
                        "name": 'Смолінська',
                        "name_en": 'Smolinska',
                    },
                    {
                        "uid": 799,
                        "name": 'Тишківська',
                        "name_en": 'Tyshkivska',
                    },
                ],
            },
            {
                "uid": 80,
                "name": 'Олександрійський',
                "name_en": 'Oleksandriiskyi',
                "hromadas": [
                    {
                        "uid": 778,
                        "name": 'Великоандрусівська',
                        "name_en": 'Velykoandrusivska',
                    },
                    {
                        "uid": 779,
                        "name": 'Новопразька',
                        "name_en": 'Novoprazka',
                    },
                    {
                        "uid": 780,
                        "name": 'м. Олександрія та Олександрійська',
                        "name_en": 'Oleksandriia and Oleksandriiska',
                    },
                    {
                        "uid": 781,
                        "name": 'Онуфріївська',
                        "name_en": 'Onufriivska',
                    },
                    {
                        "uid": 782,
                        "name": 'Пантаївська',
                        "name_en": 'Pantaivska',
                    },
                    {
                        "uid": 783,
                        "name": 'Петрівська',
                        "name_en": 'Petrivska',
                    },
                    {
                        "uid": 784,
                        "name": 'Попельнастівська',
                        "name_en": 'Popelnastivska',
                    },
                    {
                        "uid": 785,
                        "name": 'Приютівська',
                        "name_en": 'Pryiutivska',
                    },
                    {
                        "uid": 786,
                        "name": 'м. Світловодськ та Світловодська',
                        "name_en": 'Svitlovodsk and Svitlovodska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 16,
        "name": 'Луганська',
        "type": LocationType.OBLAST,
        "name_en": 'Luhanska',
        "districts": [
            {
                "uid": 1803,
                "name": 'Алчевський',
                "name_en": 'Alchevskyi',
                "hromadas": [
                    {
                        "uid": 1903,
                        "name": 'м. Алчевськ та Алчевська',
                        "name_en": 'Alchevsk and Alchevska',
                    },
                    {
                        "uid": 1911,
                        "name": "м. Зимогір'я та Зимогір'ївська",
                        "name_en": 'Zymohiria and Zymohirivska',
                    },
                    {
                        "uid": 1909,
                        "name": 'м. Кадіївка та Кадіївська',
                        "name_en": 'Kadiivka and Kadiivska',
                    },
                ],
            },
            {
                "uid": 1804,
                "name": 'Довжанський',
                "name_en": 'Dovzhanskyi',
                "hromadas": [
                    {
                        "uid": 1908,
                        "name": 'м. Довжанськ та Довжанська',
                        "name_en": 'Dovzhansk and Dovzhanska',
                    },
                    {
                        "uid": 1905,
                        "name": 'м. Сорокине та Сорокинська',
                        "name_en": 'Sorokyne and Sorokynska',
                    },
                ],
            },
            {
                "uid": 1801,
                "name": 'Луганський',
                "name_en": 'Luhanskyi',
                "hromadas": [
                    {
                        "uid": 1901,
                        "name": 'м. Луганськ та Луганська',
                        "name_en": 'Luhansk and Luhanska',
                    },
                    {
                        "uid": 1910,
                        "name": 'м. Лутугине та Лутугинська',
                        "name_en": 'Lutuhyne and Lutuhynska',
                    },
                    {
                        "uid": 1904,
                        "name": 'м. Молодогвардійськ та Молодогвардійська',
                        "name_en": 'Molodohvardiisk and Molodohvardiiska',
                    },
                ],
            },
            {
                "uid": 1802,
                "name": 'Ровеньківський',
                "name_en": 'Rovenkivskyi',
                "hromadas": [
                    {
                        "uid": 1902,
                        "name": 'м. Антрацит та Антрацитівська',
                        "name_en": 'Antratsyt and Antratsytivska',
                    },
                    {
                        "uid": 1907,
                        "name": 'м. Ровеньки та Ровеньківська',
                        "name_en": 'Rovenky and Rovenkivska',
                    },
                    {
                        "uid": 1906,
                        "name": 'м. Хрустальний та Хрустальненська',
                        "name_en": 'Khrustalnyi and Khrustalnenska',
                    },
                ],
            },
            {
                "uid": 85,
                "name": 'Сватівський',
                "name_en": 'Svativskyi',
                "hromadas": [
                    {
                        "uid": 808,
                        "name": 'Білокуракинська',
                        "name_en": 'Bilokurakynska',
                    },
                    {
                        "uid": 809,
                        "name": 'Коломийчиська',
                        "name_en": 'Kolomyichyska',
                    },
                    {
                        "uid": 810,
                        "name": 'Красноріченська',
                        "name_en": 'Krasnorichenska',
                    },
                    {
                        "uid": 811,
                        "name": 'Лозно-Олександрівська',
                        "name_en": 'Lozno-Oleksandrivska',
                    },
                    {
                        "uid": 812,
                        "name": 'Нижньодуванська',
                        "name_en": 'Nyzhnoduvanska',
                    },
                    {
                        "uid": 813,
                        "name": 'Сватівська',
                        "name_en": 'Svativska',
                    },
                    {
                        "uid": 814,
                        "name": 'Троїцька',
                        "name_en": 'Troitska',
                    },
                ],
            },
            {
                "uid": 86,
                "name": 'Старобільський',
                "name_en": 'Starobilskyi',
                "hromadas": [
                    {
                        "uid": 800,
                        "name": 'Біловодська',
                        "name_en": 'Bilovodska',
                    },
                    {
                        "uid": 801,
                        "name": 'Білолуцька',
                        "name_en": 'Bilolutska',
                    },
                    {
                        "uid": 802,
                        "name": 'Марківська',
                        "name_en": 'Markivska',
                    },
                    {
                        "uid": 803,
                        "name": 'Міловська',
                        "name_en": 'Milovska',
                    },
                    {
                        "uid": 804,
                        "name": 'Новопсковська',
                        "name_en": 'Novopskovska',
                    },
                    {
                        "uid": 805,
                        "name": 'Старобільська',
                        "name_en": 'Starobilska',
                    },
                    {
                        "uid": 806,
                        "name": 'Чмирівська',
                        "name_en": 'Chmyrivska',
                    },
                    {
                        "uid": 807,
                        "name": 'Шульгинська',
                        "name_en": 'Shulhynska',
                    },
                ],
            },
            {
                "uid": 84,
                "name": 'Сіверськодонецький',
                "name_en": 'Siverskodonetskyi',
                "hromadas": [
                    {
                        "uid": 815,
                        "name": 'Гірська',
                        "name_en": 'Hirska',
                    },
                    {
                        "uid": 816,
                        "name": 'м. Кремінна та Кремінська',
                        "name_en": 'Kreminna and Kreminska',
                    },
                    {
                        "uid": 817,
                        "name": 'м. Лисичанськ та Лисичанська',
                        "name_en": 'Lysychansk and Lysychanska',
                    },
                    {
                        "uid": 818,
                        "name": 'Попаснянська',
                        "name_en": 'Popasnianska',
                    },
                    {
                        "uid": 819,
                        "name": 'м. Рубіжне та Рубіжанська',
                        "name_en": 'Rubizhne and Rubizhanska',
                    },
                    {
                        "uid": 820,
                        "name": 'м. Сіверськодонецьк та Сіверськодонецька',
                        "name_en": 'Siverskodonetsk and Siverskodonetska',
                    },
                ],
            },
            {
                "uid": 87,
                "name": 'Щастинський',
                "name_en": 'Shchastynskyi',
                "hromadas": [
                    {
                        "uid": 821,
                        "name": 'Нижньотеплівська',
                        "name_en": 'Nyzhnoteplivska',
                    },
                    {
                        "uid": 822,
                        "name": 'Новоайдарська',
                        "name_en": 'Novoaidarska',
                    },
                    {
                        "uid": 823,
                        "name": 'Станично-Луганська',
                        "name_en": 'Stanychno-Luhanska',
                    },
                    {
                        "uid": 824,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska',
                    },
                    {
                        "uid": 825,
                        "name": 'Щастинська',
                        "name_en": 'Shchastynska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 27,
        "name": 'Львівська',
        "type": LocationType.OBLAST,
        "name_en": 'Lvivska',
        "districts": [
            {
                "uid": 91,
                "name": 'Дрогобицький',
                "name_en": 'Drohobytskyi',
                "hromadas": [
                    {
                        "uid": 867,
                        "name": 'м. Борислав та Бориславська',
                        "name_en": 'Boryslav and Boryslavska',
                    },
                    {
                        "uid": 868,
                        "name": 'м. Дрогобич та Дрогобицька',
                        "name_en": 'Drohobych and Drohobytska',
                    },
                    {
                        "uid": 869,
                        "name": 'Меденицька',
                        "name_en": 'Medenytska',
                    },
                    {
                        "uid": 870,
                        "name": 'Східницька',
                        "name_en": 'Skhidnytska',
                    },
                    {
                        "uid": 871,
                        "name": 'м. Трускавець та Трускавецька',
                        "name_en": 'Truskavets and Truskavetska',
                    },
                ],
            },
            {
                "uid": 94,
                "name": 'Золочівський',
                "name_en": 'Zolochivskyi',
                "hromadas": [
                    {
                        "uid": 872,
                        "name": 'Бродівська',
                        "name_en": 'Brodivska',
                    },
                    {
                        "uid": 873,
                        "name": 'Буська',
                        "name_en": 'Buska',
                    },
                    {
                        "uid": 874,
                        "name": 'Заболотцівська',
                        "name_en": 'Zabolottsivska',
                    },
                    {
                        "uid": 875,
                        "name": 'Золочівська',
                        "name_en": 'Zolochivska',
                    },
                    {
                        "uid": 876,
                        "name": 'Красненська',
                        "name_en": 'Krasnenska',
                    },
                    {
                        "uid": 878,
                        "name": 'Поморянська',
                        "name_en": 'Pomorianska',
                    },
                    {
                        "uid": 877,
                        "name": 'Підкамінська',
                        "name_en": 'Pidkaminska',
                    },
                ],
            },
            {
                "uid": 90,
                "name": 'Львівський',
                "name_en": 'Lvivskyi',
                "hromadas": [
                    {
                        "uid": 833,
                        "name": 'Бібрська',
                        "name_en": 'Bibrska',
                    },
                    {
                        "uid": 834,
                        "name": 'Великолюбінська',
                        "name_en": 'Velykoliubinska',
                    },
                    {
                        "uid": 835,
                        "name": 'Глинянська',
                        "name_en": 'Hlynianska',
                    },
                    {
                        "uid": 836,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska',
                    },
                    {
                        "uid": 837,
                        "name": 'Давидівська',
                        "name_en": 'Davydivska',
                    },
                    {
                        "uid": 838,
                        "name": 'Добросинсько-Магерівська',
                        "name_en": 'Dobrosynsko-Maherivska',
                    },
                    {
                        "uid": 839,
                        "name": 'Жовківська',
                        "name_en": 'Zhovkivska',
                    },
                    {
                        "uid": 840,
                        "name": 'Жовтанецька',
                        "name_en": 'Zhovtanetska',
                    },
                    {
                        "uid": 841,
                        "name": 'Зимноводівська',
                        "name_en": 'Zymnovodivska',
                    },
                    {
                        "uid": 842,
                        "name": 'Кам’янка-Бузька',
                        "name_en": 'Kamyanka-Buzka',
                    },
                    {
                        "uid": 843,
                        "name": 'Комарнівська',
                        "name_en": 'Komarnivska',
                    },
                    {
                        "uid": 844,
                        "name": 'Куликівська',
                        "name_en": 'Kulykivska',
                    },
                    {
                        "uid": 845,
                        "name": 'м. Львів та Львівська',
                        "name_en": 'Lviv and Lvivska',
                    },
                    {
                        "uid": 846,
                        "name": 'Мурованська',
                        "name_en": 'Murovanska',
                    },
                    {
                        "uid": 847,
                        "name": 'Новояричівська',
                        "name_en": 'Novoiarychivska',
                    },
                    {
                        "uid": 848,
                        "name": 'Оброшинська',
                        "name_en": 'Obroshynska',
                    },
                    {
                        "uid": 849,
                        "name": 'Перемишлянська',
                        "name_en": 'Peremyshlianska',
                    },
                    {
                        "uid": 851,
                        "name": 'Пустомитівська',
                        "name_en": 'Pustomytivska',
                    },
                    {
                        "uid": 850,
                        "name": 'Підберізцівська',
                        "name_en": 'Pidberiztsivska',
                    },
                    {
                        "uid": 852,
                        "name": 'Рава-Руська',
                        "name_en": 'Rava-Ruska',
                    },
                    {
                        "uid": 853,
                        "name": 'Сокільницька',
                        "name_en": 'Sokilnytska',
                    },
                    {
                        "uid": 854,
                        "name": 'Солонківська',
                        "name_en": 'Solonkivska',
                    },
                    {
                        "uid": 855,
                        "name": 'Щирецька',
                        "name_en": 'Shchyretska',
                    },
                ],
            },
            {
                "uid": 88,
                "name": 'Самбірський',
                "name_en": 'Sambirskyi',
                "hromadas": [
                    {
                        "uid": 857,
                        "name": 'Боринська',
                        "name_en": 'Borynska',
                    },
                    {
                        "uid": 856,
                        "name": 'Бісковицька',
                        "name_en": 'Biskovytska',
                    },
                    {
                        "uid": 858,
                        "name": 'Добромильська',
                        "name_en": 'Dobromylska',
                    },
                    {
                        "uid": 859,
                        "name": 'Новокалинівська',
                        "name_en": 'Novokalynivska',
                    },
                    {
                        "uid": 860,
                        "name": 'Ралівська',
                        "name_en": 'Ralivska',
                    },
                    {
                        "uid": 861,
                        "name": 'Рудківська',
                        "name_en": 'Rudkivska',
                    },
                    {
                        "uid": 862,
                        "name": 'м. Самбір та Самбірська',
                        "name_en": 'Sambir and Sambirska',
                    },
                    {
                        "uid": 863,
                        "name": 'Старосамбірська',
                        "name_en": 'Starosambirska',
                    },
                    {
                        "uid": 864,
                        "name": 'Стрілківська',
                        "name_en": 'Strilkivska',
                    },
                    {
                        "uid": 865,
                        "name": 'Турківська',
                        "name_en": 'Turkivska',
                    },
                    {
                        "uid": 866,
                        "name": 'Хирівська',
                        "name_en": 'Khyrivska',
                    },
                ],
            },
            {
                "uid": 89,
                "name": 'Стрийський',
                "name_en": 'Stryiskyi',
                "hromadas": [
                    {
                        "uid": 879,
                        "name": 'Гніздичівська',
                        "name_en": 'Hnizdychivska',
                    },
                    {
                        "uid": 880,
                        "name": 'Грабовецько-Дулібівська',
                        "name_en": 'Hrabovetsko-Dulibivska',
                    },
                    {
                        "uid": 881,
                        "name": 'Жидачівська',
                        "name_en": 'Zhydachivska',
                    },
                    {
                        "uid": 882,
                        "name": 'Журавненська',
                        "name_en": 'Zhuravnenska',
                    },
                    {
                        "uid": 883,
                        "name": 'Козівська',
                        "name_en": 'Kozivska',
                    },
                    {
                        "uid": 884,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 885,
                        "name": 'м. Моршин та Моршинська',
                        "name_en": 'Morshyn and Morshynska',
                    },
                    {
                        "uid": 886,
                        "name": 'м. Новий Розділ та Новороздільська',
                        "name_en": 'Novyi Rozdil and Novorozdilska',
                    },
                    {
                        "uid": 887,
                        "name": 'Розвадівська',
                        "name_en": 'Rozvadivska',
                    },
                    {
                        "uid": 888,
                        "name": 'Сколівська',
                        "name_en": 'Skolivska',
                    },
                    {
                        "uid": 889,
                        "name": 'Славська',
                        "name_en": 'Slavska',
                    },
                    {
                        "uid": 890,
                        "name": 'м. Стрий та Стрийська',
                        "name_en": 'Stryi and Stryiska',
                    },
                    {
                        "uid": 891,
                        "name": 'Тростянецька',
                        "name_en": 'Trostianetska',
                    },
                    {
                        "uid": 892,
                        "name": 'Ходорівська',
                        "name_en": 'Khodorivska',
                    },
                ],
            },
            {
                "uid": 92,
                "name": 'Шептицький',
                "name_en": 'Sheptytskyi',
                "hromadas": [
                    {
                        "uid": 826,
                        "name": 'Белзька',
                        "name_en": 'Belzka',
                    },
                    {
                        "uid": 827,
                        "name": 'Великомостівська',
                        "name_en": 'Velykomostivska',
                    },
                    {
                        "uid": 828,
                        "name": 'Добротвірська',
                        "name_en": 'Dobrotvirska',
                    },
                    {
                        "uid": 829,
                        "name": 'Лопатинська',
                        "name_en": 'Lopatynska',
                    },
                    {
                        "uid": 830,
                        "name": 'Радехівська',
                        "name_en": 'Radekhivska',
                    },
                    {
                        "uid": 831,
                        "name": 'Сокальська',
                        "name_en": 'Sokalska',
                    },
                    {
                        "uid": 832,
                        "name": 'м. Шептицький та Шептицька',
                        "name_en": 'Sheptytskyi and Sheptytska',
                    },
                ],
            },
            {
                "uid": 93,
                "name": 'Яворівський',
                "name_en": 'Yavorivskyi',
                "hromadas": [
                    {
                        "uid": 894,
                        "name": 'Мостиська',
                        "name_en": 'Mostyska',
                    },
                    {
                        "uid": 895,
                        "name": 'Новояворівськ',
                        "name_en": 'Novoiavorivsk',
                    },
                    {
                        "uid": 896,
                        "name": 'Судововишнянська',
                        "name_en": 'Sudovovyshnianska',
                    },
                    {
                        "uid": 897,
                        "name": 'Шегинівська',
                        "name_en": 'Shehynivska',
                    },
                    {
                        "uid": 898,
                        "name": 'Яворівська',
                        "name_en": 'Yavorivska',
                    },
                    {
                        "uid": 893,
                        "name": 'Івано-Франківська',
                        "name_en": 'Ivano-Frankivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 17,
        "name": 'Миколаївська',
        "type": LocationType.OBLAST,
        "name_en": 'Mykolaivska',
        "districts": [
            {
                "uid": 96,
                "name": 'Баштанський',
                "name_en": 'Bashtanskyi',
                "hromadas": [
                    {
                        "uid": 907,
                        "name": 'м. Баштанка та Баштанська',
                        "name_en": 'Bashtanka and Bashtanska',
                    },
                    {
                        "uid": 908,
                        "name": 'Березнегуватська',
                        "name_en": 'Bereznehuvatska',
                    },
                    {
                        "uid": 910,
                        "name": 'Володимирівська',
                        "name_en": 'Volodymyrivska',
                    },
                    {
                        "uid": 909,
                        "name": 'Вільнозапорізька',
                        "name_en": 'Vilnozaporizka',
                    },
                    {
                        "uid": 911,
                        "name": 'Горохівська',
                        "name_en": 'Horokhivska',
                    },
                    {
                        "uid": 913,
                        "name": 'Казанківська',
                        "name_en": 'Kazankivska',
                    },
                    {
                        "uid": 914,
                        "name": 'Новобузька',
                        "name_en": 'Novobuzka',
                    },
                    {
                        "uid": 915,
                        "name": 'Привільненська',
                        "name_en": 'Pryvilnenska',
                    },
                    {
                        "uid": 916,
                        "name": 'м. Снігурівка та Снігурівська',
                        "name_en": 'Snihurivka and Snihurivska',
                    },
                    {
                        "uid": 917,
                        "name": 'Софіївська',
                        "name_en": 'Sofiivska',
                    },
                    {
                        "uid": 918,
                        "name": 'Широківська',
                        "name_en": 'Shyrokivska',
                    },
                    {
                        "uid": 912,
                        "name": 'Інгульська',
                        "name_en": 'Inhulska',
                    },
                ],
            },
            {
                "uid": 95,
                "name": 'Вознесенський',
                "name_en": 'Voznesenskyi',
                "hromadas": [
                    {
                        "uid": 938,
                        "name": 'Братська',
                        "name_en": 'Bratska',
                    },
                    {
                        "uid": 939,
                        "name": 'Бузька',
                        "name_en": 'Buzka',
                    },
                    {
                        "uid": 940,
                        "name": 'Веселинівська',
                        "name_en": 'Veselynivska',
                    },
                    {
                        "uid": 941,
                        "name": 'м. Вознесенськ та Вознесенська',
                        "name_en": 'Voznesensk and Voznesenska',
                    },
                    {
                        "uid": 942,
                        "name": 'Доманівська',
                        "name_en": 'Domanivska',
                    },
                    {
                        "uid": 943,
                        "name": 'Дорошівська',
                        "name_en": 'Doroshivska',
                    },
                    {
                        "uid": 945,
                        "name": 'Мостівська',
                        "name_en": 'Mostivska',
                    },
                    {
                        "uid": 946,
                        "name": "Новомар'ївська",
                        "name_en": 'Novomarivska',
                    },
                    {
                        "uid": 947,
                        "name": 'Олександрівська',
                        "name_en": 'Oleksandrivska',
                    },
                    {
                        "uid": 948,
                        "name": 'Прибужанівська',
                        "name_en": 'Prybuzhanivska',
                    },
                    {
                        "uid": 949,
                        "name": 'Прибузька',
                        "name_en": 'Prybuzka',
                    },
                    {
                        "uid": 950,
                        "name": 'м. Южноукраїнськ та Южноукраїнська',
                        "name_en": 'Yuzhnoukrainsk and Yuzhnoukrainska',
                    },
                    {
                        "uid": 944,
                        "name": 'Єланецька',
                        "name_en": 'Yelanetska',
                    },
                ],
            },
            {
                "uid": 98,
                "name": 'Миколаївський',
                "name_en": 'Mykolaivskyi',
                "hromadas": [
                    {
                        "uid": 919,
                        "name": 'Березанська',
                        "name_en": 'Berezanska',
                    },
                    {
                        "uid": 920,
                        "name": 'Веснянська',
                        "name_en": 'Vesnianska',
                    },
                    {
                        "uid": 921,
                        "name": 'Воскресенська',
                        "name_en": 'Voskresenska',
                    },
                    {
                        "uid": 922,
                        "name": 'Галицинівська',
                        "name_en": 'Halytsynivska',
                    },
                    {
                        "uid": 923,
                        "name": 'Коблівська',
                        "name_en": 'Koblivska',
                    },
                    {
                        "uid": 924,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska',
                    },
                    {
                        "uid": 925,
                        "name": 'Куцурубська',
                        "name_en": 'Kutsurubska',
                    },
                    {
                        "uid": 926,
                        "name": 'м. Миколаїв та Миколаївська',
                        "name_en": 'Mykolaiv and Mykolaivska',
                    },
                    {
                        "uid": 927,
                        "name": 'Мішково-Погорілівська',
                        "name_en": 'Mishkovo-Pohorilivska',
                    },
                    {
                        "uid": 928,
                        "name": 'Нечаянська',
                        "name_en": 'Nechaianska',
                    },
                    {
                        "uid": 929,
                        "name": 'м. Нова-Одеса та Новоодеська',
                        "name_en": 'Nova-Odesa and Novoodeska',
                    },
                    {
                        "uid": 930,
                        "name": 'Ольшанська',
                        "name_en": 'Olshanska',
                    },
                    {
                        "uid": 931,
                        "name": 'м. Очаків та Очаківська',
                        "name_en": 'Ochakiv and Ochakivska',
                    },
                    {
                        "uid": 932,
                        "name": 'Первомайська',
                        "name_en": 'Pervomaiska',
                    },
                    {
                        "uid": 933,
                        "name": 'Радсадівська',
                        "name_en": 'Radsadivska',
                    },
                    {
                        "uid": 934,
                        "name": 'Степівська',
                        "name_en": 'Stepivska',
                    },
                    {
                        "uid": 935,
                        "name": 'Сухоєланецька',
                        "name_en": 'Sukhoielanetska',
                    },
                    {
                        "uid": 936,
                        "name": 'Чорноморська',
                        "name_en": 'Chornomorska',
                    },
                    {
                        "uid": 937,
                        "name": 'Шевченківська',
                        "name_en": 'Shevchenkivska',
                    },
                ],
            },
            {
                "uid": 97,
                "name": 'Первомайський',
                "name_en": 'Pervomaiskyi',
                "hromadas": [
                    {
                        "uid": 899,
                        "name": 'Арбузинська',
                        "name_en": 'Arbuzynska',
                    },
                    {
                        "uid": 900,
                        "name": 'Благодатненська',
                        "name_en": 'Blahodatnenska',
                    },
                    {
                        "uid": 901,
                        "name": 'Врадіївська',
                        "name_en": 'Vradiivska',
                    },
                    {
                        "uid": 902,
                        "name": "Кам'яномостівська",
                        "name_en": 'Kamianomostivska',
                    },
                    {
                        "uid": 903,
                        "name": 'Кривоозерська',
                        "name_en": 'Kryvoozerska',
                    },
                    {
                        "uid": 904,
                        "name": 'Мигіївська',
                        "name_en": 'Myhiivska',
                    },
                    {
                        "uid": 905,
                        "name": 'м. Первомайськ та Первомайська',
                        "name_en": 'Pervomaisk and Pervomaiska',
                    },
                    {
                        "uid": 906,
                        "name": 'Синюхинобрідська',
                        "name_en": 'Syniukhynobridska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 18,
        "name": 'Одеська',
        "type": LocationType.OBLAST,
        "name_en": 'Odeska',
        "districts": [
            {
                "uid": 100,
                "name": 'Березівський',
                "name_en": 'Berezivskyi',
                "hromadas": [
                    {
                        "uid": 985,
                        "name": 'Андрієво-Іванівська',
                        "name_en": 'Andriievo-Ivanivska',
                    },
                    {
                        "uid": 986,
                        "name": 'Березівська',
                        "name_en": 'Berezivska',
                    },
                    {
                        "uid": 987,
                        "name": 'Великобуялицька',
                        "name_en": 'Velykobuialytska',
                    },
                    {
                        "uid": 988,
                        "name": 'Знам’янська',
                        "name_en": 'Znamyanska',
                    },
                    {
                        "uid": 990,
                        "name": 'Коноплянська',
                        "name_en": 'Konoplianska',
                    },
                    {
                        "uid": 991,
                        "name": 'Курісовська',
                        "name_en": 'Kurisovska',
                    },
                    {
                        "uid": 992,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 993,
                        "name": 'Новокальчевська',
                        "name_en": 'Novokalchevska',
                    },
                    {
                        "uid": 994,
                        "name": 'Петровірівська',
                        "name_en": 'Petrovirivska',
                    },
                    {
                        "uid": 995,
                        "name": 'Раухівська',
                        "name_en": 'Raukhivska',
                    },
                    {
                        "uid": 996,
                        "name": 'Розквітівська',
                        "name_en": 'Rozkvitivska',
                    },
                    {
                        "uid": 997,
                        "name": 'Старомаяківська',
                        "name_en": 'Staromaiakivska',
                    },
                    {
                        "uid": 998,
                        "name": 'Стрюківська',
                        "name_en": 'Striukivska',
                    },
                    {
                        "uid": 999,
                        "name": 'Чогодарівська',
                        "name_en": 'Chohodarivska',
                    },
                    {
                        "uid": 1000,
                        "name": 'Ширяївська',
                        "name_en": 'Shyriaivska',
                    },
                    {
                        "uid": 989,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska',
                    },
                ],
            },
            {
                "uid": 105,
                "name": 'Болградський',
                "name_en": 'Bolhradskyi',
                "hromadas": [
                    {
                        "uid": 1001,
                        "name": 'Арцизька',
                        "name_en": 'Artsyzka',
                    },
                    {
                        "uid": 1002,
                        "name": 'Болградська',
                        "name_en": 'Bolhradska',
                    },
                    {
                        "uid": 1003,
                        "name": 'Бородінська',
                        "name_en": 'Borodinska',
                    },
                    {
                        "uid": 1004,
                        "name": 'Василівська',
                        "name_en": 'Vasylivska',
                    },
                    {
                        "uid": 1005,
                        "name": 'Городненська',
                        "name_en": 'Horodnenska',
                    },
                    {
                        "uid": 1006,
                        "name": 'Криниченська',
                        "name_en": 'Krynychenska',
                    },
                    {
                        "uid": 1007,
                        "name": 'Кубейська',
                        "name_en": 'Kubeiska',
                    },
                    {
                        "uid": 1008,
                        "name": 'Павлівська',
                        "name_en": 'Pavlivska',
                    },
                    {
                        "uid": 1009,
                        "name": 'Тарутинська',
                        "name_en": 'Tarutynska',
                    },
                    {
                        "uid": 1010,
                        "name": 'Теплицька',
                        "name_en": 'Teplytska',
                    },
                ],
            },
            {
                "uid": 102,
                "name": 'Білгород-Дністровський',
                "name_en": 'Bilhorod-Dnistrovskyi',
                "hromadas": [
                    {
                        "uid": 1011,
                        "name": 'м. Білгород-Дністровський та Білгород-Дністровська',
                        "name_en": 'Bilhorod-Dnistrovskyi and Bilhorod-Dnistrovska',
                    },
                    {
                        "uid": 1012,
                        "name": 'Дивізійська',
                        "name_en": 'Dyviziiska',
                    },
                    {
                        "uid": 1013,
                        "name": 'Кароліно-Бугазька',
                        "name_en": 'Karolino-Buhazka',
                    },
                    {
                        "uid": 1014,
                        "name": 'Кулевчанська',
                        "name_en": 'Kulevchanska',
                    },
                    {
                        "uid": 1015,
                        "name": 'Лиманська',
                        "name_en": 'Lymanska',
                    },
                    {
                        "uid": 1016,
                        "name": 'Маразліївська',
                        "name_en": 'Marazliivska',
                    },
                    {
                        "uid": 1017,
                        "name": 'Мологівська',
                        "name_en": 'Molohivska',
                    },
                    {
                        "uid": 1018,
                        "name": 'Петропавлівська',
                        "name_en": 'Petropavlivska',
                    },
                    {
                        "uid": 1019,
                        "name": 'Плахтіївська',
                        "name_en": 'Plakhtiivska',
                    },
                    {
                        "uid": 1020,
                        "name": 'Саратська',
                        "name_en": 'Saratska',
                    },
                    {
                        "uid": 1021,
                        "name": 'Сергіївська',
                        "name_en": 'Serhiivska',
                    },
                    {
                        "uid": 1022,
                        "name": 'Старокозацька',
                        "name_en": 'Starokozatska',
                    },
                    {
                        "uid": 1023,
                        "name": 'Татарбунарська',
                        "name_en": 'Tatarbunarska',
                    },
                    {
                        "uid": 1024,
                        "name": 'Тузлівська',
                        "name_en": 'Tuzlivska',
                    },
                    {
                        "uid": 1025,
                        "name": 'Успенівська',
                        "name_en": 'Uspenivska',
                    },
                    {
                        "uid": 1026,
                        "name": 'Шабівська',
                        "name_en": 'Shabivska',
                    },
                ],
            },
            {
                "uid": 104,
                "name": 'Одеський',
                "name_en": 'Odeskyi',
                "hromadas": [
                    {
                        "uid": 951,
                        "name": 'Авангардівська',
                        "name_en": 'Avanhardivska',
                    },
                    {
                        "uid": 952,
                        "name": 'Біляївська',
                        "name_en": 'Biliaivska',
                    },
                    {
                        "uid": 953,
                        "name": 'Великодальницька',
                        "name_en": 'Velykodalnytska',
                    },
                    {
                        "uid": 954,
                        "name": 'Великодолинська',
                        "name_en": 'Velykodolynska',
                    },
                    {
                        "uid": 955,
                        "name": 'Вигодянська',
                        "name_en": 'Vyhodianska',
                    },
                    {
                        "uid": 956,
                        "name": 'Визирська',
                        "name_en": 'Vyzyrska',
                    },
                    {
                        "uid": 957,
                        "name": 'Дальницька',
                        "name_en": 'Dalnytska',
                    },
                    {
                        "uid": 958,
                        "name": 'Дачненська',
                        "name_en": 'Dachnenska',
                    },
                    {
                        "uid": 959,
                        "name": 'Доброславська',
                        "name_en": 'Dobroslavska',
                    },
                    {
                        "uid": 960,
                        "name": 'Красносільська',
                        "name_en": 'Krasnosilska',
                    },
                    {
                        "uid": 961,
                        "name": 'Маяківська',
                        "name_en": 'Maiakivska',
                    },
                    {
                        "uid": 962,
                        "name": 'Нерубайська',
                        "name_en": 'Nerubaiska',
                    },
                    {
                        "uid": 963,
                        "name": 'Овідіопольська',
                        "name_en": 'Ovidiopolska',
                    },
                    {
                        "uid": 964,
                        "name": 'м. Одеса та Одеська',
                        "name_en": 'Odesa and Odeska',
                    },
                    {
                        "uid": 971,
                        "name": 'м. Південне та Південна',
                        "name_en": 'Pivdenne and Pivdenna',
                    },
                    {
                        "uid": 965,
                        "name": 'Таїровська',
                        "name_en": 'Tairovska',
                    },
                    {
                        "uid": 966,
                        "name": 'Теплодарська',
                        "name_en": 'Teplodarska',
                    },
                    {
                        "uid": 967,
                        "name": 'Усатівська',
                        "name_en": 'Usativska',
                    },
                    {
                        "uid": 968,
                        "name": 'Фонтанська',
                        "name_en": 'Fontanska',
                    },
                    {
                        "uid": 969,
                        "name": 'м. Чорноморськ та Чорноморська',
                        "name_en": 'Chornomorsk and Chornomorska',
                    },
                    {
                        "uid": 970,
                        "name": 'Чорноморська',
                        "name_en": 'Chornomorska',
                    },
                    {
                        "uid": 972,
                        "name": 'Яськівська',
                        "name_en": 'Yaskivska',
                    },
                ],
            },
            {
                "uid": 99,
                "name": 'Подільський',
                "name_en": 'Podilskyi',
                "hromadas": [
                    {
                        "uid": 973,
                        "name": 'Ананьївська',
                        "name_en": 'Ananivska',
                    },
                    {
                        "uid": 974,
                        "name": 'Балтська',
                        "name_en": 'Baltska',
                    },
                    {
                        "uid": 975,
                        "name": 'Долинська',
                        "name_en": 'Dolynska',
                    },
                    {
                        "uid": 976,
                        "name": 'Зеленогірська',
                        "name_en": 'Zelenohirska',
                    },
                    {
                        "uid": 977,
                        "name": 'Кодимська',
                        "name_en": 'Kodymska',
                    },
                    {
                        "uid": 978,
                        "name": 'Куяльницька',
                        "name_en": 'Kuialnytska',
                    },
                    {
                        "uid": 979,
                        "name": 'Любашівська',
                        "name_en": 'Liubashivska',
                    },
                    {
                        "uid": 980,
                        "name": 'Окнянська',
                        "name_en": 'Oknianska',
                    },
                    {
                        "uid": 982,
                        "name": 'Подільська',
                        "name_en": 'Podilska',
                    },
                    {
                        "uid": 981,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska',
                    },
                    {
                        "uid": 983,
                        "name": 'Савранська',
                        "name_en": 'Savranska',
                    },
                    {
                        "uid": 984,
                        "name": 'Слобідська',
                        "name_en": 'Slobidska',
                    },
                ],
            },
            {
                "uid": 103,
                "name": 'Роздільнянський',
                "name_en": 'Rozdilnianskyi',
                "hromadas": [
                    {
                        "uid": 1027,
                        "name": 'Великомихайлівська',
                        "name_en": 'Velykomykhailivska',
                    },
                    {
                        "uid": 1028,
                        "name": 'Великоплосківська',
                        "name_en": 'Velykoploskivska',
                    },
                    {
                        "uid": 1029,
                        "name": 'Затишанська',
                        "name_en": 'Zatyshanska',
                    },
                    {
                        "uid": 1030,
                        "name": 'Захарівська',
                        "name_en": 'Zakharivska',
                    },
                    {
                        "uid": 1031,
                        "name": 'Лиманська',
                        "name_en": 'Lymanska',
                    },
                    {
                        "uid": 1032,
                        "name": 'Новоборисівська',
                        "name_en": 'Novoborysivska',
                    },
                    {
                        "uid": 1033,
                        "name": 'Роздільнянська',
                        "name_en": 'Rozdilnianska',
                    },
                    {
                        "uid": 1034,
                        "name": 'Степанівська',
                        "name_en": 'Stepanivska',
                    },
                    {
                        "uid": 1035,
                        "name": 'Цебриківська',
                        "name_en": 'Tsebrykivska',
                    },
                ],
            },
            {
                "uid": 101,
                "name": 'Ізмаїльський',
                "name_en": 'Izmailskyi',
                "hromadas": [
                    {
                        "uid": 1036,
                        "name": 'Вилківська',
                        "name_en": 'Vylkivska',
                    },
                    {
                        "uid": 1038,
                        "name": 'Кілійська',
                        "name_en": 'Kiliiska',
                    },
                    {
                        "uid": 1039,
                        "name": 'Ренійська',
                        "name_en": 'Reniiska',
                    },
                    {
                        "uid": 1040,
                        "name": "Саф'янівська",
                        "name_en": 'Safianivska',
                    },
                    {
                        "uid": 1041,
                        "name": 'Суворовська',
                        "name_en": 'Suvorovska',
                    },
                    {
                        "uid": 1037,
                        "name": 'м. Ізмаїл та Ізмаїльська',
                        "name_en": 'Izmail and Izmailska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 19,
        "name": 'Полтавська',
        "type": LocationType.OBLAST,
        "name_en": 'Poltavska',
        "districts": [
            {
                "uid": 107,
                "name": 'Кременчуцький',
                "name_en": 'Kremenchutskyi',
                "hromadas": [
                    {
                        "uid": 1083,
                        "name": 'Глобинська',
                        "name_en": 'Hlobynska',
                    },
                    {
                        "uid": 1084,
                        "name": 'м. Горішні плавні та Горішньоплавнівська',
                        "name_en": 'Horishni plavni and Horishnoplavnivska',
                    },
                    {
                        "uid": 1085,
                        "name": 'Градизька',
                        "name_en": 'Hradyzka',
                    },
                    {
                        "uid": 1086,
                        "name": "Кам'янопотоківська",
                        "name_en": 'Kamianopotokivska',
                    },
                    {
                        "uid": 1087,
                        "name": 'Козельщинська',
                        "name_en": 'Kozelshchynska',
                    },
                    {
                        "uid": 1088,
                        "name": 'м. Кременчук та Кременчуцька',
                        "name_en": 'Kremenchuk and Kremenchutska',
                    },
                    {
                        "uid": 1089,
                        "name": 'Новогалещинська',
                        "name_en": 'Novohaleshchynska',
                    },
                    {
                        "uid": 1090,
                        "name": 'Оболонська',
                        "name_en": 'Obolonska',
                    },
                    {
                        "uid": 1091,
                        "name": 'Омельницька',
                        "name_en": 'Omelnytska',
                    },
                    {
                        "uid": 1093,
                        "name": 'Пришибська',
                        "name_en": 'Pryshybska',
                    },
                    {
                        "uid": 1092,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska',
                    },
                    {
                        "uid": 1094,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska',
                    },
                ],
            },
            {
                "uid": 106,
                "name": 'Лубенський',
                "name_en": 'Lubenskyi',
                "hromadas": [
                    {
                        "uid": 1095,
                        "name": 'Гребінківська',
                        "name_en": 'Hrebinkivska',
                    },
                    {
                        "uid": 1096,
                        "name": 'м. Лубни та Лубенська',
                        "name_en": 'Lubny and Lubenska',
                    },
                    {
                        "uid": 1097,
                        "name": 'Новооржицька',
                        "name_en": 'Novoorzhytska',
                    },
                    {
                        "uid": 1098,
                        "name": 'Оржицька',
                        "name_en": 'Orzhytska',
                    },
                    {
                        "uid": 1099,
                        "name": 'м. Пирятин та Пирятинська',
                        "name_en": 'Pyriatyn and Pyriatynska',
                    },
                    {
                        "uid": 1100,
                        "name": 'Хорольська',
                        "name_en": 'Khorolska',
                    },
                    {
                        "uid": 1101,
                        "name": 'Чорнухинська',
                        "name_en": 'Chornukhynska',
                    },
                ],
            },
            {
                "uid": 108,
                "name": 'Миргородський',
                "name_en": 'Myrhorodskyi',
                "hromadas": [
                    {
                        "uid": 1066,
                        "name": 'Білоцерківська',
                        "name_en": 'Bilotserkivska',
                    },
                    {
                        "uid": 1067,
                        "name": 'Великобагачанська',
                        "name_en": 'Velykobahachanska',
                    },
                    {
                        "uid": 1068,
                        "name": 'Великобудищанська',
                        "name_en": 'Velykobudyshchanska',
                    },
                    {
                        "uid": 1069,
                        "name": 'Великосорочинська',
                        "name_en": 'Velykosorochynska',
                    },
                    {
                        "uid": 1070,
                        "name": 'Гадяцька',
                        "name_en": 'Hadiatska',
                    },
                    {
                        "uid": 1071,
                        "name": 'Гоголівська',
                        "name_en": 'Hoholivska',
                    },
                    {
                        "uid": 1072,
                        "name": 'Заводська',
                        "name_en": 'Zavodska',
                    },
                    {
                        "uid": 1073,
                        "name": 'Комишнянська',
                        "name_en": 'Komyshnianska',
                    },
                    {
                        "uid": 1074,
                        "name": 'Краснолуцька',
                        "name_en": 'Krasnolutska',
                    },
                    {
                        "uid": 1075,
                        "name": 'м. Лохвиця та Лохвицька',
                        "name_en": 'Lokhvytsia and Lokhvytska',
                    },
                    {
                        "uid": 1076,
                        "name": 'Лютенська',
                        "name_en": 'Liutenska',
                    },
                    {
                        "uid": 1077,
                        "name": 'м. Миргород та Миргородська',
                        "name_en": 'Myrhorod and Myrhorodska',
                    },
                    {
                        "uid": 1078,
                        "name": 'Петрівсько-Роменська',
                        "name_en": 'Petrivsko-Romenska',
                    },
                    {
                        "uid": 1079,
                        "name": 'Ромоданівська',
                        "name_en": 'Romodanivska',
                    },
                    {
                        "uid": 1080,
                        "name": 'Сенчанська',
                        "name_en": 'Senchanska',
                    },
                    {
                        "uid": 1081,
                        "name": 'Сергіївська',
                        "name_en": 'Serhiivska',
                    },
                    {
                        "uid": 1082,
                        "name": 'Шишацька',
                        "name_en": 'Shyshatska',
                    },
                ],
            },
            {
                "uid": 109,
                "name": 'Полтавський',
                "name_en": 'Poltavskyi',
                "hromadas": [
                    {
                        "uid": 1042,
                        "name": 'Білицька',
                        "name_en": 'Bilytska',
                    },
                    {
                        "uid": 1043,
                        "name": 'Великорублівська',
                        "name_en": 'Velykorublivska',
                    },
                    {
                        "uid": 1044,
                        "name": 'Диканьська',
                        "name_en": 'Dykanska',
                    },
                    {
                        "uid": 1045,
                        "name": 'Драбинівська',
                        "name_en": 'Drabynivska',
                    },
                    {
                        "uid": 1046,
                        "name": 'Зіньківська',
                        "name_en": 'Zinkivska',
                    },
                    {
                        "uid": 1047,
                        "name": 'Карлівська',
                        "name_en": 'Karlivska',
                    },
                    {
                        "uid": 1048,
                        "name": 'Кобеляцька',
                        "name_en": 'Kobeliatska',
                    },
                    {
                        "uid": 1049,
                        "name": 'Коломацька',
                        "name_en": 'Kolomatska',
                    },
                    {
                        "uid": 1050,
                        "name": 'Котелевська',
                        "name_en": 'Kotelevska',
                    },
                    {
                        "uid": 1051,
                        "name": 'Ланнівська',
                        "name_en": 'Lannivska',
                    },
                    {
                        "uid": 1052,
                        "name": 'Мартинівська',
                        "name_en": 'Martynivska',
                    },
                    {
                        "uid": 1053,
                        "name": 'Мачухівська',
                        "name_en": 'Machukhivska',
                    },
                    {
                        "uid": 1054,
                        "name": 'Машівська',
                        "name_en": 'Mashivska',
                    },
                    {
                        "uid": 1055,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska',
                    },
                    {
                        "uid": 1056,
                        "name": 'Нехворощанська',
                        "name_en": 'Nekhvoroshchanska',
                    },
                    {
                        "uid": 1057,
                        "name": 'Новосанжарська',
                        "name_en": 'Novosanzharska',
                    },
                    {
                        "uid": 1058,
                        "name": 'Новоселівська',
                        "name_en": 'Novoselivska',
                    },
                    {
                        "uid": 1059,
                        "name": 'Опішнянська',
                        "name_en": 'Opishnianska',
                    },
                    {
                        "uid": 1060,
                        "name": 'м. Полтава та Полтавська',
                        "name_en": 'Poltava and Poltavska',
                    },
                    {
                        "uid": 1061,
                        "name": 'Решетилівська',
                        "name_en": 'Reshetylivska',
                    },
                    {
                        "uid": 1062,
                        "name": 'Скороходівська',
                        "name_en": 'Skorokhodivska',
                    },
                    {
                        "uid": 1063,
                        "name": 'Терешківська',
                        "name_en": 'Tereshkivska',
                    },
                    {
                        "uid": 1064,
                        "name": 'Чутівська',
                        "name_en": 'Chutivska',
                    },
                    {
                        "uid": 1065,
                        "name": 'Щербанівська',
                        "name_en": 'Shcherbanivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 5,
        "name": 'Рівненська',
        "type": LocationType.OBLAST,
        "name_en": 'Rivnenska',
        "districts": [
            {
                "uid": 110,
                "name": 'Вараський',
                "name_en": 'Varaskyi',
                "hromadas": [
                    {
                        "uid": 1102,
                        "name": 'Антонівська',
                        "name_en": 'Antonivska',
                    },
                    {
                        "uid": 1103,
                        "name": 'м. Вараш та Вараська',
                        "name_en": 'Varash and Varaska',
                    },
                    {
                        "uid": 1104,
                        "name": 'Володимирецька',
                        "name_en": 'Volodymyretska',
                    },
                    {
                        "uid": 1105,
                        "name": 'Зарічненська',
                        "name_en": 'Zarichnenska',
                    },
                    {
                        "uid": 1106,
                        "name": 'Каноницька',
                        "name_en": 'Kanonytska',
                    },
                    {
                        "uid": 1107,
                        "name": 'Локницька',
                        "name_en": 'Loknytska',
                    },
                    {
                        "uid": 1108,
                        "name": 'Полицька',
                        "name_en": 'Polytska',
                    },
                    {
                        "uid": 1109,
                        "name": 'Рафалівська',
                        "name_en": 'Rafalivska',
                    },
                ],
            },
            {
                "uid": 111,
                "name": 'Дубенський',
                "name_en": 'Dubenskyi',
                "hromadas": [
                    {
                        "uid": 1147,
                        "name": 'Бокіймівська',
                        "name_en": 'Bokiimivska',
                    },
                    {
                        "uid": 1148,
                        "name": 'Боремельська',
                        "name_en": 'Boremelska',
                    },
                    {
                        "uid": 1149,
                        "name": 'Варковицька',
                        "name_en": 'Varkovytska',
                    },
                    {
                        "uid": 1150,
                        "name": 'Вербська',
                        "name_en": 'Verbska',
                    },
                    {
                        "uid": 1151,
                        "name": 'Демидівська',
                        "name_en": 'Demydivska',
                    },
                    {
                        "uid": 1152,
                        "name": 'м. Дубно та Дубенська',
                        "name_en": 'Dubno and Dubenska',
                    },
                    {
                        "uid": 1153,
                        "name": 'Козинська',
                        "name_en": 'Kozynska',
                    },
                    {
                        "uid": 1154,
                        "name": 'Крупецька',
                        "name_en": 'Krupetska',
                    },
                    {
                        "uid": 1155,
                        "name": 'Мирогощанська',
                        "name_en": 'Myrohoshchanska',
                    },
                    {
                        "uid": 1156,
                        "name": 'Млинівська',
                        "name_en": 'Mlynivska',
                    },
                    {
                        "uid": 1157,
                        "name": 'Острожецька',
                        "name_en": 'Ostrozhetska',
                    },
                    {
                        "uid": 1159,
                        "name": 'Повчанська',
                        "name_en": 'Povchanska',
                    },
                    {
                        "uid": 1160,
                        "name": 'Привільненська',
                        "name_en": 'Pryvilnenska',
                    },
                    {
                        "uid": 1158,
                        "name": 'Підлозцівська',
                        "name_en": 'Pidloztsivska',
                    },
                    {
                        "uid": 1161,
                        "name": 'Радивилівська',
                        "name_en": 'Radyvylivska',
                    },
                    {
                        "uid": 1162,
                        "name": 'Семидубська',
                        "name_en": 'Semydubska',
                    },
                    {
                        "uid": 1163,
                        "name": 'Смизька',
                        "name_en": 'Smyzka',
                    },
                    {
                        "uid": 1164,
                        "name": 'Тараканівська',
                        "name_en": 'Tarakanivska',
                    },
                    {
                        "uid": 1165,
                        "name": 'Ярославицька',
                        "name_en": 'Yaroslavytska',
                    },
                ],
            },
            {
                "uid": 112,
                "name": 'Рівненський',
                "name_en": 'Rivnenskyi',
                "hromadas": [
                    {
                        "uid": 1110,
                        "name": 'Бабинська',
                        "name_en": 'Babynska',
                    },
                    {
                        "uid": 1111,
                        "name": 'Березнівська',
                        "name_en": 'Bereznivska',
                    },
                    {
                        "uid": 1113,
                        "name": 'Бугринська',
                        "name_en": 'Buhrynska',
                    },
                    {
                        "uid": 1112,
                        "name": 'Білокриницька',
                        "name_en": 'Bilokrynytska',
                    },
                    {
                        "uid": 1114,
                        "name": 'Великомежиріцька',
                        "name_en": 'Velykomezhyritska',
                    },
                    {
                        "uid": 1115,
                        "name": 'Великоомелянська',
                        "name_en": 'Velykoomelianska',
                    },
                    {
                        "uid": 1116,
                        "name": 'Головинська',
                        "name_en": 'Holovynska',
                    },
                    {
                        "uid": 1117,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska',
                    },
                    {
                        "uid": 1118,
                        "name": 'Гощанська',
                        "name_en": 'Hoshchanska',
                    },
                    {
                        "uid": 1119,
                        "name": 'Деражненська',
                        "name_en": 'Derazhnenska',
                    },
                    {
                        "uid": 1120,
                        "name": 'Дядьковицька',
                        "name_en": 'Diadkovytska',
                    },
                    {
                        "uid": 1121,
                        "name": 'Здовбицька',
                        "name_en": 'Zdovbytska',
                    },
                    {
                        "uid": 1122,
                        "name": 'Здолбунівська',
                        "name_en": 'Zdolbunivska',
                    },
                    {
                        "uid": 1123,
                        "name": 'Зорянська',
                        "name_en": 'Zorianska',
                    },
                    {
                        "uid": 1124,
                        "name": 'Клеванська',
                        "name_en": 'Klevanska',
                    },
                    {
                        "uid": 1125,
                        "name": 'Корецька',
                        "name_en": 'Koretska',
                    },
                    {
                        "uid": 1126,
                        "name": 'Корнинська',
                        "name_en": 'Kornynska',
                    },
                    {
                        "uid": 1127,
                        "name": 'Костопільська',
                        "name_en": 'Kostopilska',
                    },
                    {
                        "uid": 1128,
                        "name": 'Малинська',
                        "name_en": 'Malynska',
                    },
                    {
                        "uid": 1129,
                        "name": 'Малолюбашанська',
                        "name_en": 'Maloliubashanska',
                    },
                    {
                        "uid": 1130,
                        "name": 'Мізоцька',
                        "name_en": 'Mizotska',
                    },
                    {
                        "uid": 1131,
                        "name": 'Олександрійська',
                        "name_en": 'Oleksandriiska',
                    },
                    {
                        "uid": 1132,
                        "name": 'м. Острог та Острозька',
                        "name_en": 'Ostroh and Ostrozka',
                    },
                    {
                        "uid": 1133,
                        "name": 'м. Рівне та Рівненська',
                        "name_en": 'Rivne and Rivnenska',
                    },
                    {
                        "uid": 1134,
                        "name": 'Соснівська',
                        "name_en": 'Sosnivska',
                    },
                    {
                        "uid": 1135,
                        "name": 'Шпанівська',
                        "name_en": 'Shpanivska',
                    },
                ],
            },
            {
                "uid": 113,
                "name": 'Сарненський',
                "name_en": 'Sarnenskyi',
                "hromadas": [
                    {
                        "uid": 1136,
                        "name": 'Березівська',
                        "name_en": 'Berezivska',
                    },
                    {
                        "uid": 1137,
                        "name": 'Вирівська',
                        "name_en": 'Vyrivska',
                    },
                    {
                        "uid": 1138,
                        "name": 'Висоцька',
                        "name_en": 'Vysotska',
                    },
                    {
                        "uid": 1139,
                        "name": 'Дубровицька',
                        "name_en": 'Dubrovytska',
                    },
                    {
                        "uid": 1140,
                        "name": 'Клесівська',
                        "name_en": 'Klesivska',
                    },
                    {
                        "uid": 1141,
                        "name": 'Миляцька',
                        "name_en": 'Myliatska',
                    },
                    {
                        "uid": 1142,
                        "name": 'Немовицька',
                        "name_en": 'Nemovytska',
                    },
                    {
                        "uid": 1143,
                        "name": 'Рокитнівська',
                        "name_en": 'Rokytnivska',
                    },
                    {
                        "uid": 1144,
                        "name": 'м. Сарни та Сарненська',
                        "name_en": 'Sarny and Sarnenska',
                    },
                    {
                        "uid": 1145,
                        "name": 'Старосільська',
                        "name_en": 'Starosilska',
                    },
                    {
                        "uid": 1146,
                        "name": 'Степанська',
                        "name_en": 'Stepanska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 20,
        "name": 'Сумська',
        "type": LocationType.OBLAST,
        "name_en": 'Sumska',
        "districts": [
            {
                "uid": 117,
                "name": 'Конотопський',
                "name_en": 'Konotopskyi',
                "hromadas": [
                    {
                        "uid": 1209,
                        "name": 'Бочечківська',
                        "name_en": 'Bochechkivska',
                    },
                    {
                        "uid": 1210,
                        "name": 'м. Буринь та Буринська',
                        "name_en": 'Buryn and Burynska',
                    },
                    {
                        "uid": 1211,
                        "name": 'Дубов’язівська',
                        "name_en": 'Dubovyazivska',
                    },
                    {
                        "uid": 1212,
                        "name": 'м. Конотоп та Конотопська',
                        "name_en": 'Konotop and Konotopska',
                    },
                    {
                        "uid": 1213,
                        "name": 'м. Кролевець та Кролевецька',
                        "name_en": 'Krolevets and Krolevetska',
                    },
                    {
                        "uid": 1214,
                        "name": 'Новослобідська',
                        "name_en": 'Novoslobidska',
                    },
                    {
                        "uid": 1215,
                        "name": 'Попівська',
                        "name_en": 'Popivska',
                    },
                    {
                        "uid": 1216,
                        "name": 'м. Путивль та Путивльська',
                        "name_en": 'Putyvl and Putyvlska',
                    },
                ],
            },
            {
                "uid": 118,
                "name": 'Охтирський',
                "name_en": 'Okhtyrskyi',
                "hromadas": [
                    {
                        "uid": 1200,
                        "name": 'Боромлянська',
                        "name_en": 'Boromlianska',
                    },
                    {
                        "uid": 1201,
                        "name": 'м. Велика Писарівка та Великописарівська',
                        "name_en": 'Velyka Pysarivka and Velykopysarivska',
                    },
                    {
                        "uid": 1202,
                        "name": 'Грунська',
                        "name_en": 'Hrunska',
                    },
                    {
                        "uid": 1203,
                        "name": 'Кириківська',
                        "name_en": 'Kyrykivska',
                    },
                    {
                        "uid": 1204,
                        "name": 'Комишанська',
                        "name_en": 'Komyshanska',
                    },
                    {
                        "uid": 1205,
                        "name": 'м. Охтирка та Охтирська',
                        "name_en": 'Okhtyrka and Okhtyrska',
                    },
                    {
                        "uid": 1206,
                        "name": 'м. Тростянець та Тростянецька',
                        "name_en": 'Trostianets and Trostianetska',
                    },
                    {
                        "uid": 1207,
                        "name": 'Чернеччинська',
                        "name_en": 'Chernechchynska',
                    },
                    {
                        "uid": 1208,
                        "name": 'Чупахівська',
                        "name_en": 'Chupakhivska',
                    },
                ],
            },
            {
                "uid": 116,
                "name": 'Роменський',
                "name_en": 'Romenskyi',
                "hromadas": [
                    {
                        "uid": 1166,
                        "name": 'Андріяшівська',
                        "name_en": 'Andriiashivska',
                    },
                    {
                        "uid": 1167,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska',
                    },
                    {
                        "uid": 1168,
                        "name": 'Коровинська',
                        "name_en": 'Korovynska',
                    },
                    {
                        "uid": 1169,
                        "name": 'м. Липова Долина та Липоводолинська',
                        "name_en": 'Lypova Dolyna and Lypovodolynska',
                    },
                    {
                        "uid": 1170,
                        "name": 'м. Недригайлів та Недригайлівська',
                        "name_en": 'Nedryhailiv and Nedryhailivska',
                    },
                    {
                        "uid": 1171,
                        "name": 'м. Ромни та Роменська',
                        "name_en": 'Romny and Romenska',
                    },
                    {
                        "uid": 1172,
                        "name": 'Синівська',
                        "name_en": 'Synivska',
                    },
                    {
                        "uid": 1173,
                        "name": 'Хмелівська',
                        "name_en": 'Khmelivska',
                    },
                ],
            },
            {
                "uid": 114,
                "name": 'Сумський',
                "name_en": 'Sumskyi',
                "hromadas": [
                    {
                        "uid": 1174,
                        "name": 'Бездрицька',
                        "name_en": 'Bezdrytska',
                    },
                    {
                        "uid": 1175,
                        "name": 'м. Білопілля та Білопільська',
                        "name_en": 'Bilopillia and Bilopilska',
                    },
                    {
                        "uid": 1176,
                        "name": 'Верхньосироватська',
                        "name_en": 'Verkhnosyrovatska',
                    },
                    {
                        "uid": 1177,
                        "name": 'Ворожбянська',
                        "name_en": 'Vorozhbianska',
                    },
                    {
                        "uid": 1178,
                        "name": 'м. Краснопілля та Краснопільська',
                        "name_en": 'Krasnopillia and Krasnopilska',
                    },
                    {
                        "uid": 1179,
                        "name": 'м. Лебедин та Лебединська',
                        "name_en": 'Lebedyn and Lebedynska',
                    },
                    {
                        "uid": 1181,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 1180,
                        "name": 'Миколаївська',
                        "name_en": 'Mykolaivska',
                    },
                    {
                        "uid": 1182,
                        "name": 'Миропільська',
                        "name_en": 'Myropilska',
                    },
                    {
                        "uid": 1183,
                        "name": 'Нижньосироватська',
                        "name_en": 'Nyzhnosyrovatska',
                    },
                    {
                        "uid": 1184,
                        "name": 'Річківська',
                        "name_en": 'Richkivska',
                    },
                    {
                        "uid": 1185,
                        "name": 'Садівська',
                        "name_en": 'Sadivska',
                    },
                    {
                        "uid": 1186,
                        "name": 'Степанівська',
                        "name_en": 'Stepanivska',
                    },
                    {
                        "uid": 1187,
                        "name": 'м. Суми та Сумська',
                        "name_en": 'Sumy and Sumska',
                    },
                    {
                        "uid": 1188,
                        "name": 'Хотінська',
                        "name_en": 'Khotinska',
                    },
                    {
                        "uid": 1189,
                        "name": 'Юнаківська',
                        "name_en": 'Yunakivska',
                    },
                ],
            },
            {
                "uid": 115,
                "name": 'Шосткинський',
                "name_en": 'Shostkynskyi',
                "hromadas": [
                    {
                        "uid": 1190,
                        "name": 'Березівська',
                        "name_en": 'Berezivska',
                    },
                    {
                        "uid": 1191,
                        "name": 'м. Глухів та Глухівська',
                        "name_en": 'Hlukhiv and Hlukhivska',
                    },
                    {
                        "uid": 1192,
                        "name": 'Дружбівська',
                        "name_en": 'Druzhbivska',
                    },
                    {
                        "uid": 1193,
                        "name": 'Есманьська',
                        "name_en": 'Esmanska',
                    },
                    {
                        "uid": 1194,
                        "name": 'Зноб-Новгородська',
                        "name_en": 'Znob-Novhorodska',
                    },
                    {
                        "uid": 1195,
                        "name": 'Свеська',
                        "name_en": 'Sveska',
                    },
                    {
                        "uid": 1196,
                        "name": 'м. Середина-Буда та Середино-Будська',
                        "name_en": 'Seredyna-Buda and Seredyno-Budska',
                    },
                    {
                        "uid": 1197,
                        "name": 'Шалигинська',
                        "name_en": 'Shalyhynska',
                    },
                    {
                        "uid": 1198,
                        "name": 'м. Шостка та Шосткинська',
                        "name_en": 'Shostka and Shostkynska',
                    },
                    {
                        "uid": 1199,
                        "name": 'м. Ямпіль та Ямпільська',
                        "name_en": 'Yampil and Yampilska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 21,
        "name": 'Тернопільська',
        "type": LocationType.OBLAST,
        "name_en": 'Ternopilska',
        "districts": [
            {
                "uid": 120,
                "name": 'Кременецький',
                "name_en": 'Kremenetskyi',
                "hromadas": [
                    {
                        "uid": 1264,
                        "name": 'Борсуківська',
                        "name_en": 'Borsukivska',
                    },
                    {
                        "uid": 1265,
                        "name": 'Великодедеркальська',
                        "name_en": 'Velykodederkalska',
                    },
                    {
                        "uid": 1266,
                        "name": 'Вишнівецька',
                        "name_en": 'Vyshnivetska',
                    },
                    {
                        "uid": 1267,
                        "name": 'м. Кременець та Кременецька',
                        "name_en": 'Kremenets and Kremenetska',
                    },
                    {
                        "uid": 1268,
                        "name": 'Лановецька',
                        "name_en": 'Lanovetska',
                    },
                    {
                        "uid": 1269,
                        "name": 'Лопушненська',
                        "name_en": 'Lopushnenska',
                    },
                    {
                        "uid": 1270,
                        "name": 'Почаївська',
                        "name_en": 'Pochaivska',
                    },
                    {
                        "uid": 1271,
                        "name": 'Шумська',
                        "name_en": 'Shumska',
                    },
                ],
            },
            {
                "uid": 119,
                "name": 'Тернопільський',
                "name_en": 'Ternopilskyi',
                "hromadas": [
                    {
                        "uid": 1217,
                        "name": 'Байковецька',
                        "name_en": 'Baikovetska',
                    },
                    {
                        "uid": 1218,
                        "name": 'м. Бережани та Бережанська',
                        "name_en": 'Berezhany and Berezhanska',
                    },
                    {
                        "uid": 1219,
                        "name": 'Білецька',
                        "name_en": 'Biletska',
                    },
                    {
                        "uid": 1220,
                        "name": 'Великоберезовицька',
                        "name_en": 'Velykoberezovytska',
                    },
                    {
                        "uid": 1221,
                        "name": 'Великобірківська',
                        "name_en": 'Velykobirkivska',
                    },
                    {
                        "uid": 1222,
                        "name": 'Великогаївська',
                        "name_en": 'Velykohaivska',
                    },
                    {
                        "uid": 1223,
                        "name": 'Залозецька',
                        "name_en": 'Zalozetska',
                    },
                    {
                        "uid": 1224,
                        "name": 'Збаразька',
                        "name_en": 'Zbarazka',
                    },
                    {
                        "uid": 1225,
                        "name": 'Зборівська',
                        "name_en": 'Zborivska',
                    },
                    {
                        "uid": 1226,
                        "name": 'Золотниківська',
                        "name_en": 'Zolotnykivska',
                    },
                    {
                        "uid": 1229,
                        "name": 'Козлівська',
                        "name_en": 'Kozlivska',
                    },
                    {
                        "uid": 1228,
                        "name": 'Козівська',
                        "name_en": 'Kozivska',
                    },
                    {
                        "uid": 1230,
                        "name": 'Купчинецька',
                        "name_en": 'Kupchynetska',
                    },
                    {
                        "uid": 1231,
                        "name": 'Микулинецька',
                        "name_en": 'Mykulynetska',
                    },
                    {
                        "uid": 1232,
                        "name": 'Нараївська',
                        "name_en": 'Naraivska',
                    },
                    {
                        "uid": 1233,
                        "name": 'Озернянська',
                        "name_en": 'Ozernianska',
                    },
                    {
                        "uid": 1234,
                        "name": 'Підволочиська',
                        "name_en": 'Pidvolochyska',
                    },
                    {
                        "uid": 1235,
                        "name": 'Підгаєцька',
                        "name_en": 'Pidhaietska',
                    },
                    {
                        "uid": 1236,
                        "name": 'Підгороднянська',
                        "name_en": 'Pidhorodnianska',
                    },
                    {
                        "uid": 1237,
                        "name": 'Саранчуківська',
                        "name_en": 'Saranchukivska',
                    },
                    {
                        "uid": 1238,
                        "name": 'Скалатська',
                        "name_en": 'Skalatska',
                    },
                    {
                        "uid": 1239,
                        "name": 'Скориківська',
                        "name_en": 'Skorykivska',
                    },
                    {
                        "uid": 1240,
                        "name": 'Теребовлянська',
                        "name_en": 'Terebovlianska',
                    },
                    {
                        "uid": 1241,
                        "name": 'м. Тернопіль та Тернопільська',
                        "name_en": 'Ternopil and Ternopilska',
                    },
                    {
                        "uid": 1227,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska',
                    },
                ],
            },
            {
                "uid": 121,
                "name": 'Чортківський',
                "name_en": 'Chortkivskyi',
                "hromadas": [
                    {
                        "uid": 1244,
                        "name": 'Борщівська',
                        "name_en": 'Borshchivska',
                    },
                    {
                        "uid": 1245,
                        "name": 'Бучацька',
                        "name_en": 'Buchatska',
                    },
                    {
                        "uid": 1242,
                        "name": 'Білобожницька',
                        "name_en": 'Bilobozhnytska',
                    },
                    {
                        "uid": 1243,
                        "name": 'Більче-Золотецька',
                        "name_en": 'Bilche-Zolotetska',
                    },
                    {
                        "uid": 1246,
                        "name": 'Васильковецька',
                        "name_en": 'Vasylkovetska',
                    },
                    {
                        "uid": 1247,
                        "name": 'Гримайлівська',
                        "name_en": 'Hrymailivska',
                    },
                    {
                        "uid": 1248,
                        "name": 'Гусятинська',
                        "name_en": 'Husiatynska',
                    },
                    {
                        "uid": 1249,
                        "name": 'Заводська',
                        "name_en": 'Zavodska',
                    },
                    {
                        "uid": 1250,
                        "name": 'Заліщицька',
                        "name_en": 'Zalishchytska',
                    },
                    {
                        "uid": 1251,
                        "name": 'Золотопотіцька',
                        "name_en": 'Zolotopotitska',
                    },
                    {
                        "uid": 1253,
                        "name": 'Колиндянська',
                        "name_en": 'Kolyndianska',
                    },
                    {
                        "uid": 1254,
                        "name": 'Копичинецька',
                        "name_en": 'Kopychynetska',
                    },
                    {
                        "uid": 1255,
                        "name": 'Коропецька',
                        "name_en": 'Koropetska',
                    },
                    {
                        "uid": 1256,
                        "name": 'Мельнице-Подільська',
                        "name_en": 'Melnytse-Podilska',
                    },
                    {
                        "uid": 1257,
                        "name": 'Монастириська',
                        "name_en": 'Monastyryska',
                    },
                    {
                        "uid": 1258,
                        "name": 'Нагірянська',
                        "name_en": 'Nahirianska',
                    },
                    {
                        "uid": 1259,
                        "name": 'Скала-Подільська',
                        "name_en": 'Skala-Podilska',
                    },
                    {
                        "uid": 1260,
                        "name": 'Товстенська',
                        "name_en": 'Tovstenska',
                    },
                    {
                        "uid": 1261,
                        "name": 'Трибухівська',
                        "name_en": 'Trybukhivska',
                    },
                    {
                        "uid": 1262,
                        "name": 'Хоростківська',
                        "name_en": 'Khorostkivska',
                    },
                    {
                        "uid": 1263,
                        "name": 'м. Чортків та Чортківська',
                        "name_en": 'Chortkiv and Chortkivska',
                    },
                    {
                        "uid": 1252,
                        "name": 'Іване-Пустенська',
                        "name_en": 'Ivane-Pustenska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 22,
        "name": 'Харківська',
        "type": LocationType.OBLAST,
        "name_en": 'Kharkivska',
        "districts": [
            {
                "uid": 127,
                "name": 'Берестинський',
                "name_en": 'Berestynskyi',
                "hromadas": [
                    {
                        "uid": 1324,
                        "name": 'Берестинська',
                        "name_en": 'Berestynska',
                    },
                    {
                        "uid": 1322,
                        "name": 'Зачепилівська',
                        "name_en": 'Zachepylivska',
                    },
                    {
                        "uid": 1323,
                        "name": 'Кегичівська',
                        "name_en": 'Kehychivska',
                    },
                    {
                        "uid": 1325,
                        "name": 'Наталинська',
                        "name_en": 'Natalynska',
                    },
                    {
                        "uid": 1326,
                        "name": 'Сахновщинська',
                        "name_en": 'Sakhnovshchynska',
                    },
                    {
                        "uid": 1327,
                        "name": 'Старовірівська',
                        "name_en": 'Starovirivska',
                    },
                ],
            },
            {
                "uid": 126,
                "name": 'Богодухівський',
                "name_en": 'Bohodukhivskyi',
                "hromadas": [
                    {
                        "uid": 1300,
                        "name": 'м. Богодухів та Богодухівська',
                        "name_en": 'Bohodukhiv and Bohodukhivska',
                    },
                    {
                        "uid": 1301,
                        "name": 'Валківська',
                        "name_en": 'Valkivska',
                    },
                    {
                        "uid": 1302,
                        "name": 'Золочівська',
                        "name_en": 'Zolochivska',
                    },
                    {
                        "uid": 1303,
                        "name": 'Коломацька',
                        "name_en": 'Kolomatska',
                    },
                    {
                        "uid": 1304,
                        "name": 'Краснокутська',
                        "name_en": 'Krasnokutska',
                    },
                ],
            },
            {
                "uid": 123,
                "name": "Куп'янський",
                "name_en": 'Kupianskyi',
                "hromadas": [
                    {
                        "uid": 1305,
                        "name": 'Великобурлуцька',
                        "name_en": 'Velykoburlutska',
                    },
                    {
                        "uid": 1306,
                        "name": 'Вільхуватська',
                        "name_en": 'Vilkhuvatska',
                    },
                    {
                        "uid": 1307,
                        "name": 'Дворічанська',
                        "name_en": 'Dvorichanska',
                    },
                    {
                        "uid": 1309,
                        "name": "м. Куп'янськ та Куп'янська",
                        "name_en": 'Kupiansk and Kupianska',
                    },
                    {
                        "uid": 1310,
                        "name": 'Курилівська',
                        "name_en": 'Kurylivska',
                    },
                    {
                        "uid": 1308,
                        "name": 'Кіндрашівська',
                        "name_en": 'Kindrashivska',
                    },
                    {
                        "uid": 1311,
                        "name": 'Петропавлівська',
                        "name_en": 'Petropavlivska',
                    },
                    {
                        "uid": 1312,
                        "name": 'Шевченківська',
                        "name_en": 'Shevchenkivska',
                    },
                ],
            },
            {
                "uid": 128,
                "name": 'Лозівський',
                "name_en": 'Lozivskyi',
                "hromadas": [
                    {
                        "uid": 1296,
                        "name": 'Близнюківська',
                        "name_en": 'Blyzniukivska',
                    },
                    {
                        "uid": 1295,
                        "name": 'Біляївська',
                        "name_en": 'Biliaivska',
                    },
                    {
                        "uid": 1299,
                        "name": 'м. Златопіль та Златопільська',
                        "name_en": 'Zlatopil and Zlatopilska',
                    },
                    {
                        "uid": 1297,
                        "name": 'м. Лозова та Лозівська',
                        "name_en": 'Lozova and Lozivska',
                    },
                    {
                        "uid": 1298,
                        "name": 'Олексіївська',
                        "name_en": 'Oleksiivska',
                    },
                ],
            },
            {
                "uid": 124,
                "name": 'Харківський',
                "name_en": 'Kharkivskyi',
                "hromadas": [
                    {
                        "uid": 1280,
                        "name": 'Безлюдівська',
                        "name_en": 'Bezliudivska',
                    },
                    {
                        "uid": 1281,
                        "name": 'Височанська',
                        "name_en": 'Vysochanska',
                    },
                    {
                        "uid": 1282,
                        "name": 'Вільхівська',
                        "name_en": 'Vilkhivska',
                    },
                    {
                        "uid": 1283,
                        "name": 'Дергачівська',
                        "name_en": 'Derhachivska',
                    },
                    {
                        "uid": 1284,
                        "name": 'Липецька',
                        "name_en": 'Lypetska',
                    },
                    {
                        "uid": 1285,
                        "name": 'м. Люботин та Люботинська',
                        "name_en": 'Liubotyn and Liubotynska',
                    },
                    {
                        "uid": 1286,
                        "name": 'Малоданилівська',
                        "name_en": 'Malodanylivska',
                    },
                    {
                        "uid": 1287,
                        "name": "Мереф'янська",
                        "name_en": 'Merefianska',
                    },
                    {
                        "uid": 1288,
                        "name": 'Нововодолазька',
                        "name_en": 'Novovodolazka',
                    },
                    {
                        "uid": 1289,
                        "name": 'Південноміська',
                        "name_en": 'Pivdennomiska',
                    },
                    {
                        "uid": 1290,
                        "name": 'Пісочинська',
                        "name_en": 'Pisochynska',
                    },
                    {
                        "uid": 1291,
                        "name": 'Роганська',
                        "name_en": 'Rohanska',
                    },
                    {
                        "uid": 1292,
                        "name": 'Солоницівська',
                        "name_en": 'Solonytsivska',
                    },
                    {
                        "uid": 1293,
                        "name": 'м. Харків та Харківська',
                        "name_en": 'Kharkiv and Kharkivska',
                    },
                    {
                        "uid": 1294,
                        "name": 'Циркунівська',
                        "name_en": 'Tsyrkunivska',
                    },
                ],
            },
            {
                "uid": 122,
                "name": 'Чугуївський',
                "name_en": 'Chuhuivskyi',
                "hromadas": [
                    {
                        "uid": 1313,
                        "name": 'Вовчанська',
                        "name_en": 'Vovchanska',
                    },
                    {
                        "uid": 1314,
                        "name": 'Зміївська',
                        "name_en": 'Zmiivska',
                    },
                    {
                        "uid": 1315,
                        "name": 'Малинівська',
                        "name_en": 'Malynivska',
                    },
                    {
                        "uid": 1316,
                        "name": 'Новопокровська',
                        "name_en": 'Novopokrovska',
                    },
                    {
                        "uid": 1317,
                        "name": 'Печенізька',
                        "name_en": 'Pechenizka',
                    },
                    {
                        "uid": 1318,
                        "name": 'Слобожанська',
                        "name_en": 'Slobozhanska',
                    },
                    {
                        "uid": 1319,
                        "name": 'Старосалтівська',
                        "name_en": 'Starosaltivska',
                    },
                    {
                        "uid": 1320,
                        "name": 'Чкаловська',
                        "name_en": 'Chkalovska',
                    },
                    {
                        "uid": 1321,
                        "name": 'м. Чугуїв та Чугуївська',
                        "name_en": 'Chuhuiv and Chuhuivska',
                    },
                ],
            },
            {
                "uid": 125,
                "name": 'Ізюмський',
                "name_en": 'Iziumskyi',
                "hromadas": [
                    {
                        "uid": 1272,
                        "name": 'Балаклійська',
                        "name_en": 'Balakliiska',
                    },
                    {
                        "uid": 1273,
                        "name": 'Барвінківська',
                        "name_en": 'Barvinkivska',
                    },
                    {
                        "uid": 1274,
                        "name": 'Борівська',
                        "name_en": 'Borivska',
                    },
                    {
                        "uid": 1275,
                        "name": 'Донецька',
                        "name_en": 'Donetska',
                    },
                    {
                        "uid": 1277,
                        "name": 'Куньєвська',
                        "name_en": 'Kunievska',
                    },
                    {
                        "uid": 1278,
                        "name": 'Оскільська',
                        "name_en": 'Oskilska',
                    },
                    {
                        "uid": 1279,
                        "name": 'Савинська',
                        "name_en": 'Savynska',
                    },
                    {
                        "uid": 1276,
                        "name": 'м. Ізюм та Ізюмська',
                        "name_en": 'Izium and Iziumska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 23,
        "name": 'Херсонська',
        "type": LocationType.OBLAST,
        "name_en": 'Khersonska',
        "districts": [
            {
                "uid": 129,
                "name": 'Бериславський',
                "name_en": 'Beryslavskyi',
                "hromadas": [
                    {
                        "uid": 1343,
                        "name": 'Бериславська',
                        "name_en": 'Beryslavska',
                    },
                    {
                        "uid": 1344,
                        "name": 'Борозенська',
                        "name_en": 'Borozenska',
                    },
                    {
                        "uid": 1345,
                        "name": 'Великоолександрівська',
                        "name_en": 'Velykooleksandrivska',
                    },
                    {
                        "uid": 1346,
                        "name": 'Високопільська',
                        "name_en": 'Vysokopilska',
                    },
                    {
                        "uid": 1347,
                        "name": 'Калинівська',
                        "name_en": 'Kalynivska',
                    },
                    {
                        "uid": 1348,
                        "name": 'Кочубеївська',
                        "name_en": 'Kochubeivska',
                    },
                    {
                        "uid": 1349,
                        "name": 'Милівська',
                        "name_en": 'Mylivska',
                    },
                    {
                        "uid": 1350,
                        "name": 'Нововоронцовська',
                        "name_en": 'Novovorontsovska',
                    },
                    {
                        "uid": 1351,
                        "name": 'Новоолександрівська',
                        "name_en": 'Novooleksandrivska',
                    },
                    {
                        "uid": 1352,
                        "name": 'Новорайська',
                        "name_en": 'Novoraiska',
                    },
                    {
                        "uid": 1353,
                        "name": 'Тягинська',
                        "name_en": 'Tiahynska',
                    },
                ],
            },
            {
                "uid": 133,
                "name": 'Генічеський',
                "name_en": 'Henicheskyi',
                "hromadas": [
                    {
                        "uid": 1373,
                        "name": 'Генічеська',
                        "name_en": 'Henicheska',
                    },
                    {
                        "uid": 1375,
                        "name": 'Нижньосірогозька',
                        "name_en": 'Nyzhnosirohozka',
                    },
                    {
                        "uid": 1376,
                        "name": 'Новотроїцька',
                        "name_en": 'Novotroitska',
                    },
                    {
                        "uid": 1374,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska',
                    },
                ],
            },
            {
                "uid": 131,
                "name": 'Каховський',
                "name_en": 'Kakhovskyi',
                "hromadas": [
                    {
                        "uid": 1328,
                        "name": 'Асканія-Нова',
                        "name_en": 'Askaniia-Nova',
                    },
                    {
                        "uid": 1329,
                        "name": 'Великолепетиська',
                        "name_en": 'Velykolepetyska',
                    },
                    {
                        "uid": 1330,
                        "name": 'Верхньорогачицька',
                        "name_en": 'Verkhnorohachytska',
                    },
                    {
                        "uid": 1331,
                        "name": 'Горностаївська',
                        "name_en": 'Hornostaivska',
                    },
                    {
                        "uid": 1332,
                        "name": 'Зеленопідська',
                        "name_en": 'Zelenopidska',
                    },
                    {
                        "uid": 1333,
                        "name": 'м. Каховка та Каховська',
                        "name_en": 'Kakhovka and Kakhovska',
                    },
                    {
                        "uid": 1334,
                        "name": 'Костянтинівська',
                        "name_en": 'Kostiantynivska',
                    },
                    {
                        "uid": 1335,
                        "name": 'Любимівська',
                        "name_en": 'Liubymivska',
                    },
                    {
                        "uid": 1336,
                        "name": 'м. Нова Каховка та Новокаховська',
                        "name_en": 'Nova Kakhovka and Novokakhovska',
                    },
                    {
                        "uid": 1337,
                        "name": 'Присиваська',
                        "name_en": 'Prysyvaska',
                    },
                    {
                        "uid": 1338,
                        "name": 'Рубанівська',
                        "name_en": 'Rubanivska',
                    },
                    {
                        "uid": 1339,
                        "name": 'Тавричанська',
                        "name_en": 'Tavrychanska',
                    },
                    {
                        "uid": 1340,
                        "name": 'Таврійська',
                        "name_en": 'Tavriiska',
                    },
                    {
                        "uid": 1341,
                        "name": 'Хрестівська',
                        "name_en": 'Khrestivska',
                    },
                    {
                        "uid": 1342,
                        "name": 'Чаплинська',
                        "name_en": 'Chaplynska',
                    },
                ],
            },
            {
                "uid": 130,
                "name": 'Скадовський',
                "name_en": 'Skadovskyi',
                "hromadas": [
                    {
                        "uid": 1354,
                        "name": 'Бехтерська',
                        "name_en": 'Bekhterska',
                    },
                    {
                        "uid": 1355,
                        "name": 'м. Гола Пристань та Голопристанська',
                        "name_en": 'Hola Prystan and Holoprystanska',
                    },
                    {
                        "uid": 1356,
                        "name": 'Долматівська',
                        "name_en": 'Dolmativska',
                    },
                    {
                        "uid": 1357,
                        "name": 'Каланчацька',
                        "name_en": 'Kalanchatska',
                    },
                    {
                        "uid": 1358,
                        "name": 'Лазурненська',
                        "name_en": 'Lazurnenska',
                    },
                    {
                        "uid": 1359,
                        "name": 'Мирненська',
                        "name_en": 'Myrnenska',
                    },
                    {
                        "uid": 1360,
                        "name": 'Новомиколаївська',
                        "name_en": 'Novomykolaivska',
                    },
                    {
                        "uid": 1361,
                        "name": 'Скадовська',
                        "name_en": 'Skadovska',
                    },
                    {
                        "uid": 1362,
                        "name": 'Чулаківська',
                        "name_en": 'Chulakivska',
                    },
                ],
            },
            {
                "uid": 132,
                "name": 'Херсонський',
                "name_en": 'Khersonskyi',
                "hromadas": [
                    {
                        "uid": 1363,
                        "name": 'Білозерська',
                        "name_en": 'Bilozerska',
                    },
                    {
                        "uid": 1364,
                        "name": 'Великокопанівська',
                        "name_en": 'Velykokopanivska',
                    },
                    {
                        "uid": 1365,
                        "name": 'Виноградівська',
                        "name_en": 'Vynohradivska',
                    },
                    {
                        "uid": 1366,
                        "name": 'Дар’ївська',
                        "name_en": 'Daryivska',
                    },
                    {
                        "uid": 1367,
                        "name": 'Музиківська',
                        "name_en": 'Muzykivska',
                    },
                    {
                        "uid": 1368,
                        "name": 'Олешківська',
                        "name_en": 'Oleshkivska',
                    },
                    {
                        "uid": 1369,
                        "name": 'Станіславська',
                        "name_en": 'Stanislavska',
                    },
                    {
                        "uid": 1370,
                        "name": 'м. Херсон та Херсонська',
                        "name_en": 'Kherson and Khersonska',
                    },
                    {
                        "uid": 1371,
                        "name": 'Чорнобаївська',
                        "name_en": 'Chornobaivska',
                    },
                    {
                        "uid": 1372,
                        "name": 'Ювілейна',
                        "name_en": 'Yuvileina',
                    },
                ],
            },
        ],
    },
    {
        "uid": 3,
        "name": 'Хмельницька',
        "type": LocationType.OBLAST,
        "name_en": 'Khmelnytska',
        "districts": [
            {
                "uid": 135,
                "name": "Кам'янець-Подільський",
                "name_en": 'Kamianets-Podilskyi',
                "hromadas": [
                    {
                        "uid": 1422,
                        "name": 'Гуківська',
                        "name_en": 'Hukivska',
                    },
                    {
                        "uid": 1423,
                        "name": 'Гуменецька',
                        "name_en": 'Humenetska',
                    },
                    {
                        "uid": 1424,
                        "name": 'Дунаєвецька',
                        "name_en": 'Dunaievetska',
                    },
                    {
                        "uid": 1425,
                        "name": 'Жванецька',
                        "name_en": 'Zhvanetska',
                    },
                    {
                        "uid": 1426,
                        "name": 'Закупненська',
                        "name_en": 'Zakupnenska',
                    },
                    {
                        "uid": 1427,
                        "name": "м. Кам'янець-Подільський та Кам'янець-Подільська",
                        "name_en": 'Kamianets-Podilskyi and Kamianets-Podilska',
                    },
                    {
                        "uid": 1428,
                        "name": 'Китайгородська',
                        "name_en": 'Kytaihorodska',
                    },
                    {
                        "uid": 1429,
                        "name": 'Маківська',
                        "name_en": 'Makivska',
                    },
                    {
                        "uid": 1430,
                        "name": 'Новодунаєвецька',
                        "name_en": 'Novodunaievetska',
                    },
                    {
                        "uid": 1431,
                        "name": 'Новоушицька',
                        "name_en": 'Novoushytska',
                    },
                    {
                        "uid": 1432,
                        "name": 'Орининська',
                        "name_en": 'Orynynska',
                    },
                    {
                        "uid": 1433,
                        "name": 'Слобідсько-Кульчієвецьк',
                        "name_en": 'Slobidsko-Kulchiievetsk',
                    },
                    {
                        "uid": 1434,
                        "name": 'Смотрицька',
                        "name_en": 'Smotrytska',
                    },
                    {
                        "uid": 1435,
                        "name": 'Староушицька',
                        "name_en": 'Staroushytska',
                    },
                    {
                        "uid": 1436,
                        "name": 'Чемеровецька',
                        "name_en": 'Chemerovetska',
                    },
                ],
            },
            {
                "uid": 134,
                "name": 'Хмельницький',
                "name_en": 'Khmelnytskyi',
                "hromadas": [
                    {
                        "uid": 1377,
                        "name": 'Антонінська',
                        "name_en": 'Antoninska',
                    },
                    {
                        "uid": 1380,
                        "name": 'Вовковинецька',
                        "name_en": 'Vovkovynetska',
                    },
                    {
                        "uid": 1381,
                        "name": 'Волочиська',
                        "name_en": 'Volochyska',
                    },
                    {
                        "uid": 1378,
                        "name": 'Війтовецька',
                        "name_en": 'Viitovetska',
                    },
                    {
                        "uid": 1379,
                        "name": 'Віньковецька',
                        "name_en": 'Vinkovetska',
                    },
                    {
                        "uid": 1382,
                        "name": 'Гвардійська',
                        "name_en": 'Hvardiiska',
                    },
                    {
                        "uid": 1383,
                        "name": 'Городоцька',
                        "name_en": 'Horodotska',
                    },
                    {
                        "uid": 1384,
                        "name": 'Деражнянська',
                        "name_en": 'Derazhnianska',
                    },
                    {
                        "uid": 1385,
                        "name": 'Заслучненська',
                        "name_en": 'Zasluchnenska',
                    },
                    {
                        "uid": 1386,
                        "name": 'Зіньківська',
                        "name_en": 'Zinkivska',
                    },
                    {
                        "uid": 1387,
                        "name": 'Красилівська',
                        "name_en": 'Krasylivska',
                    },
                    {
                        "uid": 1388,
                        "name": 'Летичівська',
                        "name_en": 'Letychivska',
                    },
                    {
                        "uid": 1389,
                        "name": 'Лісовогринівецька',
                        "name_en": 'Lisovohrynivetska',
                    },
                    {
                        "uid": 1390,
                        "name": 'Меджибізька',
                        "name_en": 'Medzhybizka',
                    },
                    {
                        "uid": 1391,
                        "name": 'Миролюбненська',
                        "name_en": 'Myroliubnenska',
                    },
                    {
                        "uid": 1392,
                        "name": 'Наркевицька',
                        "name_en": 'Narkevytska',
                    },
                    {
                        "uid": 1393,
                        "name": 'Розсошанська',
                        "name_en": 'Rozsoshanska',
                    },
                    {
                        "uid": 1394,
                        "name": 'Сатанівська',
                        "name_en": 'Satanivska',
                    },
                    {
                        "uid": 1395,
                        "name": 'Солобковецька',
                        "name_en": 'Solobkovetska',
                    },
                    {
                        "uid": 1396,
                        "name": 'м. Старокостянтинів та Старокостянтинівська',
                        "name_en": 'Starokostiantyniv and Starokostiantynivska',
                    },
                    {
                        "uid": 1397,
                        "name": 'Староостропільська',
                        "name_en": 'Staroostropilska',
                    },
                    {
                        "uid": 1398,
                        "name": 'Старосинявська',
                        "name_en": 'Starosyniavska',
                    },
                    {
                        "uid": 1399,
                        "name": 'Теофіпольська',
                        "name_en": 'Teofipolska',
                    },
                    {
                        "uid": 1400,
                        "name": 'м. Хмельницький та Хмельницька',
                        "name_en": 'Khmelnytskyi and Khmelnytska',
                    },
                    {
                        "uid": 1401,
                        "name": 'Чорноострівська',
                        "name_en": 'Chornoostrivska',
                    },
                    {
                        "uid": 1402,
                        "name": 'Щиборівська',
                        "name_en": 'Shchyborivska',
                    },
                    {
                        "uid": 1403,
                        "name": 'Ярмолинецька',
                        "name_en": 'Yarmolynetska',
                    },
                ],
            },
            {
                "uid": 136,
                "name": 'Шепетівський',
                "name_en": 'Shepetivskyi',
                "hromadas": [
                    {
                        "uid": 1404,
                        "name": 'Берездівська',
                        "name_en": 'Berezdivska',
                    },
                    {
                        "uid": 1405,
                        "name": 'Білогірська',
                        "name_en": 'Bilohirska',
                    },
                    {
                        "uid": 1406,
                        "name": 'Ганнопільська',
                        "name_en": 'Hannopilska',
                    },
                    {
                        "uid": 1407,
                        "name": 'Грицівська',
                        "name_en": 'Hrytsivska',
                    },
                    {
                        "uid": 1409,
                        "name": 'Крупецька',
                        "name_en": 'Krupetska',
                    },
                    {
                        "uid": 1410,
                        "name": 'Ленковецька',
                        "name_en": 'Lenkovetska',
                    },
                    {
                        "uid": 1411,
                        "name": 'Михайлюцька',
                        "name_en": 'Mykhailiutska',
                    },
                    {
                        "uid": 1412,
                        "name": 'м. Нетішин та Нетішинська',
                        "name_en": 'Netishyn and Netishynska',
                    },
                    {
                        "uid": 1413,
                        "name": 'Плужненська',
                        "name_en": 'Pluzhnenska',
                    },
                    {
                        "uid": 1414,
                        "name": 'Полонська',
                        "name_en": 'Polonska',
                    },
                    {
                        "uid": 1415,
                        "name": 'Понінківська',
                        "name_en": 'Poninkivska',
                    },
                    {
                        "uid": 1416,
                        "name": 'Сахновецька',
                        "name_en": 'Sakhnovetska',
                    },
                    {
                        "uid": 1417,
                        "name": 'м. Славута та Славутська',
                        "name_en": 'Slavuta and Slavutska',
                    },
                    {
                        "uid": 1418,
                        "name": 'Судилківська',
                        "name_en": 'Sudylkivska',
                    },
                    {
                        "uid": 1419,
                        "name": 'Улашанівська',
                        "name_en": 'Ulashanivska',
                    },
                    {
                        "uid": 1420,
                        "name": 'м. Шепетівка та Шепетівська',
                        "name_en": 'Shepetivka and Shepetivska',
                    },
                    {
                        "uid": 1421,
                        "name": 'Ямпільська',
                        "name_en": 'Yampilska',
                    },
                    {
                        "uid": 1408,
                        "name": 'Ізяславська',
                        "name_en": 'Iziaslavska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 24,
        "name": 'Черкаська',
        "type": LocationType.OBLAST,
        "name_en": 'Cherkaska',
        "districts": [
            {
                "uid": 150,
                "name": 'Звенигородський',
                "name_en": 'Zvenyhorodskyi',
                "hromadas": [
                    {
                        "uid": 1475,
                        "name": 'Бужанська',
                        "name_en": 'Buzhanska',
                    },
                    {
                        "uid": 1476,
                        "name": 'м. Ватутіне та Ватутінська',
                        "name_en": 'Vatutine and Vatutinska',
                    },
                    {
                        "uid": 1477,
                        "name": 'Виноградська',
                        "name_en": 'Vynohradska',
                    },
                    {
                        "uid": 1479,
                        "name": 'Водяницька',
                        "name_en": 'Vodianytska',
                    },
                    {
                        "uid": 1478,
                        "name": 'Вільшанська',
                        "name_en": 'Vilshanska',
                    },
                    {
                        "uid": 1481,
                        "name": 'Звенигородська',
                        "name_en": 'Zvenyhorodska',
                    },
                    {
                        "uid": 1482,
                        "name": 'Катеринопільська',
                        "name_en": 'Katerynopilska',
                    },
                    {
                        "uid": 1483,
                        "name": "Лип'янська",
                        "name_en": 'Lypianska',
                    },
                    {
                        "uid": 1484,
                        "name": 'Лисянська',
                        "name_en": 'Lysianska',
                    },
                    {
                        "uid": 1485,
                        "name": 'Матусівська',
                        "name_en": 'Matusivska',
                    },
                    {
                        "uid": 1486,
                        "name": 'Мокрокалигірська',
                        "name_en": 'Mokrokalyhirska',
                    },
                    {
                        "uid": 1487,
                        "name": 'Селищенська',
                        "name_en": 'Selyshchenska',
                    },
                    {
                        "uid": 1488,
                        "name": 'Стеблівська',
                        "name_en": 'Steblivska',
                    },
                    {
                        "uid": 1489,
                        "name": 'м. Тальне та Тальнівська',
                        "name_en": 'Talne and Talnivska',
                    },
                    {
                        "uid": 1490,
                        "name": 'Шевченківська',
                        "name_en": 'Shevchenkivska',
                    },
                    {
                        "uid": 1491,
                        "name": 'м. Шпола та Шполянська',
                        "name_en": 'Shpola and Shpolianska',
                    },
                    {
                        "uid": 1480,
                        "name": 'Єрківська',
                        "name_en": 'Yerkivska',
                    },
                ],
            },
            {
                "uid": 153,
                "name": 'Золотоніський',
                "name_en": 'Zolotoniskyi',
                "hromadas": [
                    {
                        "uid": 1492,
                        "name": 'Великохутірська',
                        "name_en": 'Velykokhutirska',
                    },
                    {
                        "uid": 1493,
                        "name": 'Вознесенська',
                        "name_en": 'Voznesenska',
                    },
                    {
                        "uid": 1494,
                        "name": 'Гельмязівська',
                        "name_en": 'Helmiazivska',
                    },
                    {
                        "uid": 1495,
                        "name": 'Драбівська',
                        "name_en": 'Drabivska',
                    },
                    {
                        "uid": 1496,
                        "name": 'Золотоніська',
                        "name_en": 'Zolotoniska',
                    },
                    {
                        "uid": 1497,
                        "name": 'Зорівська',
                        "name_en": 'Zorivska',
                    },
                    {
                        "uid": 1499,
                        "name": 'Новодмитрівська',
                        "name_en": 'Novodmytrivska',
                    },
                    {
                        "uid": 1500,
                        "name": 'Піщанська',
                        "name_en": 'Pishchanska',
                    },
                    {
                        "uid": 1501,
                        "name": 'Чорнобаївська',
                        "name_en": 'Chornobaivska',
                    },
                    {
                        "uid": 1502,
                        "name": 'Шрамківська',
                        "name_en": 'Shramkivska',
                    },
                    {
                        "uid": 1498,
                        "name": 'Іркліївська',
                        "name_en": 'Irkliivska',
                    },
                ],
            },
            {
                "uid": 151,
                "name": 'Уманський',
                "name_en": 'Umanskyi',
                "hromadas": [
                    {
                        "uid": 1437,
                        "name": 'Бабанська',
                        "name_en": 'Babanska',
                    },
                    {
                        "uid": 1438,
                        "name": 'Баштечківська',
                        "name_en": 'Bashtechkivska',
                    },
                    {
                        "uid": 1439,
                        "name": 'Буцька',
                        "name_en": 'Butska',
                    },
                    {
                        "uid": 1440,
                        "name": 'Дмитрушківська',
                        "name_en": 'Dmytrushkivska',
                    },
                    {
                        "uid": 1441,
                        "name": 'Жашківська',
                        "name_en": 'Zhashkivska',
                    },
                    {
                        "uid": 1443,
                        "name": 'Ладижинська',
                        "name_en": 'Ladyzhynska',
                    },
                    {
                        "uid": 1444,
                        "name": 'Маньківська',
                        "name_en": 'Mankivska',
                    },
                    {
                        "uid": 1445,
                        "name": 'м. Монастирище та Монастрищенська',
                        "name_en": 'Monastyryshche and Monastryshchenska',
                    },
                    {
                        "uid": 1446,
                        "name": 'Паланська',
                        "name_en": 'Palanska',
                    },
                    {
                        "uid": 1447,
                        "name": 'Уманська',
                        "name_en": 'Umanska',
                    },
                    {
                        "uid": 1448,
                        "name": 'м. Христинівка та Христинівська',
                        "name_en": 'Khrystynivka and Khrystynivska',
                    },
                    {
                        "uid": 1442,
                        "name": 'Іваньківська',
                        "name_en": 'Ivankivska',
                    },
                ],
            },
            {
                "uid": 152,
                "name": 'Черкаський',
                "name_en": 'Cherkaskyi',
                "hromadas": [
                    {
                        "uid": 1449,
                        "name": 'Балаклеївська',
                        "name_en": 'Balakleivska',
                    },
                    {
                        "uid": 1450,
                        "name": 'Березняківська',
                        "name_en": 'Berezniakivska',
                    },
                    {
                        "uid": 1452,
                        "name": 'Бобрицька',
                        "name_en": 'Bobrytska',
                    },
                    {
                        "uid": 1453,
                        "name": 'Будищенська',
                        "name_en": 'Budyshchenska',
                    },
                    {
                        "uid": 1451,
                        "name": 'Білозірська',
                        "name_en": 'Bilozirska',
                    },
                    {
                        "uid": 1454,
                        "name": 'Городищенська',
                        "name_en": 'Horodyshchenska',
                    },
                    {
                        "uid": 1455,
                        "name": 'Кам’янська',
                        "name_en": 'Kamyanska',
                    },
                    {
                        "uid": 1456,
                        "name": 'Канівська',
                        "name_en": 'Kanivska',
                    },
                    {
                        "uid": 1457,
                        "name": 'м. Корсунь-Шевченківський та Корсунь-Шевченківська',
                        "name_en": 'Korsun-Shevchenkivskyi and Korsun-Shevchenkivska',
                    },
                    {
                        "uid": 1458,
                        "name": 'Леськівська',
                        "name_en": 'Leskivska',
                    },
                    {
                        "uid": 1459,
                        "name": 'Ліплявська',
                        "name_en": 'Lipliavska',
                    },
                    {
                        "uid": 1460,
                        "name": 'Медведівська',
                        "name_en": 'Medvedivska',
                    },
                    {
                        "uid": 1461,
                        "name": 'Михайлівська',
                        "name_en": 'Mykhailivska',
                    },
                    {
                        "uid": 1462,
                        "name": 'Мліївська',
                        "name_en": 'Mliivska',
                    },
                    {
                        "uid": 1463,
                        "name": 'Мошнівська',
                        "name_en": 'Moshnivska',
                    },
                    {
                        "uid": 1464,
                        "name": 'Набутівська',
                        "name_en": 'Nabutivska',
                    },
                    {
                        "uid": 1465,
                        "name": 'Ротмістрівська',
                        "name_en": 'Rotmistrivska',
                    },
                    {
                        "uid": 1466,
                        "name": 'Русько-Полянська',
                        "name_en": 'Rusko-Polianska',
                    },
                    {
                        "uid": 1467,
                        "name": 'Сагунівська',
                        "name_en": 'Sahunivska',
                    },
                    {
                        "uid": 1468,
                        "name": 'Смілянська',
                        "name_en": 'Smilianska',
                    },
                    {
                        "uid": 1469,
                        "name": 'Степанецька',
                        "name_en": 'Stepanetska',
                    },
                    {
                        "uid": 1470,
                        "name": 'Степанківська',
                        "name_en": 'Stepankivska',
                    },
                    {
                        "uid": 1471,
                        "name": 'Тернівська',
                        "name_en": 'Ternivska',
                    },
                    {
                        "uid": 1472,
                        "name": 'Червонослобідська',
                        "name_en": 'Chervonoslobidska',
                    },
                    {
                        "uid": 1473,
                        "name": 'м. Черкаси та Черкаська',
                        "name_en": 'Cherkasy and Cherkaska',
                    },
                    {
                        "uid": 1474,
                        "name": 'м. Чигирин та Чигиринська',
                        "name_en": 'Chyhyryn and Chyhyrynska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 26,
        "name": 'Чернівецька',
        "type": LocationType.OBLAST,
        "name_en": 'Chernivetska',
        "districts": [
            {
                "uid": 138,
                "name": 'Вижницький',
                "name_en": 'Vyzhnytskyi',
                "hromadas": [
                    {
                        "uid": 1503,
                        "name": 'Банилівська',
                        "name_en": 'Banylivska',
                    },
                    {
                        "uid": 1504,
                        "name": 'Берегометська',
                        "name_en": 'Berehometska',
                    },
                    {
                        "uid": 1505,
                        "name": 'Брусницька',
                        "name_en": 'Brusnytska',
                    },
                    {
                        "uid": 1506,
                        "name": 'Вашківецька',
                        "name_en": 'Vashkivetska',
                    },
                    {
                        "uid": 1507,
                        "name": 'Вижницька',
                        "name_en": 'Vyzhnytska',
                    },
                    {
                        "uid": 1508,
                        "name": 'Конятинська',
                        "name_en": 'Koniatynska',
                    },
                    {
                        "uid": 1509,
                        "name": 'Путильська',
                        "name_en": 'Putylska',
                    },
                    {
                        "uid": 1510,
                        "name": 'Селятинська',
                        "name_en": 'Seliatynska',
                    },
                    {
                        "uid": 1511,
                        "name": 'Усть-Путильська',
                        "name_en": 'Ust-Putylska',
                    },
                ],
            },
            {
                "uid": 139,
                "name": 'Дністровський',
                "name_en": 'Dnistrovskyi',
                "hromadas": [
                    {
                        "uid": 1545,
                        "name": 'Вашковецька',
                        "name_en": 'Vashkovetska',
                    },
                    {
                        "uid": 1546,
                        "name": 'Кельменецька',
                        "name_en": 'Kelmenetska',
                    },
                    {
                        "uid": 1547,
                        "name": 'Клішковецька',
                        "name_en": 'Klishkovetska',
                    },
                    {
                        "uid": 1548,
                        "name": 'Лівинецька',
                        "name_en": 'Livynetska',
                    },
                    {
                        "uid": 1549,
                        "name": 'Мамалигівська',
                        "name_en": 'Mamalyhivska',
                    },
                    {
                        "uid": 1550,
                        "name": 'Недобоївська',
                        "name_en": 'Nedoboivska',
                    },
                    {
                        "uid": 1551,
                        "name": 'м. Новодністровськ та Новодністровська',
                        "name_en": 'Novodnistrovsk and Novodnistrovska',
                    },
                    {
                        "uid": 1552,
                        "name": 'Рукшинська',
                        "name_en": 'Rukshynska',
                    },
                    {
                        "uid": 1553,
                        "name": 'Сокирянська',
                        "name_en": 'Sokyrianska',
                    },
                    {
                        "uid": 1554,
                        "name": 'Хотинська',
                        "name_en": 'Khotynska',
                    },
                ],
            },
            {
                "uid": 137,
                "name": 'Чернівецький',
                "name_en": 'Chernivetskyi',
                "hromadas": [
                    {
                        "uid": 1512,
                        "name": 'Боянська',
                        "name_en": 'Boianska',
                    },
                    {
                        "uid": 1513,
                        "name": 'Ванчиковецька',
                        "name_en": 'Vanchykovetska',
                    },
                    {
                        "uid": 1514,
                        "name": 'Великокучурівська',
                        "name_en": 'Velykokuchurivska',
                    },
                    {
                        "uid": 1515,
                        "name": 'Веренчацька',
                        "name_en": 'Verenchatska',
                    },
                    {
                        "uid": 1517,
                        "name": 'Волоківська',
                        "name_en": 'Volokivska',
                    },
                    {
                        "uid": 1516,
                        "name": 'Вікнянська',
                        "name_en": 'Viknianska',
                    },
                    {
                        "uid": 1518,
                        "name": 'Герцаївська',
                        "name_en": 'Hertsaivska',
                    },
                    {
                        "uid": 1519,
                        "name": 'Глибоцька',
                        "name_en": 'Hlybotska',
                    },
                    {
                        "uid": 1520,
                        "name": 'Горішньошеровецька',
                        "name_en": 'Horishnosherovetska',
                    },
                    {
                        "uid": 1521,
                        "name": 'Заставнівська',
                        "name_en": 'Zastavnivska',
                    },
                    {
                        "uid": 1522,
                        "name": 'Кадубовецька',
                        "name_en": 'Kadubovetska',
                    },
                    {
                        "uid": 1523,
                        "name": "Кам'янецька",
                        "name_en": 'Kamianetska',
                    },
                    {
                        "uid": 1524,
                        "name": "Кам'янська",
                        "name_en": 'Kamianska',
                    },
                    {
                        "uid": 1525,
                        "name": 'Карапачівська',
                        "name_en": 'Karapachivska',
                    },
                    {
                        "uid": 1527,
                        "name": 'Кострижівська',
                        "name_en": 'Kostryzhivska',
                    },
                    {
                        "uid": 1528,
                        "name": 'Красноїльська',
                        "name_en": 'Krasnoilska',
                    },
                    {
                        "uid": 1526,
                        "name": 'Кіцманська',
                        "name_en": 'Kitsmanska',
                    },
                    {
                        "uid": 1529,
                        "name": 'Магальська',
                        "name_en": 'Mahalska',
                    },
                    {
                        "uid": 1530,
                        "name": 'Мамаївська',
                        "name_en": 'Mamaivska',
                    },
                    {
                        "uid": 1531,
                        "name": 'Неполоковецька',
                        "name_en": 'Nepolokovetska',
                    },
                    {
                        "uid": 1532,
                        "name": 'Новоселицька',
                        "name_en": 'Novoselytska',
                    },
                    {
                        "uid": 1533,
                        "name": 'Острицька',
                        "name_en": 'Ostrytska',
                    },
                    {
                        "uid": 1534,
                        "name": 'Петровецька',
                        "name_en": 'Petrovetska',
                    },
                    {
                        "uid": 1535,
                        "name": 'Ставчанська',
                        "name_en": 'Stavchanska',
                    },
                    {
                        "uid": 1536,
                        "name": 'Сторожинецька',
                        "name_en": 'Storozhynetska',
                    },
                    {
                        "uid": 1537,
                        "name": 'Сучевенська',
                        "name_en": 'Suchevenska',
                    },
                    {
                        "uid": 1538,
                        "name": 'Тарашанська',
                        "name_en": 'Tarashanska',
                    },
                    {
                        "uid": 1539,
                        "name": 'Тереблеченська',
                        "name_en": 'Tereblechenska',
                    },
                    {
                        "uid": 1540,
                        "name": 'Топорівська',
                        "name_en": 'Toporivska',
                    },
                    {
                        "uid": 1541,
                        "name": 'Чагорська',
                        "name_en": 'Chahorska',
                    },
                    {
                        "uid": 1542,
                        "name": 'м. Чернівці та Чернівецька',
                        "name_en": 'Chernivtsi and Chernivetska',
                    },
                    {
                        "uid": 1543,
                        "name": 'Чудейська',
                        "name_en": 'Chudeiska',
                    },
                    {
                        "uid": 1544,
                        "name": 'Юрковецька',
                        "name_en": 'Yurkovetska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 25,
        "name": 'Чернігівська',
        "type": LocationType.OBLAST,
        "name_en": 'Chernihivska',
        "districts": [
            {
                "uid": 144,
                "name": 'Корюківський',
                "name_en": 'Koriukivskyi',
                "hromadas": [
                    {
                        "uid": 1607,
                        "name": 'Корюківська',
                        "name_en": 'Koriukivska',
                    },
                    {
                        "uid": 1608,
                        "name": 'Менська',
                        "name_en": 'Menska',
                    },
                    {
                        "uid": 1609,
                        "name": 'Сновська',
                        "name_en": 'Snovska',
                    },
                    {
                        "uid": 1610,
                        "name": 'Сосницька',
                        "name_en": 'Sosnytska',
                    },
                    {
                        "uid": 1611,
                        "name": 'Холминська',
                        "name_en": 'Kholmynska',
                    },
                ],
            },
            {
                "uid": 141,
                "name": 'Новгород-Сіверський',
                "name_en": 'Novhorod-Siverskyi',
                "hromadas": [
                    {
                        "uid": 1603,
                        "name": 'Коропська',
                        "name_en": 'Koropska',
                    },
                    {
                        "uid": 1604,
                        "name": 'м. Новгород-Сіверський та Новгород-Сіверська',
                        "name_en": 'Novhorod-Siverskyi and Novhorod-Siverska',
                    },
                    {
                        "uid": 1605,
                        "name": 'Понорницька',
                        "name_en": 'Ponornytska',
                    },
                    {
                        "uid": 1606,
                        "name": 'Семенівська',
                        "name_en": 'Semenivska',
                    },
                ],
            },
            {
                "uid": 142,
                "name": 'Ніжинський',
                "name_en": 'Nizhynskyi',
                "hromadas": [
                    {
                        "uid": 1555,
                        "name": 'Батуринська',
                        "name_en": 'Baturynska',
                    },
                    {
                        "uid": 1556,
                        "name": 'Бахмацька',
                        "name_en": 'Bakhmatska',
                    },
                    {
                        "uid": 1557,
                        "name": 'Бобровицька',
                        "name_en": 'Bobrovytska',
                    },
                    {
                        "uid": 1558,
                        "name": 'Борзнянська',
                        "name_en": 'Borznianska',
                    },
                    {
                        "uid": 1559,
                        "name": 'Вертіївська',
                        "name_en": 'Vertiivska',
                    },
                    {
                        "uid": 1560,
                        "name": 'Височанська',
                        "name_en": 'Vysochanska',
                    },
                    {
                        "uid": 1561,
                        "name": 'Дмитрівська',
                        "name_en": 'Dmytrivska',
                    },
                    {
                        "uid": 1562,
                        "name": 'Комарівська',
                        "name_en": 'Komarivska',
                    },
                    {
                        "uid": 1563,
                        "name": 'Крутівська',
                        "name_en": 'Krutivska',
                    },
                    {
                        "uid": 1564,
                        "name": 'Лосинівська',
                        "name_en": 'Losynivska',
                    },
                    {
                        "uid": 1565,
                        "name": 'Макіївська',
                        "name_en": 'Makiivska',
                    },
                    {
                        "uid": 1566,
                        "name": 'Мринська',
                        "name_en": 'Mrynska',
                    },
                    {
                        "uid": 1568,
                        "name": 'Новобасанська',
                        "name_en": 'Novobasanska',
                    },
                    {
                        "uid": 1569,
                        "name": 'Носівська',
                        "name_en": 'Nosivska',
                    },
                    {
                        "uid": 1567,
                        "name": 'м. Ніжин та Ніжинська',
                        "name_en": 'Nizhyn and Nizhynska',
                    },
                    {
                        "uid": 1570,
                        "name": 'Плисківська',
                        "name_en": 'Plyskivska',
                    },
                    {
                        "uid": 1571,
                        "name": 'Талалаївська',
                        "name_en": 'Talalaivska',
                    },
                ],
            },
            {
                "uid": 143,
                "name": 'Прилуцький',
                "name_en": 'Prylutskyi',
                "hromadas": [
                    {
                        "uid": 1592,
                        "name": 'Варвинська',
                        "name_en": 'Varvynska',
                    },
                    {
                        "uid": 1594,
                        "name": 'Ладанська',
                        "name_en": 'Ladanska',
                    },
                    {
                        "uid": 1595,
                        "name": 'Линовицька',
                        "name_en": 'Lynovytska',
                    },
                    {
                        "uid": 1596,
                        "name": 'Малодівицька',
                        "name_en": 'Malodivytska',
                    },
                    {
                        "uid": 1597,
                        "name": 'Парафіївська',
                        "name_en": 'Parafiivska',
                    },
                    {
                        "uid": 1598,
                        "name": 'м. Прилуки та Прилуцька',
                        "name_en": 'Pryluky and Prylutska',
                    },
                    {
                        "uid": 1599,
                        "name": 'Срібнянська',
                        "name_en": 'Sribnianska',
                    },
                    {
                        "uid": 1600,
                        "name": "Сухополов'янська",
                        "name_en": 'Sukhopolovianska',
                    },
                    {
                        "uid": 1601,
                        "name": 'Талалаївська',
                        "name_en": 'Talalaivska',
                    },
                    {
                        "uid": 1602,
                        "name": 'Яблунівська',
                        "name_en": 'Yablunivska',
                    },
                    {
                        "uid": 1593,
                        "name": 'Ічнянська',
                        "name_en": 'Ichnianska',
                    },
                ],
            },
            {
                "uid": 140,
                "name": 'Чернігівський',
                "name_en": 'Chernihivskyi',
                "hromadas": [
                    {
                        "uid": 1572,
                        "name": 'Березнянська',
                        "name_en": 'Bereznianska',
                    },
                    {
                        "uid": 1573,
                        "name": 'Гончарівська',
                        "name_en": 'Honcharivska',
                    },
                    {
                        "uid": 1574,
                        "name": 'Городнянська',
                        "name_en": 'Horodnianska',
                    },
                    {
                        "uid": 1575,
                        "name": 'Деснянська',
                        "name_en": 'Desnianska',
                    },
                    {
                        "uid": 1576,
                        "name": 'Добрянська',
                        "name_en": 'Dobrianska',
                    },
                    {
                        "uid": 1579,
                        "name": 'Киселівська',
                        "name_en": 'Kyselivska',
                    },
                    {
                        "uid": 1578,
                        "name": 'Киїнська',
                        "name_en": 'Kyinska',
                    },
                    {
                        "uid": 1581,
                        "name": 'Козелецька',
                        "name_en": 'Kozeletska',
                    },
                    {
                        "uid": 1582,
                        "name": 'Куликівська',
                        "name_en": 'Kulykivska',
                    },
                    {
                        "uid": 1580,
                        "name": 'Кіптівська',
                        "name_en": 'Kiptivska',
                    },
                    {
                        "uid": 1583,
                        "name": 'Любецька',
                        "name_en": 'Liubetska',
                    },
                    {
                        "uid": 1584,
                        "name": 'Михайло-Коцюбинська',
                        "name_en": 'Mykhailo-Kotsiubynska',
                    },
                    {
                        "uid": 1585,
                        "name": 'Новобілоуська',
                        "name_en": 'Novobilouska',
                    },
                    {
                        "uid": 1586,
                        "name": 'Олишівська',
                        "name_en": 'Olyshivska',
                    },
                    {
                        "uid": 1587,
                        "name": 'Остерська',
                        "name_en": 'Osterska',
                    },
                    {
                        "uid": 1588,
                        "name": 'Ріпкинська',
                        "name_en": 'Ripkynska',
                    },
                    {
                        "uid": 1589,
                        "name": 'Седнівська',
                        "name_en": 'Sednivska',
                    },
                    {
                        "uid": 1590,
                        "name": 'Тупичівська',
                        "name_en": 'Tupychivska',
                    },
                    {
                        "uid": 1591,
                        "name": 'м. Чернігів та Чернігівська',
                        "name_en": 'Chernihiv and Chernihivska',
                    },
                    {
                        "uid": 1577,
                        "name": 'Іванівська',
                        "name_en": 'Ivanivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 13,
        "name": 'Івано-Франківська',
        "type": LocationType.OBLAST,
        "name_en": 'Ivano-Frankivska',
        "districts": [
            {
                "uid": 67,
                "name": 'Верховинський',
                "name_en": 'Verkhovynskyi',
                "hromadas": [
                    {
                        "uid": 620,
                        "name": 'Білоберізька',
                        "name_en": 'Biloberizka',
                    },
                    {
                        "uid": 621,
                        "name": 'Верховинська',
                        "name_en": 'Verkhovynska',
                    },
                    {
                        "uid": 622,
                        "name": 'Зеленська',
                        "name_en": 'Zelenska',
                    },
                ],
            },
            {
                "uid": 71,
                "name": 'Калуський',
                "name_en": 'Kaluskyi',
                "hromadas": [
                    {
                        "uid": 643,
                        "name": 'м. Болехів та Болехівська',
                        "name_en": 'Bolekhiv and Bolekhivska',
                    },
                    {
                        "uid": 644,
                        "name": 'Брошнів-Осадська',
                        "name_en": 'Broshniv-Osadska',
                    },
                    {
                        "uid": 645,
                        "name": 'Верхнянська',
                        "name_en": 'Verkhnianska',
                    },
                    {
                        "uid": 646,
                        "name": 'Вигодська',
                        "name_en": 'Vyhodska',
                    },
                    {
                        "uid": 647,
                        "name": 'Витвицька',
                        "name_en": 'Vytvytska',
                    },
                    {
                        "uid": 648,
                        "name": 'Войнилівська',
                        "name_en": 'Voinylivska',
                    },
                    {
                        "uid": 649,
                        "name": 'м. Долина та Долинська',
                        "name_en": 'Dolyna and Dolynska',
                    },
                    {
                        "uid": 650,
                        "name": 'Дубівська',
                        "name_en": 'Dubivska',
                    },
                    {
                        "uid": 651,
                        "name": 'м. Калуш та Калуська',
                        "name_en": 'Kalush and Kaluska',
                    },
                    {
                        "uid": 652,
                        "name": 'Новицька',
                        "name_en": 'Novytska',
                    },
                    {
                        "uid": 653,
                        "name": 'Перегінська',
                        "name_en": 'Perehinska',
                    },
                    {
                        "uid": 654,
                        "name": 'Рожнятівська',
                        "name_en": 'Rozhniativska',
                    },
                    {
                        "uid": 655,
                        "name": 'Спаська',
                        "name_en": 'Spaska',
                    },
                ],
            },
            {
                "uid": 70,
                "name": 'Коломийський',
                "name_en": 'Kolomyiskyi',
                "hromadas": [
                    {
                        "uid": 664,
                        "name": 'Гвіздецька',
                        "name_en": 'Hvizdetska',
                    },
                    {
                        "uid": 665,
                        "name": 'Городенківська',
                        "name_en": 'Horodenkivska',
                    },
                    {
                        "uid": 666,
                        "name": 'Заболотівська',
                        "name_en": 'Zabolotivska',
                    },
                    {
                        "uid": 667,
                        "name": 'м. Коломия та Коломийська',
                        "name_en": 'Kolomyia and Kolomyiska',
                    },
                    {
                        "uid": 668,
                        "name": 'Коршівська',
                        "name_en": 'Korshivska',
                    },
                    {
                        "uid": 669,
                        "name": 'Матеївецька',
                        "name_en": 'Mateivetska',
                    },
                    {
                        "uid": 670,
                        "name": 'Нижньовербізька',
                        "name_en": 'Nyzhnoverbizka',
                    },
                    {
                        "uid": 671,
                        "name": 'Отинійська',
                        "name_en": 'Otyniiska',
                    },
                    {
                        "uid": 674,
                        "name": "П'ядицька",
                        "name_en": 'Piadytska',
                    },
                    {
                        "uid": 672,
                        "name": 'Печеніжинська',
                        "name_en": 'Pechenizhynska',
                    },
                    {
                        "uid": 673,
                        "name": 'Підгайчиківська',
                        "name_en": 'Pidhaichykivska',
                    },
                    {
                        "uid": 675,
                        "name": 'Снятинська',
                        "name_en": 'Sniatynska',
                    },
                    {
                        "uid": 676,
                        "name": 'Чернелицька',
                        "name_en": 'Chernelytska',
                    },
                ],
            },
            {
                "uid": 69,
                "name": 'Косівський',
                "name_en": 'Kosivskyi',
                "hromadas": [
                    {
                        "uid": 678,
                        "name": 'Космацька',
                        "name_en": 'Kosmatska',
                    },
                    {
                        "uid": 677,
                        "name": 'Косівська',
                        "name_en": 'Kosivska',
                    },
                    {
                        "uid": 679,
                        "name": 'Кутська',
                        "name_en": 'Kutska',
                    },
                    {
                        "uid": 680,
                        "name": 'Рожнівська',
                        "name_en": 'Rozhnivska',
                    },
                    {
                        "uid": 681,
                        "name": 'Яблунівська',
                        "name_en": 'Yablunivska',
                    },
                ],
            },
            {
                "uid": 72,
                "name": 'Надвірнянський',
                "name_en": 'Nadvirnianskyi',
                "hromadas": [
                    {
                        "uid": 656,
                        "name": 'Ворохтянська',
                        "name_en": 'Vorokhtianska',
                    },
                    {
                        "uid": 657,
                        "name": 'Делятинська',
                        "name_en": 'Deliatynska',
                    },
                    {
                        "uid": 658,
                        "name": 'Ланчинська',
                        "name_en": 'Lanchynska',
                    },
                    {
                        "uid": 659,
                        "name": 'м. Надвірна та Надвірнянська',
                        "name_en": 'Nadvirna and Nadvirnianska',
                    },
                    {
                        "uid": 660,
                        "name": 'Пасічнянська',
                        "name_en": 'Pasichnianska',
                    },
                    {
                        "uid": 661,
                        "name": 'Переріслянська',
                        "name_en": 'Pererislianska',
                    },
                    {
                        "uid": 662,
                        "name": 'Поляницька',
                        "name_en": 'Polianytska',
                    },
                    {
                        "uid": 663,
                        "name": 'м. Яремче та Яремчанська',
                        "name_en": 'Yaremche and Yaremchanska',
                    },
                ],
            },
            {
                "uid": 68,
                "name": 'Івано-Франківський',
                "name_en": 'Ivano-Frankivskyi',
                "hromadas": [
                    {
                        "uid": 624,
                        "name": 'Богородчанська',
                        "name_en": 'Bohorodchanska',
                    },
                    {
                        "uid": 625,
                        "name": 'Букачівська',
                        "name_en": 'Bukachivska',
                    },
                    {
                        "uid": 626,
                        "name": 'м. Бурштин та Бурштинська',
                        "name_en": 'Burshtyn and Burshtynska',
                    },
                    {
                        "uid": 623,
                        "name": 'Більшівцівська',
                        "name_en": 'Bilshivtsivska',
                    },
                    {
                        "uid": 627,
                        "name": 'Галицька',
                        "name_en": 'Halytska',
                    },
                    {
                        "uid": 628,
                        "name": 'Дзвиняцька',
                        "name_en": 'Dzvyniatska',
                    },
                    {
                        "uid": 629,
                        "name": 'Дубовецька',
                        "name_en": 'Dubovetska',
                    },
                    {
                        "uid": 631,
                        "name": 'Загвіздянська',
                        "name_en": 'Zahvizdianska',
                    },
                    {
                        "uid": 633,
                        "name": 'Лисецька',
                        "name_en": 'Lysetska',
                    },
                    {
                        "uid": 634,
                        "name": 'Обертинська',
                        "name_en": 'Obertynska',
                    },
                    {
                        "uid": 635,
                        "name": 'Олешанська',
                        "name_en": 'Oleshanska',
                    },
                    {
                        "uid": 636,
                        "name": 'Рогатинська',
                        "name_en": 'Rohatynska',
                    },
                    {
                        "uid": 637,
                        "name": 'Солотвинська',
                        "name_en": 'Solotvynska',
                    },
                    {
                        "uid": 638,
                        "name": 'Старобогородчанська',
                        "name_en": 'Starobohorodchanska',
                    },
                    {
                        "uid": 639,
                        "name": 'Тисменицька',
                        "name_en": 'Tysmenytska',
                    },
                    {
                        "uid": 640,
                        "name": 'Тлумацька',
                        "name_en": 'Tlumatska',
                    },
                    {
                        "uid": 641,
                        "name": 'Угринівська',
                        "name_en": 'Uhrynivska',
                    },
                    {
                        "uid": 642,
                        "name": 'Ямницька',
                        "name_en": 'Yamnytska',
                    },
                    {
                        "uid": 630,
                        "name": 'Єзупільська',
                        "name_en": 'Yezupilska',
                    },
                    {
                        "uid": 632,
                        "name": 'м. Івано-Франківськ та Івано-Франківська',
                        "name_en": 'Ivano-Frankivsk and Ivano-Frankivska',
                    },
                ],
            },
        ],
    },
    {
        "uid": 9,
        "name": 'Крим',
        "type": LocationType.AUTONOMOUS_REPUBLIC,
        "name_en": 'Crimea',
    },
]
