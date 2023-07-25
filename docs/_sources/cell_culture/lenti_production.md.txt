# Lenti virus production with HEK293T

```{note}
This theme is still under active development
```

## Cell lines

> HEK293T

## Reagent

- Cell
- DMEM (high glucose without L-glutamine)
- Fetal bovine serum
- TrypLE Express
- Penicillin/Streptomycin (P/S)
- Cell cutlure medium
- PEI, 1 mg/mL
- 0.22 μm polyethersulfone (PES) filter
- 0.45 μm PES filter
- psPAX2 (Addgene, [#12260](https://www.addgene.org/12260/))
- pMD2.G (Addgene, [#12259](https://www.addgene.org/12259/))
- pRSV-REV (Addgene, [#12253](https://www.addgene.org/12253/))
- pMDLg/pRRE  (Addgene, [#12251](https://www.addgene.org/2251/))
- Transfecr plasmid

Culture medium
: DMEM +10% FBS + 1%P/S

| Reagent | Volume |
| :---- | ----: |
| DMEM    | 450 ml |
| FBS     |  50 ml |
| P/S     |   5 ml |
|
| Total   | 505 ml |

---

## Protocols
### Thawing cells from freezing cells

1. Seed 293T packaging cells at 3.8×106 cells per plate in DMEM complete in 10 cm tissue culture plates.
2. Incubate the cells at 37 ℃, 5% CO2 for ~20 hours.
3. Prepare a mixture of the 3 transfection plasmids:

2nd generation lenti virus
: 3 plasmid system

|           Reagent           | Amount per 10 cm dish |
|-----------------------------|---------------------:|
|           psPAX2            |       1.3 pmol        |
|           pMD2.G            |       0.72 pmol       |
|      Transfer Plasmid*      |       1.64 pmol       |
| OptiPro SFM to total volume |        500 μL         |

3rd generation lenti virus
: 4 plasmid system

|           Reagent           | Amount per 10 cm dish |
|:---------------------------|--------------------:|
|           pMDLg/pRRE        |       1.3 pmol        |
|           pRSV-REV          |       0.72 pmol       |
|           pMD2.G            |       0.72 pmol       |
|      Transfer Plasmid*      |       1.64 pmol       |
| OptiPro SFM to total volume |        500 μL         |

```{important}
Endotoxins can inhibit transfection, therefore, plasmid DNA purification should include an endotoxin removal step. For high quality plasmid DNA, the plasimd should also be propagated in an endonuclease negative E. coli strain such as NEB stable.
```

1. Dilute the above 500 μL mixture into 500 μL PEI-OptiPro SFM with enough PEI such that the ratio of μg DNA:μg PEI is 1:3 (1000 μL total per 10 cm dish).
2. 
   ```{tips}
   There can be batch to batch variation when making the PEI working stock, therefore the ratio of μg DNA:μg PEI needs to be empirically determined. Once a batch of PEI is prepared, transfect cells with a fluorescent plasmid using a variety of ratios. Check the cells 1-2 days after transfection to determine what ratio gives the highest percentage of GFP positive cells.
   ```

|Ratio of DNA:PEI | μg of DNA | μL of 1 mg/mL PEI |
|:---------------:|:--------:|:----------:|
|1:1 | 18.9 | 18.9 |
|1:2 | 18.9 | 37.8 |
|1:3 | 18.9 | 56.7|
|1:4 | 18.9 | 75.6|
|1:5 | 18.9 | 94.5|
|1:6 | 18.9 | 113.4|



1. Gently add the diluted PEI to the diluted DNA. Add the diluted PEI dropwise while gently flicking the diluted DNA tube. 
2. Incubate the mixture 15-20 min at room temperature.
3. Carefully transfer the transfection mix to the Lenti-X 293T packaging cells. Add the transfection mix dropwise being careful not to dislodge the cells.
4. Incubate the cells for 18 hours, or until the following morning.
The following morning, carefully aspirate the media. Replace the media with 15 mL of DMEM complete or OptiPro SFM.
1. Incubate the cells.
2.  Virus can be harvested at 48, 72, and 96 hours post transfection in individual harvests or a combined harvest where all the individual harvests are pooled. If pooling harvests, transfer the harvested media to a polypropylene storage tube and store at 4 ℃ between harvest.
3.  Centrifuge the viral supernatant at ~500 x g for 5 minutes to pellet any packaging cells that were collected during harvesting.
4.  Filter supernatant through a 0.45 μm PES filter.
5.  The viral supernatant can be stored at 4 ℃ for several hours but should be aliquotted and snap frozen in liquid nitrogen and stored at -80 ℃ as soon as possible to avoid loss of titer. 