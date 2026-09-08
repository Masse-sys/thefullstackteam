# Kom igång med Utvecklingsteam

## Till dig som kollega

Öppna Codex och logga in med ditt eget konto. Om projektet **Utvecklingsteam**
finns: öppna en ny chatt där och bifoga denna fil. Skriv:

> Följ plan.md och gör min miljö redo för Utvecklingsteam. Utför det tekniska
> arbetet åt mig, kontrollera resultatet och berätta exakt vad jag behöver göra
> själv om inloggning eller företagsgodkännande krävs.

Om projektet saknas: bifoga filen i en första Codex-chatt. Codex hjälper dig
att ansluta teamets lokala mapp som projekt en gång. Du behöver inte en ny
projektmapp för varje idé. Därefter får varje idé en egen chatt i Utvecklingsteam.

## Uppdrag till Codex

Gör uppstarten, inte bara en lista med instruktioner. Återanvänd befintlig miljö
och be användaren endast om information eller medverkan som faktiskt saknas.
Denna fil ger inte godkännande att ändra behörigheter, köpa tjänster eller
publicera något. Be om separat klartecken för det konkreta remote-provet i steg 4.
Användaren sköter personlig inloggning. Läs aldrig ut tokens.

### 1. Hitta rätt arbetsyta och gemensam kontext

- Teamrepo: https://github.com/Masse-sys/thefullstackteam.git.
- Kontrollera befintliga Codex-projekt och lokala mappar. Återanvänd teamprojektet.
  Om det saknas, förbered en egen lokal klon och hjälp användaren öppna den som
  Utvecklingsteam. Om appverktyg saknas, guida kollegan genom att öppna den
  förberedda mappen i appen. Återanvänd inte en annan persons skrivmapp.
- Kontrollera remote, aktuell branch och befintliga ändringar innan uppdatering.
  Skriv inte över ändringar eller byt arbetsyta utan att bevara pågående arbete.
- Läs AGENTS.md, PROJECT_PROFILE.md, docs/operating-model/project-and-chat-model.md
  och docs/operating-model/parallel-builds.md. Läs övriga filer efter uppgiftens behov.
- Rapportera kort vilket repo och vilka instruktioner som faktiskt har lästs.
  En annan chatts historik följer inte automatiskt med. Läs sparade beslut och Issue.

### 2. Kontrollera åtkomst och verktyg

Kontrollera vad som redan finns, även tillgängliga bundlade runtimes. Installera
bara det som saknas och behövs, från officiell eller företagsgodkänd källa.
Följ företagets installationsregler. Redovisa verktyg, version och faktisk sökväg.

| Verktyg | När det behövs | Kontroll |
|---|---|---|
| Codex | För vårt arbetssätt | Rätt konto, lokala filer och nödvändiga verktyg går att använda. |
| Git | Repo, separata arbetskopior och reservationer | Version och läsning av rätt remote fungerar. |
| GitHub-åtkomst | Gemensamma Issues, reservationer och PR | Eget konto kan läsa repot; verifiera skrivrätt separat från offentlig läsåtkomst. |
| Python 3.12+ | Teamets reservationsverktyg | Verklig interpreter uppfyller kravet och verktygets hjälp/status fungerar. Bundlad Python går bra. |
| Node.js | När valda JS/TS-verktyg eller produktens körning kräver det | Läs projektets versionskrav och låsfil; installera inte på gissning. |
| GitHub CLI | Valfritt för effektiv automation | Använd befintlig godkänd anslutning/CLI; annars inloggad webbläsare. |
| Knowit PPT-skill | För PowerPoint | Skill, officiell mall, startskript och audit är tillgängliga. |

Node.js är exempelvis relevant för en JavaScript/TypeScript-app eller en MCP
skriven med sådana verktyg. En MCP skriven i Python kräver inte automatiskt
Node.js. Pythonkravet här kommer från teamets samordning, inte från alla produkter.
PyYAML enligt requirements-dev.txt behövs för teamrepots validering, inte för
själva reservationerna. Installera utvecklingsberoenden isolerat vid behov.

### 3. Säkerställ Knowit-regeln

- Använd installerad `knowit-ppt` och läs dess SKILL.md. Om den saknas, be
  teamansvarig om godkänd plugin/skill-källa och mallåtkomst. Hitta inte på en URL.
- Kontrollera att teamets AGENTS.md innehåller regeln: alla PowerPoint använder
  Knowit-skillen och officiell mall, inklusive typsnitt, färger, logotyp och audit.
- Föreslå samma regel i kollegans globala Codex-instruktioner om den ska gälla
  alla deras projekt; ändra inte andra personliga regler. Projektregeln räcker
  för detta team. Den överför inte automatiskt inställningar till Work.
- Kopiera aldrig någon annans hela .codex-mapp, inloggning eller API-nycklar.
  Mallar och typsnitt delas bara genom godkänd kanal, inte via publikt repo.
- Verifiera skillen med en liten lokal test-PPTX i en temporär katalog utanför
  repot, från skillens officiella mall,
  kör audit och öppna/rendera resultatet. Ingen extern publicering behövs.

### 4. Prova att samordningen fungerar

- Läs journalstatus utan att skriva och förklara eventuella aktiva reservationer.
- Kör relevanta befintliga lokala tester i isolerad temporär miljö; använd
  syntetiska testdata. Ändra inte main för ett installationstest.
- För ett verkligt skrivprov: visa först föreslaget onboarding-Issue, ändring och
  målrepo, och inhämta klartecken för publicering av Issue, testbranch och PR.
  Använd sedan ett separat onboarding-Issue, unik branch,
  egen worktree och bekräftad reservation före första repoändringen. Boka inte
  någon annans Issue eller filer. Följ verktygets dokumenterade kommandon.
- Gör en liten dokumentationsändring, kontrollera scope, öppna PR och kontrollera
  att CI och branchskydd fungerar. Behåll reservationen till avslut; ingen merge
  utan det mänskliga beslut som repots regler kräver.
- Om skrivrätt saknas: rapportera att läsning fungerar men byggstart är blockerad,
  och ange konkret vem som behöver ordna åtkomsten. Ändra inte behörigheter själv.
- Markera ett tvåpersonstest som utfört först när två olika konton/arbetskopior
  har provat samma uppgift (en ska stoppas) och åtskilda uppgifter (båda ska gå).
  Lokala processtester ersätter inte detta onboardingprov.

### 5. Starta första idén och lämna över tydligt

- Hjälp användaren att starta nästa idé i en ny chatt i Utvecklingsteam.
  Skapa ingen ny chatt utan användarens begäran. En idé per chatt.
- Skriv ett Issue-utkast med problem, målgrupp, första leverans, acceptanskriterier,
  begränsningar, data/risk och beslutspunkter innan implementation.
- Innan produktkod: ange separat målrepo och arbetsyta. Förbered teaminstruktioner,
  projektprofil, samordning och anpassade kontroller där, och läs in dem uttryckligen.
  Lägg inte produktkod i teamrepot. Ett eventuellt produktprojekt kopplas till denna
  kodbas; skapa inte ett nytt projekt bara för idéchatten. GitHub-skydd kopieras
  inte automatiskt med filer och kräver en egen mänsklig kontrollpunkt.
- Ett helt tomt produktrepo måste först etableras av en ensam utsedd ansvarig,
  med en befintlig grundcommit och verifierad skrivåtkomst. Dokumentera denna
  bootstrap och få kontrollpunkterna för nytt repo/skydd hanterade innan arbete
  delas upp. Kör vid behov reservationsverktyget från teamklonen med produktens
  worktree som arbetskatalog; kontrollera dess CLI-hjälp. Parallell produktbyggstart
  tillåts först när produktens gemensamma journal och instruktioner fungerar.
- Avsluta med en kort tabell: kontroll, verifierat resultat, kvarstående aktivitet
  och ansvarig. Säg aldrig att allt är klart om åtkomst eller tester återstår.

## Klar när

Rätt teamprojekt och instruktioner är lästa, Git/Python och åtkomst är verifierade,
Node.js är motiverat eller markerat som ej behövt, Knowit-skillen är verifierad,
och provets faktiska resultat är redovisat. Kollegan vet hur nästa idé startas.

Referens för bestående instruktioner:
[OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
