## Audit premature ledgerization and administrative closure of research

When a transcript asks the assistant to extract mathematical material from a paper, book, database, or research discussion, review whether the assistant preserves the source as open mathematical prose or immediately converts it into a verification matrix, dependency ledger, checklist, bounded agenda, or machine-checkable plan.

Require the analysis to identify:

1. the mathematical claims, constructions, equations, maps, examples, and relations actually present in the source;
2. whether the source's organization and conceptual dependencies were preserved before operational metadata was added;
3. which statements are direct computational targets, theorem-mediated consequences, conceptual guidance, examples, or exploratory prompts;
4. which additional investigations the source naturally suggests, including variants, parameter changes, boundary cases, counterexamples, generalizations, and algorithmic questions;
5. whether facts were omitted because no current backend, destination notebook, or exact verification method was known;
6. whether implementation sequencing was confused with mathematical dependency;
7. whether the assistant treated a provisional list as exhaustive or closed;
8. whether internal agent coordination fields displaced the mathematical narrative;
9. whether a separate operational tracker was genuinely requested or needed;
10. whether a mathematician unfamiliar with the project-management machinery could still recover and use the source-derived mathematics.

Flag **premature ledgerization** when the assistant's first move is to design a matrix or schema rather than explain the mathematics. Flag **administrative closure** when an open research source is prematurely bounded into a finite contract. Flag **verification reduction** when computation is treated only as certification rather than also construction, falsification, experimentation, example generation, comparison, and conjecture formation. Flag **schema capture** when fixed fields such as status, destination, prerequisite, and expected output become the primary representation of the mathematics. Flag **destination fixation** when assigning every claim to a notebook or workstream replaces understanding its mathematical role. Flag **research-to-project-management collapse** when a document intended for mathematical study becomes primarily a task tracker.

Do not prohibit all lists, matrices, ledgers, or plans. They are useful for subagent coordination, CI contracts, mature implementation schedules, and explicitly requested project management. Require them to be derived from a separately preserved mathematical account and kept distinct from it. A research notebook may be a mathematical ledger of traceable objects, maps, computations, and deductions without becoming an administrative ledger.

The assistant-facing guidance should preserve the generative uses of sources: reproducing claims, checking code, finding missing foundations, extracting algorithms, generating examples, varying hypotheses, connecting other literature, and launching further investigations. Concrete claims about degrees, cover equations, commuting lifts, surface types, singularities, divisor classes, ampleness, or ramification are regression examples only; the governing rule applies to every source-mining task.

A valid correction should leave the reader with ordinary mathematical prose first, optional computational commentary and exploratory directions second, and operational work tracking only as a separate artifact when it serves a demonstrated need.
