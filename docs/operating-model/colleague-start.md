# Kollegans första arbetsdag med teamet

## Var börjar jag?

Öppna produktens lokala projekt i Codex och skapa en planeringsuppgift. Beskriv
vem produkten hjälper, vilket problem den löser och vad du vill prova först.
Codex formulerar Issue och föreslår en liten leverans. Efter godkänt scope
förbereder Codex en bygguppgift med egen arbetskopia och reservation. Du provar
resultatet och ger feedback i bygguppgiften. Produktionsgodkännande ligger hos
en människa.

Varje produkt har egen mapp och eget repo. Teamets repo innehåller arbetssättet,
inte alla produkters kod. Flera funktioner får separata uppgifter i samma
produktprojekt. Work är valfritt för research och affärsunderlag; kod hanteras
av Codex. Överlämna dokumenterade beslut och Issue, inte hela chatthistoriken.

## Vad behöver installeras?

| Behov | Krävs för vårt lokala arbetssätt? |
|---|---|
| Codex och ett konto med rätt tillgång | Ja. Kollegan loggar in själv. |
| Git och åtkomst till produktens GitHub-repo | Ja, för kloner, worktrees, reservationer och PR-flödet. |
| Python 3.12+ | Ja för just vårt reservationsverktyg; bundlad runtime går bra. |
| Node.js | Bara när produktens verktyg eller valda tillägg kräver det. |
| PowerShell | Windows-shell, inget universellt ramverkskrav på alla datorer. |
| GitHub CLI | Rekommenderas för effektiv Issue/PR-automation; inloggad webbläsare kan användas. |
| PyYAML 6.0.3 | Endast för teamrepots utvecklingskontroller/CI, inte för reservationer. MIT-licens. |

Codex kontrollerar befintliga verktyg innan installation föreslås. Kollegan ska
inte behöva arbeta i terminalen. Konto-, företags- och administrationsgodkännanden
kan kräva kollegans eller IT:s medverkan. En ny appanslutning ger inte automatiskt
åtkomst till alla repos.

## Hur gör vi teamet tillgängligt?

1. Teamansvarig delar repo-länken och sliden. Varje kollega använder eget konto.
2. Efter godkänd åtkomst hjälper Codex kollegan att klona rätt produktrepo och
   ansluta mappen som lokalt projekt. Ingen delad skrivmapp används.
3. Vid ny produkt inför Codex teamets AGENTS.md, relevanta agentinstruktioner,
   reservationsverktyget, mallar och anpassade kontroller. Produktens profil
   beskriver teknik, data och testkommandon. Detta sker via granskad ändring.
4. Teamansvarig godkänner produktens GitHub-skydd och granskarupplägg. Skydden
   är inställningar per repo och följer inte automatiskt med kopierade filer.
5. Kollegan kör en liten provuppgift via Codex innan större arbete startar.

Kopiera aldrig någon annans personliga `.codex`-hemkatalog, credentials eller
API-nycklar. Personliga plugins/roller kan behöva konfigureras separat; en kopia
av repo-instruktionerna bevisar inte att alla lokala funktioner är aktiverade.

## Kostnad och fokus

Använd en liten tydlig uppgift per byggchatt. Läs bara relevanta filer, spara
beslut i repo/Issue och använd fler agenter när de har avgränsade deluppgifter.
Modellval prövas mot kvalitet och total förbrukning, inte enbart pris per token.

Källor kontrollerade 2026-09-08:
[Codex på Windows](https://learn.chatgpt.com/docs/windows/windows-app),
[Codex app](https://learn.chatgpt.com/docs/app),
[Projekt och chattar](https://learn.chatgpt.com/docs/projects).
