# ADR 0001: gemensam reservation före byggstart

Status: implementeras för Issue #1, 2026-09-08.

## Beslut

Git är redan teamets gemensamma infrastruktur. En separat branch,
`codex/coordination`, innehåller en JSON-journal över aktiva reservationer.
Ingen ny tjänst eller databas införs. Detta konkretiserar det tidigare förslagets
administrativa tilldelning med atomisk publicering i Git; en separat låstjänst
ingår fortfarande inte.

Varje ändring har senaste journalcommit som förälder och publiceras med vanlig
fast-forward push. Två samtidiga ändringar blir syskon: bara en kan accepteras.
Förloraren hämtar journalen på nytt och kontrollerar överlapp innan nytt försök.
Ingen force-push används. Även första skapandet fungerar med separata rotcommits.

En reservation identifieras med ett unikt ID och binder Issue, GitHub-ansvarig,
session, branch, lokal arbetskopia (endast hash), paths och namngivna resurser.
Samma Issue, branch, arbetskopia, överlappande path eller resurs får inte bokas
två gånger. Paths är bokstavliga repo-relativa kataloger/filer, inte globbar.
Jämförelsen är konservativ och skiftlägesokänslig även på Linux.

Kontroll före skrivning hämtar aktuell journal. Release kräver både ID och
session och samma arbetskopia. Ingen timeout frigör en reservation automatiskt.
Vid haveri måste den gamla agenten stoppas och ansvarig kontrollera ändringarna
innan samma session återupptas för release. Automatisk stöld/övertagning saknas.

## Gränser

Detta är en teknisk samordning för betrodda deltagare, inte autentisering eller
en sandbox. Den som har Git-skrivåtkomst kan kringgå verktyget eller manipulera
journalen. Sessions-ID är en identifierare, inte ett lösenord. GitHub main-skydd
är en separat mekanism. Ett godkänt Issue och en reservation ersätter inte test,
granskning eller mänskligt produktionsgodkännande.

Varje repo har en journal. Resurser delade mellan repos måste fortfarande ha en
gemensam utsedd samordnare; verktyget löser inte det automatiskt. Ingen känslig
data, maskinnamn eller absoluta lokala sökvägar sparas i remote-journalen.

## Verifiering

Integrationstester använder riktiga Git-processer och en isolerad bare remote:
samtidiga anspråk, överlapp, åtskilda områden, fel session, release och offline.
GitHub-pilot ska dessutom visa blockerad PR när den obligatoriska kontrollen
misslyckas. Utfallet dokumenteras separat utan att lokala prov likställs med
flerpersonstest på flera datorer.
