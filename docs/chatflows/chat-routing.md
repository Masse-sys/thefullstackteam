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

Alla dessa är chattar i samma Codex-projekt när arbetet gäller teamets operativsystem eller samma produktrepo. Skapa bara de chattar som behövs.

### Setup-chatt

Den aktuella chatten för att färdigställa teamets operativsystem. Den behöver inte ersättas av en särskild Control Room.

### `Discovery – [ämne]`

Nya idéer, användarproblem, research, konkurrensbild och avgränsning.

### `Architecture – [ämne eller Issue]`

Tekniska alternativ, kontrakt, risker och ADR:er.

### `Build – Issue #N`

En konkret byggchatt per Issue. Här arbetar Codex och dess agenter i egen worktree
och unik branch, med bekräftad [reservation](../operating-model/parallel-builds.md).

### `Review – PR #N`

Testluckor, säkerhet, diffgranskning och uppföljning.

### `Release – [version eller mål]`

Releaseunderlag, changelog, deploymentplan och rollback.

### `Retrospective – [period eller leverans]`

Lärdomar som ska förbättra instruktioner, skills, mallar eller CI.

### Valfri `Control Room`

En samordningschatt kan skapas senare om många parallella arbetsströmmar gör det svårt att se nästa steg. Den är inte ett krav och ska inte skapas som ett separat lokalt projekt.

## Routingregler

- Ny idé → skapa en `Discovery – [ämne]`-chatt i rätt Codex-projekt.
- Ny idé som är tillräckligt tydlig → skapa Issue-utkast.
- Godkänt scope → starta `Build – Issue #N` i samma projekt som äger kodbasen.
- Kod, tester, branch eller Pull Request → Codex i lämplig chatt och branch/worktree.
- Produktbeslut, prioritering eller osäker målbild → Discovery- eller planeringschatt.
- Fynd i review → Review-chatt och därefter samma Build-chatt för fix.

## Viktig kontextregel

Projektet delar instruktioner, filer och annan ansluten kontext mellan sina chattar, men en ny chatt har inte automatiskt hela historiken från andra chattar. Därför ska viktiga beslut skrivas till repo-dokumentation, GitHub Issues, ADR:er eller Pull Requests. Den lokala Codex-projektmappen ska vara kopplad till rätt repo och användas för all filändring.

## Standardfraser

- `Ny idé:` startar idéintag.
- `Skapa draft issue:` skapar ett så komplett Issue-utkast som tillgänglig information medger.
- `Förbered för implementation:` kompletterar frågor och flyttar Issue mot `ready-for-build`.
- `Implementera Issue #N:` startar byggflödet.
- `Granska PR #N:` startar QA- och säkerhetsgranskning.
- `Förbered release:` tar fram releaseunderlag men stoppar före produktion.
