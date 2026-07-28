
## 43. Derive universal constructions inside the established \(\infty\)-categorical foundation

When a project has already fixed an ambient categorical universe, that choice is operative mathematics, not background commentary. If ordinary categories are represented as truncated objects of an \(\infty\)-categorical framework, later constructions must be derived in that framework and only then truncated, projected, or strictified when the mathematics permits it.

Do not replace an existing diagrammatic construction by a fresh vocabulary of bare maps, Hom-set formulas, or local helper methods. The framework must accumulate mathematics: each new construction should be visibly assembled from previously established categories, functor categories, slices, full subcategories, universal objects, and comparison cells.

### 43.1 Start from diagram categories and their evaluation functors

For an \(\infty\)-category \(\mathcal C\), the arrow category is

\[
\operatorname{Ar}(\mathcal C)=\operatorname{Fun}(\Delta^1,\mathcal C).
\]

Its objects are arrows of \(\mathcal C\). Its morphisms are comparison cells between arrows. For an ordinary category viewed through its nerve, these are ordinary commutative squares. In a genuinely higher setting, the same functor category retains the required coherent square data.

The evaluation functors

\[
\operatorname{ev}_0,\operatorname{ev}_1:
\operatorname{Ar}(\mathcal C)\longrightarrow\mathcal C
\]

recover the source and target. For \(R\in\mathcal C\), the coslice is the fiber

\[
\mathcal C_{R/}
\simeq
\{R\}\times_{\mathcal C,\operatorname{ev}_0}
\operatorname{Ar}(\mathcal C).
\]

Thus an object of \(\mathcal C_{R/}\) is an arrow \(R\to T\), and a morphism in \(\mathcal C_{R/}\) is already a morphism in \(\operatorname{Ar}(\mathcal C)\) whose source component is \(\operatorname{id}_R\).

Under this project convention, do not claim that one must first invent or separately specify an ambient \(2\)-category before recognizing a morphism between arrows. The arrow category already supplies the relevant next-dimensional comparison datum.

### 43.2 Use the full localization construction, not a Hom-set paraphrase

Let \(R\) be a commutative ring and let \(S\subseteq R\) be multiplicatively closed. Work in the established category \(\mathcal C=\mathbf{CRing}\), viewed at the categorical level fixed by the project.

Inside the coslice \(\mathcal C_{R/}\), define the replete full subcategory

\[
\operatorname{Inv}_S(R)\subseteq \mathcal C_{R/}
\]

whose objects are arrows

\[
\phi:R\longrightarrow T
\]

satisfying

\[
\phi(S)\subseteq T^\times.
\]

A localization is an initial object

\[
\ell:R\longrightarrow L
\]

of \(\operatorname{Inv}_S(R)\). The usual localized ring is recovered by evaluation:

\[
L=\operatorname{ev}_1(\ell)=\ell.\operatorname{codomain}.
\]

For every admissible \(\phi:R\to T\), initiality gives a contractible mapping object

\[
\operatorname{Map}_{\operatorname{Inv}_S(R)}(\ell,\phi).
\]

A point

\[
\alpha_\phi:\ell\longrightarrow\phi
\]

of this mapping object is a morphism in \(\operatorname{Ar}(\mathcal C)\). In the ordinary truncated case it is the commutative square

\[
\begin{CD}
R @>{\operatorname{id}_R}>> R\\
@V{\ell}VV @VV{\phi}V\\
L @>{\widetilde\phi}>> T,
\end{CD}
\]

with

\[
\widetilde\phi\circ\ell=\phi.
\]

The familiar factor map

\[
\widetilde\phi:L\longrightarrow T
\]

is the target component

\[
\widetilde\phi=\operatorname{ev}_1(\alpha_\phi),
\]

not the whole universal comparison datum. The source component, source and target arrows, square, ambient coslice, and contractibility statement must remain recoverable.

Equivalently, precomposition with \(\ell\) gives a natural equivalence of mapping spaces

\[
\ell_T^*:
\operatorname{Map}_{\mathcal C}(L,T)
\xrightarrow{\;\simeq\;}
\operatorname{Map}_S(R,T),
\]

where \(\operatorname{Map}_S(R,T)\) is the full subspace of maps \(R\to T\) that send \(S\) to units. Its inverse sends \(\phi\) to the target component of the universal comparison cell \(\alpha_\phi\).

The classical bijection

\[
\operatorname{Hom}(L,T)
\cong
\{\phi:R\to T\mid \phi(S)\subseteq T^\times\}
\]

is the ordinary set-level shadow obtained by truncating this mapping-space equivalence. It is not a second semantic foundation to be implemented beside the initial-object construction.

For a prime ideal \(\mathfrak p\subseteq R\), prime localization is the same construction with

\[
S=R\setminus\mathfrak p.
\]

The facts that \(R_{\mathfrak p}\) is local, that its maximal ideal is \(\mathfrak pR_{\mathfrak p}\), and that it has a residue morphism are properties and derived constructions of the codomain. They do not define another universal object or justify a separate “prime-localization universal-property” class.

### 43.3 Return the comparison cell; expose components as derived accessors

A semantic convenience interface may read schematically as

```sage
Inv = C.coslice(R).replete_full_subcategory(is_S_inverting)
ell = Inv.initial_object()
alpha = ell.lift(phi)
```

but `alpha` must denote a point of

\[
\operatorname{Map}_{\operatorname{Inv}_S(R)}(\ell,\phi),
\]

hence a morphism of arrows. The concrete map is then obtained explicitly:

```sage
tilde_phi = alpha.target_component()
```

The implementation should make the following data inspectable:

```sage
alpha.source()            # ell
alpha.target()            # phi
alpha.source_component()  # id_R
alpha.target_component()  # tilde_phi
alpha.verify_square()      # tilde_phi * ell == phi, in the strict case
```

A backend may compute \(\widetilde\phi(r/s)=\phi(r)\phi(s)^{-1}\), but that formula implements one component of \(\alpha_\phi\). It does not replace the arrow-category morphism or the initiality statement.

If the framework chooses lifts coherently for all \(\phi\), that choice must be derived from the initial-object structure and represented through the existing undercategory, section, or natural-transformation machinery. Do not create independent per-target helpers whose naturality and compatibility must later be patched by hand.

### 43.4 Apply the same universal-object pattern throughout the project

Before inventing an operation-specific wrapper, search for the category in which the construction is initial, final, a limit, or a colimit.

The reusable pattern is:

1. choose the existing diagram category \(\operatorname{Fun}(K,\mathcal C)\), slice, coslice, comma category, or category of cones or cocones;
2. impose admissibility by a full or replete subcategory, an axiomatic refinement, or a pullback of categories;
3. define the desired construction as an initial object, final object, limit, colimit, adjoint image, or reflective localization in that category;
4. obtain comparison maps as points of the relevant mapping objects;
5. obtain ordinary maps, equations, matrices, or coordinate formulas by evaluation or another explicit forgetful functor;
6. preserve the mapping-space contractibility or corresponding universal witness as the source of uniqueness and coherence.

Examples include:

- a quotient \(R\to R/I\) as initial among arrows out of \(R\) that kill \(I\);
- a localization as initial among arrows that invert the specified multiplicative subset;
- a free object as an initial object in the appropriate comma category;
- products and pullbacks as final cones;
- coproducts and pushouts as initial cocones;
- sheafification or another reflective localization through the unit arrow into the reflective subcategory;
- universal families and moduli constructions through their actual representability or universal-arrow statements.

Do not replace any of these by a class named after “the universal property.” The mathematical primitive is the universal object or diagram in its ambient category; the universal property is its characterization through mapping objects.

### 43.5 Maintain an explicit abstraction-derivation ledger

For every foundational addition, write the actual derivation chain, not merely a list of related abstractions. For localization, the chain is

\[
\operatorname{Ar}(\mathcal C)
\longrightarrow
\mathcal C_{R/}
\longrightarrow
\operatorname{Inv}_S(R)
\longrightarrow
\ell\in\operatorname{Init}(\operatorname{Inv}_S(R))
\longrightarrow
\operatorname{Map}(\ell,\phi)
\longrightarrow
\operatorname{ev}_1(\alpha_\phi)=\widetilde\phi.
\]

The ledger must state:

1. which previously implemented construction supplies each arrow in the chain;
2. which new predicate, subcategory, or datum is genuinely added;
3. which output is the full semantic object;
4. which outputs are components or truncations;
5. which earlier ad hoc methods become derived syntax;
6. which composition, naturality, and coherence tests must hold in the existing framework.

If the proposed implementation cannot give this derivation, it is probably rebuilding the mathematics locally rather than extending the project.

### 43.6 Make every truncation, projection, and strictification explicit

A weaker backend does not determine the mathematical level of the public interface. When computation requires forgetting structure, name the operation:

- apply \(\pi_0\) or another truncation to a mapping space;
- project a morphism in \(\operatorname{Ar}(\mathcal C)\) to its target component;
- apply a forgetful functor from structured arrows to underlying arrows;
- choose a strict representative using a stated strictification theorem;
- pass from a coherent equivalence to a proposition only when the theorem requires no more.

State what data are lost and retain the full object whenever later composition or coherence may need it.

Conversely, do not invoke \(\infty\)-categorical language merely to avoid a strict equation that the theorem genuinely requires. The rule is to use the established categorical level faithfully, not to maximize abstraction.

### 43.7 Repair abstraction amnesia from the earliest divergence

Stop and re-audit when a later construction no longer visibly uses an earlier arrow, slice, limit, or comparison-cell abstraction; when a mapping object is silently replaced by a set; when only one component of a cell is returned; or when a fresh local API duplicates a universal construction already present.

Then:

1. freeze dependent work;
2. identify the first point where the established categorical derivation was abandoned;
3. translate every local object and method back into the existing diagram categories and universal objects;
4. restore full comparison cells and mapping objects;
5. retain coordinate formulas only as component computations or backends;
6. remove parallel Hom-set, factorization-helper, or theorem-wrapper foundations;
7. re-establish downstream naturality, functoriality, and coherence.

The user should not need to restore the project’s own \(\operatorname{Ar}(\mathcal C)\), slice, initial-object, or mapping-object machinery after it has already been implemented. Forgetting those foundations changes the mathematics, not merely the code organization.
