# Chatt- och routingmodell

## Roller för användaren

Användaren är Product Owner och beslutsfattare. Användaren skriver naturligt språk och behöver inte skriva kod eller använda terminalen.

Codex ska:

- ställa få men viktiga frågor
- förklara alternativ på begriplig svenska
- rekommendera ett alternativ när beslut behövs
- visa vad som är klart, vad som är osäkert och vad som kräver godkännande
- aldrig låtsas att en implementation är färdig utan verifiering

## Chattkarta

### `00 – Control Room`

Huvudchatten för målbild, prioritering, coachning, beslut och koordinering.

### `01 – Discovery`

Nya idéer, användarproblem, research, konkurrensbild och avgränsning.

### `02 – Architecture`

Tekniska alternativ, kontrakt, risker och ADR:er.

### `03 – Build – Issue #N`

En konkret byggchatt per Issue. Här arbetar Codex och dess agenter i branch/worktree.

### `04 – Review – PR #N`

Testluckor, säkerhet, diffgranskning och uppföljning.

### `05 – Release`

Releaseunderlag, changelog, deploymentplan och rollback.

### `06 – Retrospective`

Lärdomar som ska förbättra instruktioner, skills, mallar eller CI.

## Routingregler

- Ny idé → Discovery eller Control Room.
- Ny idé som är tillräckligt tydlig → skapa Issue-utkast.
- Godkänt scope → starta Codex Build-chatt.
- Kod, tester, branch eller Pull Request → Codex.
- Produktbeslut, prioritering eller osäker målbild → Control Room.
- Fynd i review → Review-chatt och därefter samma Build-chatt för fix.

## Viktig begränsning

Projektinstruktioner kan göra routing konsekvent, men ChatGPT och Codex är separata arbetsytor. Den lokala Codex-projektmappen ska vara kopplad till repot och användas för all filändring. En ChatGPT-chatt ska inte antas ha tillgång till lokala filer om den inte körs i rätt lokal Codex-kontext.

## Standardfraser

- `Ny idé:` startar idéintag.
- `Skapa draft issue:` skapar ett så komplett Issue-utkast som tillgänglig information medger.
- `Förbered för implementation:` kompletterar frågor och flyttar Issue mot `ready-for-build`.
- `Implementera Issue #N:` startar byggflödet.
- `Granska PR #N:` startar QA- och säkerhetsgranskning.
- `Förbered release:` tar fram releaseunderlag men stoppar före produktion.

