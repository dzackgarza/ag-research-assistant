# Foundation Amnesia and Cumulative Research

**Audience:** contributors, editors, and reviewers of the Algebraic Geometry Research Assistant guidance.  
**Source:** user correction concerning failure to reuse `Ar(C)`, slices, limits, and other previously established foundations, followed by concern that the localization derivation had been promoted too literally into the guide.  
**Status:** contributor-facing analysis; not part of the deployed assistant prompt.

## 1. Governing diagnosis

The principal failure is not that the assistant forgot one definition. It failed to treat the project as an accumulating body of mathematics.

A research framework should have compounding returns:

\[
F_0
\longrightarrow
F_1
\longrightarrow
F_2
\longrightarrow\cdots,
\]

where each foundation \(F_{n+1}\) reuses and refines \(F_n\), and later constructions are derived from the accumulated substrate. In the observed trajectory, each new problem instead generated a fresh local theory. Earlier categories, arrow constructions, limits, equality conventions, and backend routes ceased to constrain the work.

The effective process became

\[
\text{new problem}
\longrightarrow
\text{new local vocabulary}
\longrightarrow
\text{new local implementation}
\longrightarrow
\text{new incompatibilities},
\]

with no assimilation into a shared foundation. This makes sustained research impossible: the cost of the \(n\)-th task does not decrease, previous correctness arguments are not inherited, and conventions diverge across notebooks.

## 2. Amnesia has several distinct forms

### 2.1 Retrieval failure

The relevant construction exists in versioned source, prior notebooks, project decisions, or connected repositories, but the assistant does not search for it. A context reset is treated as absence of mathematics.

### 2.2 Recognition failure

The assistant finds an earlier abstraction but does not recognize the current problem as an instance of it. For example, it knows that `Ar(C)` exists but still treats a comparison between ring maps as a new factorization helper.

### 2.3 Composition failure

The assistant recognizes related primitives but does not derive the new construction by composing them. It writes a parallel API rather than using a slice, pullback, initial object, or evaluation functor already present.

### 2.4 Extension bypass

An existing primitive is almost sufficient. Instead of extending it at its natural owner, the assistant works around it in a local class or notebook. The shared foundation remains incomplete and the next problem repeats the same detour.

### 2.5 Propagation failure

A good general primitive is added, but the motivating computation and downstream consumers continue to use the old private implementation. The foundation exists nominally but does not govern the project.

### 2.6 Consolidation failure

Old and new interfaces remain side by side without a comparison theorem, deprecation plan, or ownership distinction. Later agents cannot determine which is canonical and may choose the weaker one.

These failures are mathematical. Parallel interfaces may use different equality notions, truncation levels, hypotheses, or universal properties even when they appear to compute the same result.

## 3. Cumulative work requires three recurring phases

### 3.1 Retrieval before construction

At task start or resumption, query the actual project artifacts. Recover the ambient categories, standard objects and morphisms, universal constructions, predicates, theorem certificates, backend adapters, and unresolved limitations relevant to the task.

The output should be a reuse map

\[
\text{requested construction}
\longrightarrow
\text{existing dependencies}
\longrightarrow
\text{irreducible missing capability}.
\]

This is not a memory exercise. The repository and local corpus are the source of truth.

### 3.2 Resurvey during construction

Long work changes shape. A local computation becomes a family; one helper becomes several; a backend limitation exposes a missing category; a foundation is improved mid-session. Each such event can invalidate the original reuse map.

Therefore retrieval must recur. In particular, resurvey when a new public abstraction is proposed, a second similar helper appears, categorical level changes, a context or kernel resets, or a completion claim is imminent.

### 3.3 Assimilation after construction

A new primitive becomes research progress only after it is integrated. Migrate callers, remove duplicate public methods, preserve special formulas as backends or regressions, update the dependency record, and re-audit affected theorems.

Without assimilation, the project accumulates files rather than mathematics.

## 4. A foundation inventory is operational mathematics

The project needs a searchable record of reusable constructions. It need not be a large administrative document; it can be distributed across source documentation, registries, indices, graphs, and tests. It must nevertheless expose:

- the mathematical type and ambient category of each construction;
- its defining maps and universal property;
- its categorical level and equality convention;
- source location and public owner;
- dependencies on earlier constructions;
- derived consumers;
- backend coverage and gates;
- proof, certificate, and regression status;
- known extension points.

This inventory makes context recovery possible and prevents a model from treating absence from its current prompt as absence from the project.

## 5. Reuse does not mean preserving a defective foundation

The assistant must not obey old abstractions mechanically. If an earlier primitive is false, incoherent, or insufficient, it should be repaired or replaced. The cumulative requirement is:

1. identify the existing owner;
2. state the defect precisely;
3. strengthen or replace the primitive at that layer;
4. provide comparison or migration data;
5. propagate the correction through dependent work;
6. remove the obsolete parallel path.

Thus cumulative development combines memory with criticism. It forbids both amnesia and blind compatibility with a bad abstraction.

## 6. The localization derivation is an example, not the general rule

The localization chain

\[
\operatorname{Ar}(\mathcal C)
\to
\mathcal C_{R/}
\to
\operatorname{Inv}_S(R)
\to
\ell
\to
\operatorname{Map}(\ell,\phi)
\to
\widetilde\phi
\]

contains important mathematical information that should not be compressed into a slogan. It is nevertheless one worked regression example.

The general principle is to derive each construction through its own appropriate diagram category, admissibility condition, universal object, mapping object, and projection. A quotient, free object, pullback, sheafification, or moduli construction will have a different derivation. Copying the localization symbols into every case would be another form of overfitting.

A style guide should therefore retain enough detail in one or more worked examples to make the desired mathematical thinking concrete, while marking clearly which features belong to the example and which define the reusable schema.

## 7. Research progress must compound

A useful end-of-task audit asks:

- Which prior foundations did this work use?
- What irreducible capability was added?
- Which old special cases now route through it?
- Which future tasks become easier?
- Which comparison theorems and regressions protect the extension?
- Where is the new dependency recorded?

If none of these questions has an answer, the work may still solve a bounded mathematical problem, but it has not advanced the reusable research framework.

## 8. Required editorial response

Contributor guidance should prevent editors from reducing foundation amnesia to “remember to reuse code.” It must preserve the mathematical consequences of forgetting: change of categorical level, duplicated universal properties, inconsistent equality, lost coherence, and repeated proof burden.

It should also prevent the opposite error of copying a detailed regression derivation verbatim as the universal standing rule. The correct synthesis has two layers:

1. an explicit general cumulative-development workflow;
2. carefully labeled worked examples that show what sufficient mathematical precision looks like.
