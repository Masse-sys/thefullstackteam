# [IDEA] Säker samordning av flera personer och Codex-agenter

Status: historiskt lokalt utkast, publicerat och vidareutvecklat som
[Issue #1](https://github.com/Masse-sys/thefullstackteam/issues/1).
Användaren har därefter beställt implementation och verkliga tester.
Föreslagna etiketter: draft, needs-discovery.
Beslutsunderlag: [Kartläggning och förslag](parallel-work-proposal.md).

## Problem och målgrupp

Flera personer och fristående Codex-sessioner kan börja på samma uppgift eller påverka samma resurs utan gemensam tilldelning. Teamets användare behöver kunna arbeta samtidigt med tydligt ansvar och kontroller innan ändringar når main.

## Önskat resultat och scope

Inför en enkel, dokumenterad tilldelning med en ansvarig samordnare, konsekvent isolering, stopp- och överlämningsregler samt verifierade kontroller för sammanslagning.

Berörda filer: AGENTS.md, .codex/agents/orchestrator.toml, .codex/agents/implementer.toml, .codex/agents/qa.toml, .codex/agents/release.toml, docs/chatflows/chat-routing.md, docs/automation/issue-intake.md, docs/operating-model/, docs/bootstrap/README.md, .github/ISSUE_TEMPLATE/, .github/pull_request_template.md och .github/workflows/team-guardrails.yml. CODEOWNERS ändras först efter beslut om verkliga granskare. Tillkommande valideringsfiler specificeras i byggplanen.

## Acceptanskriterier

- [ ] Uppgiftsmallen anger ansvarig person, huvudagent, branch, arbetskopia, skrivområden, delade resurser och beroenden.
- [ ] Ready-for-build skiljs från bekräftad tilldelning; två samtidiga anspråk ger endast en bekräftad byggstart genom en utsedd samordnare.
- [ ] Alla berörda instruktioner kräver egen arbetsmapp/worktree och unik branch.
- [ ] Överlapp, utökad scope, förlorad tillgång till tilldelning och övertagande har tydliga stoppregler.
- [ ] TOML/YAML valideras med relevanta parser-/schemakontroller; verktygsval dokumenteras.
- [ ] Effektiva GitHub-regler och obligatoriska kontrollers namn är dokumenterade med datum och bevis, inklusive bypass och granskningsidentiteter.
- [ ] En PR utan godkänd kontroll eller nödvändig granskning kan inte införlivas i pilotmiljön.
- [ ] Två tillåtna, åtskilda uppgifter kan genomföras parallellt. Överlappande anspråk och delad resurs fångas före berört skrivarbete.
- [ ] Efter en första sammanslagning omverifieras den andra PR:ens aktuella kombination. Ett avsiktligt kombinationsfel upptäcks av ett relevant test.
- [ ] Övertagande provas utan förlust av tidigare ändringar; gammal agent är stoppad innan den nya börjar skriva.
- [ ] Pilotrapport skiljer manuellt upprätthållna regler från tekniskt tvingande skydd och beskriver kvarvarande risker.

## Utanför scope

Produktimplementation, automatisk distribuerad låstjänst, nya agentroller, produktionsrelease och automatisk ändring av behörigheter. Ingen merge queue i första versionen.

## Risk, data och kostnad

Ingen persondata eller hemligheter behövs i pilot eller testdata. Felkonfigurerade skydd kan blockera arbete eller lämna kringvägar. Administrativ tilldelning kan kringgås och är inget atomiskt lås. Inga nya produktionsberoenden planeras. GitHub-plan, CI-kostnad och tillgängliga skydd kontrolleras före aktivering.

## Beslut och beroenden

- GitHub-åtkomst behövs för att verifiera nuvarande skydd, CI och eventuella befintliga Issues före publicering.
- Utse samordnare och en oberoende mänsklig granskare. Agenter under samma konto är inte separata godkännare.
- Godkänn scope före ready-for-build. Skydds- och behörighetsändringar kräver den mänskliga kontrollpunkten i AGENTS.md.

## Agentordning och klart-kriterier

Product Planner färdigställer Issue; Architect dokumenterar tilldelning och integrationsordning; en Implementer äger filändringarna. QA och Security Reviewer granskar avgränsat och read-only parallellt när lämpligt. Release förbereder PR och inställningsunderlag.

Klart när acceptanskriterierna är verifierade, CI passerar, dokumentation överensstämmer och PR redovisar resultat och kvarvarande mänskliga beslut. Detta lokala utkast innebär inte att implementationen är klar eller att GitHub-skydd är aktiverade.
