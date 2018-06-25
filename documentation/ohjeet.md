# Ohjeet

## Sovelluksen asentaminen ja käynnistäminen  

Sovellus pyörii valmiina [Herokussa](https://tsoha-foutain-pen-store.herokuapp.com/). 
Sovelluksen voi myös ladata omalle koneelle painamalla repositorion pääsivulla olevaa vihreää "Clown or Dowload"-painiketta ja valitsemalla "Dowload ZIP".  
Ladattuasi ZIP-tiedoston, pura ohjelma haluamaasi kansioon. Sovelluksen käyttämät riippuvuudet löytyvät tiedostosa nimeltä _requirements.txt_. Riippuvuudet saadaan ladattua komennolla ``` pip install -r requirements.txt ```. Tässä kannattaa käyttää myös virtuaaliympristöä (venv).  
Kun ohjelma on ladattu ja purattu ja käytössäsi on ohjelman tarvitsemat riippuvuudet, navigoi sovelluksen root-kansioon (_tsohasovellus_) ja käynnistä sovellus komentamalla ``` python run.py ```.  
Nyt sovelluksen pitäisi olla päällä ja pääset käyttämään sitä selaimellasi.  

## Sovelluksen käyttäminen  

Etusivulla näkyy (hyvin) lyhyt kuvaus sivusta ja hieno kuva täytekynästä. Lisäksi sivun yläreunassa on navigointi-palkki.  
Kirjautumatta ei sivulla voi tehdä juuri mitään, joten ensimmäisenä kannattaa joko kirjautua olemassa olevaa käyttäjää käyttäen tai rekisteröidä uusi käyttäjä.  
Jos kirjautumaton käyttäjä yrittää painaa jotain muuta navigointi-palkin painiketta, ohjataan hänet kirjautumissivulle. 
Jos haluat täydet oikeudet sivule, kirjaudu järjestelmänvalvojana. Tämä onnistuu käyttämällä käyttäjänimeä "admin" ja salasanaa "admin".  
Jos haluat luoda oman käyttäjän, onnistuu se rekisteröintisivulta. Rekisteröityäsi uuden käyttäjän tulee sinun vielä kirjautua.  
Kun olet kirjautunut, pääset käyttämään vapaasti sivun kaikkia toimintoja (muiden käyttäjien poistaminen on varattu järjestelmänvalvojalle).  
Navigointi-palkin linkint ovat vasemmalta oikealle seuraavat: "My Collection", "All Fountain Pens", "Add New" ja "Users".  
  
_HUOM:_ Sovelluksessa on tarkoitus käyttää järjestelmänvalvojana ainoastaan ennalta luotua admin- käyttäjää.  
Jos kuitenkin tahdot luoda uuden järjestelmän valvojan tai muuttaa olemassa olevan adminin tunnuksia (mikä saattaa olla hyväkin idea),  
tulee tämä tehdä suoraan tietokantaan. Eli avaa application kansiossa oleva pens.db tiedosto esim. SQLite:llä ja luo uusi järjestelmän valvoja INSERT INTO lauseella.  

### My Collection  

My Collection- painike vie sinut sivulle, jossa voi tarkastella ja hallinnoida omaa kokoelmaasi ja lisätä siihen kyniä. Kokoelma näkyy taulukossa sivun yläosassa jossa jokainen rivi vastaa yhtä kynää. 
Sarake Nib tarkoittaa kynän kärjen koko/mallia, muut sarakkeet lienee itsestäänselviä.  
Sivun alaosassa on lomake, jolla voit lisätä kokoelmaasi kynän. Tämä onnistuu valitsemalla ensin sivulle jo lisätty kynä monivalintakentästä ja syöttämällä kynän kärjen koko ja kynän väri ja lopuksi painamalla Add To My Collection- painiketta.  
Mikäli haluat poistaa kokoelmastasi kynän, onnistuu tämä yksinkertaisesti painalla taulukossa olevaa Delete- nappulaa kynää vastaavalla rivillä. Tämä poistaa kynän vain oasta kokoelmastasi.  
Delete- painikkeen vieressä olevaa View- painiketta painamalla pääset tarkastelemaan kyseisen kynän tarkempia tietoja. Tällöin näytetään kynän malli, kärjen koko, väri, aika milloin kynä on lisätty kokoelmaasi ja aika milloin viimeksi muokkasit sen tietoja.  
Samalla sivulla voit myös muokata kynän tietoja käyttämällä Edit Information- otsikon alla olevaa lomaketta.  

### All Fountain Pens  

All Fountain Pens- painike näyttää listan kaikista sivulla lisätyistä kynistä. Taulukosta näkyy kynän malli, sen valmistaja ja alkuperämaa.  
Lisäksi jokaisella riviltä löytyy Delete- ja View- painikkeet. Delete poistaa kyseisen kynän ja View avaa sivun jossa kerrotaan kynän tarkemmat tiedot. 
Mallin, alkuperämaan ja valmistajan lisäksi kynästä näkyy milloin se on lisätty sivulle ja milloi sen tietoja on viimeksi muokattu.  
Samalla sivulla voi myös tuttuun tapaan muokata kynän tietoja käyttämällä Edit This Pen- otsakkeen alta löytyvää lomaketta. Huomaathan, että jos poistat kynän tai muokkaat sen tietoja, näkyvät muutokset myös kaikkien niiden käyttäjien kokoelmissa joihin kynä on listattu. 
Mieti siis tarkkaan ennen kuin poistat kynän, joku saattaa jäädä kaipaamaan sitä!  

### Add New  

Add New- painike avaa lomakkeen jolla voit lisätä sivulle uuden kynän. Kynästä syötetään sen malli, alkuperämaa ja valmistaja.  
Kynän luomisen ajankohta tallentuu automaattisesti, joten siitä ei tarvitse huolehtia.  

### Users  

Users- painike voi näyttää kaksi erilaista näkymää. Jos olet kirjautuneena tavallisella käyttäjänä, näkyy sivulla taulukko jossa on jokaisen käyttäjän nimi ja heidän kokoelmansa koko.  
Jos taas olet kirjautunut järjestelmänvalvojana (_admin_), näet lisäksi jokaiselle rivillä Delete- painikkeen. Tämä painike poistaa kyseisen käyttäjän sivulta. 
Tämän jälkeen käyttäjällä ei luonnollisesti voida enää kirjautua.  
  
_HUOM:_ Taulukon Name- sarakkeiden arvot saattavat näyttää erikoisilta. Tämä johtuu eri tietokantojen välisestä erosta. Herokun käyttämää PostgreSQL:ää käyttämällää nimet tulevat oikein näkyviin, mutta
joidenkin tietokantojen kanssa kenttään saattaa livahtaa ylimääräisiä merkkejä.  

## Muuta Huomioitavaa

* Sivu käyttää bootstrap-kirjastoa tyylittelyyn.  
* Sivulla käytetty kuva on varustettu Creative Commons- lisenssillä. Linkki alkuperäiseen kuvaan löytyy kuvan alta.  
* Sivun Footterissa löytyy tekijän nimi ja linkki sovelluksen GitHub repositorioon.  





