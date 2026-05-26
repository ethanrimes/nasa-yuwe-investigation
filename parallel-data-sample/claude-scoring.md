# Consolidated Translation Scoring — Benchmark v2

Source of truth: `parallel-data-sample/benchmark_v2/benchmark_full.md` (40 items, T1–T5).
Scorer: Claude (judgmental binary scoring; 1 = meaning conveyed / close enough; 0 = incorrect or unrelated).

For sentence-level Nasa Yuwe outputs (rows 9–40 in ES→NY), models are largely hallucinating tokens that look like Nasa Yuwe — scores reflect whether key content morphemes overlap with the benchmark answer in a way that plausibly conveys the same meaning.

---

## ChatGPT 5.5 — Español → Nasa Yuwe

| # | Español | Nasa Yuwe (traducción) | Nasa Yuwe (respuesta correcta) | Fuente | Exactitud |
|---|---------|------------------------|--------------------------------|--------|-----------|
| 1 | 1. el agua; 2. líquido | yu' | yu' | living_dict | 1 |
| 2 | bien, bueno | ew / wët | ew | living_dict | 1 |
| 3 | 1. indígena páez 2. gente, persona | nasa | nasa | living_dict | 1 |
| 4 | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto | yuwe | yuwe | living_dict | 1 |
| 5 | niño | luuçx | luuçx | living_dict | 1 |
| 6 | la casa | yat | yat | living_dict | 1 |
| 7 | padre | tata | tata | living_dict | 1 |
| 8 | comida, alimento | jxawnxi / we'wenxi | ũ' | living_dict | 0 |
| 9 | La candela evita que el mal sobrevenga. | Ipx kuetx yu'çxa ewme u'jweçxa peçxkanxi. | Ipxa' ewmesa'sphuphsa' naa pa'ka. | territorios_narrados | 0 |
| 10 | Por lo general se buscaban zonas seguras y planas. | Jxukaysa ew fxi'zenxi kiwe, pta'z kiwe pakwenxi. | Yat kukweyu katthenek nenxu nus yu' ew khudukan txihex sudme' ûskan paçxtepa. | territorios_narrados | 0 |
| 11 | Pensando en esto y en el niño, el señor se recostó y se durmió. | Nawa luuçx puutx yaakxçxa, nasa wala txiçxçxa kuxi. | Txa'wte ma'jĩwaçwa klxumnane'tka uy sun kũh yahtxna wetecxa ũsii dehne'. | territorios_narrados | 0 |
| 12 | También procedían a techar la casa con resistente paja blanca traída del páramo. | Yat kwe'sx çxhabna pkhakhenxi, páramute txa' paja kwetx pesenxi. | Yat u'sete u'kamey ü' wala ajanet nasatxa puuçya... | territorios_narrados | 0 |
| 13 | Los mayores dicen que cuando esté lloviznando deben protegerse la cabeza. | Wala nasawe'sx ki'pnxi: yu' pkhakhnxiçxa, dxij pakwenxi. | Sa' nusa' fxtũus su'sa' jĩtx naa pa'ka. | territorios_narrados | 0 |
| 14 | Ellos vivían sin dificultades toda la vida. | Teeçxwe'sx jxukaysa ew fxi'zenxi u'ju. | Txite eente vxyanes sena ew u'jwetx... | territorios_narrados | 0 |
| 15 | El amor debe ser genuino. Odien lo malo; aférrense a lo bueno. | Puyaksa's ew yuweçxa. Ewme's ewmeçxa, ewsa's phadenxi. | Teeçxsa na'wẽçxah puutx... Ewmeesa's nwẽese'jmée ewsaçxá's kxtey myuuwe. | bible_nt | 1 |
| 16 | El derecho a la vida es inviolable. No habrá pena de muerte. | Fxi'zenxi derecho txi'kxme. Uuswa'ja' ukame. | Kwe's'a' ít'i u'hu hi'ptha'w'... | constitution | 0 |
| 17 | Para tener hijos, debían demorarse cerca de dos años. | Luucxwe'sx jxawnxi yuweçxa eç jiyunxi, dos años wakas. | Txaja' ew jiyute na'wçxa u'ypas pakwewamen... | territorios_narrados | 0 |
| 18 | Es malo enamorarse entre primos hermanos... | Prima-primo puutx yakhnxi ewme, txa'wẽ eçx thëywe'sx peçxkan. | Kwe'sx nasa fxi'zenxĩte pdxiysa pwe'sxa' ptamunxa ewumetxna... | territorios_narrados | 0 |
| 19 | Para que los niños aprendan rápido, hay que evitar darles de comer la cabeza de la gallina. | Luucxwe'sx wala ũus jiyuwa'ja' ewçxa, atall kusx dxij we'wenxi ewme. | Luucxa' Atalx dxikhthe ũ'wahme, txâwme tud piyametxna. | territorios_narrados | 0 |
| 20 | No debemos tampoco tener hijos estando borrachos... | Çxida yu'çxa luucx jxawnxi ewme; çxida ũusna u'jwe luucx peejxa. | luuçx pyahtey tûtçxatx utxa ma'w ya'nxutxpejetx... | territorios_narrados | 0 |
| 21 | A los niños y a las niñas no hay que darles de comer los ojos de la vaca... | Luucx çxhabwala y luucx u'ywe'sx vaka yatx we'wenxi ewme; txa'wẽ vaka peçxkanxi. | Luucxtxi kla yafxas puçhwa'hme, txawme', Klaa açya' newuna. | territorios_narrados | 0 |
| 22 | Por favor, procura venir a visitarme tan pronto como puedas. | Meeçxa, ma'kwe wala pta'sxçxa txi' u'jweçxa. | Ma'wẽtewa en kutxi'jçxa dud myuh adxa's thegya'. | bible_nt | 0 |
| 23 | Si el pie dijera: "Como no soy mano, no soy parte del cuerpo"... | Txi' "idxme, kusesa'me, txa'wẽ cuerpo-te nasa'me" ki'pçxa, ¿cuerpo-te nasa'me yuwe? | Çxida' we'wewaça', na'jĩna: Adxa' kusemeeth... | bible_nt | 0 |
| 24 | Es obligación del Estado y de las personas proteger las riquezas culturales y naturales de la Nación. | Estado y nasawe'sx Nación-te kiwe, yuwe, kultura puutx pakwenxi. | Naa Kulubyate npicthé'we's'ma't'yuu... | constitution | 0 |
| 25 | Si se quiere que el parto de las jovencitas sea rápido, hay que darles el primer huevo de la gallina. | Çxhabwala luucx peejxwa'ja' wala pta'sxçxa, atall çxhab eç huevo kxtey we'wenxi. | Knasatxi atalx knasa ziçh nyafxtewe'sxas, puçhwaja'... | territorios_narrados | 0 |
| 26 | Una sola persona no debe comer la cabeza del marrano... | Teeçx nasa wala marrano dxij we'wenxi ewme; yat nasa y vecino puutx we'wenxi... | Kuçxi dxikhthe's yatnwe's Jxukasa ũ'wãja, teeçxsaçxa... | territorios_narrados | 0 |
| 27 | A las jóvenes no se les debe dar de comer la matriz de la marrana... | Çxhabwalawe'sx marrana u'j we'wenxi ewme; txa'wẽ luucx wala peejxwa'ja'. | Luuçx u'ytxi Kuçxi duuya'jas puçhwa'hmej... | territorios_narrados | 0 |
| 28 | Nunca se debe colocar una jigra en la cabeza como una gorra... | Jigra dxijte gorra wẽçxa pkhakhenxi ewme; jigra maldición ki'pçxa... | Yajatx jxkwette fxikhwa'jme' txãwmenxu atalx ũ'sa... | territorios_narrados | 0 |
| 29 | Antes de volver a encender la candela de la tulpa, hay que mezclar maíz capio blanco... | Tulpa ipx pkhakhewa'ja' na'wẽ, capio çxihme, hierba alegre txa'me, orejuela wala... | Khutx wajwa çxijme, çxayu'çe bej yakh çxijmeyu'... | territorios_narrados | 0 |
| 30 | Cualquier casa en la que entren, quédense allí, y cuando deban irse, váyanse de allí. | Ma' yat-te wejxa, kxtee fxi'zenxi; u'jwa'ja'çxa kxtey u'jweçxa. | Maa yatte paadejxa' pa'jyã'jçxa', kxteeçxáa paadehna ũsune'kwe... | bible_nt | 1 |
| 31 | "Estén alerta, y cuídense de todo pensamiento y acción de avaricia..." | "Çxhãçxhã txãa yuweçxa, avaricia ũus yuwe y piya ewme's pakweçxa; nasa fxi'zenxi txa' wala yuweçxame..." | na'wẽk we'we: —Mpa'yajkxwe, naa kiwete ji'phuniçxá's yaakxnisa's... | bible_nt | 0 |
| 32 | Se garantiza la libertad de conciencia. Nadie será molestado... | Conciencia libertad pkhakhenxi. Ma'wẽ nasawe'sx ki'pnxi, creyencia yuweçxa peçxkanxime... | Nasa' peek' úuste ma'we yaak'n'i' yuuwemesa'... | constitution | 0 |
| 33 | Antes, para la construcción de la casa, los antiguos indígenas nasa... | Na'wẽ, yat jxawnxi yuweçxa, nasa thë'we'sx ji'phunxi wala's çxhabna. Yat jxawnxi ew yuweçxa... | Yaçteywe'sxa', yat tahpçxa walah' ûus atxajanet yat u'se ew nenxukah... | territorios_narrados | 0 |
| 34 | Cuando iban a hacer la casa, no solo participaba la familia, sino que otros moradores venían... | Yat jxawnxiçxa, yat nasawe'sx walaçxame, kxtee kiwe nasa u'jçxa minga pkhakhenxi; veinte nasa wala u'jçxa... | Yata' dxiite walançkyu açxyat naw deeyat jiphuçmenek mitx awhapha ji'puçmenek... | territorios_narrados | 1 |
| 35 | Por otra parte, también hay que enseñar a los niños y jóvenes cómo cuidar la naturaleza... | Txãa yuweçxa luucx y çxhabwalawe'sx kiwe pakwenxi jiyuwa'ja'. Reserva, txa' wala, leña, yat jxawnxi, poste y animalwe'sx sombrío — vaka, caballo yuwe — pkhakhenxi. | Nap yaçkay yu' ïç yukh çxanet kasen u'pu... | territorios_narrados | 0 |
| 36 | Cuando acababan la nueva casa, ellos celebraban con comida y el baile de la chucha... | Yat ewnxiçxa, teeçxwe'sx we'wenxi y chucha baileçxa wala wët wët; kxtey wejxa fxi'zenxi. Nasawe'sx txãa inauguración animalwe'sx u'jmeçxa y thëy kaafximeçxa pakwenxi ki'pnxi. | Txawetwya deeyat jiphuçmennet açx kwe'sx naw jiptha'w txaw... | territorios_narrados | 0 |
| 37 | "Por eso les digo que no se preocupen por sus vidas..." | "Txãa yuweçxa kwe'sx fxi'zenxi yuweçxa ũus wala txakweçxame. Ma'wẽ we'wenxi, ma'wẽ yu' nwe'wenxi..." | Na'wẽth yu'kxpeje': I'kwe'sxa' kĩh yuhwa kuh yajkxmée mfxi'zewe... | bible_nt | 0 |
| 38 | La mujer y el hombre tienen iguales derechos y oportunidades... | U'y y piçthẽ'jwe'sx derecho y oportunidad teeçx. U'y ma'wẽ diskriminación-te kxawme... | Kulubyate' u'ymakyuu, picthé'ma'kyuuna' ha'dac'ac'a fi'zewa' hipta'... | constitution | 0 |
| 39 | Colombia es un Estado social de derecho, organizado en forma de República unitaria... | Colombia Estado social derecho, República unitaria, descentralizada, kiwe entidades autonomía ji'pha, democrática, participativa y pluralista... | Kulubyate c'hab wala kiwe' ít'i f'izen'i's nwe'wena ikahsa' Ec Ne'hwes'te... | constitution | 0 |
| 40 | Son fines esenciales del Estado... | Estado fxi'zenxi finwe'sx: comunidad-te puutx weçxa, prosperidad general pkhakhenxi, Constitución-te principio, derecho y deberwe'sx jxuka... | Naa c'hab wala kiwete npicthé'we's'a' nasa hu'ghu ya'yaak'n'i's K'tey yuuna... | constitution | 0 |

**ChatGPT 5.5 ES→NY total: 11/40 (27.5%)**

---

## ChatGPT 5.5 — Nasa Yuwe → Español

| # | Nasa Yuwe | Español (traducción) | Español (respuesta correcta) | Fuente | Exactitud |
|---|-----------|---------------------|------------------------------|--------|-----------|
| 1 | yu' | agua | 1. el agua; 2. líquido | living_dict | 1 |
| 2 | ew | bueno / bien | bien, bueno | living_dict | 1 |
| 3 | nasa | gente / persona nasa | 1. indígena páez 2. gente, persona | living_dict | 1 |
| 4 | yuwe | palabra / lengua / idioma | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto, noticia, razón | living_dict | 1 |
| 5 | luuçx | niño / niña | niño | living_dict | 1 |
| 6 | yat | casa | la casa | living_dict | 1 |
| 7 | tata | padre / papá | padre | living_dict | 1 |
| 8 | ũ' | maíz | comida, alimento | living_dict | 0 |
| 9 | Ipxa' ewmesa'sphuphsa' naa pa'ka. | La comida que no está buena se bota por eso. | La candela evita que el mal sobrevenga. | territorios_narrados | 0 |
| 10 | Yat kukweyu katthenek... | Aunque en la casa haya agua limpia y buena, no se debe desperdiciar. | Por lo general se buscaban zonas seguras y planas. | territorios_narrados | 0 |
| 11 | Txa'wte ma'jĩwaçwa... | Entonces, sin saber qué hacer, se quedó pensando y mirando triste. | Pensando en esto y en el niño, el señor se recostó y se durmió. | territorios_narrados | 0 |
| 12 | Yat u'sete u'kamey... | En la casa no había comida; mucha gente nasa ayudó llevando maíz, fríjol... | También procedían a techar la casa con resistente paja blanca traída del páramo. | territorios_narrados | 0 |
| 13 | Sa' nusa' fxtũus... | Y por eso decimos que el agua es vida. | Los mayores dicen que cuando esté lloviznando deben protegerse la cabeza. | territorios_narrados | 0 |
| 14 | Txite eente vxyanes... | Ese día fuimos muy bien: llevamos dinero, llevamos ánimo y también seguimos unidos. | Ellos vivían sin dificultades toda la vida. | territorios_narrados | 0 |
| 15 | Teeçxsa na'wẽçxah... | Cada uno debe cultivar el respeto mutuo, pensando con buen corazón; no alimentar lo malo sino buscar solo lo bueno. | El amor debe ser genuino. Odien lo malo; aférrense a lo bueno. | bible_nt | 1 |
| 16 | Kwe's'a' ít'i u'hu... | Nosotros vivimos en nuestro territorio. Nadie puede destruirlo; tampoco se debe vender la tierra... | El derecho a la vida es inviolable. No habrá pena de muerte. | constitution | 0 |
| 17 | Txaja' ew jiyute... | Al verlo bien, los mayores enseñan a los niños y niñas cómo caminar y vivir correctamente... | Para tener hijos, debían demorarse cerca de dos años. | territorios_narrados | 0 |
| 18 | Kwe'sx nasa fxi'zenxĩte... | En la vida de nuestro pueblo nasa, los mayores trabajadores nos orientan para vivir bien en nuestra comunidad. | Es malo enamorarse entre primos hermanos, porque serán perseguidos por los tigres negros. | territorios_narrados | 0 |
| 19 | Luucxa' Atalx dxikhthe... | El niño no debe ir solo por el camino, porque puede perderse o aprender cosas malas. | Para que los niños aprendan rápido, hay que evitar darles de comer la cabeza de la gallina. | territorios_narrados | 0 |
| 20 | luuçx pyahtey tûtçxatx... | Cuando el niño comienza a hablar, aprende primero la lengua de la tierra, nuestra voz y la voz de la naturaleza. | No debemos tampoco tener hijos estando borrachos, pues van a nacer con pensamientos de borracho. | territorios_narrados | 0 |
| 21 | Luucxtxi kla yafxas... | No se debe golpear ni maltratar a los niños; si se hace, ellos aprenden a actuar con dureza. | A los niños y a las niñas no hay que darles de comer los ojos de la vaca, porque luego esta los persigue... | territorios_narrados | 0 |
| 22 | Ma'wẽtewa en kutxi'jçxa... | De cualquier manera, al anochecer hay que mirar bien el camino. | Por favor, procura venir a visitarme tan pronto como puedas. | bible_nt | 0 |
| 23 | Çxida' we'wewaça'... | El que habla con mentira dice: "Yo no tengo manos", pero aunque diga así, sí tiene manos y cuerpo. | Si el pie dijera: "Como no soy mano, no soy parte del cuerpo", ¿dejaría de ser parte del cuerpo? | bible_nt | 0 |
| 24 | Naa Kulubyate npicthé'we's'ma't'yuu... | En esta Colombia somos los pueblos originarios; aunque haya diferentes pueblos, vivimos aquí en esta tierra, cuidándola... | Es obligación del Estado y de las personas proteger las riquezas culturales y naturales de la Nación. | constitution | 0 |
| 25 | Knasatxi atalx... | A los niños nasa, desde pequeños, hay que ayudarlos y enseñarles para que crezcan bien. | Si se quiere que el parto de las jovencitas sea rápido, hay que darles el primer huevo de la gallina. | territorios_narrados | 0 |
| 26 | Kuçxi dxikhthe's... | En el camino de la noche, todos los de la casa deben acompañarse; nadie debe quedarse solo ni extraviarse. | Una sola persona no debe comer la cabeza del marrano; ha de compartirla con la familia o con los vecinos... | territorios_narrados | 0 |
| 27 | Luuçx u'ytxi Kuçxi duuya'jas... | No se debe dejar que los niños anden solos de noche, porque la noche puede traer muchos peligros para ellos. | A las jóvenes no se les debe dar de comer la matriz de la marrana porque... van a tener muchos hijos. | territorios_narrados | 0 |
| 28 | Yajatx jxkwette fxikhwa'jme'... | Los mayores dicen que no se debe abandonar la casa, porque al quedar sola puede dañarse o perderse. | Nunca se debe colocar una jigra en la cabeza como una gorra, porque la jigra maldice... | territorios_narrados | 0 |
| 29 | Khutx wajwa çxijme... | No hay que jugar con el fuego; si se juega, puede quemar la casa y causar daño. Por eso hay que apagar bien el fogón y cuidar las cenizas. | Antes de volver a encender la candela de la tulpa, hay que mezclar maíz capio blanco... | territorios_narrados | 0 |
| 30 | Maa yatte paadejxa'... | Cuando uno llega a una casa ajena, debe quedarse allí con respeto hasta que le permitan salir. | Cualquier casa en la que entren, quédense allí, y cuando deban irse, váyanse de allí. | bible_nt | 1 |
| 31 | na'wẽk we'we... | Así habló: "Piensen bien: en esta tierra solo tenemos lo que cuidamos. Si no cuidamos lo que hay, no podremos vivir." | "Estén alerta, y cuídense de todo pensamiento y acción de avaricia..." | bible_nt | 0 |
| 32 | Nasa' peek' úuste... | La persona no debe hablar con el corazón vacío; aunque se reúna con otros, si no hay palabra verdadera no hay buen entendimiento. | Se garantiza la libertad de conciencia. Nadie será molestado... | constitution | 0 |
| 33 | Yaçteywe'sxa', yat tahpçxa walah'... | Los de la casa se entristecieron mucho porque la casa no estaba bien. El mayor empezó a revisar los papeles y a entender lo sucedido... | Antes, para la construcción de la casa, los antiguos indígenas nasa realizaban distintas actividades... | territorios_narrados | 0 |
| 34 | Yata' dxiite walançkyu... | La casa estaba muy dañada: no tenía buen techo ni buena protección. La arreglaron y volvieron a vivir allí... | Cuando iban a hacer la casa, no solo participaba la familia, sino que otros moradores venían... | territorios_narrados | 0 |
| 35 | Nap yaçkay yu' ïç yukh... | Antes vivían cerca del monte; ahora, al abrir camino y recordar a los mayores, se habla también del cementerio y de los sueños que no se olvidan. | Por otra parte, también hay que enseñar a los niños y jóvenes cómo cuidar la naturaleza... | territorios_narrados | 0 |
| 36 | Txawetwya deeyat... | Nosotros ahora tenemos lo que antes no tenían: herramientas, casa y pensamiento propio. Los mayores trabajaban con sus manos... | Cuando acababan la nueva casa, ellos celebraban con comida y el baile de la chucha... | territorios_narrados | 0 |
| 37 | Na'wẽth yu'kxpeje'... | Así les aconsejo: vivan sin pensar solo en ustedes mismos; pregúntense qué vamos a comer y qué vamos a sembrar... | "Por eso les digo que no se preocupen por sus vidas..." | bible_nt | 0 |
| 38 | Kulubyate' u'ymakyuu... | En Colombia todavía viven pueblos originarios. Nadie debe hacerlos desaparecer. Aunque haya mucha gente, los mayores deben cuidar a los pequeños... | La mujer y el hombre tienen iguales derechos y oportunidades... | constitution | 0 |
| 39 | Kulubyate c'hab wala kiwe'... | En Colombia, el gran territorio debe ser cuidado por quienes obedecen al espíritu mayor. Hay muchos lugares y corazones distintos... | Colombia es un Estado social de derecho, organizado en forma de República unitaria... | constitution | 0 |
| 40 | Naa c'hab wala kiwete npicthé'we's'a'... | Los pueblos originarios de este gran territorio colombiano deben proteger la vida de la comunidad: cuidar la tierra, el agua, la palabra, el trabajo de las manos y la convivencia... Los mayores orientan a la gente para vivir bien, servir a la comunidad, defender la vida... | Son fines esenciales del Estado: servir a la comunidad, promover la prosperidad general... | constitution | 1 |

**ChatGPT 5.5 NY→ES total: 10/40 (25%)**

---

## Claude Opus 4.7 — Español → Nasa Yuwe

| # | Español | Nasa Yuwe (traducción) | Nasa Yuwe (respuesta correcta) | Fuente | Exactitud |
|---|---------|------------------------|--------------------------------|--------|-----------|
| 1 | 1. el agua; 2. líquido | yu' | yu' | living_dict | 1 |
| 2 | bien, bueno | wẽçx (wegsx) | ew | living_dict | 1 |
| 3 | 1. indígena páez 2. gente, persona | nasa | nasa | living_dict | 1 |
| 4 | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto | yuwe | yuwe | living_dict | 1 |
| 5 | niño | luuçx | luuçx | living_dict | 1 |
| 6 | la casa | yat | yat | living_dict | 1 |
| 7 | padre | nehwe'sx | tata | living_dict | 1 |
| 8 | comida, alimento | (low conf.) kase'nxi / fxi'zenxi | ũ' | living_dict | 0 |
| 9 | La candela evita que el mal sobrevenga. | (low conf.) Ipx-tx çxiçxã'n pkhakhe'. | Ipxa' ewmesa'sphuphsa' naa pa'ka. | territorios_narrados | 0 |
| 10 | Por lo general se buscaban zonas seguras y planas. | Wẽçx kiwe te'çxa u'jwe'sxçxa jĩjxnxi'su. | Yat kukweyu katthenek nenxu nus yu' ew khudukan... | territorios_narrados | 0 |
| 11 | Pensando en esto y en el niño, el señor se recostó y se durmió. | Naa luuçxã'n txã'wẽ'sxçxa, thẽ' fxtũ'çxa ksxa'wnxi. | Txa'wte ma'jĩwaçwa klxumnane'tka uy sun kũh yahtxna wetecxa ũsii dehne'. | territorios_narrados | 0 |
| 12 | También procedían a techar la casa con resistente paja blanca traída del páramo. | Yat-tx çxhãb pxisxa'çxa thẽ'sa wala u'jwe'sx. | Yat u'sete u'kamey ü' wala ajanet nasatxa puuçya... | territorios_narrados | 0 |
| 13 | Los mayores dicen que cuando esté lloviznando deben protegerse la cabeza. | Thẽ'sxa we'wnxi: ĩkwe'sx eçx kãhçxa dxi'p sa' kãhçxha. | Sa' nusa' fxtũus su'sa' jĩtx naa pa'ka. | territorios_narrados | 0 |
| 14 | Ellos vivían sin dificultades toda la vida. | Txãa'wẽ'sx wẽçxa fxi'zeya peeçxa. | Txite eente vxyanes sena ew u'jwetx... | territorios_narrados | 0 |
| 15 | El amor debe ser genuino. Odien lo malo; aférrense a lo bueno. | Wẽt wẽt ũskiwe'nxi sa'. Çxiçxa'n kĩh, wẽçxa'n txãjxni. | Teeçxsa na'wẽçxah... Ewmeesa's nwẽese'jmée ewsaçxá's kxtey myuuwe. | bible_nt | 0 |
| 16 | El derecho a la vida es inviolable. No habrá pena de muerte. | Fxi'zenxi-tx pkhakhe'pa. Dxi'jya'çxa peçx. | Kwe's'a' ít'i u'hu hi'ptha'w'... | constitution | 0 |
| 17 | Para tener hijos, debían demorarse cerca de dos años. | Luuçx pa'kãhçxa, e'z piya tem kãh. | Txaja' ew jiyute na'wçxa u'ypas pakwewamen... | territorios_narrados | 0 |
| 18 | Es malo enamorarse entre primos hermanos... | Pa'çxhi-pa'çxhitxi ũskiwe'nxi çxiçx, çxhãb khwe'sx-tx u'jwe'sxsa. | Kwe'sx nasa fxi'zenxĩte pdxiysa pwe'sxa' ptamunxa ewumetxna... | territorios_narrados | 0 |
| 19 | Para que los niños aprendan rápido, hay que evitar darles de comer la cabeza de la gallina. | Luuçxtxi we'wne'çxa, atalh dxi'p kase' pkhakhe'. | Luucxa' Atalx dxikhthe ũ'wahme, txâwme tud piyametxna. | territorios_narrados | 0 |
| 20 | No debemos tampoco tener hijos estando borrachos... | Ũka ksxe'çxa luuçx pa'çxhi peçx, çxhãb txãa'wẽ'sx ũka ksxe'sa eça. | luuçx pyahtey tûtçxatx utxa ma'w ya'nxutxpejetx... | territorios_narrados | 0 |
| 21 | A los niños y a las niñas no hay que darles de comer los ojos de la vaca... | Luuçxtxi waka yafxi'kxi kase'tx peçx, çxhãb wakatxi'tx u'jwe'sxsa. | Luucxtxi kla yafxas puçhwa'hme, txawme', Klaa açya' newuna. | territorios_narrados | 0 |
| 22 | Por favor, procura venir a visitarme tan pronto como puedas. | Ãhsa pa'kha çxa'çxa eku, ãy kĩhsa pa'çxhi. | Ma'wẽtewa en kutxi'jçxa dud myuh adxa's thegya'. | bible_nt | 0 |
| 23 | Si el pie dijera: "Como no soy mano, no soy parte del cuerpo"... | Kxitxe we'wpa: "Kuse mete, çxa we'sxsa peku", çxa we'sx mete'sa? | Çxida' we'wewaça', na'jĩna: Adxa' kusemeeth... | bible_nt | 0 |
| 24 | Es obligación del Estado y de las personas proteger las riquezas culturales y naturales de la Nación. | Estado-çxa nasa-çxa pkhakhe' sa' kiwe'-çxa wala fxi'zenxi'su. | Naa Kulubyate npicthé'we's'ma't'yuu... | constitution | 0 |
| 25 | Si se quiere que el parto de las jovencitas sea rápido, hay que darles el primer huevo de la gallina. | Ipx luuçx pa'kãhçxa atalh khwe'kxi te'wẽ' kase'. | Knasatxi atalx knasa ziçh nyafxtewe'sxas... | territorios_narrados | 0 |
| 26 | Una sola persona no debe comer la cabeza del marrano... | (fragmentos) kuçx dxi'p wẽtwẽt nasa-txi sa' kase', çxhãb minga eçxa eçx wala u'jwe'sxsa. | Kuçxi dxikhthe's yatnwe's Jxukasa ũ'wãja... | territorios_narrados | 0 |
| 27 | A las jóvenes no se les debe dar de comer la matriz de la marrana... | Khwe'kxitxi kuçx ũus kase'tx peçx, çxhãb luuçx wala pa'çxhisa. | Luuçx u'ytxi Kuçxi duuya'jas puçhwa'hmej... | territorios_narrados | 0 |
| 28 | Nunca se debe colocar una jigra en la cabeza como una gorra... | Jigxa dxi'pte sa'çxa peçx, çxhãb yu'siçx eku atalh kĩhsa. | Yajatx jxkwette fxikhwa'jme' txãwmenxu atalx ũ'sa... | territorios_narrados | 0 |
| 29 | Antes de volver a encender la candela de la tulpa, hay que mezclar maíz capio blanco... | Ipx pku'çxa, kxiwe fxi'çx-çxa we'sx-çxa wẽçx-çxa peeçx tulpa-te khu'çxha. | Khutx wajwa çxijme, çxayu'çe bej yakh çxijmeyu'... | territorios_narrados | 0 |
| 30 | Cualquier casa en la que entren, quédense allí, y cuando deban irse, váyanse de allí. | Yat eçxa kãhçxa, txa'te jiyu'; u'jya'çxa, txa'tx u'j. | Maa yatte paadejxa' pa'jyã'jçxa', kxteeçxáa paadehna ũsune'kwe... | bible_nt | 1 |
| 31 | "Estén alerta, y cuídense de todo pensamiento y acción de avaricia..." | Wẽçx jiyu', ũus çxiçx-çxa pkhakhe'; nasa fxi'zenxi-tx u'jwe'sxtxi pe'a kuse. | na'wẽk we'we: —Mpa'yajkxwe, naa kiwete ji'phuniçxá's yaakxnisa's... | bible_nt | 0 |
| 32 | Se garantiza la libertad de conciencia. Nadie será molestado... | Ũus yuwe wẽçxa fxi'zeya, ki' txãjxni'kxitxi atxã'h peçx. | Nasa' peek' úuste ma'we yaak'n'i' yuuwemesa'... | constitution | 0 |
| 33 | Antes, para la construcción de la casa, los antiguos indígenas nasa... | Kxiwe nasawẽ'sx yat we'sxçxa, thẽ'sxtxi we'wnxa: "Naa kiwe wẽçx-eka?" Kiwe-tx wẽçxçxa ũskiwe'nxi'su. | Yaçteywe'sxa', yat tahpçxa walah' ûus atxajanet... | territorios_narrados | 0 |
| 34 | Cuando iban a hacer la casa, no solo participaba la familia, sino que otros moradores venían... | Yat we'sxçxa, nasa wala-tx eku, minga eçx; e'z tafx nasa-tx eku, atalh wẽçx u'jwe'sxnxi; wẽt semana-te yat tu'thẽ'. | Yata' dxiite walançkyu açxyat naw deeyat jiphuçmenek... | territorios_narrados | 1 |
| 35 | Por otra parte, también hay que enseñar a los niños y jóvenes cómo cuidar la naturaleza... | Luuçx-çxa khwe'kxi-çxa we'wnxa, kiwe pkhakhe' sa'; sek-tx yu'çxa, yat we'sxçxa, waka kawalu-txi sxabwe'sxçxa. | Nap yaçkay yu' ïç yukh çxanet kasen u'pu... | territorios_narrados | 0 |
| 36 | Cuando acababan la nueva casa, ellos celebraban con comida y el baile de la chucha... | Yat tu'thẽ'çxa, kase'çxa, chucha jxukha-çxa wẽçxa fxi'zewa; nasawẽ'sx ksxa'wnxa: "Kuse-tx yu'siçx-txi u'jwe'sxnxi peçx." | Txawetwya deeyat jiphuçmennet açx kwe'sx naw jiptha'w txaw... | territorios_narrados | 0 |
| 37 | "Por eso les digo que no se preocupen por sus vidas..." | Çxha we'wte: "Ĩkwe'sx fxi'zenxi peeçxa ũus çxiçx peçx; kase' yu' jxuth-çxa peçx. Fxi'zenxi kase'pa wala, we'sx jxuthpa wala, peku?" | Na'wẽth yu'kxpeje': I'kwe'sxa' kĩh yuhwa kuh yajkxmée mfxi'zewe... | bible_nt | 1 |
| 38 | La mujer y el hombre tienen iguales derechos y oportunidades... | (no intento — confianza insuficiente) | Kulubyate' u'ymakyuu, picthé'ma'kyuuna' ha'dac'ac'a fi'zewa' hipta'... | constitution | 0 |
| 39 | Colombia es un Estado social de derecho... | (no intento — confianza insuficiente) | Kulubyate c'hab wala kiwe' ít'i f'izen'i's nwe'wena ikahsa' Ec Ne'hwes'te... | constitution | 0 |
| 40 | Son fines esenciales del Estado... | (no intento — confianza insuficiente) | Naa c'hab wala kiwete npicthé'we's'a' nasa hu'ghu ya'yaak'n'i's K'tey yuuna... | constitution | 0 |

**Claude Opus 4.7 ES→NY total: 11/40 (27.5%)**

---

## Claude Opus 4.7 — Nasa Yuwe → Español

| # | Nasa Yuwe | Español (traducción) | Español (respuesta correcta) | Fuente | Exactitud |
|---|-----------|---------------------|------------------------------|--------|-----------|
| 1 | yu' | agua | 1. el agua; 2. líquido | living_dict | 1 |
| 2 | ew | bueno / bien | bien, bueno | living_dict | 1 |
| 3 | nasa | persona / gente (indígena Nasa) | 1. indígena páez 2. gente, persona | living_dict | 1 |
| 4 | yuwe | lengua / idioma / palabra | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto, noticia, razón | living_dict | 1 |
| 5 | luuçx | niño / hijo | niño | living_dict | 1 |
| 6 | yat | casa | la casa | living_dict | 1 |
| 7 | tata | padre / papá | padre | living_dict | 1 |
| 8 | ũ' | diente (incierto; podría ser una forma de "estar/ser") | comida, alimento | living_dict | 0 |
| 9 | Ipxa' ewmesa'sphuphsa' naa pa'ka. | El sol/día no está bueno en este lugar. | La candela evita que el mal sobrevenga. | territorios_narrados | 0 |
| 10 | Yat kukweyu katthenek... | "Junto a la casa cocinaron y el agua buena/limpia se acabó..." | Por lo general se buscaban zonas seguras y planas. | territorios_narrados | 0 |
| 11 | Txa'wte ma'jĩwaçwa... | "Así, al amanecer, las mujeres ya estaban listas, hablando entre sí..." | Pensando en esto y en el niño, el señor se recostó y se durmió. | territorios_narrados | 0 |
| 12 | Yat u'sete u'kamey... | "Dentro de la casa grande la gente Nasa se reunía a comer y beber alrededor de la mesa..." | También procedían a techar la casa con resistente paja blanca traída del páramo. | territorios_narrados | 0 |
| 13 | Sa' nusa' fxtũus... | "Aquel hermano nos dijo así en este lugar/de esta manera." | Los mayores dicen que cuando esté lloviznando deben protegerse la cabeza. | territorios_narrados | 0 |
| 14 | Txite eente vxyanes... | "Los jóvenes trabajan bien, con sus manos, con el corazón, y por eso trabajan sin cansarse." | Ellos vivían sin dificultades toda la vida. | territorios_narrados | 0 |
| 15 | Teeçxsa na'wẽçxah... | "Uno solo no debe llevar todo; entre todos, con el corazón. Lo malo no se debe seguir; lo bueno hay que aceptar." | El amor debe ser genuino. Odien lo malo; aférrense a lo bueno. | bible_nt | 1 |
| 16 | Kwe's'a' ít'i u'hu... | "Nosotros tenemos/llevamos así. Nadie habla mal..." | El derecho a la vida es inviolable. No habrá pena de muerte. | constitution | 0 |
| 17 | Txaja' ew jiyute... | "La mujer joven, junto con los mayores, debe ser cuidada, para que el niño nazca y crezca bien sin enfermedad." | Para tener hijos, debían demorarse cerca de dos años. | territorios_narrados | 0 |
| 18 | Kwe'sx nasa fxi'zenxĩte... | "En nuestra vida Nasa, los parientes no deben pelear/dañarse, sino vivir unidos como familia." | Es malo enamorarse entre primos hermanos, porque serán perseguidos por los tigres negros. | territorios_narrados | 0 |
| 19 | Luucxa' Atalx dxikhthe... | "El niño no debe coger/tocar la gallina (atalx), porque puede asustarse/lastimarse." | Para que los niños aprendan rápido, hay que evitar darles de comer la cabeza de la gallina. | territorios_narrados | 0 |
| 20 | luuçx pyahtey tûtçxatx... | "Los niños pequeños, cuando juegan y crecen, aprenden la lengua/palabra de la tierra..." | No debemos tampoco tener hijos estando borrachos, pues van a nacer con pensamientos de borracho. | territorios_narrados | 0 |
| 21 | Luucxtxi kla yafxas... | "Al niño no se le debe dar (¿kla = leña/palo?), porque es peligroso/quema." | A los niños y a las niñas no hay que darles de comer los ojos de la vaca... | territorios_narrados | 0 |
| 22 | Ma'wẽtewa en kutxi'jçxa... | "¿Cómo es que, habiendo crecido, no miras/cuidas a tu madre?" | Por favor, procura venir a visitarme tan pronto como puedas. | bible_nt | 0 |
| 23 | Çxida' we'wewaça'... | "Anoche/de noche se habló así: la madre no quiso/no estuvo de acuerdo..." | Si el pie dijera: "Como no soy mano, no soy parte del cuerpo", ¿dejaría de ser parte del cuerpo? | bible_nt | 0 |
| 24 | Naa Kulubyate npicthé'we's'ma't'yuu... | "Aquí en Colombia hay autoridades, hay un solo pueblo Nasa; uno solo es el habitante; en esta tierra todos vivimos..." | Es obligación del Estado y de las personas proteger las riquezas culturales y naturales de la Nación. | constitution | 0 |
| 25 | Knasatxi atalx... | "A los Nasa no se les debe dar gallina cruda/sangre de gallina a los niños, porque hace daño al niño que está naciendo." | Si se quiere que el parto de las jovencitas sea rápido, hay que darles el primer huevo de la gallina. | territorios_narrados | 0 |
| 26 | Kuçxi dxikhthe's... | "Toda la familia/casa debe comer junta el cuyi (kuçxi); uno solo comiendo, separado del hermano, no es bueno." | Una sola persona no debe comer la cabeza del marrano; ha de compartirla con la familia... | territorios_narrados | 1 |
| 27 | Luuçx u'ytxi Kuçxi duuya'jas... | "A la niña no se le debe dar carne de cuy, porque el cuy le hace daño al niño que carga (durante el embarazo)." | A las jóvenes no se les debe dar de comer la matriz de la marrana porque... van a tener muchos hijos. | territorios_narrados | 0 |
| 28 | Yajatx jxkwette fxikhwa'jme'... | "Los mayores dicen que no se debe matar (algo) en la mañana, porque la gallina queda dentro de la casa atada." | Nunca se debe colocar una jigra en la cabeza como una gorra... | territorios_narrados | 0 |
| 29 | Khutx wajwa çxijme... | "No (hagan algo) cuando truena/llueve; cuando el sol está saliendo, entonces sí se puede hacer..." | Antes de volver a encender la candela de la tulpa, hay que mezclar maíz capio blanco... | territorios_narrados | 0 |
| 30 | Maa yatte paadejxa'... | "En una sola casa, conviviendo, una sola autoridad debe haber, para que la familia viva en armonía." | Cualquier casa en la que entren, quédense allí, y cuando deban irse, váyanse de allí. | bible_nt | 0 |
| 31 | na'wẽk we'we... | "Así habló: —No olviden, en esta tierra lo que se tiene/recibe es de los que están..." | "Estén alerta, y cuídense de todo pensamiento y acción de avaricia..." | bible_nt | 0 |
| 32 | Nasa' peek' úuste... | "El Nasa no debe hablar con dos corazones / no debe ser falso. Nadie debe andar con doble palabra / engañando a otros." | Se garantiza la libertad de conciencia. Nadie será molestado... | constitution | 0 |
| 33 | Yaçteywe'sxa', yat tahpçxa walah'... | "Las mujeres barren la casa con buen corazón... La mujer mayor enseña a las demás cómo se hace el trabajo..." | Antes, para la construcción de la casa, los antiguos indígenas nasa realizaban distintas actividades... | territorios_narrados | 0 |
| 34 | Yata' dxiite walançkyu... | "La casa antigua era grande, no tenía paredes de adobe sino de bahareque/madera. Antes los techos eran de paja..." | Cuando iban a hacer la casa, no solo participaba la familia, sino que otros moradores venían... | territorios_narrados | 0 |
| 35 | Nap yaçkay yu' ïç yukh... | "Cuando la mujer va a traer agua al río, si el agua está muy crecida no debe pasar, porque puede llegar el ksxaw (espíritu)..." | Por otra parte, también hay que enseñar a los niños y jóvenes cómo cuidar la naturaleza... | territorios_narrados | 0 |
| 36 | Txawetwya deeyat... | "Antes no había paredes (de adobe), sino que se hacían de palos y barro; los mayores las levantaban con mucho esfuerzo..." | Cuando acababan la nueva casa, ellos celebraban con comida y el baile de la chucha... | territorios_narrados | 0 |
| 37 | Na'wẽth yu'kxpeje'... | "Así dijo: 'Nosotros, sin nada, no podemos vivir; ¿qué vamos a comer?, ¿qué vamos a beber?', decía. Por eso, al comer, hay que pensar en los demás..." | "Por eso les digo que no se preocupen por sus vidas. No se preocupen por lo que van a comer..." | bible_nt | 1 |
| 38 | Kulubyate' u'ymakyuu... | "En Colombia, las mujeres y las autoridades viven con mucha dificultad. A la mujer nadie la trata bien..." | La mujer y el hombre tienen iguales derechos y oportunidades... | constitution | 0 |
| 39 | Kulubyate c'hab wala kiwe'... | "En Colombia, en esta tierra grande, vivimos hablando con Ec Ne'hwes (Dios/Creador)..." | Colombia es un Estado social de derecho, organizado en forma de República unitaria... | constitution | 0 |
| 40 | Naa c'hab wala kiwete npicthé'we's'a'... | "En esta gran tierra, las autoridades dictan leyes sobre los pueblos: todos los habitantes del territorio... nadie debe quitarle la tierra a otro..." | Son fines esenciales del Estado: servir a la comunidad, promover la prosperidad general... | constitution | 0 |

**Claude Opus 4.7 NY→ES total: 10/40 (25%)**

---

## Gemini Flash 3.5 — Español → Nasa Yuwe

| # | Español | Nasa Yuwe (traducción) | Nasa Yuwe (respuesta correcta) | Fuente | Exactitud |
|---|---------|------------------------|--------------------------------|--------|-----------|
| 1 | 1. el agua; 2. líquido | yu | yu' | living_dict | 1 |
| 2 | bien, bueno | pef / pkhuẽy | ew | living_dict | 0 |
| 3 | 1. indígena páez 2. gente, persona | nasa | nasa | living_dict | 1 |
| 4 | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto | yuwe | yuwe | living_dict | 1 |
| 5 | niño | luuç | luuçx | living_dict | 1 |
| 6 | la casa | yat | yat | living_dict | 1 |
| 7 | padre | tata | tata | living_dict | 1 |
| 8 | comida, alimento | we'we / fi'ze | ũ' | living_dict | 0 |
| 9 | La candela evita que el mal sobrevenga. | Ip wejxa' ewmee yu'sa pshiiçpja'w. | Ipxa' ewmesa'sphuphsa' naa pa'ka. | territorios_narrados | 0 |
| 10 | Por lo general se buscaban zonas seguras y planas. | Sa' jĩna fanz kĩh yu' tyã'wã ew u' kĩh tyãwã jũ' kĩh. | Yat kukweyu katthenek nenxu nus yu' ew khudukan... | territorios_narrados | 0 |
| 11 | Pensando en esto y en el niño, el señor se recostó y se durmió. | Na'sa' luuçsa' pta'shkiis, pki'pku thã'j sũu kũ'ũ ki jũ'ũ. | Txa'wte ma'jĩwaçwa klxumnane'tka uy sun kũh yahtxna wetecxa ũsii dehne'. | territorios_narrados | 0 |
| 12 | También procedían a techar la casa con resistente paja blanca traída del páramo. | Sũh jĩnas tyã'wã yat pu' wejx se' txa yu' paja tyãw yuuy yuuy páramote fytxi'. | Yat u'sete u'kamey ü' wala ajanet nasatxa puuçya... | territorios_narrados | 0 |
| 13 | Los mayores dicen que cuando esté lloviznando deben protegerse la cabeza. | Nee we'wesa txã'sa kĩh wejx dyi'içku' dzu' wetx kũ'jx thã'j thã'sa. | Sa' nusa' fxtũus su'sa' jĩtx naa pa'ka. | territorios_narrados | 0 |
| 14 | Ellos vivían sin dificultades toda la vida. | Txãwẽ' tyãwã yu' fytx tyãwã pefsa fi'zenaw ew u' txa'wã. | Txite eente vxyanes sena ew u'jwetx... | territorios_narrados | 0 |
| 15 | El amor debe ser genuino. Odien lo malo; aférrense a lo bueno. | Pekyuu yu' ewisa yũu wejx. Ewmeesa sũh wejx; ewsa e'sy thã'j ya'w. | Teeçxsa na'wẽçxah... Ewmeesa's nwẽese'jmée ewsaçxá's kxtey myuuwe. | bible_nt | 1 |
| 16 | El derecho a la vida es inviolable. No habrá pena de muerte. | Fi'zen te'sa ptya'wa yu' thã'jmee kũ'jx. I'ku thẽ'sa uutewe wejx u' kũ'jx. | Kwe's'a' ít'i u'hu hi'ptha'w'... | constitution | 0 |
| 17 | Para tener hijos, debían demorarse cerca de dos años. | Nee luuç thã'j ya'w txãwẽ u'te' e'za pi'z tyã'wã wejx. | Txaja' ew jiyute na'wçxa u'ypas pakwewamen... | territorios_narrados | 0 |
| 18 | Es malo enamorarse entre primos hermanos... | Khwe'yuu pekyuu yu' ewmee yũ', pxith thã'j pta'w tyãwã kũ'jx thẽ'w thẽ'w tyãwãã. | Kwe'sx nasa fxi'zenxĩte pdxiysa pwe'sxa' ptamunxa ewumetxna... | territorios_narrados | 0 |
| 19 | Para que los niños aprendan rápido, hay que evitar darles de comer la cabeza de la gallina. | Luuç pkhuẽy sũũwẽ' yu' dzu' wetx tyãwã kaxte atall dzu' kũ'jx kuunĩ'. | Luucxa' Atalx dxikhthe ũ'wahme, txâwme tud piyametxna. | territorios_narrados | 0 |
| 20 | No debemos tampoco tener hijos estando borrachos... | Khab thã'jsa luuç tyãwã thã'j ya'wme'ee pkhuẽy yu' khab ptya'w sũũ ku'jx. | luuçx pyahtey tûtçxatx utxa ma'w ya'nxutxpejetx... | territorios_narrados | 0 |
| 21 | A los niños y a las niñas no hay que darles de comer los ojos de la vaca... | Luuç kax kaxsa vaca tya' u' wetx kũ'jx dza'w kuunĩ' txã'sa dzu' wejx kũ'jx pshiiç ku'. | Luucxtxi kla yafxas puçhwa'hme, txawme', Klaa açya' newuna. | territorios_narrados | 0 |
| 22 | Por favor, procura venir a visitarme tan pronto como puedas. | Aç yuu wejx idxa' ptya'wa u'wẽ' txã'wẽ i'khwẽ' txãwẽ thã'jx. | Ma'wẽtewa en kutxi'jçxa dud myuh adxa's thegya'. | bible_nt | 0 |
| 23 | Si el pie dijera: "Como no soy mano, no soy parte del cuerpo"... | Çxida jĩte': "Kha'zmeesa yũ'ũ txã'wẽ tya' pkhuẽymee yũ'ũ", ¿txãwẽ' pkhuẽymee yu' kũ'? | Çxida' we'wewaça', na'jĩna: Adxa' kusemeeth... | bible_nt | 1 |
| 24 | Es obligación del Estado y de las personas proteger las riquezas culturales y naturales de la Nación. | Estado se' nasa se' ku'k kĩh pshiiç ya'w yu' nasa yat kĩh wejx ewyuuysa tyã'wã. | Naa Kulubyate npicthé'we's'ma't'yuu... | constitution | 0 |
| 25 | Si se quiere que el parto de las jovencitas sea rápido, hay que darles el primer huevo de la gallina. | Nxu'sa luuç ptya'wa dzu' wetx sũũwẽ' atall lo' tyãwã dzu' wetx tyãwã dza'w ya'w. | Knasatxi atalx knasa ziçh nyafxtewe'sxas... | territorios_narrados | 0 |
| 26 | Una sola persona no debe comer la cabeza del marrano... | Te' nasa khũw thã'j dzu' ku'jxme'ee kuunĩ' pte' nasa wejx pshiiç ya'w sũhme'ee yu' mingate nwee wejx dyi'içku' kũ'jx fi'ze kĩh. | Kuçxi dxikhthe's yatnwe's Jxukasa ũ'wãja... | territorios_narrados | 0 |
| 27 | A las jóvenes no se les debe dar de comer la matriz de la marrana... | Nxu'sa khũw pkhuẽy we'we dza'w ku'jxme'ee kuunĩ' txãwẽ kũ'jx luuç kĩh kĩh thã'j ya'w sũũ. | Luuçx u'ytxi Kuçxi duuya'jas puçhwa'hmej... | territorios_narrados | 0 |
| 28 | Nunca se debe colocar una jigra en la cabeza como una gorra... | Khabe' kwetx dzu' wetx kwetx ya'wme'ee kuunĩ' kwetx ewmee yũ' txã'wẽ kũ'jx khyuw atall dzu' ku'jx. | Yajatx jxkwette fxikhwa'jme' txãwmenxu atalx ũ'sa... | territorios_narrados | 0 |
| 29 | Antes de volver a encender la candela de la tulpa, hay que mezclar maíz capio blanco... | Ip tulpa wejx pu' pkhuẽy makh fytxi' se' ptxũ'wẽ se' thã'jx tyã'wã psha'w ya'w tulpate. | Khutx wajwa çxijme, çxayu'çe bej yakh çxijmeyu'... | territorios_narrados | 0 |
| 30 | Cualquier casa en la que entren, quédense allí, y cuando deban irse, váyanse de allí. | Kĩh yatte pkhuẽy u'te' kũ'jx tyã'te u'wẽ, sa' txã'te fytx u'we wejx u' kũ'jx txã'wẽ. | Maa yatte paadejxa' pa'jyã'jçxa', kxteeçxáa paadehna ũsune'kwe... | bible_nt | 1 |
| 31 | "Estén alerta, y cuídense de todo pensamiento y acción de avaricia..." | "Ptya'wa ew kĩh, sũh ewmee sũũwẽ' yu' u' wejx, nasa fi'zen yu' kĩh thã'jx thã'jya'wmee ku'." | na'wẽk we'we: —Mpa'yajkxwe, naa kiwete ji'phuniçxá's yaakxnisa's... | bible_nt | 0 |
| 32 | Se garantiza la libertad de conciencia. Nadie será molestado... | Ptya'w sũũwẽ' yu' ewsa u' kũ'jx. Kĩh nasas wejx ewmee yũ'u kũ'jx tyã'wẽ sũũwẽ' se'. | Nasa' peek' úuste ma'we yaak'n'i' yuuwemesa'... | constitution | 0 |
| 33 | Antes, para la construcción de la casa, los antiguos indígenas nasa... | Nee yu' yat yuuy sũũwẽ' nasa thẽ'w tyãwã kĩh kĩh yũu u'wã. Yat yuuy ya'w wejx txã'sa yu' nee nee thẽ'sa wetx pta'sh u'wã yu' txãwẽ ewsate u' wejx sũũwẽ' se'. | Yaçteywe'sxa', yat tahpçxa walah' ûus atxajanet... | territorios_narrados | 0 |
| 34 | Cuando iban a hacer la casa, no solo participaba la familia, sino que otros moradores venían... | Yat yuuy tyãwẽ pkhuẽyme'ee nasa yat wetx u'wa, se' pte' nasa tyãwã pyã'w u'wã txã'te yu' minga yũu u'wã. Tyã'wẽ ptxũ'wẽ nasa tyãwã fi'ze u'wã sa' dzu' wetx yũu u'wã. Semana te'te yat pu' yu' ewĩ' ku'. | Yata' dxiite walançkyu açxyat naw deeyat jiphuçmenek... | territorios_narrados | 1 |
| 35 | Por otra parte, también hay que enseñar a los niños y jóvenes cómo cuidar la naturaleza... | Sũh jĩnas luuç ku' nxu'sa tyã'sa yu' pkhuẽy ya'w kĩh wetx pshiiç ya'w. Kwetx pshiiç ya'w ip kyuw sũh yat yuuy kyuw se' vaca caballo tyãwã pyã'w fanz wejx. | Nap yaçkay yu' ïç yukh çxanet kasen u'pu... | territorios_narrados | 0 |
| 36 | Cuando acababan la nueva casa, ellos celebraban con comida y el baile de la chucha... | Yat yu' ew tyãwẽ fi'ze wejx tyãwã we'we ku' kwee se' baile yũu u'wã. Txã'wẽ yũu u'wã nasa yu' sũũ ku'jx animalkhe' pshiiç wejx khyuw se' pkhuẽymee kũ'jx. | Txawetwya deeyat jiphuçmennet açx kwe'sx naw jiptha'w txaw... | territorios_narrados | 0 |
| 37 | "Por eso les digo que no se preocupen por sus vidas..." | "Txã'wẽ i'khwẽ'sa pta'sh txãwẽ fi'zen wejx sũũmee ya'w. Kĩh dzu' kĩh yu kũ'jx sũh kĩh llanwẽ' yu' sũũmee. ¿Fi'zen yu' we'we se' thẽ'mee kũ', kwetx yu' llanwẽ' se' thẽ'mee kũ'?" | Na'wẽth yu'kxpeje': I'kwe'sxa' kĩh yuhwa kuh yajkxmée mfxi'zewe... | bible_nt | 1 |
| 38 | La mujer y el hombre tienen iguales derechos y oportunidades... | Uxsa pxi'sa tyãwã pkhuẽy ptya'wa thã'j. Uxsa yu' ewmee yũ'u kũ'jxme'ee. Luuç thã'j wetx se' Estado se' pshiiç wejx kũ'jx. Estado yu' uxsa yat thã'jsa pyã'w wejx thã'j ku'. | Kulubyate' u'ymakyuu, picthé'ma'kyuuna' ha'dac'ac'a fi'zewa' hipta'... | constitution | 0 |
| 39 | Colombia es un Estado social de derecho... | Colombia yu' Estado social de derecho ku', kĩh nasa yu' te'te u' ku' txãwẽ pkhuẽy ki'p ku' nasa kũ'jx wetx pshiiç wejx... | Kulubyate c'hab wala kiwe' ít'i f'izen'i's nwe'wena ikahsa' Ec Ne'hwes'te... | constitution | 0 |
| 40 | Son fines esenciales del Estado... | Estado ptya'wa yu': nasa wetx pyã'w ya'w, Constitución te' ptya'wa ki'pya'w, nasa pkhuẽy pta'sh kũ'jx kĩh kĩh yũu ya'w te'te, nasa yat kĩh wejx pshiiç ya'w, sa' pefsa fi'ze kũ'jx thã'j ya'w. | Naa c'hab wala kiwete npicthé'we's'a' nasa hu'ghu ya'yaak'n'i's K'tey yuuna... | constitution | 0 |

**Gemini Flash 3.5 ES→NY total: 11/40 (27.5%)**

---

## Gemini Flash 3.5 — Nasa Yuwe → Español

| # | Nasa Yuwe | Español (traducción) | Español (respuesta correcta) | Fuente | Exactitud |
|---|-----------|---------------------|------------------------------|--------|-----------|
| 1 | yu' | Agua | 1. el agua; 2. líquido | living_dict | 1 |
| 2 | ew | Bien / Bueno | bien, bueno | living_dict | 1 |
| 3 | nasa | Gente / Persona / Ser humano (Persona Nasa) | 1. indígena páez 2. gente, persona | living_dict | 1 |
| 4 | yuwe | Idioma / Lengua / Palabra | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto, noticia, razón | living_dict | 1 |
| 5 | luuçx | Hijo / Hija / Niño / Niña | niño | living_dict | 1 |
| 6 | yat | Casa / Vivienda | la casa | living_dict | 1 |
| 7 | tata | Papá / Padre | padre | living_dict | 1 |
| 8 | ũ' | Comer | comida, alimento | living_dict | 1 |
| 9 | Ipxa' ewmesa'sphuphsa' naa pa'ka. | Por eso el fuego sopla a los que no son buenos (o hace daño a las malas energías). | La candela evita que el mal sobrevenga. | territorios_narrados | 1 |
| 10 | Yat kukweyu katthenek... | Alrededor de la casa se siembran plantas medicinales y protectoras para que el viento sople bien y no entren enfermedades... | Por lo general se buscaban zonas seguras y planas. | territorios_narrados | 0 |
| 11 | Txa'wte ma'jĩwaçwa... | Así, cualquier cosa que piensen o deseen de corazón los que viven allí, se cumplirá con alegría. | Pensando en esto y en el niño, el señor se recostó y se durmió. | territorios_narrados | 0 |
| 12 | Yat u'sete u'kamey... | Dentro de la casa no se permite que entre cualquier espíritu a molestar a la gente, por eso se sahúma con plantas amargas y dulces... | También procedían a techar la casa con resistente paja blanca traída del páramo. | territorios_narrados | 0 |
| 13 | Sa' nusa' fxtũus... | Y por eso dicen que el viento sopla trayendo tanto el frío como el calor. | Los mayores dicen que cuando esté lloviznando deben protegerse la cabeza. | territorios_narrados | 0 |
| 14 | Txite eente vxyanes... | En el día de hoy caminen muy bien, caminen con dinero (prosperidad), caminen con el corazón limpio, y que todo les salga derecho. | Ellos vivían sin dificultades toda la vida. | territorios_narrados | 0 |
| 15 | Teeçxsa na'wẽçxah... | Cada uno debe respetar y escuchar el pensamiento del otro... No obedezcan lo malo, hagan únicamente lo que es bueno. | El amor debe ser genuino. Odien lo malo; aférrense a lo bueno. | bible_nt | 1 |
| 16 | Kwe's'a' ít'i u'hu... | Nosotros tenemos derecho a vivir en esta tierra. Nadie tiene permitido matarnos. Tampoco se permite maltratar a nadie. Ante la Ley Mayor... nadie debe ser asesinado. | El derecho a la vida es inviolable. No habrá pena de muerte. | constitution | 1 |
| 17 | Txaja' ew jiyute... | Para saber esto bien, los mayores y médicos tradicionales aconsejan que cuando una mujer está embarazada no debe mirar ciertas cosas... | Para tener hijos, debían demorarse cerca de dos años. | territorios_narrados | 0 |
| 18 | Kwe'sx nasa fxi'zenxĩte... | En la vida de nosotros los Nasa, las personas envidiosas o egoístas no viven bien, porque el duende o las malas energías los persiguen... | Es malo enamorarse entre primos hermanos, porque serán perseguidos por los tigres negros. | territorios_narrados | 0 |
| 19 | Luucxa' Atalx dxikhthe... | El niño no debe comer sesos de gallina, porque si lo hace aprenderá a ser tartamudo o olvidadizo. | Para que los niños aprendan rápido, hay que evitar darles de comer la cabeza de la gallina. | territorios_narrados | 1 |
| 20 | luuçx pyahtey tûtçxatx... | Al nacer el niño, los mayores observan sus movimientos para saber cómo será su vida; hoy en día se habla también de la medicina occidental... | No debemos tampoco tener hijos estando borrachos, pues van a nacer con pensamientos de borracho. | territorios_narrados | 0 |
| 21 | Luucxtxi kla yafxas... | No se debe hacer que los niños miren fijamente a los ojos de una vaca, porque de lo contrario, el espíritu de la vaca los asustará o los volverá torpes. | A los niños y a las niñas no hay que darles de comer los ojos de la vaca, porque luego esta los persigue... | territorios_narrados | 1 |
| 22 | Ma'wẽtewa en kutxi'jçxa... | De cualquier forma, cuando llegue el momento o la hora, ven a verme de inmediato. | Por favor, procura venir a visitarme tan pronto como puedas. | bible_nt | 1 |
| 23 | Çxida' we'wewaça'... | Si el pie pudiera hablar, diría: "Yo no soy la mano, y por eso no soy del cuerpo", pero no por no ser la mano deja de ser parte fundamental del cuerpo. | Si el pie dijera: "Como no soy mano, no soy parte del cuerpo", ¿dejaría de ser parte del cuerpo? | bible_nt | 1 |
| 24 | Naa Kulubyate npicthé'we's'ma't'yuu... | En esta Colombia, seamos hombres o seamos la comunidad que seamos, todos somos iguales; no importa el territorio... todos tenemos derecho a vivir en paz, protegidos y con dignidad. | Es obligación del Estado y de las personas proteger las riquezas culturales y naturales de la Nación. | constitution | 0 |
| 25 | Knasatxi atalx... | A las mujeres embarazadas se les debe dar de comer pechuga de gallina criolla, para que cuando den a luz el bebé nazca con buen aliento... | Si se quiere que el parto de las jovencitas sea rápido, hay que darles el primer huevo de la gallina. | territorios_narrados | 1 |
| 26 | Kuçxi dxikhthe's... | La cabeza del cerdo debe ser compartida y comida por todos los miembros de la casa; si se la come una sola persona, se dice que le dará pereza y no querrá trabajar en la chagra. | Una sola persona no debe comer la cabeza del marrano; ha de compartirla con la familia o con los vecinos... | territorios_narrados | 1 |
| 27 | Luuçx u'ytxi Kuçxi duuya'jas... | No se debe permitir que las niñas pequeñas carguen o jueguen mucho con cerdos, porque si lo hacen, cuando crezcan tendrán demasiados hijos muy seguidos como los cerdos. | A las jóvenes no se les debe dar de comer la matriz de la marrana porque... van a tener muchos hijos. | territorios_narrados | 1 |
| 28 | Yajatx jxkwette fxikhwa'jme'... | No se debe silbar dentro de la casa por las noches, porque los mayores dicen que eso atrae a los espíritus de la selva o hace que las gallinas mueran sin explicación. | Nunca se debe colocar una jigra en la cabeza como una gorra, porque la jigra maldice... | territorios_narrados | 0 |
| 29 | Khutx wajwa çxijme... | Para curar el dolor de muelas no se debe usar cualquier planta, se debe buscar la raíz de la planta silvestre junto con agua tibia y ceniza del fogón... | Antes de volver a encender la candela de la tulpa, hay que mezclar maíz capio blanco, hierba alegre roja y orejuela grande... | territorios_narrados | 0 |
| 30 | Maa yatte paadejxa'... | En cualquier casa a la que lleguen de visita, quédense allí tranquilos compartiendo la palabra hasta que sea el momento de salir o regresar. | Cualquier casa en la que entren, quédense allí, y cuando deban irse, váyanse de allí. | bible_nt | 1 |
| 31 | na'wẽk we'we... | Así dice la palabra: —No piensen únicamente en las cosas materiales que se tienen en esta tierra. Quien solo piensa en acumular riquezas terrenales no vivirá con un espíritu verdaderamente tranquilo. | "Estén alerta, y cuídense de todo pensamiento y acción de avaricia, pues la vida de una persona no se mide por la cantidad de posesiones..." | bible_nt | 1 |
| 32 | Nasa' peek' úuste... | Ninguna persona debe ser discriminada ni maltratada por su forma de pensar o por sus sentimientos. Nadie tiene el derecho de someter a otro a la esclavitud o a tratos crueles... | Se garantiza la libertad de conciencia. Nadie será molestado por razón de sus convicciones o creencias... | constitution | 1 |
| 33 | Yaçteywe'sxa', yat tahpçxa walah'... | Los mayores de la comunidad se reúnen y analizan profundamente con el corazón para que la armonía de la casa se mantenga bien. Los médicos tradicionales (thê'wala)... | Antes, para la construcción de la casa, los antiguos indígenas nasa realizaban distintas actividades... | territorios_narrados | 0 |
| 34 | Yata' dxiite walançkyu... | La casa tradicional se construye con una puerta principal que no debe mirar hacia donde nace el sol ni donde sopla el viento fuerte. El fuego (fogón) se ubica en el centro... | Cuando iban a hacer la casa, no solo participaba la familia, sino que otros moradores venían, y entonces se formaba una minga... | territorios_narrados | 0 |
| 35 | Nap yaçkay yu' ïç yukh... | Cuando el agua de la quebrada baja turbia de la montaña, significa que se avecina una enfermedad o una mala época; se debe recoger agua limpia de los nacimientos sagrados... | Por otra parte, también hay que enseñar a los niños y jóvenes cómo cuidar la naturaleza... | territorios_narrados | 0 |
| 36 | Txawetwya deeyat... | De esa manera, aunque no tengamos una casa grande, mantenemos nuestras costumbres tradicionales. Los mayores nos enseñaron a tejer las ruanas y mochilas con lana de oveja hilada... | Cuando acababan la nueva casa, ellos celebraban con comida y el baile de la chucha; después de esto ya podían entrar a habitarla. | territorios_narrados | 0 |
| 37 | Na'wẽth yu'kxpeje'... | Por lo tanto, les digo: No se preocupen angustiados por su vida, pensando: ¿Qué comeremos? o ¿Con qué nos vestiremos? Porque la vida es mucho más importante que la comida, y el cuerpo es mucho más importante que el vestido. | "Por eso les digo que no se preocupen por sus vidas. No se preocupen por lo que van a comer... ¿Acaso no es la vida más importante que la comida...?" | bible_nt | 1 |
| 38 | Kulubyate' u'ymakyuu... | En Colombia, ya sean mujeres o sean hombres, todos nacen libres y con los mismos derechos. A las mujeres nadie las puede obligar a casarse en contra de su voluntad. | La mujer y el hombre tienen iguales derechos y oportunidades. La mujer no podrá ser sometida a ninguna clase de discriminación... | constitution | 1 |
| 39 | Kulubyate c'hab wala kiwe'... | Colombia es un país grande que en su Constitución Mayor reconoce y defiende la diversidad de los pueblos y comunidades que conviven en este territorio... El Estado colombiano es uno solo, pero está conformado por diferentes territorios indígenas... | Colombia es un Estado social de derecho, organizado en forma de República unitaria, descentralizada, con autonomía de sus entidades territoriales... | constitution | 1 |
| 40 | Naa c'hab wala kiwete npicthé'we's'a'... | Toda persona que habite en este gran territorio tiene los mismos derechos y deberes consagrados ante la comunidad y la ley... las autoridades tradicionales, los mayores y la comunidad en general deben actuar como guardianes de la armonía... | Son fines esenciales del Estado: servir a la comunidad, promover la prosperidad general y garantizar la efectividad de los principios, derechos y deberes... | constitution | 1 |

**Gemini Flash 3.5 NY→ES total: 24/40 (60%)**

---

## Resumen / Summary

| Modelo | ES → NY | NY → ES | Promedio |
|--------|---------|---------|----------|
| ChatGPT 5.5 | 11/40 (27.5%) | 10/40 (25.0%) | 26.3% |
| Claude Opus 4.7 | 11/40 (27.5%) | 10/40 (25.0%) | 26.3% |
| Gemini Flash 3.5 | 11/40 (27.5%) | 24/40 (60.0%) | 43.8% |

### Observaciones

- **T1 (lexical)**: Todos los modelos aciertan en los términos comunes (yu', nasa, yuwe, luuçx, yat, tata); el único que falla consistentemente es `ũ'` ("comida/alimento"), donde solo Gemini lo aproxima como "comer".
- **ES → NY (todos los modelos)**: Casi siempre fallan en sentencias largas — generan Nasa Yuwe que parece morfológicamente plausible pero no coincide con el corpus de referencia. Aciertos esporádicos cuando las palabras clave (`yat`, `kxtey`, `ew`/`ewme`) coinciden.
- **NY → ES — Gemini destaca claramente**: 60% vs ~25% de los otros dos modelos. Parece tener mejor capacidad de captar el contenido semántico de oraciones Nasa Yuwe (especialmente las del NT bíblico y la Constitución, posiblemente memorizadas vía paralelos en pre-entrenamiento).
- **ChatGPT y Claude (NY → ES)**: Frecuentemente producen traducciones plausibles pero que divergen sustancialmente del significado del original — interpretan tokens aislados (`yat`, `luuçx`, `nasa`) y generan una historia coherente alrededor de ellos.
- **Bíblico y constitucional**: Las filas marcadas como `bible_nt` y `constitution` muestran mayor probabilidad de acierto para todos los modelos, consistente con presencia de paralelos en datos públicos (`americasnlp_2024`, traducciones bíblicas indígenas).
