# Förslag: säkert parallellt teamarbete

Datum: 2026-09-08. Status: historiskt beslutsunderlag från första kartläggningen.
Aktuellt genomförande: [ADR 0001](0001-shared-build-reservations.md) och
[arbetsflödet](../operating-model/parallel-builds.md). Åtkomsthindret nedan är
senare löst via webbläsaren och grundskydden för main har aktiverats med användarens godkännande.
Granskat lokalt underlag: commit `862b892`. Oberoende read-only-agentgranskning genomförd.

## Vad kartläggningen visar

| Område | Verifierat lokalt | Lucka |
|---|---|---|
| Uppgiftsägarskap | `docs/automation/issue-intake.md` beskriver ready-for-build. | Ingen gemensam tilldelning som hindrar dubbel byggstart. |
| Arbetskopior | `AGENTS.md` kräver worktree och branch. | Implementer och `docs/chatflows/chat-routing.md` säger branch eller worktree. |
| Granskning | `.github/CODEOWNERS` anger enbart @Masse-sys. | En andra behörig mänsklig granskare behöver identifieras; agentroller ger inte separata GitHub-identiteter. |
| Automatiska kontroller | `.github/workflows/team-guardrails.yml` kontrollerar filnärvaro, agentfiler och enstaka strängar. | Inga parserkontroller eller verifierat samordningsflöde. |
| Gemensamma resurser | Orchestrator begränsar överlappande filändringar. | Saknar uttrycklig samordning av kontrakt, databaser och delade testmiljöer. |
| Sammanslagning | PR-mall med verifieringslista finns. | Ingen dokumenterad ansvarig eller ordning för att testa slutlig kombination. |

Aktiva GitHub-inställningar, öppna uppgifter, fjärrversion och CI-resultat har inte kunnat verifieras. `gh auth status` visar ingen inloggning och webbläsaranslutningen gav timeout. Det betyder inte att skydd saknas. Inga externa inställningar har ändrats.

## Rekommenderad första version

En utsedd mänsklig samordnare per repo bekräftar byggtilldelningar i GitHub, med Codex som stöd. Samordnaren behandlar anspråk i ordning. En agent får inte själv starta en uppgift enbart för att den verkar ledig eller har etiketten ready-for-build.

Varje tilldelning anger Issue, ansvarig person, huvudagent/byggchatt, unik branch, separat arbetskopia, tillåtna skrivområden, delade resurser, beroenden och tidpunkt för senaste status. En andra skrivagent får bara börja efter uttrycklig uppdelning av ansvar. Etiketter och kommentarer är administrativ samordning, inte ett tekniskt lås. Ett framtida automatiserat bokningssystem behöver atomisk tilldelning och en separat design.

Före skrivning kontrollerar agenten aktuell tilldelning, arbetsmapp, branch och befintliga ändringar. Saknas tillgång till den gemensamma tilldelningen får den inte påbörja nytt skrivarbete. Vid överlapp eller utökad scope pausas berörd del tills samordnaren har avgjort ansvar och ordning.

Vid övertagande stoppas först tidigare skrivagent. Pågående ändringar och verifieringsresultat bevaras, tilldelningen uppdateras och mottagaren bekräftar övertagandet. Ett gammalt statusdatum ger inte automatiskt rätt att ta över.

Delade kontrakt, databasscheman och miljöer räknas som arbetsområden även om agenterna ändrar olika filer. Använd separata testresurser när möjligt; annars utses en ägare och körordning.

En utsedd mergeansvarig införlivar en PR i taget. Före varje sammanslagning krävs aktuell kombination med main, relevanta gröna kontroller och oberoende granskning. Agentgranskning kompletterar mänskligt ansvar.

## Föreslagna GitHub-skydd att verifiera och därefter besluta om

- PR krävs för main och den identifierade CI-kontrollen måste vara obligatorisk.
- Kräv aktuell branch före merge, godkänd granskning och CODEOWNERS-granskning.
- Ogiltigförklara gamla godkännanden när kod ändras; verifiera oberoende godkännande av senaste ändring.
- Blockera force-push och radering; granska reglernas bypass och administratörsundantag.
- Identifiera en ytterligare behörig mänsklig granskare utan att dela konton eller utöka behörigheter automatiskt.

Merge queue är ett senare alternativ efter kontroll av abonnemang och stöd för `merge_group` i CI. Första versionen använder sekventiell sammanslagning.

GitHubs dokumentation bekräftar stöd för PR-krav, aktuella kontroller och granskningsregler: [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule). Tillgänglighet och effektiv konfiguration måste verifieras för detta repo.

## Genomförande och beslutsgräns

1. Publicera och komplettera det bifogade Issue-utkastet när GitHub är tillgängligt.
2. Fastställ samordnare och oberoende granskare, och godkänn scope.
3. Genomför dokument-, mall- och CI-ändringar i egen byggchatt, branch och worktree.
4. Läs effektiva GitHub-regler och förbered en exakt ändringslista. Ändrade behörigheter/skydd hanteras vid mänsklig kontrollpunkt enligt AGENTS.md.
5. Kör pilot med två samtidiga uppgifter och verifiera accepterade och avvisade förlopp i isolerad testmiljö.

Ingen produktkod, ny produktionsdependency eller automatisk release ingår. Säkerheten bygger på efterlevd tilldelning plus serverkontroller; den innebär ingen garanti mot alla logiska fel.
