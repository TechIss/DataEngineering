CREATE TABLE Movies (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Title varchar(255) NOT NULL,
    Duration TIME(N),
    Releasedate DATE, 
    Country varchar(255) NOT NULL,
    Discription varchar(255) NOT NULL,
    Trailer varchar(255) NOT NULL
);


INSERT INTO Movies
    (Title, Duration, Releasedate, Country, Discription, Trailer)
VALUES
    ('Mortal Kombat', '1h50m', 2021, 'US', 'Cole Young, een uitgerangeerde MMA-vechter, raakt betrokken bij de decennialange bovennatuurlijke oorlog tussen twee lang geleden overleden ninja-clans. Young raakt vervolgens met verschillende anderen verwikkeld in een vechttoernooi dat georganiseerd wordt door Raiden. Onder hen bevinden zich onder andere Jax en Sonya Blade, die een vreemde band met Young delen in de vorm van mysterieuze moedervlekken. Samen vechten ze tot de dood om de wereld te beschermen tegen de slechte tovenaar Shang Tsung', 'https://youtu.be/NYH2sLid0Zc'), 
    ('Nobody', '1h32m', 2021, 'US', 'Hutch Mansell is vader die overal waar hij komt geen enkele indruk achterlaat. Wanneer twee dieven in zijn huis inbreken is dit voor Hutch het ultieme moment om zijn woede, waarmee hij al lang rondloopt, kwijt te kunnen. Op zijn weg naar brute vergelding worden duistere geheimen uit zijn verleden onthuld.', 'https://youtu.be/wZti8QKBWPo'), 
    ('The Marksman', '1h48m', 2021, 'US', 'Langs de grens tussen de VS en Mexico in Arizona heeft Jim Hanson, een veeboer en Vietnamveteraan, het moeilijk. Zijn geliefde vrouw is net overleden aan kanker en de bank staat op het punt zijn enorme eigendom af te nemen. Zijn rustige leven wordt plotseling verstoord door de onverwachte komst van twee illegale immigranten die de grens naar zijn land oversteken.', 'https://youtu.be/lEBPNi4bEbc'), 
    ('Godzilla vs. Kong ', '1h53m', 2021, 'US', 'In een nieuwe wereld leven mensen en titanen samen. Maar er is een geheime factie die wil dat de titanen oorlog met elkaar voeren, een strijd die al het leven op aarde zou kunnen bedreigen. Ondertussen trekt een vreemde seismische activiteit op Skull Island de aandacht van zowel Godzilla als Kong. Een oorlog lijkt onafwendbaar.', 'https://youtu.be/odM92ap8_c0'), 
    ('Baby Driver', '1h55m', 2017, 'UK', 'Baby Driver volgt een jonge, getalenteerde chauffeur van vluchtauto die leidt aan tinnitus en vertrouwt op het ritme van zijn persoonlijke soundtrack om de beste te kunnen worden. Wanneer hij de vrouw van zijn leven ontmoet, doet hij een poging om uit de criminele wereld te stappen.', 'https://youtu.be/6XMuUVw7TOM'),
    ('Kingsman: The Secret Service', '2h9m', 2014, 'UK', 'Gary, een jongeman wiens leven dreigt te ontsporen, vult zijn dagen door elke avond te zuipen met vrienden. Harry Hart, een veteraan MI6 agent van een geheime organisatie, probeert hem te redden en zodoende niet te laten omgaan met de verkeerde mensen.', 'https://youtu.be/kl8F-8tR8to');