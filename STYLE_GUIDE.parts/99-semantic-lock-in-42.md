
## 42. Prevent prolonged semantic lock-in

An incoherent abstraction becomes more dangerous when later work treats it as settled. Methods, examples, tests, documentation, and dependent classes can all be internally consistent relative to a false premise. Their accumulation does not supply the missing mathematical meaning.

### 42.1 Revalidate when downstream dependence grows

Reopen the mathematical definition whenever a provisional abstraction begins to organize substantial work. In particular, stop and revalidate when:

- the noun acquires multiple public methods or dependent constructions;
- tests use only the abstraction's own vocabulary;
- the class bundles construction data, theorem consequences, certificates, and algorithms;
- its methods cannot be translated immediately into well-typed mathematical sentences;
- implementation effort grows without a standard source or independent definition;
- the abstraction begins to justify further architecture.

Revalidation must occur before more downstream code is added.

### 42.2 Erase the private vocabulary and reconstruct the mathematics

Temporarily forbid every term coined by the implementation. Restate the construction using established objects, morphisms, diagrams, properties, theorems, proof data, and algorithms. Identify:

1. the ambient category or type;
2. the actual objects and maps;
3. every public input and output;
4. the equations, universal properties, or propositions involved;
5. the distinction between mathematical data and backend state;
6. the standard source or independently recognizable construction.

Then try to falsify the abstraction. Check whether its fields have incompatible mathematical types, its methods lack a common owner, its morphisms or equality convention cannot be stated, its instances are characterized only by the constructor, or its tests are tautological consequences of the wrapper.

If the interface cannot be recovered without its private noun, it has no established public mathematical meaning. Keep the implementation private or delete the abstraction.

### 42.3 Use a semantic stop-loss

When revalidation fails:

1. freeze dependent work;
2. identify the earliest point where the false noun entered the design;
3. discard claims whose statements depend on that vocabulary;
4. decompose the implementation into independently valid computations, maps, predicates, certificates, and backend routines;
5. reassign those pieces to standard mathematical owners;
6. delete the public pseudo-object;
7. re-audit downstream mathematics from the corrected foundation.

Time already invested does not alter the mathematical status. Hours of executable work inside an incoherent ontology do not establish the claims suggested by that ontology; only independently retyped components survive.
