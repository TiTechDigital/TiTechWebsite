# -*- coding: utf-8 -*-
"""Builds the Albanian content pages of titech.al: Tirana first.

Service pages, the Tirana landing page, a services hub and four guides that
answer questions the Albanian-language web answers poorly (cost, online store
payments, local SEO, choosing an agency). Same shell, styles and animations as
the rest of the site: the header and footer come from the translated English
blog template, the page body is written here.

First-draft Albanian: a native speaker must read everything before launch. No
claim of an office, a phone number or a client in Albania is made; no figure is
invented. Run after tools/build_albanian_site.py.

Run: python tools/build_albanian_pages.py
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_albanian_site as site

ROOT = site.ROOT
OUT = site.OUT
BASE = site.BASE
DATE = '2026-11-25'
DATE_SQ = '25 nëntor 2026'
SHELL_SRC = 'en/blog/website-maintenance/index.html'


def a(href, text):
    return '<a href="%s">%s</a>' % (href, text)


def checks(items):
    out = ['<ul class="checks">']
    out += ['<li><strong>%s</strong><span>%s</span></li>' % (t, d) for t, d in items]
    out.append('</ul>')
    return out


def esc(t):
    return html.escape(t, quote=False)


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t))


NOTE = ("Askush nuk mund të garantojë një pozicion në Google: varet nga konkurrenca, mosha e faqes dhe vlerësimet. "
        "Ajo që bëhet është të ndërtohen baza të sakta dhe të matet rezultati me kohën.")
REMOTE = ("Punojmë në distancë: takime me video, skedarë të ndarë dhe një person kontakti. Kur projekti kërkon takim në vend, "
          "e organizojmë dhe e shënojmë në ofertë si udhëtim.")

# ---------------------------------------------------------------------------
# pages
# ---------------------------------------------------------------------------
PAGES = []


def page(**kw):
    PAGES.append(kw)


# -------- hub
page(slug='sherbimet', kind='hub', title='Shërbimet: faqe interneti, softuer dhe SEO | TiTech Digital',
     h1='Shërbimet', eyebrow='Shërbimet',
     description='Faqe interneti, dyqane online, softuer me porosi, aplikacione mobile dhe SEO për biznese në Tiranë dhe në Shqipëri.',
     lead='Shërbime të qarta, një partner. Zgjidhni atë që ju nevojitet dhe na shkruani: përgjigjemi me një vlerësim të shkruar.',
     takeaways=[('Një ofertë e shkruar.', 'Faza, afate dhe kosto para se të nisim.'), ('Një person kontakti.', 'Nuk flisni me pesë departamente.'),
                ('Punë në distancë.', 'Takime me video dhe, kur duhet, në vend.')],
     sections=[('lista', 'Çfarë ofrojmë', 'Secili shërbim ka faqen e vet me hollësi.', checks([
         ('Krijimi i faqeve web', a('/krijimi-i-faqeve-web-tirane/', 'Faqe interneti të shpejta, të qarta dhe të gjetshme në Google.')),
         ('Hotele, restorante dhe klinika', a('/sektoret/', 'Faqe për sektorë me nevoja të veçanta.')),
         ('Automatizim me AI', a('/automatizim-me-ai-shqiperi/', 'Përgjigje të shpejta, njoftime dhe raporte, me njeri pas çdo hapi.')),
         ('Dyqan online', a('/dyqan-online-tirane/', 'Katalog, pagesa dhe dërgesa, me platformën që ju përshtatet.')),
         ('Softuer me porosi', a('/softuer-me-porosi-tirane/', 'Paneli dhe sisteme që zëvendësojnë Excel-in dhe punën me dorë.')),
         ('Aplikacione mobile', a('/aplikacione-mobile-tirane/', 'Kur ka kuptim aplikacion dhe kur mjafton një faqe web.')),
         ('SEO dhe prania lokale', a('/seo-tirane/', 'SEO teknike, Profili i Biznesit në Google dhe matje e rezultateve.')),
     ]))],
     faq=[('Si zgjedh shërbimin e duhur?', 'Na shkruani çfarë nuk funksionon sot dhe çfarë dëshironi të arrini. Prej andej ju thomi se cili shërbim ka kuptim dhe cili jo.'),
          ('Punoni vetëm në Tiranë?', 'Punojmë me biznese në Tiranë dhe në gjithë Shqipërinë, në distancë. ' + REMOTE)],
     related=[('/tirane/', 'Faqe interneti dhe softuer në Tiranë', 'Si punojmë me bizneset e Tiranës.'),
              ('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'Sa kushton një faqe interneti', 'Çfarë e ndryshon çmimin.'),
              ('/kontakt/', 'Na kontaktoni', 'Na tregoni projektin tuaj.')],
     cta_title='Na tregoni çfarë ju nevojitet', cta_text='Shkruani në pak rreshta çfarë duhet të ndryshojë. Përgjigjemi brenda një dite pune.')

# -------- Tirana landing
page(slug='tirane', kind='local', title='Faqe interneti dhe softuer në Tiranë | TiTech Digital',
     h1='Faqe interneti dhe softuer për bizneset e Tiranës', eyebrow='Tiranë',
     description='TiTech Digital punon me biznese në Tiranë: krijim faqesh web, dyqane online, softuer me porosi, aplikacione mobile dhe SEO. Ofertë e shkruar para se të nisim.',
     lead='Biznese të Tiranës na kërkojnë faqe interneti të qarta, dyqane online që funksionojnë dhe softuer që zëvendëson punën me dorë. ' + REMOTE,
     takeaways=[('Një faqe që shpjegon çfarë bëni.', 'Pak faqe, të qarta, që lexohen mirë nga telefoni.'),
                ('Të gjendeni në Google në Tiranë.', 'Faqe e saktë, Profili i Biznesit në Google dhe vlerësime të vërteta.'),
                ('Ofertë e shkruar.', 'Faza, afate dhe kosto para se të nisni.'),
                ('Pa premtime të rreme.', NOTE)],
     sections=[
         ('sherbime', 'Çfarë bëjmë për bizneset në Tiranë', 'Pesë shërbime, secili me faqen e vet.', checks([
             ('Faqe interneti', a('/krijimi-i-faqeve-web-tirane/', 'Për restorante, hotele, klinika, dyqane, studio dhe kompani prodhimi.')),
             ('Dyqan online', a('/dyqan-online-tirane/', 'Katalog, pagesa dhe dërgesa me platformën që ju shkon.')),
             ('Softuer me porosi', a('/softuer-me-porosi-tirane/', 'Panele, rezervime dhe sisteme të ndërtuara mbi procesin tuaj.')),
             ('Aplikacione mobile', a('/aplikacione-mobile-tirane/', 'Kur ka kuptim një aplikacion dhe kur jo.')),
             ('SEO', a('/seo-tirane/', 'Të gjendeni kur klientët në Tiranë kërkojnë atë që bëni.')),
         ])),
         ('punojme', 'Si punojmë, nga distanca', 'Distanca nuk është problemi; mungesa e një personi kontakti është.',
          ['<p>' + REMOTE + ' Para se të nisim merrni një ofertë të shkruar me faqet, funksionet, afatet dhe koston. Gjatë punës e shihni faqen duke u ndërtuar dhe e korrigjojmë bashkë.</p>',
           '<p>Pas publikimit keni 30 ditë mbështetje të përfshira; pastaj vendosim bashkë mirëmbajtjen, nëse e dëshironi.</p>']),
         ('google', 'Të gjendeni në Google në Tiranë', 'Kur dikush kërkon një shërbim, Google shfaq së pari hartën me profile.',
          ['<p>Për biznesin tuaj kjo do të thotë tre gjëra: një Profil Biznesi në Google i plotë (kategori e saktë, orare, foto të vërteta, vlerësime të klientëve të vërtetë), një faqe që thotë qartë çfarë bëni dhe ku, dhe të dhëna të njëjta kudo (emri, adresa, telefoni). Më shumë te ' + a('/seo-tirane/', 'SEO në Tiranë') + '. ' + NOTE + '</p>']),
         ('projekte', 'Çfarë kemi ndërtuar', 'Disa nga projektet tona, për ta parë se si mendojmë.',
          ['<p>Kemi ndërtuar faqe interneti, platforma dhe sisteme për biznese të sektorëve të ndryshëm: një sistem rradhësh për shëndetësinë publike (RadhëZero), një platformë për rezervimin e klasave në palestër (GymXam), një platformë për menaxhimin e punonjësve (TiTech Workforce) dhe faqe për biznese të vogla. Shiko ' + a('/punimet/', 'punimet') + '.</p>']),
     ],
     faq=[('A keni zyrë në Tiranë?', 'Jo: ekipi ka bazën në Itali dhe punon në distancë me klientët në Tiranë dhe në Shqipëri. Takimet bëhen me video; kur projekti kërkon një takim në vend, e organizojmë sipas marrëveshjes.'),
          ('Sa kushton një faqe interneti?', 'Varet nga faqet, funksionet dhe teksti. Nuk japim një çmim standard: japim një ofertë të shkruar pasi kuptojmë projektin. Shih ' + a('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'çfarë e ndryshon çmimin') + '.'),
          ('Sa kohë duhet për një faqe?', 'Varet nga përmbajtja dhe nga sa shpejt na jepni tekstet dhe fotot. Fillimisht e mat afatin bashkë me ju dhe e shkruan në ofertë.'),
          ('A mund të merrni një projekt të vogël?', 'Po, nëse ka kuptim. Një faqe e vogël me pak faqe qëndron në një kategori të përmbajtur. Kur një buxhet nuk mjafton për objektivin, e themi qartë dhe zvogëlojmë fushën e punës, jo cilësinë.')],
     related=[('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Çfarë përfshin një faqe interneti.'),
              ('/dyqan-online-tirane/', 'Dyqan online në Tiranë', 'Katalog, pagesa dhe dërgesa.'),
              ('/seo-tirane/', 'SEO në Tiranë', 'Të gjendeni në Google.')],
     cta_title='Të flasim për biznesin tuaj në Tiranë', cta_text='Na shkruani çfarë bëni dhe çfarë nuk funksionon sot. Përgjigjemi me një vlerësim fillestar.',
     city='Tiranë')

# -------- website service
page(slug='krijimi-i-faqeve-web-tirane', kind='service', title='Krijimi i faqeve web në Tiranë | TiTech Digital',
     h1='Krijimi i faqeve web në Tiranë', eyebrow='Faqe interneti',
     description='Krijojmë faqe interneti për biznese në Tiranë dhe Shqipëri: të shpejta, të qarta dhe të gjetshme në Google. Ofertë e shkruar para se të nisim.',
     lead='Faqet që ndërtojmë shpjegojnë çfarë bën biznesi juaj, ngarkohen shpejt nga telefoni dhe bëhen për t\'u gjetur në Google. Punojmë me biznese në Tiranë dhe në gjithë Shqipërinë.',
     takeaways=[('Nis nga objektivi.', 'Çfarë duhet të bëjë faqja: të sjellë telefonata, kërkesa, rezervime apo porosi.'),
                ('Pak faqe, të qarta.', 'Çdo faqe ka një detyrë.'), ('E shpejtë në telefon.', 'Shumica e vizitorëve vijnë nga celulari.'),
                ('E gjetshme në Google.', 'SEO bazë përfshihet që në fillim.')],
     sections=[
         ('perfshin', 'Çfarë përfshin një faqe interneti', 'Çdo projekt ka një listë të shkruar të asaj që do të merrni.', checks([
             ('Struktura dhe dizajni', 'Faqet e nevojshme, dizajn i pastër dhe i përshtatur për telefon.'),
             ('Tekstet dhe fotot', 'Tekste të qarta; ju ndihmojmë t\'i shkruani ose t\'i rishikoni. Foto të vërteta, jo të stokut, kur është e mundur.'),
             ('Shpejtësia', 'Imazhe të optimizuara dhe kod i lehtë, që faqja të hapet shpejt edhe me lidhje të dobët.'),
             ('SEO bazë', 'Titujt, përshkrimet, struktura, harta e faqes dhe të dhënat e strukturuara që Google i kupton.'),
             ('Kontakt dhe matje', 'Formular kontakti, WhatsApp dhe analitikë me pëlqimin e vizitorit.'),
             ('Publikimi dhe mbështetja', '30 ditë mbështetje pas publikimit; pastaj mirëmbajtje e dakorduar.'),
         ])),
         ('procesi', 'Si punojmë', 'Katër hapa, me një person kontakti.',
          ['<ol class="prose-steps"><li><strong>Bisedë e parë.</strong> Çfarë bën biznesi, kush janë klientët, çfarë nuk funksionon sot.</li>'
           '<li><strong>Ofertë e shkruar.</strong> Faqet, funksionet, afatet dhe kostoja, para se të nisë puna.</li>'
           '<li><strong>Ndërtim.</strong> E shihni faqen duke u formuar, e korrigjojmë bashkë dhe e provojmë në telefon.</li>'
           '<li><strong>Publikim dhe ndjekje.</strong> Faqja del online, kontrollojmë që gjithçka funksionon dhe vazhdojmë me mbështetjen.</li></ol>',
           '<p>' + REMOTE + '</p>']),
         ('biznese', 'Për çfarë biznesesh', 'Çdo sektor ka prioritete të ndryshme, jo vetëm tekste të ndryshme.',
          ['<ul><li><strong>Restorante, hotele dhe turizëm:</strong> menu, foto, rezervime direkte dhe disa gjuhë.</li><li><strong>Klinika dhe studio:</strong> shërbimet, njerëzit, kontakt i qartë dhe ruajtje e të dhënave.</li><li><strong>Dyqane dhe tregti:</strong> katalog dhe, kur ka kuptim, porosi online (shih ' + a('/dyqan-online-tirane/', 'dyqan online') + ').</li><li><strong>Kompani prodhimi dhe shërbimesh:</strong> aftësi, referenca dhe kërkesa për ofertë.</li></ul>']),
         ('google', 'Të gjendeni në Google', 'Një faqe e bukur që askush nuk e gjen nuk ndihmon.',
          ['<p>Çdo faqe nis me një fjalë kyçe të menduar, tituj të saktë dhe lidhje të brendshme. Për kërkimet vendore (si "restorant Tiranë") ndihmon edhe Profili i Biznesit në Google. Shih ' + a('/seo-tirane/', 'SEO në Tiranë') + '. ' + NOTE + '</p>']),
         ('kosto', 'Sa kushton', 'Nuk ka një listë çmimesh, sepse kostoja varet nga projekti.',
          ['<p>Varet nga numri i faqeve, funksionet (formularë, rezervime, shumë gjuhë, dyqan), teksti dhe fotot. Marrni një ofertë të shkruar. Për të kuptuar çfarë e ndryshon çmimin lexoni ' + a('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'sa kushton një faqe interneti në Shqipëri') + '.</p>']),
     ],
     faq=[('Sa kohë duhet për një faqe interneti?', 'Varet nga përmbajtja dhe nga sa shpejt na jepni tekstet dhe fotot. Afatin e matim bashkë dhe e shkruajmë në ofertë.'),
          ('A mund ta përditësoj vetë faqen?', 'Po, nëse e kërkoni që në fillim: e ndërtojmë që pjesët që ndryshojnë (orare, çmime, foto) t\'i ndryshoni vetë.'),
          ('Punoni në distancë?', REMOTE),
          ('Çfarë ndodh pas publikimit?', 'Keni 30 ditë mbështetje të përfshira. Pastaj dakordësohet mirëmbajtja: përditësime, kopje rezervë dhe kontrolle.')],
     related=[('/dyqan-online-tirane/', 'Dyqan online në Tiranë', 'Katalog, pagesa dhe dërgesa.'),
              ('/seo-tirane/', 'SEO në Tiranë', 'Të gjendeni në Google.'),
              ('/blog/si-te-zgjidhni-nje-agjenci-web/', 'Si të zgjidhni një agjenci web', 'Pyetjet që duhen bërë.')],
     cta_title='Të flasim për faqen tuaj', cta_text='Na tregoni çfarë bëni dhe çfarë nuk funksionon sot. Marrni një vlerësim fillestar.',
     service='Krijimi i faqeve web', city='Tiranë')

# -------- online store
page(slug='dyqan-online-tirane', kind='service', title='Dyqan online (e-commerce) në Tiranë | TiTech Digital',
     h1='Dyqan online në Tiranë', eyebrow='E-commerce',
     description='Ndërtojmë dyqane online për biznese në Tiranë dhe Shqipëri: katalog, pagesa dhe dërgesa. Platforma e duhur për ju, jo për ne.',
     lead='Një dyqan online funksionon kur katalogu, pagesat dhe dërgesat janë menduar bashkë. Zgjedhim platformën që përshtatet me biznesin tuaj dhe me mënyrën si paguhet dhe dërgohet në Shqipëri.',
     takeaways=[('Pagesat janë pika më e ndjeshme.', 'Jo çdo platformë pagesash mbulon Shqipërinë: kontrollohet para se të zgjidhet.'),
                ('Platforma ndryshon sipas rastit.', 'Disa produkte kërkojnë një zgjidhje të gatshme, të tjera një sistem me porosi.'),
                ('Dërgesat dhe kthimet.', 'Planifikohen që në fillim, jo kur vjen porosia e parë.'),
                ('Rregullat i verifikoni me kontabilistin.', 'Taksat dhe detyrimet varen nga biznesi juaj.')],
     sections=[
         ('platforma', 'Zgjedhja e platformës', 'Nuk ka një platformë më të mirë për të gjithë.', checks([
             ('Zgjidhje të gatshme (si Shopify)', 'Të shpejta për t\'u hapur dhe të thjeshta për t\'u menaxhuar; kufizime te pagesat në disa vende, përfshirë mundësisht Shqipërinë (shih më poshtë).'),
             ('WooCommerce mbi WordPress', 'Më shumë kontroll dhe fleksibilitet, por kërkon mirëmbajtje dhe përditësime.'),
             ('Dyqan me porosi', 'Kur procesi është i veçantë (çmime sipas klientit, porosi me afate, integrim me sisteme).'),
         ])),
         ('pagesat', 'Pagesat në Shqipëri: kontrolloni para se të zgjidhni', 'Është pika ku ndalen shumë projekte.',
          ['<p>Disa shërbime pagesash të integruara në platformat e njohura nuk janë të disponueshme në çdo vend. Në kohën e shkrimit, sipas listave të vendeve të mbështetura të vetë platformave, Shopify Payments dhe WooPayments nuk e përfshijnë Shqipërinë; kjo mund të ndryshojë, prandaj duhet verifikuar. Zgjidhja zakonisht është një ofrues pagese i jashtëm ose një procesues vendas që pranon biznese shqiptare, plus mundësia e pagesës në dorëzim.</p>',
           '<p>Para se të zgjidhet platforma, kontrollojmë me procesuesin e zgjedhur nëse e pranon biznesin tuaj, çfarë komisionesh ka dhe sa kohë duhen për aktivizim. Vetëm pastaj ndërtojmë.</p>']),
         ('dergesat', 'Dërgesat, kthimet dhe katalogu', 'Një dyqan është një proces, jo vetëm një faqe.',
          ['<ul><li><strong>Katalogu:</strong> produkte me foto të vërteta, përshkrime të qarta dhe variante të organizuara.</li><li><strong>Dërgesat:</strong> zonat, kostoja, koha dhe kompanitë me të cilat punoni.</li><li><strong>Kthimet:</strong> rregulla të shkruara qartë, që nuk i ndryshon asnjë klient.</li><li><strong>Njoftimet:</strong> emailet e konfirmimit dhe të dërgesës, në shqip.</li></ul>']),
         ('rregullat', 'Rregullat dhe detyrimet', 'Nuk jemi kontabilistë dhe nuk japim këshilla ligjore.',
          ['<p>Shitja online ka detyrime fiskale dhe tregtare që varen nga forma e biznesit tuaj. Kontrolloni me kontabilistin dhe me autoritetet kompetente (si QKB dhe Drejtoria e Tatimeve) para se të hapni dyqanin. Ne ndërtojmë dyqanin sipas asaj që na tregoni.</p>']),
         ('google', 'Të gjendeni në Google', 'Një dyqan i ri duhet të bëhet i dukshëm.',
          ['<p>Faqet e produkteve dhe kategorive duhet të kenë tituj dhe përshkrime të vërteta, jo të kopjuara nga prodhuesi. Më shumë te ' + a('/seo-tirane/', 'SEO në Tiranë') + '. ' + NOTE + '</p>']),
     ],
     faq=[('Sa kushton një dyqan online?', 'Varet nga numri i produkteve, platforma, pagesat dhe integrimet. Japim një ofertë të shkruar. Shih edhe ' + a('/blog/dyqan-online-ne-shqiperi-platforma-dhe-pagesa/', 'udhëzuesin për dyqan online në Shqipëri') + '.'),
          ('Cila platformë është më e mirë?', 'Varet nga produktet, nga pagesat që ju lejohen dhe nga kapaciteti për ta mirëmbajtur. Pas bisedës së parë ju themi se cila ka kuptim.'),
          ('A mund të paguajnë klientët me kartë?', 'Varet nga procesuesi që pranon biznesin tuaj. E verifikojmë para se të nisë ndërtimi.'),
          ('Punoni në distancë?', REMOTE)],
     related=[('/blog/dyqan-online-ne-shqiperi-platforma-dhe-pagesa/', 'Dyqan online në Shqipëri: platforma dhe pagesa', 'Udhëzues me pikat e ndjeshme.'),
              ('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Kur mjafton një faqe pa dyqan.'),
              ('/seo-tirane/', 'SEO në Tiranë', 'Të gjendeni në Google.')],
     cta_title='Të flasim për dyqanin tuaj', cta_text='Na tregoni çfarë shisni dhe si dërgohet sot. Marrni një vlerësim fillestar.',
     service='Dyqan online (e-commerce)', city='Tiranë')

# -------- custom software
page(slug='softuer-me-porosi-tirane', kind='service', title='Softuer me porosi në Tiranë | TiTech Digital',
     h1='Softuer me porosi në Tiranë', eyebrow='Softuer me porosi',
     description='Ndërtojmë softuer me porosi për biznese në Tiranë dhe Shqipëri: panele, rezervime dhe sisteme që zëvendësojnë Excel-in dhe punën me dorë.',
     lead='Kur një biznes punon me Excel, letra dhe mesazhe në WhatsApp, humbet kohë dhe të dhëna. Ndërtojmë sisteme të vogla dhe të qarta që mbledhin procesin në një vend.',
     takeaways=[('Nis nga procesi.', 'Çfarë ndodh sot, ku humbet koha, çfarë dëshironi të ndryshojë.'),
                ('Fillim i vogël.', 'Një version i parë që përdoret, pastaj përmirësohet.'),
                ('Lidhet me atë që keni.', 'Fatura, kontabilitet, faqe interneti, kalendar.'),
                ('Mirëmbahet.', 'Dokumentim dhe mbështetje pas dorëzimit.')],
     sections=[
         ('kur', 'Kur ka kuptim softuer me porosi', 'Nuk është zgjidhja e duhur për çdo problem.',
          ['<p>Ka kuptim kur procesi është i veçantë dhe zgjidhjet e gatshme ju detyrojnë të ndryshoni mënyrën si punoni, ose kur disa mjete të ndara (Excel, email, mesazhe) bëjnë të njëjtën punë dy herë. Nuk ka kuptim kur një mjet i gatshëm bën tashmë punën: atëherë ju themi të përdorni atë.</p>']),
         ('shembuj', 'Çfarë ndërtojmë', 'Shembuj nga puna jonë, jo premtime të përgjithshme.', checks([
             ('Sisteme radhësh dhe rezervimesh', 'Si RadhëZero, një sistem rradhësh për shëndetësinë publike me monitorim në kohë reale dhe rezervime nga distanca.'),
             ('Platforma për klasa dhe abonime', 'Si GymXam, për rezervimin e klasave në palestër me disponueshmëri në kohë reale.'),
             ('Menaxhim punonjësish', 'Si TiTech Workforce: paga, dokumente, pushime dhe turne në një panel të vetëm.'),
             ('Panele dhe automatizime', 'Raporte, njoftime dhe lidhje ndërmjet sistemeve që përdorni tashmë.'),
         ])),
         ('nisja', 'Si nisim', 'Pak hapa të qartë.',
          ['<ol class="prose-steps"><li><strong>Hartojmë procesin.</strong> Si funksionon sot dhe ku humbet koha.</li><li><strong>Përcaktojmë versionin e parë.</strong> Vetëm ajo që duhet për ta përdorur.</li><li><strong>Ndërtojmë dhe provojmë me përdoruesit.</strong></li><li><strong>Përmirësojmë</strong> sipas përdorimit real.</li></ol>', '<p>' + REMOTE + '</p>']),
         ('koha', 'Kostoja dhe afatet', 'Varen nga procesi, jo nga një listë çmimesh.',
          ['<p>Pas hartimit të procesit japim një ofertë me fazat dhe koston e secilës. Nuk fillojmë pa një fushë pune të shkruar: kjo mbron si ju ashtu edhe ne.</p>']),
     ],
     faq=[('A mund të zëvendësoni Excel-in tonë?', 'Po, nëse ka kuptim. Fillimisht e kuptojmë çfarë bën sot dhe pastaj ju themi nëse ia vlen një sistem me porosi.'),
          ('A lidhet me sistemet që kemi?', 'Në shumicën e rasteve po. E analizojmë para se të japim ofertën.'),
          ('Kush e mirëmban pas dorëzimit?', 'Mund ta mirëmbajmë ne, me një marrëveshje të veçantë, dhe e dokumentojmë që të mos varet nga ne.'),
          ('Punoni në distancë?', REMOTE)],
     related=[('/aplikacione-mobile-tirane/', 'Aplikacione mobile në Tiranë', 'Kur ka kuptim një aplikacion.'),
              ('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Faqe interneti të qarta.'),
              ('/sherbimet/', 'Të gjitha shërbimet', 'Çfarë ofrojmë.')],
     cta_title='Të flasim për procesin tuaj', cta_text='Na tregoni çfarë bëni sot me Excel ose me dorë. Marrni një vlerësim fillestar.',
     service='Softuer me porosi', city='Tiranë')

# -------- mobile apps
page(slug='aplikacione-mobile-tirane', kind='service', title='Aplikacione mobile në Tiranë | TiTech Digital',
     h1='Aplikacione mobile në Tiranë', eyebrow='Aplikacione mobile',
     description='Aplikacione mobile për biznese në Tiranë dhe Shqipëri: kur ka kuptim një aplikacion, çfarë duhet para se të nisë dhe si funksionon procesi.',
     lead='Para se të ndërtojmë një aplikacion, e pyesim nëse duhet. Shpesh një faqe web që funksionon mirë nga telefoni zgjidh të njëjtin problem me më pak kosto. Kur aplikacioni ka kuptim, e ndërtojmë me kujdes.',
     takeaways=[('Aplikacion apo faqe web?', 'Pyetja e parë dhe më e rëndësishme.'), ('Përdorues dhe qëllim.', 'Kush e përdor, sa shpesh dhe për çfarë.'),
                ('iOS dhe Android.', 'Zgjedhim se si të mbulohen të dyja pa e dyfishuar koston.'), ('Pas publikimit.', 'Përditësimet dhe mirëmbajtja janë pjesë e planit.')],
     sections=[
         ('apo', 'Aplikacion apo faqe web që funksionon nga telefoni', 'Dallimi ndryshon koston dhe afatin.', checks([
             ('Mjafton një faqe web', 'Informacion, rezervime, katalog, formularë. Hapet nga çdo telefon, pa instalim.'),
             ('Ka kuptim aplikacioni', 'Njoftime, përdorim pa internet, qasje te funksione të telefonit (kamera, vendndodhja) ose përdorim shumë i shpeshtë.'),
             ('Një mes i dytë', 'Një faqe web që instalohet si aplikacion (PWA), për disa raste.'),
         ])),
         ('para', 'Çfarë duhet para se të nisim', 'Një aplikacion pa objektiv të qartë është kosto pa kthim.',
          ['<ul><li><strong>Kush e përdor</strong> dhe në çfarë situate.</li><li><strong>Funksionet kryesore</strong>: një listë e shkurtër, jo një listë dëshirash.</li><li><strong>Lidhja me sisteme</strong> ekzistuese (faqe, kontabilitet, rezervime).</li><li><strong>Llogari zhvilluesi</strong> në dyqanet e aplikacioneve (Apple dhe Google), të cilat kanë rregullat dhe tarifat e tyre.</li></ul>']),
         ('procesi', 'Si punojmë', 'Hapa të qartë, me një person kontakti.',
          ['<ol class="prose-steps"><li><strong>Vlerësim.</strong> A duhet aplikacion? Çfarë versioni i parë ka kuptim?</li><li><strong>Ofertë e shkruar.</strong> Funksione, faza, afate dhe kosto.</li><li><strong>Ndërtim dhe prova.</strong> Ju jepet një version për ta provuar para publikimit.</li><li><strong>Publikim dhe mbështetje.</strong></li></ol>', '<p>' + REMOTE + '</p>']),
         ('kosto', 'Kostoja', 'Nuk ka një çmim të vetëm.',
          ['<p>Varet nga numri i funksioneve, platformat (iOS, Android ose të dyja), lidhjet me sisteme dhe dizajni. Pas vlerësimit japim një ofertë. Për ta lidhur me një sistem më të gjerë, shih ' + a('/softuer-me-porosi-tirane/', 'softuer me porosi') + '.</p>']),
     ],
     faq=[('A më duhet vërtet një aplikacion?', 'Shpesh jo: një faqe web që funksionon mirë nga telefoni mjafton. Ju themi çiltërisht nëse nuk ia vlen.'),
          ('Një aplikacion për iOS dhe Android?', 'Varet nga përdoruesit tuaj. Zgjedhim një qasje që mbulon të dyja pa e dyfishuar koston, kur është e mundur.'),
          ('Sa kohë duhet?', 'Varet nga funksionet. Pas vlerësimit e shkruajmë në ofertë.'),
          ('Punoni në distancë?', REMOTE)],
     related=[('/softuer-me-porosi-tirane/', 'Softuer me porosi në Tiranë', 'Sisteme që zëvendësojnë punën me dorë.'),
              ('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Kur mjafton një faqe web.'),
              ('/sherbimet/', 'Të gjitha shërbimet', 'Çfarë ofrojmë.')],
     cta_title='Të flasim për idenë tuaj', cta_text='Na tregoni çfarë dëshironi të bëjë aplikacioni dhe kush do ta përdorë. Marrni një vlerësim fillestar.',
     service='Aplikacione mobile', city='Tiranë')

# -------- SEO
page(slug='seo-tirane', kind='service', title='SEO në Tiranë: të gjendeni në Google | TiTech Digital',
     h1='SEO në Tiranë', eyebrow='SEO',
     description='SEO për biznese në Tiranë dhe Shqipëri: SEO teknike, Profili i Biznesit në Google, përmbajtje dhe matje. Pa premtime pozicionesh.',
     lead='SEO është puna që bën që klientët të ju gjejnë kur kërkojnë atë që bëni. Nis nga një faqe e saktë teknikisht, vazhdon me përmbajtje dhe prani vendore dhe matet në Google Search Console.',
     takeaways=[('Baza teknike së pari.', 'Shpejtësi, strukturë, harta e faqes, të dhëna të strukturuara.'),
                ('SEO vendore.', 'Profili i Biznesit në Google dhe të dhëna të njëjta kudo.'), ('Përmbajtje që përgjigjet.', 'Faqe dhe udhëzues për pyetjet që bëjnë klientët.'),
                ('Pa premtime.', NOTE)],
     sections=[
         ('teknike', 'SEO teknike', 'Nëse Google nuk e lexon mirë faqen, pjesa tjetër nuk ndihmon.', checks([
             ('Indeksimi', 'Harta e faqes, robots, URL të pastra dhe asnjë faqe të bllokuar gabimisht.'),
             ('Shpejtësia dhe celulari', 'Imazhe të lehta, kod i pastër, përdorim i mirë nga telefoni.'),
             ('Struktura', 'Tituj dhe përshkrime për secilën faqe, lidhje të brendshme logjike.'),
             ('Të dhëna të strukturuara', 'Të dhëna për biznesin, shërbimet dhe pyetjet e shpeshta që Google i kupton.'),
         ])),
         ('lokale', 'SEO vendore: Profili i Biznesit në Google', 'Për kërkimet me qytet, hartat vijnë para faqeve.',
          ['<ul><li>Kategori e saktë, orare reale, foto të vërteta.</li><li>Emri, adresa dhe telefoni njësoj në Profil, në faqe dhe kudo tjetër.</li><li>Vlerësime nga klientë të vërtetë: kërkohen te të gjithë, pa shpërblime dhe pa vlerësime të shkruara nga të tjerët.</li><li>Verifikimi i Profilit ndjek hapat që kërkon Google për biznesin tuaj.</li></ul>',
           '<p>Një udhëzues i detajuar: ' + a('/blog/seo-lokale-per-biznese-ne-shqiperi/', 'SEO lokale për biznese në Shqipëri') + '.</p>']),
         ('permbajtje', 'Përmbajtje që përgjigjet', 'Faqet e mira i përgjigjen një pyetjeje të vërtetë.',
          ['<p>Zgjedhim fjalët që klientët përdorin vërtet (në shqip, shpesh edhe në anglisht) dhe ndërtojmë faqe për to: shërbimet, udhëzues, pyetje të shpeshta. Çdo faqe ka një objektiv dhe nuk përsërit një tjetër.</p>']),
         ('matja', 'Matja', 'Pa matje nuk dihet çfarë funksionon.',
          ['<p>Google Search Console tregon për cilat kërkime shfaqet faqja, sa herë dhe në çfarë pozicioni. Në bazë të tyre vendosim çfarë të përmirësojmë, pa u mbështetur në ndjesi.</p>', '<p>' + NOTE + '</p>']),
     ],
     faq=[('Sa kohë duhet për të parë rezultate?', 'Për një faqe të re, zakonisht disa javë për kërkime të ngushta dhe disa muaj për ato më të konkurruara. Askush nuk mund të garantojë një pozicion.'),
          ('A më duhet Profili i Biznesit në Google?', 'Nëse klientët ju kërkojnë në një qytet, po: harta shfaqet para faqeve. Faqja dhe Profili duhet të thonë të njëjtën gjë.'),
          ('A blini lidhje apo vlerësime?', 'Jo. Lidhjet e blera dhe vlerësimet e rreme e dëmtojnë faqen dhe mund ta bëjnë të zhduket nga Google.'),
          ('Punoni në distancë?', REMOTE)],
     related=[('/blog/seo-lokale-per-biznese-ne-shqiperi/', 'SEO lokale për biznese në Shqipëri', 'Hap pas hapi.'),
              ('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Faqja që SEO ndihmon.'),
              ('/tirane/', 'Faqe interneti dhe softuer në Tiranë', 'Si punojmë me bizneset e Tiranës.')],
     cta_title='Të flasim për dukshmërinë tuaj', cta_text='Na tregoni çfarë bëni dhe ku dëshironi të gjendeni. Marrni një vlerësim fillestar.',
     service='SEO', city='Tiranë')

# -------- guides
page(slug='blog/sa-kushton-nje-faqe-interneti-ne-shqiperi', kind='guide', title='Sa kushton një faqe interneti në Shqipëri',
     h1='Sa kushton një faqe interneti në Shqipëri', eyebrow='Blog · Çmime', minutes=7,
     description='Nuk ka një çmim standard për një faqe interneti: kostoja varet nga faqet, funksionet dhe teksti. Çfarë e ndryshon çmimin dhe si krahasohen dy oferta.',
     lead='Kush kërkon "sa kushton një faqe interneti" gjen zakonisht një përgjigje të turbullt: çmimet shkojnë nga abonime të vogla deri në projekte me mijëra euro. Arsyeja është që "faqe interneti" mund të thotë gjëra shumë të ndryshme. Ky udhëzues shpjegon çfarë e ndryshon çmimin dhe si t\'i krahasoni ofertat.',
     takeaways=[('Nuk ka një çmim të vetëm.', 'Një faqe me pesë faqe dhe një dyqan me ERP nuk kushtojnë njëlloj.'), ('Çmimi ndryshon me fushën e punës.', 'Faqet, funksionet, tekstet, fotot, gjuhët.'),
                ('Krahasoni oferta me të njëjtën listë.', 'Çfarë përfshihet dhe çfarë jo.'), ('Kostoja vjetore ekziston.', 'Domeni, hostingu dhe mirëmbajtja.')],
     sections=[
         ('pse', 'Pse nuk ka një çmim standard', 'Dy oferta me "faqe interneti" mund të përshkruajnë gjëra krejt të ndryshme.',
          ['<p>Një faqe prezantuese me disa faqe dhe një formular është një punë e vogël. Një faqe me katalog, rezervime, disa gjuhë dhe lidhje me një sistem është një projekt tjetër. Kush ju jep një çmim pa ju pyetur për këto, ose po përsërit një model, ose po ju premton diçka që nuk e ka kuptuar.</p>']),
         ('ndryshon', 'Çfarë e ndryshon çmimin', 'Katër ndryshore bëjnë pjesën më të madhe të diferencës.', checks([
             ('Numri dhe lloji i faqeve', 'Pak faqe të qarta ose shumë faqe me përmbajtje të ndryshme.'),
             ('Funksionet', 'Formularë, rezervime, dyqan, zonë klienti, lidhje me sisteme të tjera.'),
             ('Teksti dhe fotot', 'A i keni gati, apo duhen shkruar dhe fotografuar? Shpesh është pjesa më e madhe e punës.'),
             ('Gjuhët', 'Çdo gjuhë shtesë do të thotë tekste dhe struktura shtesë, jo vetëm përkthim.'),
         ])),
         ('krahaso', 'Si krahasohen dy oferta', 'Nuk mjafton të shihni totalin.',
          ['<ul><li>A përfshihen tekstet, fotot dhe SEO bazë?</li><li>A përfshihet testimi në telefon dhe në shfletues të ndryshëm?</li><li>Çfarë ndodh pas publikimit: ka mbështetje të përfshirë, për sa kohë?</li><li>Kush e zotëron domenin, hostingun dhe qasjet?</li><li>Çfarë kushton mirëmbajtja çdo vit, e shkruar që tani?</li></ul>',
           '<p>Një çmim shumë më i ulët se të tjerët zakonisht heq diçka: teksti, testimi, mbështetja. Kërkoni ta shkruajnë.</p>']),
         ('vjetor', 'Kostot që vijnë çdo vit', 'Një faqe nuk paguhet vetëm një herë.',
          ['<p>Domeni dhe hostingu paguhen çdo vit. Faqja gjithashtu kërkon përditësime, kopje rezervë dhe kontrolle: nëse nuk bëhen, faqja plaket brenda disa muajsh. Pyesni që në fillim çfarë kushton dhe çfarë përfshin mirëmbajtja.</p>']),
         ('si', 'Si marrni një çmim të saktë', 'Tre hapa.',
          ['<ol class="prose-steps"><li><strong>Shkruani çfarë ju duhet:</strong> faqet, funksionet, gjuhët, çfarë keni gati.</li><li><strong>Kërkoni dy ose tri oferta</strong> me të njëjtën specifikim.</li><li><strong>Krahasoni çfarë përfshihet</strong>, jo vetëm totalin.</li></ol>',
           '<p>Nëse dëshironi një ofertë nga ne, shkruani në ' + a('/kontakt/', 'kontakt') + ' dhe përgjigjemi me një vlerësim fillestar. Për projektin më të ngushtë, shih ' + a('/krijimi-i-faqeve-web-tirane/', 'krijimi i faqeve web në Tiranë') + '.</p>']),
     ],
     faq=[('A është më mirë një ndërtues faqesh (Wix, Squarespace, etj.)?', 'Për një faqe shumë të thjeshtë mund të mjaftojë. Kur duhet SEO e kujdesshme, kontroll mbi shpejtësinë, funksione të veçanta ose lidhje me sisteme, zakonisht jo.'),
          ('Sa kushton hostingu dhe domeni?', 'Varet nga ofruesi dhe nga paketa; është një kosto vjetore e vogël në krahasim me projektin, por duhet të jetë në emrin tuaj.'),
          ('A mund të paguhet me këste?', 'Mund të dakordësohet një kalendar pagesash sipas fazave. E shkruajmë në ofertë.'),
          ('Si fillon një bashkëpunim me ju?', 'Me një bisedë të parë pa pagesë dhe një ofertë të shkruar. Shih ' + a('/kontakt/', 'kontakt') + '.')],
     related=[('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Çfarë përfshin një faqe interneti.'),
              ('/blog/si-te-zgjidhni-nje-agjenci-web/', 'Si të zgjidhni një agjenci web', 'Pyetjet që duhen bërë.'),
              ('/dyqan-online-tirane/', 'Dyqan online në Tiranë', 'Kur duhet një dyqan.')],
     cta_title='Marrni një ofertë të shkruar', cta_text='Na tregoni çfarë ju duhet dhe ju përgjigjemi me një vlerësim fillestar.')

page(slug='blog/dyqan-online-ne-shqiperi-platforma-dhe-pagesa', kind='guide', title='Dyqan online në Shqipëri: platforma dhe pagesa',
     h1='Dyqan online në Shqipëri: platforma, pagesa dhe dërgesa', eyebrow='Blog · E-commerce', minutes=8,
     description='Si të hapni një dyqan online në Shqipëri: zgjedhja e platformës, pagesat (ku ndalen shumë projekte), dërgesat dhe rregullat që duhen verifikuar.',
     lead='Hapja e një dyqani online duket e thjeshtë: zgjidhni një platformë, shtoni produktet dhe prisni porositë. Në praktikë, tri pika përcaktojnë nëse funksionon: pagesat, dërgesat dhe organizimi i biznesit. Ky udhëzues i shqyrton për Shqipërinë.',
     takeaways=[('Pagesat para platformës.', 'Zgjidhni platformën pasi të dini si do të paguajnë klientët.'), ('Platforma varet nga produkti.', 'Nuk ka një zgjedhje më të mirë për të gjithë.'),
                ('Dërgesat janë pjesë e përvojës.', 'Kostoja, koha dhe kthimet.'), ('Rregullat verifikohen me kontabilistin.', 'Nuk japim këshilla ligjore.')],
     sections=[
         ('pagesat', 'Pagesat: pika ku ndalen shumë projekte', 'Kontrolloni para se të ndërtoni.',
          ['<p>Shërbimet e integruara të pagesave të platformave të njohura nuk janë të disponueshme në çdo vend. Në kohën e shkrimit, sipas listave të vendeve të mbështetura të vetë platformave, Shopify Payments dhe WooPayments nuk e përfshijnë Shqipërinë; kjo mund të ndryshojë, prandaj kontrolloni listën aktuale. Atëherë ka tri rrugë: një ofrues pagese i jashtëm që pranon biznese shqiptare, një procesues vendas, ose pagesa në dorëzim.</p>',
           '<p>Çdo ofrues ka kushtet e veta: komisione, kohë aktivizimi, dokumente të kërkuara dhe monedha. Kërkoni përgjigje të shkruara dhe konfirmoni që pranon biznesin tuaj para se të ndërtoni.</p>']),
         ('platforma', 'Zgjedhja e platformës', 'Tri rrugë kryesore.', checks([
             ('Platformë e gatshme (si Shopify)', 'E shpejtë për t\'u hapur dhe e lehtë për t\'u menaxhuar, por varet nga pagesat dhe nga tarifat e saj.'),
             ('WooCommerce mbi WordPress', 'Më shumë kontroll dhe më shumë mundësi pagesash, por kërkon mirëmbajtje dhe përditësime të rregullta.'),
             ('Dyqan me porosi', 'Kur procesi është i veçantë ose duhen integrime; kushton më shumë dhe nis me një fushë pune të qartë.'),
         ])),
         ('dergesat', 'Dërgesat dhe kthimet', 'Klienti e gjykon dyqanin nga dërgesa.',
          ['<ul><li>Cilat zona mbulohen dhe sa kushton dërgesa?</li><li>Sa kohë duhet dhe si njoftohet klienti?</li><li>Si funksionojnë kthimet: kush paguan, brenda sa ditësh?</li><li>Çfarë ndodh kur një produkt mbaron?</li></ul>']),
         ('biznesi', 'Organizimi i biznesit dhe rregullat', 'Para se të shisni online.',
          ['<p>Shitja online ka detyrime fiskale dhe tregtare që varen nga forma e biznesit tuaj. Kontrolloni me kontabilistin dhe me autoritetet kompetente (si QKB dhe Drejtoria e Tatimeve) çfarë ju duhet para se të hapni dyqanin. Nuk japim këshilla ligjore: ndërtojmë dyqanin sipas asaj që na tregoni.</p>']),
         ('nis', 'Si të nisni pa e komplikuar', 'Një rrugë e arsyeshme.',
          ['<ol class="prose-steps"><li><strong>Fillo me pak produkte</strong> dhe një mënyrë pagese që e dini se funksionon.</li><li><strong>Provo dërgesën</strong> me disa porosi të para.</li><li><strong>Zgjero</strong> kur procesi është i qëndrueshëm.</li></ol>',
           '<p>Nëse dëshironi ndihmë, shih ' + a('/dyqan-online-tirane/', 'dyqan online në Tiranë') + ' dhe shkruani në ' + a('/kontakt/', 'kontakt') + '.</p>']),
     ],
     faq=[('Cila platformë është më e mirë për Shqipërinë?', 'Varet nga produktet dhe nga pagesat që ju lejohen. Zgjidhet pasi të verifikohet procesuesi i pagesave.'),
          ('A mund të pranoj pagesa me kartë?', 'Po, nëse një ofrues pagese pranon biznesin tuaj. Verifikojeni para se të zgjidhni platformën.'),
          ('A mjafton pagesa në dorëzim?', 'Për disa biznese po, për fillim. Ka kosto të veçanta (kthime, mosmarrje) që duhen llogaritur.'),
          ('Sa kushton një dyqan online?', 'Varet nga produktet, platforma, pagesat dhe integrimet. Japim një ofertë të shkruar.')],
     related=[('/dyqan-online-tirane/', 'Dyqan online në Tiranë', 'Si punojmë.'),
              ('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'Sa kushton një faqe interneti', 'Çfarë e ndryshon çmimin.'),
              ('/seo-tirane/', 'SEO në Tiranë', 'Të gjendeni në Google.')],
     cta_title='Të flasim për dyqanin tuaj', cta_text='Na tregoni çfarë shisni dhe si dërgohet sot.')

page(slug='blog/seo-lokale-per-biznese-ne-shqiperi', kind='guide', title='SEO lokale për biznese në Shqipëri: Profili në Google',
     h1='SEO lokale për biznese në Shqipëri', eyebrow='Blog · SEO', minutes=8,
     description='Si të gjendet një biznes në Shqipëri kur klientët kërkojnë me qytet: Profili i Biznesit në Google, faqja, vlerësimet dhe të dhënat e njëjta kudo.',
     lead='Kur dikush kërkon "dentist Tiranë" ose "restorant Tiranë", Google shfaq së pari një hartë me profile biznesesh. Të jesh aty vendos shumë nga telefonatat. Ky udhëzues shpjegon çfarë ndikon në atë pozicion dhe çfarë mund të bëni vetë.',
     takeaways=[('Harta vjen para faqes.', 'Profili i Biznesit në Google është pika e parë e kontaktit.'), ('Të njëjtat të dhëna kudo.', 'Emri, adresa dhe telefoni identikë.'),
                ('Vlerësimet e vërteta.', 'Kërkohen te të gjithë, pa shpërblime.'), ('Faqja i konfirmon.', 'Një faqe e qartë, me qytetin dhe shërbimet.')],
     sections=[
         ('profili', 'Profili i Biznesit në Google', 'Pjesa që jep më shumë rezultat në kërkimet vendore.',
          ['<ul><li><strong>Kategoria kryesore</strong> e saktë; kategoritë shtesë vetëm nëse janë të vërteta.</li><li><strong>Emri</strong> është emri real i biznesit, pa fjalë kyçe të shtuara: kjo shkel rregullat e Google dhe mund të pezullojë profilin.</li><li><strong>Adresa dhe zona e shërbimit</strong> të vërteta; mos përdorni adresa të rreme.</li><li><strong>Orare, telefon, foto të vërteta</strong> dhe lidhja me faqen.</li><li><strong>Verifikimi</strong>: ndiqni hapat që kërkon Google për biznesin tuaj.</li></ul>']),
         ('njejta', 'Të dhënat e njëjta kudo', 'Google krahason burimet.',
          ['<p>Emri, adresa dhe telefoni duhet të jenë identikë në Profil, në faqe, në rrjetet sociale dhe në çdo katalog ku jeni futur. Dallimet e vogla (një shkurtim, një numër i ndryshëm) krijojnë pasiguri dhe dobësojnë profilin.</p>']),
         ('vleresimet', 'Vlerësimet', 'Rëndësishme dhe të ndjeshme.',
          ['<ul><li>Kërkoni vlerësim te klientët e vërtetë, te të gjithë, pa zgjedhur vetëm të kënaqurit.</li><li>Mos ofroni shpërblime, ulje ose gjëra në këmbim: Google i ndalon dhe mund t\'i fshijë.</li><li>Mos shkruani vlerësime për veten dhe mos blini vlerësime.</li><li>Përgjigjuni çdo vlerësimi, edhe negativ, me qetësi.</li></ul>']),
         ('faqja', 'Faqja e internetit', 'Konfirmon çfarë thotë Profili.',
          ['<p>Një faqe e qartë për çdo shërbim, me qytetin ku punoni dhe të dhënat e kontaktit, plus pyetje të shpeshta që u përgjigjen klientëve. Faqet që thjesht përsërisin të njëjtin tekst me emrin e një qyteti tjetër nuk ndihmojnë dhe mund ta dëmtojnë faqen. Shih ' + a('/seo-tirane/', 'SEO në Tiranë') + '.</p>']),
         ('kohe', 'Çfarë mund të prisni', 'Pa premtime.',
          ['<p>' + NOTE + ' Për kërkime të ngushta vendore, një profil i kujdesur mund të shfaqet brenda disa javësh; për kërkime më të konkurruara duhen muaj dhe më shumë vlerësime.</p>']),
     ],
     faq=[('A mund ta bëj vetë Profilin?', 'Po, është falas. Ndjek hapat e Google dhe kujdes të dhënat të jenë të vërteta dhe të njëjta kudo.'),
          ('Çfarë bëj nëse nuk kam adresë të hapur për publikun?', 'Google ka një mundësi për bizneset që shërbejnë klientët në vendin e tyre (zona e shërbimit). Kontrolloni rregullat aktuale.'),
          ('A mjafton Profili pa faqe?', 'Për disa biznese të vogla po, por një faqe e qartë e forcon besimin dhe jep më shumë informacion.'),
          ('A ndihmoni me SEO lokale?', 'Po. Shih ' + a('/seo-tirane/', 'SEO në Tiranë') + '.')],
     related=[('/seo-tirane/', 'SEO në Tiranë', 'Si punojmë.'), ('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Faqja që mbështet Profilin.'),
              ('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'Sa kushton një faqe interneti', 'Çfarë e ndryshon çmimin.')],
     cta_title='Të flasim për Profilin tuaj', cta_text='Na tregoni çfarë bëni dhe ku. Marrni një vlerësim fillestar.')

page(slug='blog/si-te-zgjidhni-nje-agjenci-web', kind='guide', title='Si të zgjidhni një agjenci web: 7 pyetje',
     h1='Si të zgjidhni një agjenci web: 7 pyetje', eyebrow='Blog · Zgjedhja e furnitorit', minutes=7,
     description='Shtatë pyetje për të zgjedhur një agjenci web: ofertë e shkruar, pronësia e faqes, mbështetja pas publikimit dhe SEO pa premtime.',
     lead='Zgjedhja e një agjencie për faqen tuaj është një vendim që e ndjeni për vite. Ja shtatë pyetje që bëjnë dallimin, dhe disa shenja që duhet t\'ju ndalojnë.',
     takeaways=[('Kërkoni gjithçka të shkruar.', 'Faza, afate, kosto, çfarë përfshihet.'), ('Pronësia e faqes.', 'Domeni, kodi dhe qasjet duhet të jenë tuajat.'),
                ('Mbështetja pas publikimit.', 'Për sa kohë dhe çfarë përfshin.'), ('SEO pa premtime.', 'Askush nuk garanton pozicion në Google.')],
     sections=[
         ('pyetjet', 'Shtatë pyetjet', 'Nëse mund t\'u përgjigjeni të gjithave me po, keni zgjedhur me kriter.', checks([
             ('1. Kush punon në projekt?', 'Njihni personin me të cilin flisni dhe kush e bën punën.'),
             ('2. A mund t\'i shoh punë të bëra?', 'Hapni faqe të vërteta dhe lexoni vlerësimet; jo vetëm imazhe.'),
             ('3. A keni një ofertë të shkruar?', 'Me fazat, afatet, koston dhe çfarë nuk përfshihet.'),
             ('4. Kush zotëron faqen?', 'Domeni, kodi, tekstet dhe qasjet duhet të jenë tuajat.'),
             ('5. Çfarë ndodh pas publikimit?', 'Mbështetja e përfshirë dhe çmimi i mirëmbajtjes.'),
             ('6. Si e trajtoni SEO-n?', 'Me metodë dhe matje, jo me premtime pozicionesh.'),
             ('7. Si matet rezultati?', 'Çfarë tregon se faqja funksionon: telefonata, kërkesa, shfaqje në Google.'),
         ])),
         ('shenja', 'Shenja që duhet t\'ju ndalojnë', 'Pesë gjëra.',
          ['<ul><li><strong>"Faqja e parë në Google e garantuar"</strong> pa metodë.</li><li><strong>Asgjë e shkruar</strong>: gjithçka me gojë.</li><li><strong>Çmim shumë më i ulët</strong> se të tjerët, pa shpjegim çfarë hiqet.</li><li><strong>Domeni dhe qasjet në emër të agjencisë</strong> pa ju thënë.</li><li><strong>Asnjë punë për t\'u parë</strong>, vetëm imazhe të stokut.</li></ul>']),
         ('ne', 'Çfarë themi ne', 'Përgjigjet tona, për krahasim.',
          ['<p>Japim një ofertë të shkruar para se të nisim; punojmë me një person kontakti; përfshijmë 30 ditë mbështetje pas publikimit dhe pastaj dakordësojmë mirëmbajtjen; nuk premtojmë pozicione në Google. Çdo kërkesë merr përgjigje, edhe kur përgjigjja është jo. Shih ' + a('/kontakt/', 'kontakt') + '.</p>']),
         ('kosto', 'Dhe çmimi?', 'Mos e shikoni vetëm totalin.',
          ['<p>Krahasoni çfarë përfshihet. Për një metodë të plotë, lexoni ' + a('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'sa kushton një faqe interneti në Shqipëri') + '.</p>']),
     ],
     faq=[('A është më mirë një agjenci apo një freelancer?', 'Varet nga projekti. Për çdo rast, kërkoni të njëjtat gjëra: ofertë të shkruar, pronësi të qartë dhe mbështetje pas publikimit.'),
          ('A më duhet një agjenci në qytetin tim?', 'Jo domosdoshmërisht: pjesa më e madhe e punës bëhet në distancë. Konton metoda, personi i kontaktit dhe qartësia e kostos.'),
          ('Si e kuptoj nëse një ofertë është shumë e ulët?', 'Shihni çfarë mungon: tekste, testim, SEO, mbështetje. Çmimi i ulët zakonisht zhvendos koston pas publikimit.'),
          ('Si fillon një bashkëpunim me ju?', 'Me një bisedë të parë pa pagesë dhe një ofertë të shkruar. Shih ' + a('/kontakt/', 'kontakt') + '.')],
     related=[('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'Sa kushton një faqe interneti', 'Çfarë e ndryshon çmimin.'),
              ('/krijimi-i-faqeve-web-tirane/', 'Krijimi i faqeve web në Tiranë', 'Si punojmë.'), ('/sherbimet/', 'Të gjitha shërbimet', 'Çfarë ofrojmë.')],
     cta_title='Na bëni të njëjtat shtatë pyetje', cta_text='Shkruani çfarë ju duhet dhe pyesni për metodën, pronësinë, mbështetjen dhe SEO-n. Ju përgjigjemi me shkrim.')

# -------- blog hub
page(slug='blog', kind='hub', title='Blog: udhëzues për faqe interneti dhe SEO | TiTech Digital',
     h1='Blog', eyebrow='Blog',
     description='Udhëzues të shkruar në shqip për faqe interneti, dyqane online dhe SEO: çmimet, pagesat në Shqipëri, SEO lokale dhe zgjedhja e një agjencie.',
     lead='Udhëzues të shkurtër, me përgjigje që mund t\'i përdorni. Nuk botojmë për të mbushur një kalendar: çdo artikull përgjigjet një pyetjeje të vërtetë.',
     takeaways=[('Çmimet.', 'Çfarë e ndryshon koston.'), ('Pagesat.', 'Ku ndalen shumë dyqane online.'), ('SEO lokale.', 'Si të gjendeni në qytetin tuaj.')],
     sections=[('artikujt', 'Artikujt', 'Udhëzues për nisje.', checks([
         ('Sa kushton një faqe interneti', a('/blog/sa-kushton-nje-faqe-interneti-ne-shqiperi/', 'Çfarë e ndryshon çmimin dhe si krahasohen dy oferta.')),
         ('Dyqan online në Shqipëri', a('/blog/dyqan-online-ne-shqiperi-platforma-dhe-pagesa/', 'Platformat, pagesat dhe dërgesat.')),
         ('SEO lokale', a('/blog/seo-lokale-per-biznese-ne-shqiperi/', 'Profili i Biznesit në Google hap pas hapi.')),
         ('Si të zgjidhni një agjenci web', a('/blog/si-te-zgjidhni-nje-agjenci-web/', 'Shtatë pyetje para se të nënshkruani.')),
         ('Si të pranoni pagesa online', a('/blog/pagesa-online-ne-shqiperi/', 'Opsionet dhe pyetjet për çdo ofrues.')),
         ('Rezervime direkte për hotele', a('/blog/rezervime-direkte-hotel-shqiperi/', 'Si t\'i çoni mysafirët te faqja juaj.')),
         ('Sa kushton SEO', a('/blog/sa-kushton-seo-ne-shqiperi/', 'Çfarë përfshihet dhe si krahasohen ofertat.')),
         ('Sa kushton një aplikacion', a('/blog/sa-kushton-nje-aplikacion-mobile/', 'Çfarë e ndryshon çmimin.')),
     ]))],
     faq=[('Kush i shkruan artikujt?', 'Ekipi i TiTech Digital. Çdo artikull përgjigjet një pyetjeje që e dëgjojmë vërtet dhe nuk përmban premtime që nuk i mbajmë.')],
     related=[('/sherbimet/', 'Shërbimet', 'Çfarë ofrojmë.'), ('/tirane/', 'Tiranë', 'Si punojmë me bizneset e Tiranës.'), ('/kontakt/', 'Kontakt', 'Na shkruani.')],
     cta_title='Keni një pyetje?', cta_text='Na shkruani dhe, nëse ka kuptim, e kthejmë në një udhëzues.')


# ---------------------------------------------------------------------------
# template
# ---------------------------------------------------------------------------
def load_shell():
    misses = set()
    tmp_out = site.OUT
    site.OUT = os.path.join(ROOT, 'al', '.shell')
    site.build_page(SHELL_SRC, 'shell.html', '/x/', '/', '/en/', misses)
    text = open(os.path.join(site.OUT, 'shell.html'), encoding='utf-8').read()
    import shutil
    shutil.rmtree(site.OUT)
    site.OUT = tmp_out
    text = re.sub(r'(<a class="(?:nav__lang|menu__lang)" href=")[^"]*(")', r'\g<1>%s/\2' % site.IT, text)
    head_prefix = text[:text.index('<script type="application/ld+json">')]
    header_block = text[text.index('<body>'):text.index('<main id="main">')]
    footer_block = text[text.index('<footer id="footer"'):]
    return head_prefix, header_block, footer_block


def build(p, shell):
    head_prefix, header_block, footer_block = shell
    path = '/' + p['slug'] + '/'
    url = BASE + path
    kind = p['kind']
    head = head_prefix
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(p['title']), head, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(p['description']), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(p['title']), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % html.escape(p['description']), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', r'\g<1>%s\2' % url, head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*(")', r'\g<1>%s\2' % url, head)
    head = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', head)
    head = re.sub(r'(<link rel="canonical" href="[^"]*">)', r'\1\n<link rel="alternate" hreflang="sq-AL" href="%s">' % url, head, count=1)
    if kind != 'guide':
        head = head.replace('<meta property="og:type" content="article">', '<meta property="og:type" content="website">')
        head = re.sub(r'\s*<meta property="article:[^>]*>', '', head)
    else:
        head = re.sub(r'(article:published_time" content=")[^"]*(")', r'\g<1>%s\2' % DATE, head)
        head = re.sub(r'(article:modified_time" content=")[^"]*(")', r'\g<1>%s\2' % DATE, head)
        head = re.sub(r'(article:section" content=")[^"]*(")', r'\g<1>Blog\2', head)

    org = {'@type': 'Organization', '@id': 'https://www.titechdigital.it/#organization', 'name': 'TiTech Digital',
           'url': 'https://www.titechdigital.it/', 'email': 'info@titechdigital.it'}
    crumbs = [('Ballina', BASE + '/')]
    if kind == 'guide':
        crumbs.append(('Blog', BASE + '/blog/'))
    crumbs.append((p['h1'], url))
    graph = [org,
             {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
                 {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(crumbs)]},
             {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': p['title'], 'inLanguage': 'sq-AL',
              'breadcrumb': {'@id': url + '#breadcrumb'}, 'dateModified': DATE}]
    if p.get('service'):
        graph.append({'@type': 'Service', '@id': url + '#service', 'name': p['service'], 'serviceType': p['service'], 'url': url,
                      'provider': {'@id': 'https://www.titechdigital.it/#organization'},
                      'areaServed': [{'@type': 'City', 'name': p.get('city', 'Tiranë')}, {'@type': 'Country', 'name': 'Shqipëri'}],
                      'description': p['description']})
    if kind == 'guide':
        graph.append({'@type': 'BlogPosting', '@id': url + '#article', 'headline': p['h1'], 'description': p['description'], 'url': url,
                      'inLanguage': 'sq-AL', 'datePublished': DATE, 'dateModified': DATE,
                      'author': {'@id': 'https://www.titechdigital.it/#organization'}, 'publisher': {'@id': 'https://www.titechdigital.it/#organization'},
                      'mainEntityOfPage': {'@id': url + '#webpage'}})
    if p.get('faq'):
        faq_nodes = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(ans)}} for q, ans in p['faq']]
        graph.append({'@type': 'FAQPage', '@id': url + '#faq', 'isPartOf': {'@id': url + '#webpage'}, 'inLanguage': 'sq-AL', 'mainEntity': faq_nodes})
    ld = '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>\n</head>\n'

    toc = '\n'.join('        <li><a href="#%s"><span class="toc__num">%02d</span><span>%s</span></a></li>' % (sid, i + 1, esc(t))
                    for i, (sid, t, _, _) in enumerate(p['sections']))
    sections = '\n\n'.join(
        '    <section class="sect" id="%s" aria-labelledby="%s-title">\n      <div class="sect__top">\n        <h2 class="m-text-4" id="%s-title">%s</h2>\n        <p class="m-text">%s</p>\n      </div>\n      <div class="prose">\n%s\n      </div>\n    </section>'
        % (sid, sid, sid, esc(t), esc(lead), '\n'.join('        ' + b for b in body))
        for sid, t, lead, body in p['sections'])
    crumb_html = '        <li><a href="/">Ballina</a></li>\n'
    if kind == 'guide':
        crumb_html += '        <li><a href="/blog/">Blog</a></li>\n'
    crumb_html += '        <li aria-current="page">%s</li>' % esc(p['h1'])
    byline = ''
    if kind == 'guide':
        byline = '\n      <p class="byline"><span class="byline__name">Ekipi i TiTech Digital</span><span class="byline__role">%d min lexim</span><time class="byline__date" datetime="%s">Përditësuar më %s</time></p>' % (p['minutes'], DATE, DATE_SQ)
    actions = ''
    if kind != 'legal':
        actions = ('\n      <div class="head__actions">\n        <a class="m-btn" href="/kontakt/"><span>Na shkruani</span></a>\n'
                   '        <a class="m-link" href="/sherbimet/"><span class="m-link__label">Të gjitha shërbimet</span><svg class="m-link__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg></a>\n      </div>')
    aside = ''
    if p.get('takeaways'):
        aside = ('\n    <aside class="takeaways" aria-labelledby="takeaways-title">\n      <h2 class="m-text-7" id="takeaways-title">Shkurt</h2>\n      <ul>\n%s\n      </ul>\n    </aside>\n'
                 % '\n'.join('        <li><strong>%s</strong> %s</li>' % (esc(t), esc(d)) for t, d in p['takeaways']))
    faq_sec = ''
    if p.get('faq'):
        faq_items = '\n'.join('        <details class="faq__item"><summary class="m-text-7">%s<span class="faq__mark" aria-hidden="true"></span></summary><p class="m-text faq__answer">%s</p></details>' % (esc(q), ans) for q, ans in p['faq'])
        faq_sec = ('\n    <section class="sect" id="faq" aria-labelledby="faq-title">\n      <div class="sect__top">\n        <h2 class="m-text-4" id="faq-title">Pyetje të shpeshta</h2>\n      </div>\n      <div class="faq">\n%s\n      </div>\n    </section>\n' % faq_items)
    rel_sec = ''
    if p.get('related'):
        cards = '\n'.join('        <article class="card card--link">\n          <h3 class="card__title"><a href="%s">%s</a></h3>\n          <p class="card__text">%s</p>\n        </article>' % (u, esc(t), d) for u, t, d in p['related'])
        rel_sec = ('\n    <section class="sect" id="lidhur" aria-labelledby="lidhur-title">\n      <div class="sect__top">\n        <h2 class="m-text-4" id="lidhur-title">Vazhdo me leximin</h2>\n      </div>\n      <div class="cards">\n%s\n      </div>\n    </section>\n' % cards)
    cta_sec = ''
    if p.get('cta_title'):
        cta_sec = ('\n    <section class="sect" aria-labelledby="cta-title">\n      <div class="cta">\n        <h2 class="m-text-4 cta__title" id="cta-title">%s<span class="m-dot" aria-hidden="true"></span></h2>\n        <p class="m-text">%s</p>\n'
                   '        <div class="cta__actions">\n          <a class="m-btn-2" href="/kontakt/"><span>Shkruani te TiTech</span></a>\n        </div>\n      </div>\n    </section>\n' % (esc(p['cta_title']), esc(p['cta_text'])))
    main = '''<main id="main">
  <div class="shell page">
    <nav aria-label="Rruga e faqes">
      <ol class="crumbs">
%(crumbs)s
      </ol>
    </nav>
    <div class="head">
      <p class="m-eyebrow">%(eyebrow)s</p>
      <h1 class="m-text-3 head__title">%(h1)s<span class="m-dot" aria-hidden="true"></span></h1>
      <p class="m-text-5 head__lead">%(lead)s</p>%(actions)s%(byline)s
    </div>
%(aside)s
    <nav class="toc" aria-label="Në këtë faqe">
      <ol>
%(toc)s
      </ol>
    </nav>

%(sections)s
%(faq)s%(related)s%(cta)s  </div>
</main>
''' % {'crumbs': crumb_html, 'eyebrow': esc(p['eyebrow']), 'h1': esc(p['h1']), 'lead': esc(p['lead']), 'actions': actions, 'byline': byline,
       'aside': aside, 'toc': toc, 'sections': sections, 'faq': faq_sec, 'related': rel_sec, 'cta': cta_sec}
    return head + ld + header_block + main + footer_block


def main():
    import al_pages_more
    al_pages_more.register(page, a, checks, NOTE, REMOTE)
    shell = load_shell()
    for p in PAGES:
        out = os.path.join(OUT, p['slug'], 'index.html')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8', newline='\n').write(build(p, shell))
        words = len(re.sub(r'<[^>]+>', ' ', open(out, encoding='utf-8').read().split('<main')[1].split('</main>')[0]).split())
        print('wrote al/%s/index.html (%d words)' % (p['slug'], words))
    site.write_sitemap()


if __name__ == '__main__':
    main()
