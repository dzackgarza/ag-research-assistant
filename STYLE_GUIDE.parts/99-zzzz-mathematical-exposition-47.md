
## 47. Write mathematical exposition, not commentary on the artifact

A research notebook should read like mathematics with executable calculations, not like a report about the notebook, the agent, or the history of the conversation. Present definitions, objects, morphisms, equations, constructions, computations, proofs, examples, and questions directly. Do not interrupt them with recurring prose about what the notebook is for, what it has established, how its scope evolved, which stage has been reached, or why an earlier framing was abandoned.

The distinction is structural. Meta-epistemic narration makes the artifact itself the subject of the prose. Standard mathematical exposition makes the mathematical objects and claims the subject. A reader should encounter

\[
Y=\mathbf P^1\times\mathbf P^1,
\qquad
\tau:Y\longrightarrow Y,
\qquad
|\mathcal O_Y(4,4)|^\tau,
\]

and the constructions performed with them—not a running account of how the assistant came to organize the investigation.

### 47.1 Let the mathematics be the grammatical subject

Prefer sentences such as:

- “The involution \(\tau\) acts on \(H^0(Y,\mathcal O_Y(4,4))\) with invariant subspace of dimension \(13\).”
- “The fixed locus consists of four points.”
- “A branch divisor avoiding these points gives a free lift on the double cover.”
- “The pencil below witnesses nonemptiness of the smooth locus.”

Avoid replacing them by sentences whose content is primarily:

- what “this notebook records”;
- what “this section is intended to establish”;
- what “has now been verified”;
- what “the current stage of the investigation” is;
- how “the next question” arose from an earlier exchange;
- why the notebook “does not have one immutable question.”

A useful deletion test is: if a sentence can be removed without losing a definition, hypothesis, claim, argument, citation, mathematical motivation, or navigational information, it is probably editorial scaffolding rather than exposition.

### 47.2 Assimilate corrections; do not memorialize them

User corrections should change the mathematics, claims, organization, or code. They should not normally survive as warnings to a future reader.

If a user explains that an explicit pencil is only a witness and not the universal family, then:

- correct every claim that treated the pencil as universal;
- place a brief qualification at the first use of the pencil if the distinction is not already evident;
- continue with the correct mathematical object.

Do not add a global warning announcing that “throughout this notebook, pencils never replace universal families” merely because that sentence records the correction.

If a user explains that there is no single central question, remove any false central-question framing and organize the material by its natural mathematical constructions. Do not replace the false framing by a paragraph declaring that no immutable question exists. That merely preserves the conversation as editorial prose.

Conversation history, retractions, and behavioral corrections belong in commits, incident records, or contributor analyses. The mathematical notebook should contain the corrected mathematics.

### 47.3 Make evidence visible without narrating status

Epistemic precision remains mandatory, but it should be carried by the mathematical form of the argument.

- A code cell followed by an assertion and displayed output shows a computation.
- “By Proposition 2.7” identifies a theorem-derived conclusion.
- A named comparison morphism and a checked commutative square show the relevant compatibility.
- “Assume \(B\) is smooth and avoids \(\operatorname{Fix}(\tau)\)” states a hypothesis.
- “It remains to construct the quotient over the full parameter space” records an actual unresolved mathematical step.

Do not precede or follow every passage with labels such as “what has been established,” “current verified status,” “this notebook proves,” or “remaining limitation” when the local argument already makes the distinction clear.

A mathematically substantive summary theorem may collect results proved across several sections. That is different from a status summary: it states a theorem with hypotheses and conclusions, not a report on the artifact.

### 47.4 Use introductions and roadmaps only for mathematical orientation

A brief introduction may define the setting, state the mathematical aims, explain why the constructions are related, and outline the organization when that genuinely helps navigation. Write it in the style of a paper, not a work log.

For example, an opening may say:

> Let \(Y=\mathbf P^1\times\mathbf P^1\) with the involution \(\tau\). We study \(\tau\)-invariant divisors in \(|\mathcal O_Y(4,4)|\), their double covers, the lifts of \(\tau\), and the resulting quotients.

That establishes the mathematical setting directly. It does not need an additional paragraph explaining that the notebook contains “a sequence of connected investigations,” that each stage “changes or refines the next question,” or that the document has no immutable governing prompt.

Use section headings named after mathematical objects and results:

- “The invariant linear system”;
- “The smooth fixed-point-avoiding locus”;
- “Lifts to the double cover”;
- “The Enriques quotient”;
- “The quotient \(Y/\langle\tau\rangle\)”;
- “Reflexive cover algebras at the nodes.”

Avoid headings whose main purpose is status narration, such as “What this notebook has established,” “Current state,” “How the investigation developed,” or “Remaining work,” unless the user explicitly requested a status document.

### 47.5 Keep limitations and future work local and proportionate

An unresolved point should not disappear, but it should occupy the smallest place consistent with mathematical honesty.

Use one of:

- a footnote at the affected claim;
- a `Remark` immediately after the construction;
- a short “Further questions” paragraph at the end of the relevant section;
- a separate status or planning artifact when extensive tracking is needed.

Do not repeat the same caveat in the introduction, section headers, transitional prose, and conclusion. Do not force completed mathematics to carry warnings about every stronger construction not yet implemented.

When a limitation changes the theorem, state it precisely. When it merely identifies a natural continuation, a brief note suffices.

### 47.6 Interleave prose and code as one mathematical argument

The prose immediately surrounding a code cell should explain non-obvious mathematics: why the construction is the correct one, which theorem justifies the next inference, what a displayed equation represents, or which hypothesis is being checked.

Do not paraphrase the cell as a status update. After

```sage
Fix_tau = tau.fixed_subscheme()
assert Fix_tau.degree() == 4
show(Fix_tau)
```

the next paragraph should use \(\operatorname{Fix}(\tau)\) mathematically. It need not say that the notebook “has now established the fixed locus computation.”

Likewise, once a quotient, canonical divisor, singular locus, or ramification divisor has been constructed and its properties asserted, continue the argument from that object. Avoid a second prose layer whose only purpose is to certify that the preceding code exists.

### 47.7 Detect reflexive editorial accretion

Stop and edit the notebook back to standard mathematical prose when:

- a correction produces a new disclaimer rather than a corrected claim;
- the opening describes the evolution of the task more than the mathematical setting;
- numbered “stages” reproduce the chronology of the agent's work rather than the logical organization of the mathematics;
- each section begins or ends with a statement of what it has established;
- a completed computation is followed by prose that merely announces completion;
- future work is repeated throughout instead of noted once near the relevant boundary;
- the words “notebook,” “section,” “investigation,” “current,” “status,” or “stage” occur more often than the names of the mathematical objects;
- the artifact reads like warnings to a future agent rather than a document for a mathematician.

The correction is not to delete genuine motivation, mathematical summaries, citations, or scope conditions. Rewrite so that they are attached to the mathematical object or claim they clarify. The notebook should preserve the final mathematical structure, not the conversational path by which the assistant reached it.

### 47.8 Do not mirror the current artifact state in prose

The notebook itself is the primary record of which definitions, constructions, computations, and assertions are present. Code cells, mathematical exposition, outputs, tests, and version history already encode the current state. Do not manually duplicate that state in prose through tables of completed items, phase descriptions, inventories of available functionality, section-by-section completion summaries, or repeated declarations of what is and is not implemented.

Such text is derivative rather than explanatory. It has a short useful life, becomes false as soon as nearby work changes, and creates a synchronization obligation at every later edit. The usual result is not better memory but several inconsistent descriptions of the same artifact.

Preserve prose that remains useful when the implementation advances:

- the mathematical reason a construction is considered;
- definitions, hypotheses, equations, maps, and proofs;
- non-obvious design choices and theorems that justify them;
- references and comparison results;
- a precise limitation when it changes the claim;
- a mathematical question or continuation that is not otherwise inferable.

Delete prose whose only content is a restatement of the present physical arrangement of cells or methods. Historical snapshots belong in version control, not in the mathematical narrative.

### 47.9 Keep forward pointers small, local, and consumable

A short note about what comes next can be valuable because it preserves the direction of an unfinished argument. State the next mathematical object, construction, or obstruction at the point where the exposition stops. Do not expand that note into a frozen phase plan or a complete inventory of unfinished work.

For example:

> **Remark.** It remains to construct the quotient family over the full invariant parameter space.

Once work on that construction begins, replace the remark by the new mathematics or move the unresolved remainder to its new boundary. A forward pointer is temporary re-entry information; it should be consumed rather than preserved as a fossilized plan.

Extensive coordination plans belong in a separate operational artifact. They should not be interleaved with the mathematics and should not be retained after they cease to guide current work.

### 47.10 Minimize synchronization obligations

Each fact should have one natural owner. A theorem or computation owns its mathematical conclusion. A test or capability gate owns executable coverage. A local remark owns the immediate unresolved boundary. Version control owns the history of earlier states.

Do not repeat the same information in an introduction, roadmap, status table, section preamble, section conclusion, and final summary. If a summary is genuinely required for another audience, derive it from the authoritative source where possible or keep it as a separate deliberately maintained artifact.

Before adding prose, determine whether it explains *why* or *what* in a way the mathematics cannot already show, or merely announces *where the artifact currently happens to be*. Text in the second class should normally be deleted, generated, or kept as a disposable private note. A document with no identifiable reader and no durable informational content should not be created merely to externalize the agent's momentary state.