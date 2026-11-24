# Thesis review — 21 September 2026

Reviewed `master.tex`, including the mathematical arguments in the main text and appendix, reference and citation keys, and the available computational model. The thesis source was not changed. Locations below refer to the current source lines. This is a review with specific findings, not a certification that all other statements are correct. External references were not independently checked.

The most consequential findings are 1–4. Findings explicitly marked **proof gap** do not establish that the claimed theorem is false.

1. **False statement: Job bound 2 includes every maximizing instance at α = 1/2.**

   Location: [master.tex:2495](/Users/jakewefers/Desktop/Thesis-Template/master.tex:2495), Theorem 3, printed page 24; the strict-inequality argument also appears at [master.tex:5892](/Users/jakewefers/Desktop/Thesis-Template/master.tex:5892).

   The theorem asserts that every maximizing instance has at most `3m−2` jobs, including at α = 1/2. Take m = 3 and the eight processing times

   \[
   \tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac14,\tfrac14,3.
   \]

   Listing the seven small jobs first gives loads (1,1,1), followed by the job of length 3, yielding worst loads (4,1,1). Optimal loads are (3,3/2,3/2): reserve one machine for the large job and divide the remaining load equally. At α = 1/2, the ratio is

   \[
   \frac{4^2+1^2+1^2}{3^2+(3/2)^2+(3/2)^2}=\frac43.
   \]

   This attains the global bound established in Chapter 3, so it is maximizing, but n = 8 > 7 = 3m−2. I also checked its optimal assignment and worst list schedule by exhaustive enumeration. The proof's factor `1−2α` is zero at this endpoint, so its strict improvement disappears.

   **Correction:** restrict this universal theorem to 0 < α < 1/2, and treat the endpoint separately. Alternatively, formulate and prove an existence statement about a maximizing representative with the job bound; that is different from a bound on every maximizer.

2. **False auxiliary lemma: the relaxed lower-bound function can have an interior maximum.**

   Location: [master.tex:6278](/Users/jakewefers/Desktop/Thesis-Template/master.tex:6278) through the lemma at [master.tex:6306](/Users/jakewefers/Desktop/Thesis-Template/master.tex:6306), and equations (A.18)–(A.19) on printed page 65.

   For the function defined there, set k = 3 and α = 1/15. The endpoint values are both 5/2. At t = 3/4, the displayed formula gives

   \[
   \overline\lambda_{1/15}(3/4)
   =1+\frac{11}{1+\sqrt{18049/450}}
   >\frac52,
   \]

   since `18049/450 < (19/3)^2 = 18050/450`. Numerically the interior value is approximately 2.5000358865. Continuity therefore forces an interior maximum. The claimed second-derivative identity cannot establish the stated lemma; it needs to be recalculated.

   There is also an integrality issue at [master.tex:6270](/Users/jakewefers/Desktop/Thesis-Template/master.tex:6270): for fixed interior t, setting u = 1 gives m = k+t, which is not an integer. This is a relaxation, not always an admissible instance.

   **Consequence:** the argument proving endpoint optimality within the entire family fails. This counterexample concerns the relaxed function and does **not** itself refute the lower bound obtained from explicit integer instances, or the final conjecture. A simpler lower-bound proof could directly use the u = 1 integer constructions, without claiming they maximize this whole family.

3. **Proof gap: the singleton proof does not justify the correspondence between machine loads.**

   Location: [master.tex:3012](/Users/jakewefers/Desktop/Thesis-Template/master.tex:3012), in Theorem 4.

   Defining x′ᵢ through the machine containing the old last job lᵢ does not establish that the final machines are counted exactly once. The proof needs to show that each lᵢ survives unification, that distinct lᵢ map to distinct final machines, and that these are precisely the machines other than the selected maximum-load machine. None of these properties is established here.

   Moreover, an old last job completing earlier does not imply that the final total load of its new machine is smaller: other jobs may follow it. Thus both `δᵢ ≥ 0` and the replacement of `Σ x′ᵢ` by the sum of final machine loads are unsupported. Conservation of total processing time alone does not repair this.

   **Consequence:** the application of the peak-increase lemma and the conclusion `r ≥ 0` at line 3034 are not proved, leaving the singleton reduction and results depending on it unsupported by this argument.

   A related problem occurs at [master.tex:2987](/Users/jakewefers/Desktop/Thesis-Template/master.tex:2987): `S_{j′}(σ^W(I))` refers to a newly unified job that does not exist in I. The exact machine-load equality at line 2992 also needs to account for all jobs moved in the rescheduling step.

4. **Proof gap, with a false intermediate claim: the three-machine maximization does not cover the full feasible region.**

   Location: [master.tex:5590](/Users/jakewefers/Desktop/Thesis-Template/master.tex:5590) through [master.tex:5708](/Users/jakewefers/Desktop/Thesis-Template/master.tex:5708), appendix proof of Lemma 10.

   The argument sets u = v = x, chooses p₃ = p₆ = x/2, and maximizes Q−L in y. But the denominator also varies with these choices. Maximizing the numerator alone is insufficient to maximize the ratio.

   In particular, the proposed equal split need not maximize the ratio for fixed other data. With α = 1/4 and

   \[
   (p_1,\ldots,p_7)=(0.6,0.5,0.4,0.4,0.5,0.6,2),
   \]

   all ten displayed constraints hold and u = v = x = 1. The ratio is `823/573 ≈ 1.43630`. Replacing p₃ and p₆ by 0.5 leaves the constraints satisfied but decreases the ratio to `103/72 ≈ 1.43056`. The explanation at line 5597 overlooks the dependence of L on p₃ and p₆.

   Finally, introducing r and s only tests vectors of the special form `(x,s,x/2,r,x,x/2,p₇)`. General feasible vectors with positive slack need not have that form. Therefore proving monotonicity in this restricted family does not prove that every feasible point is bounded by the one-variable problem.

   **Correction:** supply a reduction valid for an arbitrary feasible vector, or prove a global inequality that bounds the entire ratio. The calculations after the one-variable reduction do not fix the missing reduction.

5. **Incorrect exact equality: the contribution of small jobs is dropped before taking a limit.**

   Location: [master.tex:1562](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1562), equation (3.1).

   For finite positive small jobs and α > 1/2, `(2α−1) Σ p_j²` is positive. Their lengths being “arbitrarily small” does not make the term exactly zero. Equation (3.1) and the subsequent cost expressions need a limiting interpretation.

   **Correction:** define an approximating sequence, retain the error until taking the limit, and justify convergence of the relevant ratios. With fixed total small-job load, `Σ p_j² ≤ (max p_j) Σ p_j` provides the needed vanishing-error estimate. At α = 1/2 the coefficient is exactly zero.

6. **Proof gap: the fractional-job replication argument assumes rationality and preservation of optimality.**

   Location: [master.tex:1651](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1651).

   Processing times are real, so `t = (Σ p_j)² / Σ p_j²` need not be rational. For lengths 1 and √2, it is `(3+2√2)/3`, and no finite number q of copies makes qt integral.

   Also, copying schedules constructs feasible schedules, but does not by itself establish that they remain optimal or worst among all schedules of the replicated instance. The assertion that replicas are consecutive in **any** maximizing order needs justification.

   **Correction:** explicitly justify a rational approximation/continuity argument. For dominance, inequalities from candidate schedules may suffice, so equality of the old and new ratios should not be asserted without proof.

7. **Proof gap: the compactness argument includes an undefined ratio.**

   Location: [master.tex:2480](/Users/jakewefers/Desktop/Thesis-Template/master.tex:2480).

   Allowing all processing times in [0,1] includes the zero vector, where the ratio is 0/0. Thus the displayed domain is not a compact domain on which the ratio is defined and continuous.

   **Correction:** for α > 0, normalize `Σ p_j = 1`, pad to at most m² jobs with zeros, and explain that optimal/worst costs are minima/maxima over finitely many assignments/list orders. The denominator is then positive on the normalized domain. Explicitly exclude α = 0 from the finite-maximum argument.

8. **Logical issue: the definition of an individually “dominant” instance is vacuous.**

   Location: [master.tex:1230](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1230).

   Every instance belongs to some dominant subclass: the full instance class is itself dominant. Therefore the definition does not identify a special kind of instance. Refer instead to membership in a specified dominant subclass, or to a maximizing instance when that is intended.

   Relatedly, [master.tex:3172](/Users/jakewefers/Desktop/Thesis-Template/master.tex:3172) concludes that instances without the structural properties cannot maximize the ratio. Existence of a structured maximizer and a non-strict dominance inequality do not exclude unstructured maximizers with the same ratio. State the existence conclusion unless a strict-improvement argument is supplied.

9. **Domain errors in the basic definitions.**

   Locations: [master.tex:1131](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1131), [master.tex:1199](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1199), and [master.tex:1202](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1202).

   Zero weights are permitted, so an all-zero-weight instance has a zero optimal cost. Even with wⱼ = pⱼ, at α = 0 an instance with at most m jobs has zero optimal and worst list costs. The ratio definition needs a convention or a restriction to positive-optimum instances, including where ratios are used in the all-α reduction.

   “An optimal schedule ... is necessarily a list schedule” is false with zero-weight jobs: they can be delayed without changing the objective. “There exists an optimal list schedule” is the appropriate assertion.

   The schedule definition should explicitly require `S_j ≥ 0` and, for nonpreemptive processing, `C_j = S_j + p_j`. The current definition omits the first condition and states only an inequality for the second.

10. **The load-square identity needs an idle-free hypothesis.**

    Location: [master.tex:1407](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1407).

    The extension says “any schedule,” but inserting idle time increases completion costs without changing any processing-time sums or machine loads. Restrict it to schedules starting at time zero on each used machine with no idle gaps, in particular list schedules. Likewise, “without intermediate idle times” in the single-machine lemma should also rule out initial idle time.

11. **Wrong side of the bipartite graph in the tight-edge count.**

    Location: [master.tex:2646](/Users/jakewefers/Desktop/Thesis-Template/master.tex:2646).

    Tight edges were defined using the **left** vertices (machines of Pᵂ), so the claim “at most one tight edge at each right vertex” and the following minimum-load statement should refer to the left vertices. Multiple left vertices can have tight edges incident to the same right vertex. The bound `|T| ≤ m−1` follows from the left-side argument.

12. **Several displayed equations contain direct errors.**

    | Location | Error | Correction |
    |---|---|---|
    | [1531](/Users/jakewefers/Desktop/Thesis-Template/master.tex:1531) | `λ_α(I′) = = γ_α(I′)/γ^W_α(I′)` | Use `λ_α(I′) = γ^W_α(I′)/γ^*_α(I′)`. |
    | [3937](/Users/jakewefers/Desktop/Thesis-Template/master.tex:3937) | `γ^W_α(I) − γ^*_α(I) P_W − P*` | Insert `=`: `γ^W_α(I) − γ^*_α(I) = P_W − P*`. |
    | [5367](/Users/jakewefers/Desktop/Thesis-Template/master.tex:5367) | At α = 0, the ratio is given as `p₂/p₁ − 1`. | The ratio is `p₂/p₁`; the displayed calculation dropped the leading 1. Unboundedness still follows. |
    | [5323](/Users/jakewefers/Desktop/Thesis-Template/master.tex:5323) | The derivative is equated to its quadratic numerator. | Say that the derivative has the sign of that quadratic, or retain its positive denominator. |
    | [3930](/Users/jakewefers/Desktop/Thesis-Template/master.tex:3930) | The cost at α = 1/2 is written with subscript α. | Use subscript 1/2 in that displayed appeal to the 4/3 bound. |

13. **Endpoint/scope qualifications are missing in several places.**

    At [master.tex:3688](/Users/jakewefers/Desktop/Thesis-Template/master.tex:3688), the function is constant at α = 1/2, not strictly increasing. The upper bound remains valid, but “only as x → 1” does not hold there.

    The machine-dependent argument explicitly assumes m ≥ 3 at [master.tex:3703](/Users/jakewefers/Desktop/Thesis-Template/master.tex:3703). Make this explicit in its corollary, or separately justify the m = 2 case before extending the bound to that case.

    The lower-bound construction at [master.tex:4362](/Users/jakewefers/Desktop/Thesis-Template/master.tex:4362) assumes `0 < N < u`, while its earlier parameter interval and later maximizers include the endpoints N = 0 and N = u. Treat these endpoints directly; they are not covered by the interior cutting argument as written.

14. **The outlook figure has swapped schedule captions and an incorrect overall caption.**

    Location: [master.tex:4997](/Users/jakewefers/Desktop/Thesis-Template/master.tex:4997), Figure 5.1, printed page 51.

    The left diagram places the large job after the small jobs on one machine: it illustrates the bad list schedule. The right diagram gives the large job its own machine and balances the other loads: it illustrates the optimal schedule. Their captions at lines 5042 and 5090 are reversed. The overall caption “Schedules for α = 0” also disagrees with the surrounding discussion of Bₘ(α) for positive α.

    In the singleton construction, step 3 at [master.tex:2860](/Users/jakewefers/Desktop/Thesis-Template/master.tex:2860) points to panel (e), already used for the preceding step; the final rescheduled schedule is panel (g).

15. **Small language and notation corrections.**

    | Source line | Current text | Suggested correction |
    |---|---|---|
    | 945 | “earliest point time” | “earliest point in time” |
    | 1126 | “weighted completion time” | “weighted α-completion time” |
    | 1140 | `instance I` | `instance $I$` |
    | 1648 | “the the number” | “the number” |
    | 2214 | “list correspondance” | “list correspondence” |
    | 2467 | “also give us” | “also gives us” |
    | 2488 | “A instance” | “An instance” |
    | 2550 | maximizing/minimizing followed by σ*/σᵂ | Reverse the schedule and partition order to match the adjectives. |
    | 2857 | “shwon” | “shown” |
    | 3249, 3288 | `I(ε)` | Use the locally defined `I_{j*}(ε)` consistently. |
    | 3762 | “a fixed costs Q independant” | “a fixed cost αQ independent” |
    | 4278 | “normalize to 1 in and” | “normalize to 1, and …” |

**Build and reference checks.** No duplicate labels, missing referenced labels, or missing cited bibliography keys were found in the source. In particular, `fig:schedule-structure` resolves to Figure 4.2 in the current build.

A clean `latexmk` build stopped because the installed Biber executable failed while extracting its ARM binary with `lipo`. Subsequent direct pdfLaTeX passes produced an 81-page PDF in a temporary directory, using the existing bibliography output only to continue the checks. That existing `.bbl` has a version mismatch and lacks the newer Rozenberg entry, so these passes do **not** constitute a successful fresh bibliography build. The source contains the entry; the resulting undefined-citation warning should not be mistaken for a missing source key.

The final TeX log reports overfull boxes of approximately 10 pt near source lines 3217–3221 and 33 pt near 5040–5041. Inspect these layouts after the mathematical corrections. Full visual page-by-page inspection was not part of this review.
