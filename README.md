
# Tsoha: täytekynäkauppa

Harjoitustyöni on mukautettu versio "kurssitarjonta ja kurssipaikan varaus"-esimerkistä. Aiheeksi tulee siis "Fountain Pen Store", eli täytekynä kauppa. Järjestelmään voi kirjautua adminina jolloin kauppaan voi lisätä kyniä ja muokata niiden tietoja. Asiakkaana kirjautuva voi ostaa kyniä, jolloin hän saa ohjeet maksusta. Halutessaan hän voi pyytää laskua. Ostoista näkyy mitä kyniä käyttäjä on ostanut ja onko hän maksanut sen. Käyttäjä voi itse perua oston ja admin (kauppa) voi perus oston käyttäjän puolesta mikäli käyttäjä ei ole vielä maksanut kynää. Mikäli kynää ei makseta tietyn ajan kuluessa, saa hän automaattisesti laskun. Admin oi vapaasti muokata kynien tietoja sivulla ja myös poistaa kyniä järjestelmästä, jolloin osto automaattisesti peruutetaan kaikilta käyttäjiltä jotka eivät ole jo maksaneet.

Jos kynä on jo maksettu, ajatellaan sen lähtevn kaupasta välittömästi, joten kynän poistaminen kaupasta ei poista sitä asiakkaan omista ostoista. Jos kynä on kirjattuna asikkaan Ostoihin ja se on maksettu, voidaan se ajatella olevan osa asiakkaan kokoelmaa. Asiakas voi halutessaan tarkastella vain niitä kyniä, jotka ovat hnen omistuksessaan (piilottaa peruutetut ja maksamattomat kynät).

Admin voi tarkkailla jokaisen asikkaa ostoja ja niiden statusta (peruutettu/aktiivinen, maksettu/maksamaton). Admin näkee myös ketkä kaikki käyttäjät ovat ostaneet tietyn kynän. 

[Tietokantakavio](/documentation/tietokantakaavio)
[User Stories](/documentation/user_stories)
[Linkki Herokuun](https://tsoha-foutain-pen-store.herokuapp.com/)


