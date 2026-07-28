## Audit semantic distance and mathematician-facing Sage style

When a transcript translates a mathematical paper or proof into Sage pseudocode, review whether the visible code remains close enough to the source mathematics that a mathematician unfamiliar with Python could audit the argument.

The governing question is not whether the code looks object-oriented. Determine whether it preserves the source's actual nouns, verbs, ownership, and proof structure. In particular, review:

1. whether schemes, morphisms, divisors, sheaves, section spaces, linear systems, covers, quotients, local rings, germs, and parameter strata remain semantic objects rather than arrays, ideals, tuples, or helper records;
2. whether each method receiver is the mathematical owner, or whether method syntax was chosen only for programming convenience;
3. whether standard mathematical sugar expands to named products, projections, quotient maps, subgroup inclusions, or other recoverable constructions;
4. whether parentage, category membership, domains, codomains, and structure maps are shown in the visible notebook;
5. whether intermediate assertions state actual computed or theorem-certified results at the strength claimed;
6. whether routine backend ceremony is hidden while the mathematical intermediate objects remain explicit;
7. whether universal families, generic members, dense-open generality, and chosen specializations are distinguished;
8. whether equations are presented as realizations of semantic objects rather than substituted for them;
9. whether classifications refine certified categories or local objects instead of becoming unchecked labels;
10. whether hypothetical methods are clearly schematic and mathematically well typed rather than asserted to exist.

Flag **software-language translation** when ordinary mathematical nouns and verbs are replaced by generic utility classes or procedural pipelines. Flag **ownership inversion** when a method is placed on the most convenient argument rather than the object or diagram that owns the construction. Flag **ceremonial decomposition** when users must manually invoke canonical implementation stages that the mathematical object should compose. Flag **type elision** when the notebook suppresses where objects live. Flag **assertion starvation** when claimed dimensions, degrees, identities, memberships, or classifications never appear as explicit mathematical checkpoints. Flag **presentation substitution** when equations, ideals, tuples, or strings displace the semantic objects they represent. Flag **semantic pseudocode overclaim** when an aesthetically mathematical sketch contains ill-typed operations or is reported as an existing API.

Do not copy every method name from a corrective transcript into the standing guide. Extract the directional style: small semantic distance, Sage-native discoverability, correct mathematical ownership, explicit parentage, visible proof checkpoints, and backend machinery hidden behind standard constructions. Retain a few examples only to show the expected mathematical readability and to prevent regression into generic software style.
