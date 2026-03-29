"""Generate narration for Alachkar × Ayass AML Collaboration Presentation."""
import asyncio, edge_tts, os

OUTDIR = os.path.dirname(os.path.abspath(__file__))
VOICE = "en-US-AvaNeural"
RATE = "-5%"
PITCH = "+2Hz"

NARRATIONS = {
    1: """Welcome to a new chapter in AML research.
Today, we're presenting a collaboration framework between the Alachkar Laboratory at USC... and Ayass Bioscience's BiRAGAS platform.
This is where deep leukemia biology meets autonomous AI-driven discovery.
Eight hundred and thirty seven modules. Eighty eight point nine billion combination predictions. Seven phases of causal validation.
All focused on one mission: accelerating the fight against Acute Myeloid Leukemia.""",

    2: """So why does this collaboration matter?
AML remains one of the most aggressive blood cancers — with a five-year survival rate of just twenty eight percent.
The Alachkar Lab brings fifteen years of AML expertise... deep knowledge of targets like FLT3, CD99, SPARC, and APOC2... plus an active NIH R01 grant and nanoparticle therapeutics.
BiRAGAS brings something these targets have never had: causal proof.
Not correlation. Not association. Actual, validated causation... through twenty three modules across seven rigorous phases.
Together? We can do what neither could alone.""",

    3: """Let's look at the specific AML targets where BiRAGAS can help.
FLT3 and FLT3-ITD — the most common oncogenic driver in AML — is our top priority. BiRAGAS can design CRISPR guides, predict knockout effects with a seven-method ensemble, model resistance mechanisms, and find synergistic combinations from eighty eight point nine billion possibilities.
CD99 — where Dr. Alachkar has developed anti-CD99 nanoworms — gets dual-modality CRISPR design: DNA knockout plus RNA knockdown.
SPARC — her flagship discovery — gets a full causal DAG mapping the SPARC to ILK to AKT to beta-catenin chain.
APOC2-CD36 — the metabolic vulnerability — gets counterfactual simulation: what happens when we knock out both genes simultaneously?
And miR-155 — the oncogenic microRNA in FLT3-ITD AML — is perfect for cross-modal CRISPR: Cas9 knockout of the pre-miRNA locus... combined with Cas13 knockdown of the mature miRNA.""",

    4: """Here's how the BiRAGAS seven-phase causality framework applies to each AML target.
Phase one builds the AML causal network from seven evidence sources — GWAS, Mendelian Randomization, eQTL, CRISPR screening, SIGNOR, temporal data, and pathway databases.
Phase two computes causal importance — classifying genes into three tiers: master regulators like FLT3... secondary drivers like APOC2... and downstream effectors.
Phase three is quality assurance — testing every edge for causality, directionality, and confounding. Only edges passing a zero point six five confidence threshold survive.
Phase four simulates interventions — Pearl's do-calculus: what happens if we knock out FLT3? What compensates? What resistance emerges?
Phase five ranks pharmaceutical targets across seven dimensions — causal evidence, centrality, druggability, efficacy, safety, resistance risk, and translatability.
Phase six stratifies patients by their individual causal architecture — not population averages.
And phase seven arbitrates conflicting evidence with a full audit trail.""",

    5: """Now let's talk about the CRISPR engines — because this is where computation meets the bench.
The Editing Engine designs guides for six nuclease platforms. SpCas9 and SaCas9 for DNA knockout. Cas12a for multiplexing. Cas13d for RNA knockdown. And dCas13 for base editing — converting adenine to inosine, or cytosine to uracil, without cutting the DNA.
The Knockout Engine uses a seven-method ensemble across two hundred ten thousand configurations — predicting which AML driver knockouts will actually reduce leukemia viability.
The Combination Engine evaluates twelve synergy models across eighty eight point nine billion combinations — finding optimal pairs like FLT3 knockout plus CD99 knockdown, or SPARC inhibition plus AKT blockade.
And the RNA Base Edit Engine can edit the FLT3-ITD mutation at the RNA level — disabling it without permanent DNA alteration. That's reversible precision medicine.""",

    6: """Here is the proposed work plan — fourteen months from setup to publication.
Month one: data sharing and BiRAGAS configuration for AML.
Months two and three: build the AML causal DAG, validate with Mendelian Randomization, rank all targets.
Months three to five: design CRISPR guide libraries, predict knockout effects, forecast resistance.
Months five to seven: run the twelve-model combination engine across all target pairs.
Months seven to ten: the Alachkar Lab validates the top BiRAGAS predictions in AML cell lines — MOLM-13, MV4-11, KG-1.
Months eight to eleven: integrate TCR repertoire data, stratify patients, identify FLT3-ITD neoantigens.
Months ten to twelve: safety profiling, druggability scoring, clinical translation reports.
And months ten to fourteen: joint manuscript preparation targeting Blood, Leukemia, and Nature Methods... plus a joint R01 grant application.""",

    7: """Let's talk about what this collaboration produces — the deliverables.
Paper one: Causal Target Discovery in AML — published in Blood or Leukemia. The first application of seven-phase causal validation to AML targets.
Paper two: Cross-Modal CRISPR Combinations for AML Drug Resistance — targeting Nature Methods or Blood Cancer Discovery. DNA knockout plus RNA knockdown strategies validated experimentally.
Paper three: Integrating TCR Repertoire with Causal Networks — directly aligned with Dr. Alachkar's R01 grant. Published in Cancer Immunology Research or Immunity.
Paper four: RNA Base Editing Strategies for FLT3-ITD — a novel approach to disabling the mutation at the RNA level.
And a joint R01 grant: Agentic AI-Driven Causal Discovery and CRISPR Validation in AML — two to three million dollars over five years.""",

    8: """To close... this collaboration brings together the best of both worlds.
The Alachkar Lab's fifteen years of AML biology — the targets, the cell lines, the patient data, the nanoparticle therapeutics, the NIH funding.
And BiRAGAS's autonomous AI infrastructure — the causal proof, the combination predictions, the CRISPR design, the resistance forecasting, the patient stratification.
Neither of these capabilities exists anywhere else in this combination.
We're not just finding targets. We're proving they cause disease. We're not just designing experiments. We're predicting outcomes before the first pipette is lifted.
This is the future of AML research. And it starts... right here.
Thank you.""",
}

async def generate():
    for n, text in NARRATIONS.items():
        out = os.path.join(OUTDIR, f"slide_{n}.mp3")
        print(f"Generating slide {n}...", end=" ", flush=True)
        c = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await c.save(out)
        print(f"OK ({os.path.getsize(out)//1024} KB)")
    print("\nAll 8 slides generated!")

asyncio.run(generate())
