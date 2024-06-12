# simulate population exoansion and shrinking of three epochs of Asian populations

import msprime
import demesdraw
from matplotlib import pyplot as plt

# add demography
demography = msprime.Demography()
demography.add_population(name="ASIA", initial_size=25_000)

# instantaneous reduction of size 
demography.add_population_parameters_change(population="ASIA", time=3200, initial_size=3_000)

# instatanous growth
demography.add_population_parameters_change(time=3800, population="ASIA", initial_size=10_000)

# instantaneous bottleneck
print(demography)

# Plot a schematic of the model
demesdraw.tubes(demography.to_demes(), ax=plt.gca(), seed=1, log_time=True)
plt.show()

ts = msprime.sim_ancestry(
        {"AFR": 10, "EUR": 10}, 
        demography=demography, 
        recombination_rate=1e-8, # as in humans
        sequence_length=10_000,
        random_seed=1234)
print(ts)

# we can add mutations
mts = msprime.sim_mutations(ts, rate=1e-8, random_seed=1234)
print(mts.tables.sites)

# show SNPs
for variant in mts.variants():
    print(variant)

# visualise the haplotypes
samples = mts.samples()
for sample_id, h in zip(samples, mts.haplotypes(samples=samples)):
    pop = ts.node(sample_id).population
    print(f"Sample {sample_id:<2} ({ts.population(pop).metadata['name']:^5}): {h}")


# visualise the site frequency spectrum
afs = mts.allele_frequency_spectrum()
plt.bar(range(mts.num_samples + 1), afs)
plt.title("Allele frequency spectrum")
plt.show()


# Define the samples between which Fst will be calculated
pop_id = {p.metadata["name"]: p.id for p in mts.populations()}
sample_sets=[mts.samples(pop_id["AFR"]), mts.samples(pop_id["EUR"])]

print(mts.Fst(sample_sets))


# Try more examples from https://tskit.dev/tutorials/popgen.html









