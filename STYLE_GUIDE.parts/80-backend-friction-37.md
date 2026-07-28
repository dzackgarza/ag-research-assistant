## 37. Use backend friction as a mathematical reformulation trigger

When a mathematically natural task becomes dominated by compensating for a Sage limitation, pause before adding more adapters, normalization rules, coercions, canonical representatives, equality patches, or presentation-specific methods.

Backend friction can indicate two different situations:

1. **The mathematical formulation is correct and Sage is deficient.** Repair the missing primitive, provide a faithful shadow, use a bridge or reference implementation, or gate the unsupported backend honestly.
2. **The formulation is unnecessarily rigid, presentation-bound, or at the wrong categorical level.** Search for the standard intrinsic formulation; it may replace a brittle backend operation by a universal construction, a quotient or localization, descent data, a comparison morphism, a homotopy, a 2-cell, or another first-class mathematical object.

Do not assume in advance which diagnosis is correct. Use the difficulty itself as a self-nudge to reassess the mathematics.

Run the following audit before continuing a long repair chain:

1. What mathematical object, relation, or theorem is actually required, independently of Sage?
2. Which exact operation does Sage fail to express, construct, compare, or certify?
3. Is that operation intrinsic to the theorem, or only an artifact of the chosen presentation, strictness convention, coordinate realization, or software parent?
4. Do the local research corpus and standard references formulate the problem through a more principled object or categorical level?
5. What explicit map, equivalence, universal property, strictification theorem, or comparison result connects the proposed reformulation to the original claim?
6. Does the reformulation preserve the research target, or does it merely replace the theorem by an easier nearby statement?
7. Does it eliminate several backend patches and produce a more compositional interface for nearby mathematics?
8. After the reformulation, what genuine Sage deficiency remains, and should it be repaired, shadowed, bridged, gated, or deferred?

Equality of composites is one important regression case. If substantial work is being spent forcing two representations to compare by `==`, determine whether the theorem requires literal equality in one Hom-set, equality after transport, a specified isomorphism, a natural transformation, a 2-cell, a homotopy, or higher coherent compatibility. Conversely, do not weaken a genuine equality theorem merely because Sage cannot normalize the representatives.

The same diagnostic applies to repeated problems with coercions, canonical representatives, quotient objects, descent, gluing, derived constructions, universal properties, and presentation-dependent predicates. Modern categorical, homotopical, derived, or higher-categorical language is appropriate only when it is the established mathematical setting and materially clarifies the construction; do not invoke it as decorative abstraction or as an excuse to avoid a correct strict statement.

Search the local corpus and appropriate references proactively. A more modern formulation is valuable when it makes the mathematical witness first-class and thereby obviates the deficient Sage operation, not merely when it sounds more abstract.

Repeated local repair around one Sage limitation is a redesign trigger. Reconstruct the theory, compare the available formulations, and choose the one that is both mathematically standard and most semantically faithful before continuing implementation.
