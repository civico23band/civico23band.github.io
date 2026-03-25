#!/usr/bin/env python3
"""Generate Civico23 Brand Brief PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas as pdfcanvas

# Colors
CREAM = HexColor("#fdf6ec")
BROWN = HexColor("#3c2415")
BURNT_ORANGE = HexColor("#c45d3e")
MUSTARD = HexColor("#d4953a")
OLIVE = HexColor("#5b8a5e")
BLUE = HexColor("#6b7fb5")
PLUM = HexColor("#9b5e8a")
WARM_BG = HexColor("#f5e6d0")
LIGHT_CREAM = HexColor("#faf3e8")

OUTPUT = "/Users/flevour/Sites/flevour/civico23band.it/Civico23_Brand_Brief.pdf"


def bg_page(canvas, doc):
    """Draw background color on every page."""
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # Footer
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#a0927e"))
    canvas.drawCentredString(A4[0] / 2, 15 * mm, "Civico23 Brand Brief — Marzo 2026")
    canvas.restoreState()


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        topMargin=25 * mm,
        bottomMargin=25 * mm,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
    )

    base = getSampleStyleSheet()

    # -- Custom styles --
    s_cover_title = ParagraphStyle(
        "CoverTitle", parent=base["Title"],
        fontName="Helvetica-Bold", fontSize=36, leading=42,
        textColor=BROWN, alignment=TA_CENTER, spaceAfter=6 * mm,
    )
    s_cover_sub = ParagraphStyle(
        "CoverSub", parent=base["Normal"],
        fontName="Helvetica", fontSize=14, leading=18,
        textColor=BURNT_ORANGE, alignment=TA_CENTER, spaceAfter=4 * mm,
    )
    s_cover_date = ParagraphStyle(
        "CoverDate", parent=base["Normal"],
        fontName="Helvetica", fontSize=11, leading=14,
        textColor=HexColor("#a0927e"), alignment=TA_CENTER,
    )
    s_h1 = ParagraphStyle(
        "H1", parent=base["Heading1"],
        fontName="Helvetica-Bold", fontSize=20, leading=26,
        textColor=BURNT_ORANGE, spaceBefore=10 * mm, spaceAfter=4 * mm,
    )
    s_h2 = ParagraphStyle(
        "H2", parent=base["Heading2"],
        fontName="Helvetica-Bold", fontSize=14, leading=18,
        textColor=BROWN, spaceBefore=6 * mm, spaceAfter=2 * mm,
    )
    s_body = ParagraphStyle(
        "Body", parent=base["Normal"],
        fontName="Helvetica", fontSize=10.5, leading=15,
        textColor=BROWN, alignment=TA_JUSTIFY, spaceAfter=2 * mm,
    )
    s_quote = ParagraphStyle(
        "Quote", parent=base["Normal"],
        fontName="Helvetica-Oblique", fontSize=11, leading=16,
        textColor=PLUM, leftIndent=12 * mm, rightIndent=12 * mm,
        spaceBefore=3 * mm, spaceAfter=3 * mm, alignment=TA_CENTER,
    )
    s_bullet = ParagraphStyle(
        "Bullet", parent=s_body,
        leftIndent=8 * mm, bulletIndent=3 * mm,
        spaceBefore=1 * mm, spaceAfter=1 * mm,
    )
    s_pillar_name = ParagraphStyle(
        "PillarName", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=12, leading=16,
        textColor=BURNT_ORANGE,
    )
    s_pillar_desc = ParagraphStyle(
        "PillarDesc", parent=base["Normal"],
        fontName="Helvetica-Oblique", fontSize=10, leading=14,
        textColor=BROWN,
    )

    story = []

    # ============ COVER ============
    story.append(Spacer(1, 50 * mm))
    story.append(Paragraph("CIVICO23", s_cover_title))
    story.append(Paragraph("Brand Brief", ParagraphStyle(
        "CoverBrief", parent=s_cover_title, fontSize=22, leading=28,
        textColor=MUSTARD,
    )))
    story.append(Spacer(1, 10 * mm))
    story.append(HRFlowable(
        width="40%", thickness=1.5, color=BURNT_ORANGE,
        spaceAfter=8 * mm, spaceBefore=2 * mm, hAlign="CENTER",
    ))
    story.append(Paragraph(
        "Sintesi delle risposte raccolte dai 5 membri della band",
        s_cover_sub,
    ))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Marzo 2026", s_cover_date))
    story.append(PageBreak())

    # ============ 1. CONVERGENZE ============
    story.append(Paragraph("1. Convergenze forti", s_h1))
    story.append(Paragraph(
        "Punti su cui tutti (o quasi) i membri convergono spontaneamente.",
        s_body,
    ))

    # 1a
    story.append(Paragraph("Ironia + Profondità", s_h2))
    story.append(Paragraph(
        "Tutti scelgono <b>\"ironico e autoironico\"</b> come tono primario. "
        "Ma sotto l'ironia c'è un nucleo serio: paternità, crescita, vita adulta. "
        "Nessuno vuole essere <i>solo</i> cazzari.",
        s_body,
    ))

    # 1b
    story.append(Paragraph("Unicità: 5 voci + testi propri", s_h2))
    story.append(Paragraph(
        "Ricorre in quasi tutte le risposte: scrivete le vostre canzoni, cantate tutti e 5, "
        "curate le armonizzazioni. Questo è un asset fortissimo — pochi gruppi lo fanno, "
        "e nessuno su questi temi.",
        s_body,
    ))

    # 1c
    story.append(Paragraph("Momenti-chiave: San Bellino 2025 + Prato della Valle", s_h2))
    story.append(Paragraph(
        "Sono i momenti in cui la band ha \"sentito\" di essere sé stessa. "
        "Tratto comune: adattamento al pubblico, canzoni nuove testate, energia dal vivo.",
        s_body,
    ))

    # 1d
    story.append(Paragraph("Pubblico ideale: genitori 35-50, famiglie", s_h2))
    story.append(Paragraph(
        "Convergenza quasi totale. Persone che si riconoscono nelle storie, "
        "che cercano complicità più che intrattenimento generico.",
        s_body,
    ))

    # 1e
    story.append(Paragraph("\"Mai essere\": finti, pomposi, commerciali, incongruenti", s_h2))
    story.append(Paragraph(
        "L'autenticità è il valore non negoziabile. Nessuno vuole una maschera.",
        s_body,
    ))

    # ============ 2. TENSIONE CREATIVA ============
    story.append(Paragraph("2. La tensione creativa principale", s_h1))

    story.append(Paragraph(
        "\"Papà scappati di casa\" vs. \"siamo musicisti, non solo papà\"",
        s_quote,
    ))
    story.append(Paragraph(
        "Questa è la tensione più interessante e produttiva:",
        s_body,
    ))
    bullets = [
        "<b>3 su 5</b> dicono che il claim attuale li rappresenta ancora",
        "<b>1</b> dice \"ci rappresenta ora, ma non per sempre\" e insiste sulla qualità musicale come identità primaria",
        "<b>1</b> parla di evoluzione narrativa (non solo papà, ma crescita come persone)",
    ]
    for b in bullets:
        story.append(Paragraph(b, s_bullet, bulletText="•"))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "Questa tensione non va risolta, va cavalcata. È il cuore del brand: "
        "siete papà <i>e</i> musicisti, il claim può evolvere man mano che i figli crescono "
        "e voi con loro. Il brand è il <b>viaggio</b>, non una foto statica.",
        s_body,
    ))

    story.append(PageBreak())

    # ============ 3. RIFERIMENTI CULTURALI ============
    story.append(Paragraph("3. Mappa dei riferimenti culturali", s_h1))
    story.append(Paragraph(
        "I personaggi e gli artisti citati dai membri tracciano il territorio espressivo della band.",
        s_body,
    ))

    ref_data = [
        ["Riferimento", "Cosa dice della band"],
        ["Shrinking (serie TV)", "Gruppo che cresce insieme, affetto + riflessione"],
        ["Modern Family", "Caos familiare, ma sotto c'è amore"],
        ["A-Team", "Squadra con talenti diversi, sfide con creatività"],
        ["One Piece", "Avventura, follia, lealtà del gruppo"],
        ["Pinguini Tattici Nucleari", "Genuinità, trasparenza"],
        ["Nicolò Fabi (x2)", "Profondità gentile, vicinanza alla gente"],
        ["Elio", "Follia, ironia totale, libertà espressiva"],
        ["Cristicchi", "Genuinità e profondità"],
        ["Vazzanikki", "Ironia pura"],
        ["Liveplay", "Qualità musicale, attenzione al suono"],
    ]
    ref_table = Table(ref_data, colWidths=[55 * mm, 105 * mm])
    ref_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BURNT_ORANGE),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("TEXTCOLOR", (0, 1), (-1, -1), BROWN),
        ("BACKGROUND", (0, 1), (-1, -1), LIGHT_CREAM),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_CREAM, WARM_BG]),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d4c4a8")),
    ]))
    story.append(ref_table)
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(
        "Lo spettro va <b>da Elio a Fabi</b>, passando per i Pinguini. "
        "Questo triangolo è il vostro territorio.",
        s_quote,
    ))

    # ============ 4. I 4 PILASTRI ============
    story.append(Paragraph("4. I 4 pilastri del brand", s_h1))
    story.append(Paragraph(
        "Dalla sintesi emergono 4 pilastri su cui costruire tutto: "
        "comunicazione, visual, testi, live.",
        s_body,
    ))

    pillars = [
        ("a) AUTENTICITÀ AUTOBIOGRAFICA",
         "Cantiamo quello che viviamo. Non recitiamo, raccontiamo.",
         BURNT_ORANGE),
        ("b) LEGGEREZZA CON SOSTANZA",
         "Ridiamo di cose serie. La risata è il nostro modo di affrontare, non di evitare.",
         MUSTARD),
        ("c) CORALITÀ",
         "5 voci, 5 storie, un suono. Non c'è frontman, c'è un coro di vite.",
         OLIVE),
        ("d) EVOLUZIONE",
         "I figli crescono, i genitori pure. Il brand cresce con noi — non è congelato nel 2017.",
         BLUE),
    ]
    for name, desc, color in pillars:
        pill_name = ParagraphStyle("pn", parent=s_pillar_name, textColor=color)
        story.append(KeepTogether([
            Spacer(1, 3 * mm),
            Paragraph(name, pill_name),
            Paragraph(f'"{desc}"', s_pillar_desc),
        ]))

    story.append(PageBreak())

    # ============ 5. TONO DI VOCE ============
    story.append(Paragraph("5. Tono di voce", s_h1))

    tone_data = [
        ["Siamo", "Non siamo"],
        ["Autoironici", "Cinici"],
        ["Scanzonati", "Superficiali"],
        ["Genuini", "Finti-spontanei"],
        ["Caldi", "Sdolcinati"],
        ["Diretti", "Volgari"],
        ["Ambiziosi sulla musica", "Presuntuosi"],
    ]
    tone_table = Table(tone_data, colWidths=[80 * mm, 80 * mm])
    tone_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), OLIVE),
        ("BACKGROUND", (1, 0), (1, 0), BURNT_ORANGE),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("TEXTCOLOR", (0, 1), (0, -1), OLIVE),
        ("TEXTCOLOR", (1, 1), (1, -1), BURNT_ORANGE),
        ("BACKGROUND", (0, 1), (-1, -1), LIGHT_CREAM),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#d4c4a8")),
    ]))
    story.append(tone_table)

    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(
        "\"Come racconteresti questa cosa a un amico al bar, "
        "sapendo che è una cosa importante?\"",
        s_quote,
    ))

    # ============ 6. DIREZIONE VISIVA ============
    story.append(Paragraph("6. Direzione visiva", s_h1))
    story.append(Paragraph(
        "L'identità visiva è da costruire da zero. "
        "Le risposte dei membri indicano chiaramente la direzione:",
        s_body,
    ))

    vis_bullets = [
        "<b>Fresca, leggera e colorata</b> — lontana da estetiche polverose o troppo retro",
        "Interesse forte per il <b>video</b> — citato da più persone: video deliranti, contenuti visivi, "
        "il video come formato di comunicazione primario",
        "Desiderio di un <b>look coerente dal vivo</b> — fil rouge cromatico, giacca/camicia "
        "(\"padri lavoratori\"), non divisa ma elemento comune riconoscibile",
        "Un brand <b>riconoscibile ma non forzato</b> — \"ben identificabile\" ma naturale",
        "L'estetica deve trasmettere <b>qualità musicale</b>, non solo il ruolo \"papà\" — "
        "il visual deve parlare anche di chi suona bene, non solo di chi è scappato di casa",
    ]
    for b in vis_bullets:
        story.append(Paragraph(b, s_bullet, bulletText="•"))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "La nuova identità visiva dovrà bilanciare i 4 pilastri: abbastanza calda da comunicare "
        "autenticità, abbastanza curata da comunicare ambizione musicale, abbastanza colorata "
        "da comunicare energia e leggerezza.",
        s_body,
    ))

    # ============ 7. DIREZIONE STRATEGICA ============
    story.append(Paragraph("7. Direzione strategica (2 anni)", s_h1))
    story.append(Paragraph(
        "Convergenza su un posizionamento <b>ibrido musica + contenuto tematico</b>:",
        s_body,
    ))

    strat_bullets = [
        "Concerti estivi: piazze, arte di strada, poche sagre selezionate",
        "<b>Spettacoli teatrali</b> con professionisti (psicologo, educatore) — unico e differenziante",
        "CD/registrazione di qualità professionale",
        "<b>Video</b> come formato di comunicazione chiave",
        "Brano a cappella a 5 voci (proposta specifica di un membro)",
    ]
    for b in strat_bullets:
        story.append(Paragraph(b, s_bullet, bulletText="•"))

    # ============ 8. PROSSIMI PASSI ============
    story.append(Paragraph("8. Prossimi passi", s_h1))

    steps = [
        "<b>Validare questi 4 pilastri</b> con il gruppo — condividere questa sintesi e discuterne",
        "<b>Definire il claim evoluto</b> — \"Papà scappati di casa\" può restare come sottotitolo/origin story, ma serve un posizionamento che includa l'ambizione musicale",
        "<b>Rinfrescare il visual</b> del sito sulla base di queste indicazioni",
        "<b>Creare una mini-guida social</b> (2 pagine) con il tono di voce ed esempi concreti",
        "<b>Definire il look dal vivo</b> — scegliere il fil rouge di outfit",
        "<b>Investire sui video</b> — anche semplici, ma coerenti con il tono",
    ]
    for i, s in enumerate(steps, 1):
        story.append(Paragraph(f"{i}. {s}", s_bullet, bulletText=""))

    # ============ CLOSING ============
    story.append(Spacer(1, 15 * mm))
    story.append(HRFlowable(
        width="60%", thickness=1, color=MUSTARD,
        spaceAfter=5 * mm, spaceBefore=5 * mm, hAlign="CENTER",
    ))
    story.append(Paragraph(
        "\"I Civico23 esistono perché c'è vita che scorre.\"",
        ParagraphStyle("Closing", parent=s_quote, fontSize=13, leading=18,
                       textColor=BROWN),
    ))

    doc.build(story, onFirstPage=bg_page, onLaterPages=bg_page)
    print(f"PDF generato: {OUTPUT}")


if __name__ == "__main__":
    build()
