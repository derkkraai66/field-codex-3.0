# 🌲 Forest Dieback — A Field-Theoretic Model of Forest Collapse  
### *Field Codex Ecology Case Study*  
### *Version 1.0 — Mathematical Edition*

---

## 1. Inleiding

Bossterfte (forest dieback) is een typisch **veldprobleem**:

- langdurige droogte en hitte
- bodemuitputting en verzuring
- stikstofdepositie
- plagen (insecten, schimmels)
- fragmentatie en verlies van structuur
- menselijke interventies (kap, beheer)

Geen enkele factor op zich verklaart de instorting; het is de **interferentie van velden** die de veerkracht breekt.

Dit document past **Field Codex 3.0** toe op bossterfte als:

- een **veld Φ_tree(x,t)** voor boombiomassa,
- met coherentie (C),
- interferentie (I),
- en mutabiliteit (M) als kernmaten van ecosysteemgezondheid.

---

## 2. Domein & velddefinities

We modelleren een bosgebied als:

\[
\mathcal{X} \subset \mathbb{R}^2
\]

Tijd:

\[
t \in \mathbb{R}_{\ge 0}
\]

### 2.1 Boomveld

\[
\Phi_{\text{tree}}(x,t) : \mathcal{X} \times \mathbb{R} \to \mathbb{R}_{\ge 0}
\]

Boombiomassa of kroonbedekking per oppervlakteeenheid.

### 2.2 Bodem- en waterstatus

- \(W(x,t) \in [0,1]\): bodemvocht / beschikbaarheid grondwater  
- \(N(x,t)\): nutriëntenbeschikbaarheid (N, P, K; evt. samengevoegd)  
- \(S(x,t)\): bodemstress (verzuring, verdichting, zout e.d.)

### 2.3 Stressoren

- \(T(x,t)\): temperatuurafwijking (hittegolven, extremen)  
- \(D(x,t)\): droogtestress (bijv. deficit t.o.v. normaal)  
- \(P_{\text{pest}}(x,t)\): plaagdruk (schorskever, schimmels)  
- \(F_{\text{frag}}(x,t)\): fragmentatie-intensiteit (randen, open plekken)

Deze stressvelden vormen samen de **interferentielaag**.

---

## 3. Hoofdvergelijking — Boomveld als reaction–diffusion–interference systeem

We schrijven de dynamiek van boombiomassa als:

\[
\frac{\partial \Phi}{\partial t}(x,t)
= D_{\text{tree}} \nabla^2 \Phi(x,t)
+ G(\Phi, W, N)
- L(\Phi, S, T, D)
- I_{\text{tot}}(x,t)
\]

### 3.1 Diffusie — ruimtelijke spreiding / regeneratie

\[
D_{\text{tree}} \nabla^2 \Phi(x,t)
\]

Interpretatie:

- natuurlijke regeneratie (zaadverspreiding, uitlopers),
- uitbreiding van bosbiomassa naar aangrenzende cellen.

### 3.2 Groei — resource-gelimiteerde productie

\[
G(\Phi, W, N) =
\alpha \, f_W(W) \, f_N(N) \,
\Phi(x,t)\left(1 - \frac{\Phi(x,t)}{K(W,N)}\right)
\]

Waar:

- \(\alpha\): maximale groeifactor  
- \(f_W(W)\in[0,1]\): modulatiegroeifactor door water (bijv. sigmoïde)  
- \(f_N(N)\in[0,1]\): idem door nutriënten  
- \(K(W,N)\): draagkracht van de standplaats

Voorbeeldkeuze:

\[
f_W(W) = \frac{W}{W + W_0}, \qquad
f_N(N) = \frac{N}{N + N_0}
\]

---

### 3.3 Verlies — sterfte door stress

\[
L(\Phi, S, T, D)
= \beta_S S(x,t)\Phi(x,t)
+ \beta_T h_T(T)\Phi(x,t)
+ \beta_D h_D(D)\Phi(x,t)
\]

- \(S\): bodemstress (b.v. verzuring → wortelschade)  
- \(h_T(T)\): niet-lineaire respons op hitte (bijv. nul tot drempel, dan stijgend)  
- \(h_D(D)\): respons op droogtestress

---

### 3.4 Interferentie — synergie van stressvelden

De totale destructieve interferentie:

\[
I_{\text{tot}}(x,t)
= \sum_{i,j} \gamma_{ij}\,F_i(x,t)F_j(x,t)\,\Phi(x,t)
\]

Met stressoren:

- \(F_1 = T\) (temperatuur, hittegolven)
- \(F_2 = D\) (droogte)
- \(F_3 = S\) (bodemstress)
- \(F_4 = P_{\text{pest}}\) (plagen)
- \(F_5 = F_{\text{frag}}\) (fragmentatie / randstress)

\(\gamma_{ij} > 0\) = sterkte van de synergie.

Voorbeelden:

- **D × T**: hittegolf + droogte → sterke waterstress  
- **D × P_pest**: droogte verzwakt bomen → vatbaarder voor kevers  
- **S × P_pest**: verstoorde bodem → minder weerstand  
- **F_frag × P_pest**: randen → ingangspoorten voor plagen

---

## 4. Boscoherentie (C) — structurele samenhang

We definiëren een **boscoherentie-index** op basis van boomveld en leeftijdsstructuur.

Laat \(F_{\text{forest}}(x)\) een binaire of gewogen indicator zijn:

- 1 = bos aanwezig, voldoende kroonbedekking  
- 0 = geen bos / zwaar gedegradeerd

Dan:

\[
C = \frac{1}{|\mathcal{X}|}
\sum_{x \in \mathcal{X}}
\frac{1}{Z}
\sum_{y \in \mathcal{N}(x)}
\exp\left(-\frac{\|x-y\|}{\xi}\right)
F_{\text{forest}}(y)
\]

- \(\xi\): ruimtelijke coherentielengte  
- \(\mathcal{N}(x)\): buurt (bijv. binnen straal R)  
- \(Z\): normalisatie

Interpretatie:

- **Hoge C**: grote aaneengesloten boscomplexen  
- **Lage C**: versnipperde bosrestanten, randen, gaten

Coherentie is hier *structuur van het bos als veld*, niet enkel oppervlak.

---

## 5. Interferentiematrix voor bossterfte

Definieer velden:

1. \(T\): temperatuurstress / hittegolven  
2. \(D\): droogtestress  
3. \(S\): bodemstress  
4. \(P_{\text{pest}}\): plaagdruk  
5. \(F_{\text{frag}}\): fragmentatie / randlengte

De interferentiematrix \(I = (\gamma_{ij})\):

|      | T | D | S | Pest | Frag |
|------|---|---|---|------|------|
| **T**    | 0 | + | + | +    | +    |
| **D**    | + | 0 | + | +    | +    |
| **S**    | + | + | 0 | +    | +    |
| **Pest** | + | + | + | 0    | +    |
| **Frag** | + | + | + | +    | 0    |

Positieve \(\gamma_{ij}\) vergroten sterfte via synergie:

\[
I_{ij}(x,t) = \gamma_{ij} F_i(x,t)F_j(x,t)\Phi(x,t)
\]

---

## 6. Mutabiliteit (M) — adaptief vermogen van het bos

Mutabiliteit van het bos als **veld-weerbaarheid**:

\[
\mathcal{M}(x,t)
= \delta_{\text{div}}\,\text{Div}(x,t)
+ \delta_{\text{age}}\,\text{AgeMix}(x,t)
+ \delta_{\text{species}}\,\text{SpMix}(x,t)
\]

Waar:

- \(\text{Div}\): genetische diversiteit  
- \(\text{AgeMix}\): menging van leeftijdsklassen  
- \(\text{SpMix}\): menging boomsoorten (monocultuur vs. gemengd)

Effect op interferentie:

\[
I^{\prime}_{\text{tot}}(x,t)
= (1 - \mathcal{M}(x,t)) \, I_{\text{tot}}(x,t)
\]

- Hoge mutabiliteit → **dempt** interferentievelden  
- Monoculturen zonder age/soort-mix → lage \(\mathcal{M}\) → hoog risico op dieback

---

## 7. Tipping points voor bosinstorting

Een bosveld kan drie fasen hebben:

1. **Coherent bos**: hoge C, stabiele Φ  
2. **Gedegradeerd bos**: C daalt, Φ fluctueert, gaten groeien  
3. **Collapse**: Φ zakt onder minimale drempel, successie naar andere vegetatie

We definiëren drempels:

- \(\Phi_{\text{avg}}(t)\): gemiddelde boombiomassa  
- \(C(t)\): boscoherentie

Een kritische toestand:

\[
C(t) < C_{\text{crit}}
\quad \wedge \quad
\Phi_{\text{avg}}(t) < \Phi_{\text{crit}}
\quad \Rightarrow \quad
\Phi(x,t) \to \Phi_{\text{alt}}(x)
\]

waar \(\Phi_{\text{alt}}\) een alternatief stabiel veld is (struikheide, grasland, steppe).

Belangrijk:

> In veldtaal sterft niet “het bos”, maar **het bosveld transformeert** naar een ander attractorveld.

---

## 8. Renormalization Group (RG) voor bosstructuur

We introduceren een coarse-graining operator \(R_\xi\):

\[
R_\xi : \Phi_{\text{tree}}(x) \mapsto \Phi_{\text{tree},\xi}(x)
\]

waar \(\xi\) een schaalgrootte is (bijv. 10 m, 100 m, 1 km).

Schaalafhankelijke coherentie:

\[
C(\xi) = \text{Coh}(R_\xi(\Phi_{\text{tree}}))
\]

RG-flow:

\[
\frac{dC}{d\log \xi} = \beta(C)
\]

Interpretatie:

- \(\beta(C) > 0\): opschalen verhoogt coherentie → fragmentatie is lokaal, niet systemisch  
- \(\beta(C) < 0\): opschalen verlaagt coherentie → fragmentatiepatroon is *schaaloverschrijdend*

Een bos in dieback vertoont vaak:

- gaten op meerdere schalen  
- randen die zich uitbreiden  
- \(\beta(C) < 0\) over een breed bereik van \(\xi\)

---

## 9. Discrete bos-simulatie — schema

Een simulatie op een \(N \times N\) grid:

- \(\Phi_{t}(i,j)\): boombiomassa  
- \(W(i,j)\), \(N(i,j)\), \(S(i,j)\), \(T(i,j)\), \(D(i,j)\), \(P_{\text{pest}}(i,j)\), \(F_{\text{frag}}(i,j)\)

Discrete update:

\[
\Phi_{t+1}(i,j) =
\Phi_t(i,j)
+ D_{\text{tree}} \Delta \Phi_t(i,j)
+ \alpha f_W(W)f_N(N)\Phi_t(i,j)\left(1 - \frac{\Phi_t(i,j)}{K(i,j)}\right)
- \beta_S S(i,j)\Phi_t(i,j)
- \beta_T h_T(T(i,j))\Phi_t(i,j)
- \beta_D h_D(D(i,j))\Phi_t(i,j)
- I_{\text{tot}}(i,j)
\]

Waar:

\[
I_{\text{tot}}(i,j) =
\sum_{p<q} \gamma_{pq} F_p(i,j)F_q(i,j)\Phi_t(i,j)
\]

Dit kan direct in Python worden geïmplementeerd analoog aan:

- `bee_collapse_simulation.ipynb`  
- met andere parameterpatronen voor \(W, N, S, T, D, P_{\text{pest}}, F_{\text{frag}}\)

---

## 10. Beleids- en beheervertaal in Field Codex termen

### 10.1 Coherentie-regeneratie

- verbinden van boskernen (corridors, stepping stones)  
- verminderen van randlengte (compactere vormen, bufferzones)  
- herstel van structuurrijke bosranden

→ verhoogt C, verlaagt \(F_{\text{frag}}\).

### 10.2 Interferentie-reductie

- beperken van bodemverdichting en verzuring  
- waterbeheer (grondwaterpeil, infiltratie) om \(D\) te verlagen  
- beetle-traps, plaagmonitoring → verlagen \(P_{\text{pest}}\)  
- adaptieve oogst = geen grootschalige clear-cuts

→ verlaagt \(I_{\text{tot}}\) door \(F_i\) en \(\gamma_{ij}\) te verminderen.

### 10.3 Mutabiliteit-versterking

- mengingen van soorten (gemengde bestanden i.p.v. monoculturen)  
- variatie in leeftijdsstructuren (geen “even-aged” uniform bos)  
- genetische diversiteit bevorderen (herkomstmix, natuurlijke verjonging)

→ verhoogt \(\mathcal{M}\), dempt interferentievelden en vergroot veerkracht.

### 10.4 Adaptive Topology

- herontwerp van bos- en landschapstopologie op basis van:

  - RG-analyse van C(\(\xi\))
  - simulaties van bosvelddynamiek
  - detectie van kritieke fragmentatiepatronen

→ je stuurt niet alleen op “aantal bomen”, maar op **veldstructuur**.

---

## 11. Conclusie

Bossterfte is:

- geen geïsoleerd biologisch defect,
- maar een **veldtransitie**: van een coherent, veerkrachtig bosveld naar een gedegradeerd, instabiel alternatief veld.

In Field Codex 3.0 termen:

- **Coherentie C** daalt door fragmentatie en structuurverlies,  
- **Interferentie I** stijgt door synergetische stressoren (droogte, hitte, bodemstress, plagen),  
- **Mutabiliteit M** is vaak laag in monoculturen met uniforme leeftijden.

Het systeem beweegt richting een andere attractor (heide, grasland, steppe),  
tenzij gericht wordt ingegrepen op:

- C ↑ (structuur & connectiviteit)  
- I ↓ (stress-synergieën verminderen)  
- M ↑ (diversiteit en adaptiviteit verhogen)

Dit document vormt een **tweede ecologische casus** in de Field Codex-reeks, complementair aan:

- *Bijensterfte in Nederland — A Field-Theoretic Model of Pollinator Collapse*

en biedt een basis voor:

- simulaties,  
- bosbeheer-scenario’s,  
- en theoretische verdere uitbouw van de Codex.

---
