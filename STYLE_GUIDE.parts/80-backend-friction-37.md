## 37. Use backend friction as a mathematical reformulation trigger

When a mathematically natural task becomes dominated by compensating for a Sage limitation, pause before adding more adapters, normalization rules, coercions, canonical representatives, equality patches, or presentation-specific methods.

Backend friction can indicate two different situations:

1. **The mathematical formulation is correct and Sage is deficient.** Repair the missing primitive, provide a faithful shadow, use a bridge or reference implementation, or gate the unsupported backend honestly.
2. **The formulation is unnecessarily rigid, presentation-bound, or at the wrong categorical level.** Search for the standard intrinsic formulation; it may replace a brittle backend operation by a universal construction, a quotient or localization, descent data, a comparison morphism, a homotopy, a 2-cell, or another first-class mathematical object.

Use the difficulty itself as a self-nudge to reassess the mathematics. Determine which diagnosis follows from the theorem and the standard references rather than from the behavior of the current representation.

Before continuing a long repair chain, determine:

1. the mathematical object, relation, or theorem required independently of Sage;
2. the exact operation Sage fails to express, construct, compare, or certify;
3. whether that operation is intrinsic to the theorem or belongs only to the chosen presentation, strictness convention, coordinate realization, or software parent;
4. whether the local research corpus and standard references use a more principled object or categorical level;
5. the explicit map, equivalence, universal property, strictification theorem, or comparison result relating any reformulation to the original claim;
6. whether the reformulation preserves the research target;
7. whether it removes a family of local patches and yields a more compositional interface;
8. the genuine Sage deficiency that remains after the mathematical reformulation.

Equality of composites is an important regression case. If substantial work is being spent forcing two representatives to compare by `==`, identify the exact relation asserted by the theorem: literal equality in one Hom-set, equality after transport, a specified isomorphism, a natural transformation, a 2-cell, a homotopy, or higher coherent compatibility. Implement that relation explicitly; Sage's normalization behavior does not determine the mathematical claim.

The same diagnostic applies to coercions, canonical representatives, quotient objects, descent, gluing, derived constructions, universal properties, and presentation-dependent predicates. Use categorical, homotopical, derived, or higher-categorical formulations when they are the standard mathematical setting and when the comparison with the original claim is part of the construction.

Search the local corpus and appropriate references proactively. A reformulation is valuable when it makes the mathematical witness first-class and thereby removes the deficient backend operation.

Repeated local repair around one Sage limitation is a redesign trigger. Reconstruct the theory, compare the available formulations, and continue from the one that is mathematically standard and semantically faithful.
