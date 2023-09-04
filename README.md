# egg4_dias_TWE_config

This repo contains a Python config file which is used with dias_batch_running to specify inputs for running the Dias pipeline for TWE data.

## What does the config do?
dias_batch_running ([https://github.com/eastgenomics/dias_batch_running](https://github.com/eastgenomics/dias_batch_running)) is a Python module that runs the Dias pipeline for germline sequence data analysis on DNAnexus. The egg5_dias_TWE_config specifies the executables and their input files to be used in the Dias pipeline for analysing TWE data.

New versions of apps and app inputs for use in the Dias pipeline can be updated in the config without needing to update the pipeline itself.

## Parts of the config
* dias_reports
    * specifies the workflow ID, stage IDs (matching those in the workflow), and dynamic files for dias_reports.

## Versions of workflows and dynamic files in the config
Workflows:
* Dias reports: **dias_reports_v2.1.0**
    * DNAnexus workflow ID: `workflow-GXzkfYj4QPQp9z4Jz4BF09y6`

Dynamic files:
| File      | File name | DNAnexus file ID |
| --------- | --------- | ---------------- |
| genepanels | **230602_genepanels.tsv** | `file-GVx0vkQ433Gvq63k1Kj4Y562` |
| genes2transcripts | **230421_g2t.tsv** | `file-GV4P970433Gj6812zGVBZvB4` |
| exons_nirvana | **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gk7gZ47gypK7ZZ` |
| exons_file for eggd_athena | **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gf99pBPbJkV7bq` |
| twe_vep_config for SNV reports | **twe_vep_config_v1.1.6.json** | `file-GYX8q204j4fpP18Qx7YGkJvX` |
