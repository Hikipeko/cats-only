PRAGMA foreign_keys = ON;
INSERT INTO users(username, fullname, email, filename, PASSWORD) VALUES
    ("FluffyPaws23", "Oliver Whiskers", "FluffyPaws23@gmail.com", "IMG_69.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("MischievousCat89", "Luna Paws", "MischievousCat89@gmail.com", "IMG_242.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("CuddlyFeline45", "Milo Feline", "CuddlyFeline45@gmail.com", "IMG_233.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("SneakyWhiskers67", "Bella Claws", "SneakyWhiskers67@gmail.com", "IMG_89.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("SassyMittens32", "Simba Tail", "SassyMittens32@gmail.com", "IMG_3.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("PurringClaws14", "Charlie Purr", "PurringClaws14@gmail.com", "IMG_146.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("FuzzyTail58", "Lucy Mittens", "FuzzyTail58@gmail.com", "IMG_59.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("PlayfulPurr9", "Max Sassy", "PlayfulPurr9@gmail.com", "IMG_10.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("WhiskeredMeow76", "Chloe Fuzzy", "WhiskeredMeow76@gmail.com", "IMG_39.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8"),
    ("ClawedKitten51", "Tiger Sneaky", "ClawedKitten51@gmail.com", "IMG_94.jpg", "sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8");

INSERT INTO posts(filename, owner) VALUES
    ("IMG_118.jpg", "FluffyPaws23"),
    ("IMG_12.jpg", "FluffyPaws23"),
    ("IMG_232.jpg", "FluffyPaws23"),
    ("IMG_33.jpg", "FluffyPaws23"),
    ("IMG_69.jpg", "FluffyPaws23"),
    ("IMG_117.jpg", "MischievousCat89"),
    ("IMG_126.jpg", "MischievousCat89"),
    ("IMG_133.jpg", "MischievousCat89"),
    ("IMG_141.jpg", "MischievousCat89"),
    ("IMG_22.jpg", "MischievousCat89"),
    ("IMG_24.jpg", "MischievousCat89"),
    ("IMG_242.jpg", "MischievousCat89"),
    ("IMG_243.jpg", "MischievousCat89"),
    ("IMG_244.jpg", "MischievousCat89"),
    ("IMG_248.jpg", "MischievousCat89"),
    ("IMG_249.jpg", "MischievousCat89"),
    ("IMG_250.jpg", "MischievousCat89"),
    ("IMG_251.jpg", "MischievousCat89"),
    ("IMG_252.jpg", "MischievousCat89"),
    ("IMG_43.jpg", "MischievousCat89"),
    ("IMG_47.jpg", "MischievousCat89"),
    ("IMG_48.jpg", "MischievousCat89"),
    ("IMG_84.jpg", "MischievousCat89"),
    ("IMG_85.jpg", "MischievousCat89"),
    ("IMG_87.jpg", "MischievousCat89"),
    ("IMG_13.jpg", "CuddlyFeline45"),
    ("IMG_156.jpg", "CuddlyFeline45"),
    ("IMG_176.jpg", "CuddlyFeline45"),
    ("IMG_2.jpg", "CuddlyFeline45"),
    ("IMG_201.jpg", "CuddlyFeline45"),
    ("IMG_203.jpg", "CuddlyFeline45"),
    ("IMG_205.jpg", "CuddlyFeline45"),
    ("IMG_207.jpg", "CuddlyFeline45"),
    ("IMG_214.jpg", "CuddlyFeline45"),
    ("IMG_228.jpg", "CuddlyFeline45"),
    ("IMG_229.jpg", "CuddlyFeline45"),
    ("IMG_231.jpg", "CuddlyFeline45"),
    ("IMG_233.jpg", "CuddlyFeline45"),
    ("IMG_255.jpg", "CuddlyFeline45"),
    ("IMG_256.jpg", "CuddlyFeline45"),
    ("IMG_257.jpg", "CuddlyFeline45"),
    ("IMG_55.jpg", "CuddlyFeline45"),
    ("IMG_14.jpg", "SneakyWhiskers67"),
    ("IMG_17.jpg", "SneakyWhiskers67"),
    ("IMG_37.jpg", "SneakyWhiskers67"),
    ("IMG_38.jpg", "SneakyWhiskers67"),
    ("IMG_44.jpg", "SneakyWhiskers67"),
    ("IMG_45.jpg", "SneakyWhiskers67"),
    ("IMG_53.jpg", "SneakyWhiskers67"),
    ("IMG_88.jpg", "SneakyWhiskers67"),
    ("IMG_89.jpg", "SneakyWhiskers67"),
    ("IMG_11.jpg", "SassyMittens32"),
    ("IMG_3.jpg", "SassyMittens32"),
    ("IMG_4.jpg", "SassyMittens32"),
    ("IMG_5.jpg", "SassyMittens32"),
    ("IMG_113.jpg", "PurringClaws14"),
    ("IMG_115.jpg", "PurringClaws14"),
    ("IMG_145.jpg", "PurringClaws14"),
    ("IMG_15.jpg", "PurringClaws14"),
    ("IMG_159.jpg", "PurringClaws14"),
    ("IMG_16.jpg", "PurringClaws14"),
    ("IMG_160.jpg", "PurringClaws14"),
    ("IMG_161.jpg", "PurringClaws14"),
    ("IMG_162.jpg", "PurringClaws14"),
    ("IMG_163.jpg", "PurringClaws14"),
    ("IMG_164.jpg", "PurringClaws14"),
    ("IMG_165.jpg", "PurringClaws14"),
    ("IMG_166.jpg", "PurringClaws14"),
    ("IMG_175.jpg", "PurringClaws14"),
    ("IMG_182.jpg", "PurringClaws14"),
    ("IMG_183.jpg", "PurringClaws14"),
    ("IMG_188.jpg", "PurringClaws14"),
    ("IMG_189.jpg", "PurringClaws14"),
    ("IMG_190.jpg", "PurringClaws14"),
    ("IMG_195.jpg", "PurringClaws14"),
    ("IMG_206.jpg", "PurringClaws14"),
    ("IMG_212.jpg", "PurringClaws14"),
    ("IMG_225.jpg", "PurringClaws14"),
    ("IMG_23.jpg", "PurringClaws14"),
    ("IMG_246.jpg", "PurringClaws14"),
    ("IMG_28.jpg", "PurringClaws14"),
    ("IMG_29.jpg", "PurringClaws14"),
    ("IMG_30.jpg", "PurringClaws14"),
    ("IMG_31.jpg", "PurringClaws14"),
    ("IMG_32.jpg", "PurringClaws14"),
    ("IMG_34.jpg", "PurringClaws14"),
    ("IMG_49.jpg", "PurringClaws14"),
    ("IMG_50.jpg", "PurringClaws14"),
    ("IMG_56.jpg", "PurringClaws14"),
    ("IMG_6.jpg", "PurringClaws14"),
    ("IMG_63.jpg", "PurringClaws14"),
    ("IMG_71.jpg", "PurringClaws14"),
    ("IMG_93.jpg", "PurringClaws14"),
    ("IMG_97.jpg", "PurringClaws14"),
    ("IMG_98.jpg", "PurringClaws14"),
    ("IMG_1.jpg", "FuzzyTail58"),
    ("IMG_107.jpg", "FuzzyTail58"),
    ("IMG_108.jpg", "FuzzyTail58"),
    ("IMG_109.jpg", "FuzzyTail58"),
    ("IMG_110.jpg", "FuzzyTail58"),
    ("IMG_26.jpg", "FuzzyTail58"),
    ("IMG_36.jpg", "FuzzyTail58"),
    ("IMG_40.jpg", "FuzzyTail58"),
    ("IMG_41.jpg", "FuzzyTail58"),
    ("IMG_42.jpg", "FuzzyTail58"),
    ("IMG_46.jpg", "FuzzyTail58"),
    ("IMG_59.jpg", "FuzzyTail58"),
    ("IMG_60.jpg", "FuzzyTail58"),
    ("IMG_61.jpg", "FuzzyTail58"),
    ("IMG_7.jpg", "FuzzyTail58"),
    ("IMG_10.jpg", "PlayfulPurr9"),
    ("IMG_120.jpg", "PlayfulPurr9"),
    ("IMG_121.jpg", "PlayfulPurr9"),
    ("IMG_18.jpg", "PlayfulPurr9"),
    ("IMG_199.jpg", "PlayfulPurr9"),
    ("IMG_20.jpg", "PlayfulPurr9"),
    ("IMG_21.jpg", "PlayfulPurr9"),
    ("IMG_219.jpg", "PlayfulPurr9"),
    ("IMG_247.jpg", "PlayfulPurr9"),
    ("IMG_261.jpg", "PlayfulPurr9"),
    ("IMG_262.jpg", "PlayfulPurr9"),
    ("IMG_8.jpg", "PlayfulPurr9"),
    ("IMG_9.jpg", "PlayfulPurr9"),
    ("IMG_149.jpg", "WhiskeredMeow76"),
    ("IMG_150.jpg", "WhiskeredMeow76"),
    ("IMG_171.jpg", "WhiskeredMeow76"),
    ("IMG_177.jpg", "WhiskeredMeow76"),
    ("IMG_19.jpg", "WhiskeredMeow76"),
    ("IMG_235.jpg", "WhiskeredMeow76"),
    ("IMG_265.jpg", "WhiskeredMeow76"),
    ("IMG_27.jpg", "WhiskeredMeow76"),
    ("IMG_35.jpg", "WhiskeredMeow76"),
    ("IMG_39.jpg", "WhiskeredMeow76"),
    ("IMG_51.jpg", "WhiskeredMeow76"),
    ("IMG_52.jpg", "WhiskeredMeow76"),
    ("IMG_54.jpg", "WhiskeredMeow76"),
    ("IMG_62.jpg", "WhiskeredMeow76"),
    ("IMG_72.jpg", "WhiskeredMeow76"),
    ("IMG_73.jpg", "WhiskeredMeow76"),
    ("IMG_74.jpg", "WhiskeredMeow76"),
    ("IMG_75.jpg", "WhiskeredMeow76"),
    ("IMG_76.jpg", "WhiskeredMeow76"),
    ("IMG_77.jpg", "WhiskeredMeow76"),
    ("IMG_78.jpg", "WhiskeredMeow76"),
    ("IMG_79.jpg", "WhiskeredMeow76"),
    ("IMG_80.jpg", "WhiskeredMeow76"),
    ("IMG_81.jpg", "WhiskeredMeow76"),
    ("IMG_82.jpg", "WhiskeredMeow76"),
    ("IMG_91.jpg", "WhiskeredMeow76"),
    ("IMG_122.jpg", "ClawedKitten51"),
    ("IMG_137.jpg", "ClawedKitten51"),
    ("IMG_138.jpg", "ClawedKitten51"),
    ("IMG_168.jpg", "ClawedKitten51"),
    ("IMG_169.jpg", "ClawedKitten51"),
    ("IMG_209.jpg", "ClawedKitten51"),
    ("IMG_25.jpg", "ClawedKitten51"),
    ("IMG_92.jpg", "ClawedKitten51"),
    ("IMG_94.jpg", "ClawedKitten51");

INSERT INTO comments(owner, postid, text) VALUES
    ("CuddlyFeline45", 155, "Awww"),
    ("FluffyPaws23", 93, "Cats are the best"),
    ("PlayfulPurr9", 72, "Just purrfect!"),
    ("MischievousCat89", 127, "Amazing pic!"),
    ("FuzzyTail58", 72, "Awww"),
    ("ClawedKitten51", 122, "I <3 cats"),
    ("WhiskeredMeow76", 148, "So cute!"),
    ("PurringClaws14", 62, "Just like my cat"),
    ("CuddlyFeline45", 14, "Awww"),
    ("ClawedKitten51", 54, "Just purrfect!"),
    ("FluffyPaws23", 136, "Amazing pic!"),
    ("MischievousCat89", 104, "Just like my cat"),
    ("PurringClaws14", 51, "Cats are the best"),
    ("SassyMittens32", 107, "Adorable!"),
    ("PlayfulPurr9", 28, "Look at those eyes!"),
    ("ClawedKitten51", 78, "Adorable!"),
    ("FuzzyTail58", 29, "Too fluffy!"),
    ("ClawedKitten51", 96, "Just like my cat"),
    ("PlayfulPurr9", 97, "Amazing pic!"),
    ("FuzzyTail58", 91, "Cats forever"),
    ("CuddlyFeline45", 12, "Simply adorable"),
    ("SassyMittens32", 29, "Feline perfection"),
    ("FluffyPaws23", 22, "Is that a kitten?"),
    ("SneakyWhiskers67", 79, "Simply adorable"),
    ("SneakyWhiskers67", 68, "This is gold"),
    ("PlayfulPurr9", 31, "Too fluffy!"),
    ("MischievousCat89", 88, "Adorable!"),
    ("FuzzyTail58", 148, "Just purrfect!"),
    ("MischievousCat89", 50, "Cat goals!"),
    ("PurringClaws14", 102, "#catoftheday"),
    ("SneakyWhiskers67", 92, "What a beauty!"),
    ("ClawedKitten51", 67, "#catsofinstagram"),
    ("MischievousCat89", 93, "#catlover"),
    ("SassyMittens32", 24, "#kittensofinstagram"),
    ("SneakyWhiskers67", 93, "Best picture ever"),
    ("SneakyWhiskers67", 29, "Cat goals!"),
    ("FuzzyTail58", 54, "I’m in love"),
    ("ClawedKitten51", 134, "#catlover"),
    ("MischievousCat89", 128, "Cats > everything"),
    ("WhiskeredMeow76", 107, "So photogenic!"),
    ("SassyMittens32", 37, "#cutecats"),
    ("PlayfulPurr9", 138, "Simply adorable"),
    ("CuddlyFeline45", 21, "This is paw-some!"),
    ("SassyMittens32", 72, "This is gold"),
    ("PlayfulPurr9", 54, "Too fluffy!"),
    ("SassyMittens32", 45, "This made my day"),
    ("SassyMittens32", 112, "So cute!"),
    ("ClawedKitten51", 61, "So photogenic!"),
    ("FuzzyTail58", 37, "Cat-tastic!"),
    ("SneakyWhiskers67", 28, "Pawsome!"),
    ("FuzzyTail58", 117, "Awww"),
    ("WhiskeredMeow76", 116, "Adorable!"),
    ("WhiskeredMeow76", 100, "Just purrfect!"),
    ("PlayfulPurr9", 47, "This is paw-some!"),
    ("ClawedKitten51", 120, "So photogenic!"),
    ("PlayfulPurr9", 14, "#catlover"),
    ("FuzzyTail58", 121, "Too fluffy!"),
    ("PlayfulPurr9", 125, "Awww"),
    ("CuddlyFeline45", 102, "#catlover"),
    ("SneakyWhiskers67", 22, "Best picture ever"),
    ("ClawedKitten51", 145, "Perfect whiskers"),
    ("PlayfulPurr9", 70, "This is amazing"),
    ("ClawedKitten51", 86, "Cuddly and cute"),
    ("SneakyWhiskers67", 149, "So much fluff"),
    ("CuddlyFeline45", 2, "Can’t get enough"),
    ("SassyMittens32", 1, "#catlover"),
    ("SneakyWhiskers67", 71, "#catsofinstagram"),
    ("FluffyPaws23", 61, "#kittensofinstagram"),
    ("SneakyWhiskers67", 1, "Cats forever"),
    ("CuddlyFeline45", 120, "Perfect whiskers"),
    ("PlayfulPurr9", 45, "Cat goals!"),
    ("CuddlyFeline45", 69, "#catlover"),
    ("MischievousCat89", 9, "#catoftheday"),
    ("PlayfulPurr9", 135, "Love this!"),
    ("CuddlyFeline45", 107, "What a beauty!"),
    ("MischievousCat89", 131, "Cat-tastic!"),
    ("PlayfulPurr9", 19, "Look at those eyes!"),
    ("FluffyPaws23", 113, "Cats > everything"),
    ("PurringClaws14", 35, "This is gold"),
    ("PlayfulPurr9", 56, "Pure joy"),
    ("FluffyPaws23", 89, "Just purrfect!"),
    ("FluffyPaws23", 57, "Feline perfection"),
    ("PlayfulPurr9", 26, "Just purrfect!"),
    ("SneakyWhiskers67", 78, "#kittensofinstagram"),
    ("FluffyPaws23", 135, "Awww"),
    ("SassyMittens32", 147, "Perfect whiskers"),
    ("WhiskeredMeow76", 81, "Cat-tastic!"),
    ("MischievousCat89", 54, "Majestic"),
    ("PurringClaws14", 81, "#cutecats"),
    ("CuddlyFeline45", 92, "Look at those paws!"),
    ("WhiskeredMeow76", 89, "This is amazing"),
    ("CuddlyFeline45", 115, "Just purrfect!"),
    ("FluffyPaws23", 113, "So cute!"),
    ("FuzzyTail58", 121, "So photogenic!"),
    ("SneakyWhiskers67", 116, "I need a cat"),
    ("WhiskeredMeow76", 76, "This made my day"),
    ("ClawedKitten51", 111, "#catoftheday"),
    ("SneakyWhiskers67", 106, "#meow"),
    ("SneakyWhiskers67", 157, "Look at those paws!"),
    ("SneakyWhiskers67", 14, "I’m in love");

INSERT INTO likes(owner, postid) VALUES
    ("PlayfulPurr9", 42),
    ("PurringClaws14", 51),
    ("SassyMittens32", 109),
    ("WhiskeredMeow76", 113),
    ("SneakyWhiskers67", 71),
    ("SassyMittens32", 41),
    ("SassyMittens32", 11),
    ("ClawedKitten51", 122),
    ("SassyMittens32", 29),
    ("PlayfulPurr9", 53),
    ("MischievousCat89", 141),
    ("CuddlyFeline45", 16),
    ("PlayfulPurr9", 46),
    ("WhiskeredMeow76", 6),
    ("SneakyWhiskers67", 117),
    ("SneakyWhiskers67", 64),
    ("FuzzyTail58", 115),
    ("FluffyPaws23", 94),
    ("ClawedKitten51", 38),
    ("PlayfulPurr9", 126),
    ("ClawedKitten51", 147),
    ("PurringClaws14", 108),
    ("SassyMittens32", 41),
    ("FluffyPaws23", 70),
    ("MischievousCat89", 153),
    ("MischievousCat89", 92),
    ("FuzzyTail58", 77),
    ("FluffyPaws23", 40),
    ("ClawedKitten51", 7),
    ("SassyMittens32", 87),
    ("PurringClaws14", 135),
    ("WhiskeredMeow76", 96),
    ("FluffyPaws23", 101),
    ("SassyMittens32", 121),
    ("SneakyWhiskers67", 94),
    ("MischievousCat89", 35),
    ("PlayfulPurr9", 134),
    ("PurringClaws14", 57),
    ("ClawedKitten51", 12),
    ("WhiskeredMeow76", 90),
    ("WhiskeredMeow76", 155),
    ("WhiskeredMeow76", 125),
    ("PlayfulPurr9", 89),
    ("SneakyWhiskers67", 52),
    ("PlayfulPurr9", 56),
    ("WhiskeredMeow76", 36),
    ("FuzzyTail58", 50),
    ("MischievousCat89", 107),
    ("PlayfulPurr9", 87),
    ("CuddlyFeline45", 109),
    ("ClawedKitten51", 113),
    ("ClawedKitten51", 70),
    ("ClawedKitten51", 146),
    ("SneakyWhiskers67", 1),
    ("PurringClaws14", 60),
    ("SneakyWhiskers67", 73),
    ("ClawedKitten51", 139),
    ("FluffyPaws23", 112),
    ("PlayfulPurr9", 88),
    ("PlayfulPurr9", 29),
    ("PlayfulPurr9", 88),
    ("PlayfulPurr9", 96),
    ("SassyMittens32", 52),
    ("PurringClaws14", 114),
    ("SneakyWhiskers67", 41),
    ("PurringClaws14", 128),
    ("FluffyPaws23", 140),
    ("PlayfulPurr9", 128),
    ("PurringClaws14", 29),
    ("WhiskeredMeow76", 109),
    ("MischievousCat89", 22),
    ("ClawedKitten51", 152),
    ("FuzzyTail58", 106),
    ("MischievousCat89", 119),
    ("PurringClaws14", 6),
    ("PurringClaws14", 40),
    ("CuddlyFeline45", 142),
    ("SassyMittens32", 8),
    ("FuzzyTail58", 100),
    ("SneakyWhiskers67", 122),
    ("WhiskeredMeow76", 156),
    ("SassyMittens32", 156),
    ("FluffyPaws23", 103),
    ("SassyMittens32", 13),
    ("PurringClaws14", 104),
    ("PurringClaws14", 141),
    ("FuzzyTail58", 88),
    ("MischievousCat89", 92),
    ("FuzzyTail58", 145),
    ("ClawedKitten51", 21),
    ("SassyMittens32", 117),
    ("FluffyPaws23", 22),
    ("SneakyWhiskers67", 22),
    ("SassyMittens32", 140),
    ("SassyMittens32", 38),
    ("PurringClaws14", 114),
    ("FuzzyTail58", 157),
    ("FluffyPaws23", 31),
    ("MischievousCat89", 47),
    ("FluffyPaws23", 102),
    ("SassyMittens32", 93),
    ("ClawedKitten51", 143),
    ("FluffyPaws23", 112),
    ("ClawedKitten51", 2),
    ("ClawedKitten51", 49),
    ("PurringClaws14", 79),
    ("ClawedKitten51", 149),
    ("FuzzyTail58", 61),
    ("SneakyWhiskers67", 38),
    ("SassyMittens32", 133),
    ("PlayfulPurr9", 9),
    ("FluffyPaws23", 118),
    ("SassyMittens32", 55),
    ("SassyMittens32", 140),
    ("ClawedKitten51", 74),
    ("PlayfulPurr9", 20),
    ("MischievousCat89", 71),
    ("SneakyWhiskers67", 63),
    ("PlayfulPurr9", 71),
    ("PurringClaws14", 85),
    ("PurringClaws14", 59),
    ("ClawedKitten51", 27),
    ("MischievousCat89", 11),
    ("PurringClaws14", 96),
    ("PurringClaws14", 98),
    ("MischievousCat89", 135),
    ("FuzzyTail58", 132),
    ("SassyMittens32", 25),
    ("PlayfulPurr9", 11),
    ("ClawedKitten51", 36),
    ("PurringClaws14", 128),
    ("WhiskeredMeow76", 75),
    ("FuzzyTail58", 20),
    ("ClawedKitten51", 130),
    ("FuzzyTail58", 28),
    ("FluffyPaws23", 48),
    ("SneakyWhiskers67", 21),
    ("SassyMittens32", 128),
    ("SneakyWhiskers67", 155),
    ("PlayfulPurr9", 6),
    ("CuddlyFeline45", 52),
    ("CuddlyFeline45", 46),
    ("PurringClaws14", 129),
    ("ClawedKitten51", 35),
    ("WhiskeredMeow76", 18),
    ("FluffyPaws23", 27),
    ("PlayfulPurr9", 32),
    ("PurringClaws14", 143),
    ("SneakyWhiskers67", 39),
    ("WhiskeredMeow76", 4),
    ("FuzzyTail58", 115),
    ("PurringClaws14", 155),
    ("ClawedKitten51", 95),
    ("ClawedKitten51", 26),
    ("WhiskeredMeow76", 58),
    ("PlayfulPurr9", 32),
    ("FuzzyTail58", 40),
    ("WhiskeredMeow76", 44),
    ("ClawedKitten51", 22),
    ("SneakyWhiskers67", 26),
    ("SassyMittens32", 72),
    ("MischievousCat89", 143),
    ("SneakyWhiskers67", 81),
    ("CuddlyFeline45", 128),
    ("SneakyWhiskers67", 19),
    ("SassyMittens32", 118),
    ("CuddlyFeline45", 27),
    ("ClawedKitten51", 11),
    ("PurringClaws14", 99),
    ("FuzzyTail58", 150),
    ("PlayfulPurr9", 114),
    ("PlayfulPurr9", 154),
    ("WhiskeredMeow76", 88),
    ("PlayfulPurr9", 98),
    ("PurringClaws14", 80),
    ("PlayfulPurr9", 84),
    ("SassyMittens32", 156),
    ("MischievousCat89", 123),
    ("WhiskeredMeow76", 67),
    ("FluffyPaws23", 97),
    ("FuzzyTail58", 11),
    ("WhiskeredMeow76", 75),
    ("CuddlyFeline45", 108),
    ("SassyMittens32", 114),
    ("FuzzyTail58", 141),
    ("CuddlyFeline45", 39),
    ("SassyMittens32", 92),
    ("FuzzyTail58", 68),
    ("MischievousCat89", 152),
    ("SneakyWhiskers67", 73),
    ("SassyMittens32", 10),
    ("CuddlyFeline45", 50),
    ("PlayfulPurr9", 105),
    ("SassyMittens32", 130),
    ("WhiskeredMeow76", 119),
    ("ClawedKitten51", 116),
    ("SassyMittens32", 153),
    ("FuzzyTail58", 12),
    ("PlayfulPurr9", 9),
    ("PurringClaws14", 91);

INSERT INTO following(username1, username2) VALUES
    ("PlayfulPurr9", "MischievousCat89"),
    ("ClawedKitten51", "FluffyPaws23"),
    ("PurringClaws14", "CuddlyFeline45"),
    ("ClawedKitten51", "SneakyWhiskers67"),
    ("MischievousCat89", "WhiskeredMeow76"),
    ("PurringClaws14", "SneakyWhiskers67"),
    ("PurringClaws14", "WhiskeredMeow76"),
    ("PurringClaws14", "SassyMittens32"),
    ("FuzzyTail58", "MischievousCat89"),
    ("FluffyPaws23", "CuddlyFeline45"),
    ("CuddlyFeline45", "MischievousCat89"),
    ("CuddlyFeline45", "PlayfulPurr9"),
    ("PurringClaws14", "ClawedKitten51"),
    ("PurringClaws14", "MischievousCat89"),
    ("WhiskeredMeow76", "FuzzyTail58"),
    ("SneakyWhiskers67", "SassyMittens32"),
    ("SassyMittens32", "FluffyPaws23"),
    ("FluffyPaws23", "MischievousCat89"),
    ("SneakyWhiskers67", "ClawedKitten51"),
    ("SassyMittens32", "PlayfulPurr9"),
    ("MischievousCat89", "SassyMittens32"),
    ("FluffyPaws23", "ClawedKitten51"),
    ("PlayfulPurr9", "ClawedKitten51"),
    ("MischievousCat89", "CuddlyFeline45"),
    ("FuzzyTail58", "SneakyWhiskers67"),
    ("MischievousCat89", "FluffyPaws23"),
    ("FuzzyTail58", "ClawedKitten51"),
    ("PlayfulPurr9", "WhiskeredMeow76"),
    ("FluffyPaws23", "SneakyWhiskers67"),
    ("SassyMittens32", "CuddlyFeline45");