# PythonProject

Student 2:
Rangiranje stranica:
    Na rang stranice je najvise uticao broj trazenih reci u stranicama koje sadrze link na trazenu stranicu. 
    Prolaskom kroz sve izlazne linkove, pronalazimo koje stranice imaju izlazne linkove ka trazenoj stranici.
    Iz tih stranica pomocu parsera brojimo broj trazenih reci iz upita. Na kraju imamo ukupan broj reci za rang 3,
    a ako nam se sve reci iz upita pojavljuju u stranici iz koje smo pretrazivali reci, ukupan rang sabiramo sa 5.
    U poslednjem koraku mnozimo ukupnu vrednost sa 3.
    Broj pojavljivanja trazenih reci na trazenoj stranici je drugo po uticaju na ukupni rang. Pronadjemo ukupan broj
    reci i ako se sve trazene reci pojavljuju na istoj stranici, ukupan broj reci sabiramo sa 5 i na kraju celu vrednost
    mnozimo sa 2.
    Broj linkova iz drugih stranica na pronadjenu stranicu je trece po uticaju na ukupni rang, i tu je samo izbrojan 
    broj ulaznih linkova za trazenu stranicu.
    Ukupan rang se dobija sabiranjem prethodne tri vrednosti.
    Zbog ponovnog parsiranja, rangiranje dosta dugo traje, pa je najbolje da se proveri za manje datoteke.
Paginacija:
    Na pocetku korisnik unosi koliko stranica zeli da prikaze. Pri pokretanju se ispisuju date komande za prikaz
    stranica.

Student 1:
    1.
    #trie, #parsiranje_skupa_HTL_dokumenata
    Prvo je potrebno napravatiti trie stablo (strukturu podataka) u koje cemo smestati podatke (reci i linkove) tokom parsiranja.
    Zato je potrebno implementirati funkcije za dodavanje i pretragu koja ce nam kasnije biti potrebna za upite. Trie struktura je
    efikasna za brzu pretragu podataka, ali zahteva puno prostora za skladistenje.
    Koristeci parser koji nam je dat(korisnik unosi putanju direktorijuma) prolazimo kroz direktorijum i parsiramo samo
    HTML dokumente i dodajemo ih u stablo pomocu funkcije
    za dodavanje iz Trie strukture - implementirano u Main-u.
    2.
    #unos_upita, #pretraga_dokumenata, #osnovne_skupovne_operacije
    Sve tri stavke implementirane su u ParsiranjeUpita. Korisnik unosi upit od jedne ili vise reci. Provera validnosti upita
    vrsena je na sledeci nacin:
    1. Ako je upit prazan, on nije validan, trazi se novi unos.
    2. Ako upit ima vise od tri reci, a u njemu se nalazi logicki operator - upit nije validan, trazi se novi unos
    jer ukoliko u upitu postoji logicki operator, on mora da bude u formatu rec1 LogOp rec2
    3. Ako upit ima jednu, dve ili tacno 3 reci proverava se da li se logicki operator nalazi na prvom ili poslednjem mestu
     jer to takodje nije ispravan upit, trazice se novi unos upita. Za jednu ili dve reci, upit prolazi samo ukoliko su unesene
     reci razdvojene razmakom bez logickih operatora.
    Nakon provere validnosti upita, prelazimo na pravljenje rezultata pretrage. Za ovo nam je potrebna struktura podataka Set, koja
    u sebi sadrzi operacije za uniju, presek i komplement skupa. Sam rezultat pretrage je skup HTML stranica odnosno Set.
    Pretraga dokumenata i osnovne skupvne operacije implementirane su zajedno u jednoj petlji. Ukoliko se radi o obicnom upitu
    vrsi se samo operacije unije, i na rezultat pretrage (set) dodaju se rezultati za svaku rec iz upita. Ukoliko se radi o logickom
    upitu, nakon utvrdjivanja operacije formira se rezultat pretrage tako sto u zavisnosti od upita, na set primenjujemo operacije
    koje su prethodno implementirane u Set strukturi podataka 
    
    