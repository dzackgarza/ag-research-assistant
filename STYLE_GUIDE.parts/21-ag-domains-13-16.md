## 13. Singular loci and local singularity theory

The singular locus belongs to the scheme or variety itself. Use or extend the existing intrinsic Sage operation such as `X.singular_locus()` rather than defining an embedding-specific free-standing constructor.

Local invariants must be grounded in the local ring or germ at a point.

Do not assume that every point has:

- a single local equation;
- a Tjurina algebra;
- a Milnor number;
- an ADE type;
- an equation in normal form.

A single local equation requires an appropriate hypersurface or Cartier presentation. Tjurina and Milnor constructions require their standard hypotheses and may depend on a chosen local presentation. ADE classification is a partial classification, typically requiring an isolated simple hypersurface singularity over an appropriate characteristic.

Methods such as `p.local_ring()`, `p.is_singular()`, or a conditional `p.ADE_type()` are valid only when their semantics and domains are explicit. Unsupported hypotheses must produce a precise mathematical failure, not a fabricated classification.

## 14. Double covers and covering morphisms

Treat a double cover primarily as a morphism

\[
\pi : X \to Y.
\]

Construct it from complete cover data, typically an invertible sheaf `L` on `Y` and a section

\[
s \in H^0(Y,L^{\otimes 2}),
\]

or equivalent branch data together with any required square-root choice.

The covering surface is recovered as the domain of `π`. Branch and ramification loci are derived from the construction and morphism.

A method such as `D.double_cover()` is valid only when the divisor object stores or canonically determines the required cover data. Otherwise require the missing line bundle, square root, or section explicitly.

Do not use a free-standing `DoubleCover(surface, divisor)` factory that hides the data needed to define the cover.

## 15. Primary outputs and return types

Return the mathematically primary object.

Examples:

- return a morphism for a cover, not merely its domain equation;
- return a subscheme for a scheme-theoretic locus, not only a list of rational points;
- return a map before its matrix;
- return a local algebra before a numerical dimension extracted from it;
- return a group, module, or representation before an arbitrary coordinate list;
- return the universal object together with its structure morphisms.

Coordinate equations, bases, matrices, dimensions, and enumerated points should remain accessible as derived data.

## 16. Hypotheses and partial operations

Before attaching an operation to a broad class of objects, determine its mathematical domain of definition and its currently implemented Sage domain.

Do not make a mathematically partial operation appear total by returning guesses, placeholders, or classifications outside its hypotheses.

State and check conditions such as:

- smoothness;
- normality;
- properness;
- projectivity;
- flatness;
- finite presentation;
- global generation;
- Cartier or hypersurface conditions;
- characteristic restrictions;
- isolatedness of a singularity;
- existence of square roots or descent data.

A mathematically partial operation should fail with an explicit violated mathematical hypothesis or return a result type that records the unresolved condition.

A mathematically well-defined operation with partial Sage coverage should retain its general interface and fail explicitly at the backend boundary. Assertions, case matches, and `NotImplementedError` are valid for this purpose when they state the unsupported representation and do not conflate implementation failure with mathematical undefinedness.

