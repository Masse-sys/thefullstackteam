# Parallellt byggarbete

Codex utför kommandona. Användaren beskriver önskat resultat och godkänner
beslut som påverkar risk, åtkomst eller produktion.

## Före byggstart

1. Läs godkänt Issue och registrera ansvarig person och huvudagent/bygguppgift.
2. Skapa egen worktree (eller separat klon på annan dator) och unik branch.
3. Ange bokstavliga repo-relativa filer/kataloger som får ändras. Reservera också
   delade kontrakt och testmiljöer som namngivna resurser.
4. Ta en reservation med `tools/coordinate.py`. Endast ett framgångsrikt svar
   ger klartecken. Spara reservationens ID och session i bygguppgiften.
5. Kör `check` före varje skrivpass och före commit/PR. Ett STOP betyder att
   berört arbete måste pausas. Förändra inte scope utan att samordna först.

```text
python tools/coordinate.py status
python tools/coordinate.py acquire --issue 12 --owner GitHub-handle --session unik-session --paths src/orders tests/orders --resource orders-contract
python tools/coordinate.py check --claim RESERVATIONS-ID --session unik-session
python tools/coordinate.py release --claim RESERVATIONS-ID --session unik-session
```

Python 3.12+ och Git behövs för reservationsverktyget. Det använder endast
Pythons standardbibliotek. En bundlad Python-runtime kan användas om Codex har
en sådan; separat systeminstallation är då inte nödvändig. Git använder den
befintliga autentiseringen; inga nycklar kopieras till projektet.

## Vad som stoppas

Samma Issue, branch eller arbetskopia kan inte ha två aktiva reservationer.
`src/orders` krockar med `src/orders/form.py`; `src/orders-other` gör det inte.
Resursnamn ska vara gemensamt överenskomna, exempelvis `staging-db`.
Olika filer kan fortfarande påverka samma kontrakt, vilket måste reserveras som
en resurs. Använd `.` för hela repot om ändringen är genomgripande.

Journalen finns på `codex/coordination`, separat från main. Verktyget använder
vanlig fast-forward push och läser om vid samtidighetskonflikt. Ingen ny server
krävs. Skapa inte en egen journal per person: då försvinner det gemensamma skyddet.
Alternativ `--ref` är endast för isolerade testjournaler eller uttrycklig migration.

## Paus och överlämning

Behåll reservationen genom granskning och eventuella rättningar. Release sker
när skrivarbete är avslutat och PR är införlivad eller uppgiften avbruten.
En pausad eller kraschad agent behåller bokningen. Tid frigör den aldrig.
Vid återstart läser Codex status och använder samma ID/session i samma arbetskopia.
Vid överlämning stoppar samordnaren först tidigare agent, bevarar ändringarna,
låter den gamla sessionen släppa och låter mottagaren boka igen. Om annan agent
vinner bokningen under mellanrummet måste mottagaren vänta. Ingen force-release
eller automatisk stöld ingår.

Vid nätverksfel får en agent inte anta att uppgiften är ledig. Läs status igen
efter återställd anslutning; vid osäkert svar kan den egna bokningen redan finnas.

## Granskning och sammanslagning

En utsedd samordnare införlivar en PR i taget. PR ska ha Issue, reservation,
berörda resurser och resultat från relevanta tester. Main kräver GitHubs kontroll
`Validate shared team configuration`, aktuell branch och PR, även för admin.
Efter att en annan PR införlivats uppdateras nästa och tester körs på nytt.
Agentgranskning kompletterar tester. Oberoende obligatoriskt GitHub-godkännande
är ännu inte aktiverat eftersom repot saknar en andra granskare.

## Begränsningar

Verktyget är samordning för betrodda deltagare, inte en behörighetsbarriär.
Den som skriver förbi klienten kan fortfarande orsaka fel. `check` upptäcker
ändrade filer utanför scope, men kan inte stoppa skrivningen i förväg.
Scope får inte innehålla symlänkar/junctions till andra områden; agenten ska
reservera den verkliga destinationen och undvika sådana alias i byggarbetsytan.
Delade resurser mellan olika repos kräver gemensam samordnare eftersom varje repo
har egen journal. Main-skydd och produktens relevanta tester behövs även då.

Inga personuppgifter eller secrets får finnas i journal, fixtures eller loggar.
Se [ADR 0001](../decisions/0001-shared-build-reservations.md).
